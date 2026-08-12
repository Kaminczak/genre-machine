# -*- coding: utf-8 -*-
"""Generate every Genre Machine illustration locally with FLUX.1-dev on ComfyUI.

Reads tools/image_prompts.csv (story_id, genre_id, genre, filename, prompt),
queues a FLUX text-to-image job per row on the local ComfyUI API, then crops
the result to the site's 720x412 and saves it into assets/images/<filename>.

Fully headless and resumable: rows whose webp already exists are skipped.
Needs ComfyUI on 127.0.0.1:8188 with flux1-dev-fp8.safetensors in
models/checkpoints. Landscape gen size 1344x768 (~ the site's 1.748 ratio),
so the final crop loses almost nothing.
"""
import csv
import io
import json
import os
import random
import time
import urllib.request

from PIL import Image

API = "http://127.0.0.1:8188"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "tools", "image_prompts.csv")
DST = os.path.join(ROOT, "assets", "images")
COMFY_OUT = os.path.expandvars(
    r"%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Shared\output")
GEN_W, GEN_H = 1344, 768
OUT_W, OUT_H = 720, 412
CKPT = "flux1-dev-fp8.safetensors"


def workflow(prompt, seed):
    return {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}},
        "2": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["1", 1], "text": prompt}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["1", 1], "text": ""}},
        "4": {"class_type": "FluxGuidance", "inputs": {"conditioning": ["2", 0], "guidance": 3.5}},
        "5": {"class_type": "EmptySD3LatentImage",
              "inputs": {"width": GEN_W, "height": GEN_H, "batch_size": 1}},
        "6": {"class_type": "KSampler",
              "inputs": {"model": ["1", 0], "positive": ["4", 0], "negative": ["3", 0],
                         "latent_image": ["5", 0], "seed": seed, "steps": 24, "cfg": 1.0,
                         "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0}},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}},
        "8": {"class_type": "SaveImage",
              "inputs": {"images": ["7", 0], "filename_prefix": "gm_img/gm"}},
    }


def queue(prompt, seed):
    body = json.dumps({"prompt": workflow(prompt, seed)}).encode()
    req = urllib.request.Request(API + "/prompt", body, {"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())["prompt_id"]


def wait(pid, timeout=300):
    t0 = time.time()
    while time.time() - t0 < timeout:
        time.sleep(4)
        try:
            h = json.loads(urllib.request.urlopen(API + "/history/" + pid, timeout=30).read())
        except Exception:
            continue
        if pid in h:
            st = h[pid].get("status", {})
            if st.get("completed"):
                for out in h[pid].get("outputs", {}).values():
                    for im in out.get("images", []):
                        return os.path.join(COMFY_OUT, im.get("subfolder", ""), im["filename"])
                return None
            if st.get("status_str") == "error":
                return None
    return None


def crop_to_site(src_png, dst_webp):
    im = Image.open(src_png).convert("RGB")
    s = max(OUT_W / im.width, OUT_H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    l, t = (im.width - OUT_W) // 2, (im.height - OUT_H) // 2
    im.crop((l, t, l + OUT_W, t + OUT_H)).save(dst_webp, "WEBP", quality=88)


def main():
    rows = list(csv.DictReader(io.open(CSV, encoding="utf-8")))
    done = skipped = failed = 0
    for r in rows:
        out = os.path.join(DST, r["filename"])
        if os.path.exists(out):
            skipped += 1
            continue
        prompt = r["prompt"]
        t0 = time.time()
        png = wait(queue(prompt, random.randint(0, 2**31)))
        if not png or not os.path.exists(png):
            print("FAILED", r["filename"], flush=True)
            failed += 1
            continue
        crop_to_site(png, out)
        os.remove(png)
        done += 1
        print("OK %-34s %4.0fs  (%d done)" % (r["filename"], time.time() - t0, done), flush=True)
    print("BATCH COMPLETE: %d generated, %d skipped, %d failed" % (done, skipped, failed), flush=True)


if __name__ == "__main__":
    main()
