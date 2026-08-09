"""Generate a 60s instrumental theme bed for every Genre Machine genre.

Queues ACE-Step jobs on local ComfyUI one at a time, saving MP3s as
genre_machine_mp3/music_<id>_<slug>. Skips ids whose MP3 already exists
in the ComfyUI output dir, so the batch is resumable.
"""
import json
import os
import random
import time
import urllib.request

API = "http://127.0.0.1:8188"
OUT = os.path.expandvars(r"%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI\output\genre_machine_mp3")
SECONDS = 60

GENRES = {
    "01": ("original",           "gentle storybook waltz, celesta, pizzicato strings, woodwinds, warm, playful, fairy tale, instrumental, 90 bpm"),
    "02": ("noir",               "smoky film noir jazz, muted trumpet, brushed drums, upright bass, rainy midnight mood, slow, instrumental"),
    "03": ("cosmic-horror",      "dark ambient drone, dissonant strings, deep sub bass, eerie choir pads, cosmic dread, slow, instrumental"),
    "04": ("gothic",             "gothic chamber music, pipe organ, harpsichord, cello, candlelit dread, minor key, slow, instrumental"),
    "05": ("steampunk",          "victorian orchestral with clockwork percussion, brass, music box, steam-engine rhythm, adventurous, instrumental, 110 bpm"),
    "06": ("cyberpunk",          "synthwave, cyberpunk, dark electronic, driving bassline, analog synth pads, neon, moody, cinematic, instrumental, 118 bpm"),
    "07": ("space-opera",        "epic orchestral space opera, soaring brass fanfare, sweeping strings, timpani, heroic, cinematic, instrumental"),
    "08": ("western",            "spaghetti western, twangy electric guitar, whistling melody, trotting rhythm, desert dusk, instrumental"),
    "09": ("post-apocalyptic",   "desolate post-apocalyptic ambient, detuned guitar, metallic percussion, wind textures, sparse, bleak, instrumental"),
    "10": ("dystopian",          "cold industrial march, mechanical percussion, ominous synth drones, surveillance tension, instrumental, 100 bpm"),
    "11": ("solarpunk",          "bright acoustic folktronica, kalimba, marimba, warm synth pads, hopeful, sunny morning, instrumental, 105 bpm"),
    "12": ("high-fantasy",       "epic fantasy orchestra, celtic harp, flute, french horns, choir pads, majestic quest theme, instrumental"),
    "13": ("anime",              "energetic anime opening style, driving rock guitar, synth leads, fast drums, heroic, uplifting, instrumental, 160 bpm"),
    "14": ("superhero",          "bold superhero orchestral theme, brass stabs, driving percussion, heroic fanfare, comic book energy, instrumental"),
    "15": ("silent-film",        "silent film accompaniment, ragtime, honky-tonk upright piano, playful chase, vaudeville, solo piano, instrumental, 140 bpm"),
    "16": ("suburban-mystery",   "1950s lounge with unease, vibraphone, soft swing drums, theremin hints, retro suburban, mysterious, instrumental"),
    "17": ("cold-war-spy",       "cold war spy tension, jazz noir, vibraphone, low brass, ticking percussion, cimbalom, covert, instrumental"),
    "18": ("true-crime",         "true crime documentary underscore, somber piano motif, tense strings, soft pulse, investigative, instrumental"),
    "19": ("courtroom",          "courtroom drama underscore, solemn strings, piano, slowly building tension, procedural gravity, instrumental"),
    "20": ("romance",            "romantic orchestral waltz, lush strings, piano, harp glissando, tender, warm, instrumental"),
    "21": ("heist",              "heist funk, wah guitar, conga groove, horn stabs, walking bass, slick seventies caper, instrumental, 112 bpm"),
    "22": ("detective",          "detective mystery jazz, clarinet, pizzicato bass, sneaky sleuthing groove, playful noir, instrumental"),
    "23": ("survival",           "arctic survival ambient, low strings, deep drum pulse, howling wind textures, vast and cold, instrumental"),
    "24": ("slapstick",          "cartoon slapstick orchestra, xylophone runs, slide whistle, trombone smears, frantic chase, zany, instrumental, 150 bpm"),
    "25": ("mythic-epic",        "ancient epic, bronze horns, war drums, lyre, chanting choir pads, mythic gravitas, instrumental"),
    "26": ("science-fiction",    "retro-futuristic science fiction score, analog synthesizers, arpeggios, sweeping pads, wonder and discovery, instrumental"),
    "27": ("action-adventure",   "adventure action score, propulsive percussion, brass ostinato, jungle drums, daring escape, instrumental, 130 bpm"),
    "28": ("ghost-horror",       "haunted music box, detuned lullaby, ghostly choir pads, creaking textures, supernatural chill, slow, instrumental"),
    "29": ("biography",          "reflective memoir underscore, solo piano, soft strings, nostalgic, gentle warmth of a life story, instrumental"),
    "30": ("historical-fiction", "wartime 1940s orchestral, solemn strings, distant snare drum, radio-era warmth, resistance and hope, instrumental"),
    "31": ("stage-drama",        "theatrical overture, string quartet, dramatic pauses, stage curtain grandeur, instrumental"),
    "32": ("graphic-novel",      "moody cinematic beat, ink-dark bass, vinyl crackle, trip-hop drums, urban noir mood, instrumental, 90 bpm"),
    "33": ("ergodic",            "unsettling experimental collage, prepared piano, tape loops, reversed textures, typewriter clicks, labyrinthine, instrumental"),
    "34": ("transgressive",      "gritty punk instrumental, distorted bass, raw drums, restless defiant energy, instrumental, 140 bpm"),
    "35": ("climate-fiction",    "elegiac ambient with hope, piano over rain textures, swelling strings, rising tide feeling, instrumental"),
    "36": ("slipstream",         "dreamlike ambient, tape-warped piano, soft static, uncanny calm, floating, slightly detuned, instrumental"),
    "37": ("bangsian",           "elysian string quartet with harp, classical garden party, gentle wit, heavenly warmth, instrumental"),
    "38": ("black-comedy",       "deadpan waltz, pizzicato strings, tuba, tiptoe rhythm, darkly comic funeral march, instrumental"),
    "39": ("magical-realism",    "latin american folk, nylon string guitar, marimba, soft accordion, warm village dusk, wistful magic, instrumental"),
    "40": ("epistolary",         "chamber piece for harpsichord and string trio, formal, prim, secretive correspondence mood, instrumental"),
}


def queue(gid, slug, tags):
    wf = {
        "1": {"class_type": "CheckpointLoaderSimple",
              "inputs": {"ckpt_name": "ace_step_v1_3.5b.safetensors"}},
        "2": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["1", 0], "shift": 5.0}},
        "3": {"class_type": "EmptyAceStepLatentAudio",
              "inputs": {"seconds": SECONDS, "batch_size": 1}},
        "4": {"class_type": "TextEncodeAceStepAudio",
              "inputs": {"clip": ["1", 1], "tags": tags,
                         "lyrics": "[instrumental]", "lyrics_strength": 0.99}},
        "5": {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["4", 0]}},
        "6": {"class_type": "KSampler",
              "inputs": {"model": ["2", 0], "positive": ["4", 0], "negative": ["5", 0],
                         "latent_image": ["3", 0], "seed": random.randint(0, 2**32),
                         "steps": 50, "cfg": 5.0, "sampler_name": "euler",
                         "scheduler": "simple", "denoise": 1.0}},
        "7": {"class_type": "VAEDecodeAudio", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}},
        "8": {"class_type": "SaveAudioMP3",
              "inputs": {"audio": ["7", 0], "quality": "128k",
                         "filename_prefix": "genre_machine_mp3/music_%s_%s" % (gid, slug)}},
    }
    req = urllib.request.Request(API + "/prompt", json.dumps({"prompt": wf}).encode(),
                                 {"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())["prompt_id"]


def wait(pid):
    while True:
        time.sleep(5)
        h = json.loads(urllib.request.urlopen(API + "/history/" + pid, timeout=30).read())
        if pid in h:
            st = h[pid].get("status", {})
            if st.get("completed"):
                return True
            if st.get("status_str") == "error":
                print("  ERROR", json.dumps(st)[:500], flush=True)
                return False


for gid, (slug, tags) in GENRES.items():
    name = "music_%s_%s_00001.mp3" % (gid, slug)
    if os.path.exists(os.path.join(OUT, name)):
        print(gid, slug, "already done, skipping", flush=True)
        continue
    t0 = time.time()
    ok = wait(queue(gid, slug, tags))
    print(gid, slug, "ok" if ok else "FAILED", "%.0fs" % (time.time() - t0), flush=True)

print("batch complete", flush=True)
