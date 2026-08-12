# -*- coding: utf-8 -*-
"""Generate Genre Machine illustrations via the Gemini image API (nano banana).

Reads tools/image_prompts.csv (story_id, genre_id, genre, filename, prompt),
calls gemini-2.5-flash-image for each row, crops the result to the site's
720x412 and saves it into assets/images/<filename>. Fully headless, resumable
(skips rows whose webp already exists), and backs off on rate limits.

The API key is read from (in order):
  1. env var GEMINI_API_KEY
  2. D:\\Kaizen\\Documents\\Keys\\gemini_api_key.txt   (one line, just the key)
The key is never printed and never committed.

Usage (from the project root):
    python tools/image_api_batch.py            # all rows
    python tools/image_api_batch.py red        # only story_id == red
    python tools/image_api_batch.py --force     # regenerate even if webp exists
"""
import base64
import csv
import io
import json
import os
import sys
import time
import urllib.error
import urllib.request

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "tools", "image_prompts.csv")
DST = os.path.join(ROOT, "assets", "images")
KEY_FILE = r"D:\Kaizen\Documents\Keys\gemini_api_key.txt"
MODEL = "gemini-2.5-flash-image"
OUT_W, OUT_H = 720, 412


def api_key():
    k = os.environ.get("GEMINI_API_KEY", "").strip()
    if k:
        return k
    if os.path.exists(KEY_FILE):
        return io.open(KEY_FILE, encoding="utf-8").read().strip()
    raise SystemExit("No API key: set GEMINI_API_KEY or create %s" % KEY_FILE)


KEY = api_key()
URL = ("https://generativelanguage.googleapis.com/v1beta/models/"
       "%s:generateContent?key=%s" % (MODEL, KEY))


def generate(prompt, tries=4):
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }).encode()
    for attempt in range(tries):
        try:
            req = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.loads(r.read())
            for part in data["candidates"][0]["content"]["parts"]:
                inline = part.get("inlineData") or part.get("inline_data")
                if inline and inline.get("data"):
                    return base64.b64decode(inline["data"])
            return None  # no image in response (e.g. safety block)
        except urllib.error.HTTPError as e:
            code = e.code
            msg = e.read().decode("utf-8", "ignore")[:200]
            if code in (429, 500, 503) and attempt < tries - 1:
                wait = 15 * (attempt + 1)
                print("  %d, backing off %ds..." % (code, wait), flush=True)
                time.sleep(wait)
                continue
            print("  HTTP %d: %s" % (code, msg), flush=True)
            return None
        except Exception as e:
            if attempt < tries - 1:
                time.sleep(10)
                continue
            print("  error:", str(e)[:150], flush=True)
            return None
    return None


def crop_to_site(raw, dst_webp):
    im = Image.open(io.BytesIO(raw)).convert("RGB")
    s = max(OUT_W / im.width, OUT_H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    l, t = (im.width - OUT_W) // 2, (im.height - OUT_H) // 2
    im.crop((l, t, l + OUT_W, t + OUT_H)).save(dst_webp, "WEBP", quality=88)


def main():
    args = sys.argv[1:]
    force = "--force" in args
    only = [a for a in args if not a.startswith("--")]
    rows = list(csv.DictReader(io.open(CSV, encoding="utf-8")))
    if only:
        rows = [r for r in rows if r["story_id"] in only]
    done = skipped = failed = 0
    for r in rows:
        out = os.path.join(DST, r["filename"])
        if os.path.exists(out) and not force:
            skipped += 1
            continue
        t0 = time.time()
        raw = generate(r["prompt"])
        if not raw:
            print("FAILED %s" % r["filename"], flush=True)
            failed += 1
            continue
        crop_to_site(raw, out)
        done += 1
        print("OK %-34s %4.0fs  (%d done)" % (r["filename"], time.time() - t0, done), flush=True)
        time.sleep(1)
    print("BATCH COMPLETE: %d generated, %d skipped, %d failed" % (done, skipped, failed), flush=True)


if __name__ == "__main__":
    main()
