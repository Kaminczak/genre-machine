"""
Genre Machine - narration pipeline.

Reads a story markdown file from Stories/, sends its voice_prompt + script to
Voice Creator Pro on 127.0.0.1:8100, saves the WAV into assets/audio/, saves the
designed voice so it can be reused, and writes voice_id + audio back into the
file's frontmatter.

Usage (from the project root):
    python tools/narrate.py 01 08 03          # genre ids
    python tools/narrate.py --story pigs 01   # a different story
    python tools/narrate.py --all             # every drafted file for the story
"""

import argparse
import base64
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

API = "http://127.0.0.1:8100/api/v1"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DIR = os.path.join(ROOT, "assets", "audio")

STORY_FILE_PREFIX = {
    "pigs": "Three Little Pigs",
    "red": "Little Red Riding Hood",
    "goldilocks": "Goldilocks and the Three Bears",
    "cinderella": "Cinderella",
}


def call(path, payload=None, method=None, timeout=1800):
    url = API + path
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers,
                                 method=method or ("POST" if data else "GET"))
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def ensure_model():
    st = call("/model/status")
    if st.get("loaded"):
        print("  model already loaded:", st.get("name") or st.get("type"))
        return
    print("  loading model...", flush=True)
    call("/model/load", {}, timeout=60)
    while True:
        p = call("/model/load/progress")
        if p.get("status") in ("complete", "loaded", "idle", "done"):
            break
        if p.get("status") == "error":
            raise SystemExit("  model load failed: " + p.get("message", ""))
        print("    %s%% %s" % (p.get("percent", 0), p.get("message", "")), flush=True)
        time.sleep(4)
    print("  model ready.", flush=True)


def parse(md_path):
    raw = open(md_path, encoding="utf-8").read()
    fm = raw.split("---", 2)[1]
    def field(k):
        m = re.search(r'^%s:\s*"?(.*?)"?\s*$' % k, fm, re.M)
        return m.group(1) if m else ""
    script = raw.split("## Script", 1)[1].split("## Voice design", 1)[0].strip()
    return raw, field("genre"), field("genre_slug"), field("voice_prompt"), script


def write_back(md_path, raw, voice_id, audio_rel):
    raw = re.sub(r'^voice_id: ".*"$', 'voice_id: "%s"' % voice_id, raw, flags=re.M)
    raw = re.sub(r'^audio: ".*"$', 'audio: "%s"' % audio_rel, raw, flags=re.M)
    raw = raw.replace("- **Saved voice id:** \n", "- **Saved voice id:** %s\n" % voice_id)
    raw = raw.replace("- **Audio file:** \n", "- **Audio file:** %s\n" % audio_rel)
    open(md_path, "w", encoding="utf-8").write(raw)


def find(story, genre_id):
    pat = os.path.join(ROOT, "Stories", "%s *" % genre_id,
                       "%s - *.md" % STORY_FILE_PREFIX[story])
    hits = glob.glob(pat)
    if not hits:
        raise SystemExit("no file for story=%s genre=%s" % (story, genre_id))
    return hits[0]


def run(story, genre_id):
    md = find(story, genre_id)
    raw, genre, slug, prompt, script = parse(md)
    print("\n=== %s / %s ===" % (story, genre), flush=True)
    if not prompt:
        print("  no voice_prompt, skipping."); return
    if not script or script.startswith("> [!todo]"):
        print("  no script drafted, skipping."); return
    print("  %d words | voice: %s" % (len(script.split()), prompt[:60] + "..."), flush=True)

    t0 = time.time()
    res = call("/generation/design?sync=true",
               {"instruct_text": prompt, "target_text": script, "language": "English"})
    if not res.get("audio_base64"):
        print("  FAILED:", res.get("status")); return
    audio = base64.b64decode(res["audio_base64"])
    os.makedirs(AUDIO_DIR, exist_ok=True)
    name = "%s_%s_%s.wav" % (story, genre_id, slug)
    open(os.path.join(AUDIO_DIR, name), "wb").write(audio)
    print("  audio: assets/audio/%s (%.1f KB, %.0fs)" % (name, len(audio) / 1024, time.time() - t0), flush=True)

    voice_id = ""
    try:
        sv = call("/voices", {"name": "GM %s - %s" % (genre, story),
                              "audio_base64": res["audio_base64"],
                              "transcript": prompt,
                              "voice_type": "design",
                              "ref_text": script[:300]})
        voice_id = (sv.get("voice") or {}).get("id", "")
        print("  saved voice:", voice_id or sv.get("message"), flush=True)
    except Exception as e:
        print("  voice save failed:", e)

    write_back(md, raw, voice_id, "assets/audio/" + name)
    print("  frontmatter updated.", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("genres", nargs="*")
    ap.add_argument("--story", default="pigs")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    try:
        call("/health", timeout=10)
    except Exception as e:
        raise SystemExit("Voice Creator Pro is not answering on 8100: %s" % e)
    ensure_model()
    ids = a.genres
    if a.all:
        ids = ["%02d" % i for i in range(1, 33)]
    for g in ids:
        run(a.story, g.zfill(2))
    print("\ndone.", flush=True)
