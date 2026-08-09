# -*- coding: utf-8 -*-
"""Generate a 90s theme bed for every Genre Machine genre (v3 prompts).

ACE-Step conditioning rule (Steve's): the lyrics field is either [inst]
for pure instrumentals, or minimal wordless vocalise ("aah... ooh...",
chant vowels) — never sentences. Anything sentence-shaped in the lyrics
field gets SUNG, badly (see the v2 heist incident). All the style and
arrangement richness lives in the tags.

Queues jobs on local ComfyUI (127.0.0.1:8188) one at a time, saving
MP3s as genre_machine_mp3_v3/music_<id>_<slug>. Skips ids already
rendered in that folder, so the batch is resumable.
"""
import json
import os
import random
import time
import urllib.request

API = "http://127.0.0.1:8188"
OUT = os.path.expandvars(
    r"%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Installs\ComfyUI\ComfyUI"
    r"\output\genre_machine_mp3_v3")
SECONDS = 90

GENRES = {
"01": ("original",
    "regal brass fanfare intro, majestic orchestral horns, transitioning to a whimsical magical forest theme, sweeping celtic harps, ethereal glockenspiel melody, dreamlike ambiance, cinematic woodwinds, storytelling pace, 80 BPM",
    '[verse]\naah... ooh... aah...\nmmm... aah... ooh...\n[chorus]\naah... aah... oooh...'),
"02": ("noir",
    "1940s vintage film noir soundtrack, classic hard-boiled detective theme, melancholic solo tenor saxophone melody, weeping muted trumpet swells, slow brushed snare drums, smoky jazz lounge ambiance, rain sound effects layered, dramatic cinematic tension, instrumental, 65 BPM",
    '[inst]'),
"03": ("cosmic-horror",
    "unsettling cosmic horror ambiance, deep sub-bass drones, eerie detached synthesizer swells, microtonal strings, slow shifting metallic textures, cold lovecraftian space void atmosphere, unearthly tension, 60 BPM",
    '[verse]\nohm... aum... ohm...\naum... ohm... aum...'),
"04": ("gothic",
    "dark gothic horror soundtrack, haunting pipe organ chords, weeping classical cello solo, cold harpsichord arpeggios, distant rolling thunder sound effects, shadowy haunted cathedral atmosphere, 70 BPM",
    '[verse]\nahh... ohh... ahh...\nohh... ahh... ohh...'),
"05": ("steampunk",
    "neoclassical steampunk orchestration, ticking clockwork percussion, rhythmic gear-grinding sound effects, lively industrial violin pizzicato, driving accordion counter-melody, brass gears, clockwork engine rhythm, instrumental, 95 BPM",
    '[inst]'),
"06": ("cyberpunk",
    "gritty cyberpunk electronic score, pulsing analogue synthwave bassline, aggressive cybernetic drum machine beats, neon retro-futurism, industrial techno synth stabs, dark dystopian city soundtrack, instrumental, 110 BPM",
    '[inst]'),
"07": ("space-opera",
    "sweeping space opera orchestration, majestic cinematic horn sections, epic ethereal synth pads, soaring starship adventure theme, orchestral strings, cosmic wonder, grand storytelling pace, 85 BPM",
    '[verse]\naah... aah... oooh...\nooh... aaah... ooh...'),
"08": ("western",
    "classic spaghetti western soundtrack, lonely whistling melody, twangy electric guitar with heavy tremolo, trotting acoustic guitar percussion, distant coyote howling sound effects, desolate desert outlaw vibe, instrumental, 75 BPM",
    '[inst]'),
"09": ("post-apocalyptic",
    "bleak post-apocalyptic soundscape, rusted acoustic guitar picking, cold hollow wind ambient drones, sparse industrial clangs, metallic percussion, desolate wasteland atmosphere, slow pace, 60 BPM",
    '[verse]\nmmm... hmm... mmm...'),
"10": ("dystopian",
    "dark dystopian industrial theme, oppressive buzzing synth drones, cold metallic sheet percussion, mechanical rhythmic pulse, tense electronic soundscape, gritty authoritarian atmosphere, instrumental, 80 BPM",
    '[inst]'),
"11": ("solarpunk",
    "optimistic solarpunk electronic ambiance, warm acoustic marimba patterns, bright uplifting synth plucks, ambient wind chime accents, clean organic grooves, eco-futuristic sunny atmosphere, 90 BPM",
    '[verse]\nooh ooh aah...\nla la ooh...\n[chorus]\naah aah ooh...'),
"12": ("high-fantasy",
    "grand high fantasy orchestration, soaring orchestral flutes, majestic sweeping violins, deep pounding elven war drums, ancient acoustic lutes, legendary adventurous kingdom theme, 85 BPM",
    '[verse]\naah oh aah...\noh aah oh...\n[chorus]\naaah... ooooh...'),
"13": ("anime",
    "high-energy anime orchestral pop, sparkling digital piano melodies, soaring emotional string arrangements, driving energetic bass guitar, upbeat j-rock drum rhythms, vibrant colorful instrumental, 130 BPM",
    '[inst]'),
"14": ("superhero",
    "epic superhero comic theme, bold punchy brass sections, driving cinematic orchestral staccato strings, heroic snare drum rolls, soaring orchestral brass, action-packed blockbuster pace, instrumental, 100 BPM",
    '[inst]'),
"15": ("silent-film",
    "1920s vintage silent film ragtime piano, upbeat honky-tonk piano melody, flickering projector sound effects, old lo-fi vinyl crackle, fast-paced slapstick piano chord progressions, nostalgic instrumental, 115 BPM",
    '[inst]'),
"16": ("suburban-mystery",
    "eerie 1950s suburban mystery theme, warbling vintage theremin melody, plucked orchestral strings, muted jazz vibraphone chords, pristine white-picket-fence suspense atmosphere, retro instrumental, 75 BPM",
    '[inst]'),
"17": ("cold-war-spy",
    "tense cold war spy thriller theme, stealthy low cimbalom plucking, muted staccato brass accents, ticking spy watch percussion, cold soviet-era concrete ambiance, high-stakes suspense, instrumental, 80 BPM",
    '[inst]'),
"18": ("true-crime",
    "modern true crime documentary score, cold repetitive felt piano keys, pulsing minimalist synth bass, sparse industrial clock textures, dark brooding investigation atmosphere, instrumental, 70 BPM",
    '[inst]'),
"19": ("courtroom",
    "serious courtroom drama score, intense staccato orchestral strings, driving classical cello ostinato, rolling timpani drums, sharp gavel strike accents, high-stakes legal tension, instrumental, 75 BPM",
    '[inst]'),
"20": ("romance",
    "sweeping cinematic romance theme, beautiful warm solo grand piano melody, lush emotional string orchestra, soft concert harp glissandos, tender passionate storytelling ambiance, instrumental, 65 BPM",
    '[verse]\nooh... aah... mmm...\nmmm... ooh... aah...'),
"21": ("heist",
    "high-stakes heist jazz soundtrack, stealthy muted walking bassline, rhythmic hi-hat jazz drums, intricate vibraphone lines, sudden sharp horn section stabs, smooth precision robbery theme, instrumental, 105 BPM",
    '[inst]'),
"22": ("detective",
    "classic detective mystery score, curious pizzicato string plucking, sneaky woodwind melodies, low inquisitive bassoon lines, quiet ticking percussion, foggy london street atmosphere, instrumental, 70 BPM",
    '[inst]'),
"23": ("survival",
    "raw wilderness survival score, primal acoustic wooden flutes, organic hand drum percussion, scraping cello textures, gritty survivalist tension, vast wild nature landscape theme, 75 BPM",
    '[verse]\nhmm... huh... hmm...\nhuh... hmm... huh...'),
"24": ("slapstick",
    "frantic 1940s slapstick cartoon score, bouncy xylophone melodies, slide whistle sound effects, boisterous muted trumpets, spring-boing percussion, chaotic funny cartoon pace, instrumental, 120 BPM",
    '[inst]'),
"25": ("mythic-epic",
    "colossal mythic epic orchestration, thunderous orchestral taiko drums, roaring cinematic horn walls, sweeping mythological strings, ancient legendary battle theme, 80 BPM",
    '[verse]\nohh! ahh! ohh!\nahh... ohh... ahh...'),
"26": ("science-fiction",
    "futuristic science fiction score, vintage analog synthesizer arpeggios, pulsing electronic sub-bass, alien theremin melodies, sleek starship laboratory atmosphere, high-tech instrumental, 90 BPM",
    '[verse]\nooh... ooh... aah...\naah... ooh... ooh...'),
"27": ("action-adventure",
    "high-octane action adventure score, fast-paced staccato strings, driving cinematic percussion loops, punchy heroic brass stabs, adrenaline-fueled chase theme, instrumental, 115 BPM",
    '[inst]'),
"28": ("ghost-horror",
    "eerie supernatural horror soundtrack, detuned nursery rhyme music box melody, creeping cold ambient string pads, ghostly haunting atmosphere, instrumental, 65 BPM",
    '[verse]\naah... aaah... aah...'),
"29": ("biography",
    "reflective biography score, nostalgic warm acoustic piano chords, gentle emotional violin solo, soft acoustic guitar picking, intimate personal storytelling ambiance, instrumental, 70 BPM",
    '[inst]'),
"30": ("historical-fiction",
    "majestic historical fiction orchestration, authentic acoustic period instrumentation, sweeping classical string sections, regal woodwinds, grand ancient castle court theme, 75 BPM",
    '[verse]\naah... ooh... aah...\nooh... aah... ooh...'),
"31": ("stage-drama",
    "intimate stage drama score, minimal melancholy felt piano, solo expressive cello, quiet theatrical room tone ambiance, intense emotional dialogue backing, instrumental, 65 BPM",
    '[inst]'),
"32": ("graphic-novel",
    "edgy graphic novel theme, dark modern industrial trip-hop beat, gritty distorted bass guitar riffs, smoky vinyl scratch textures, urban comic noir aesthetic, instrumental, 85 BPM",
    '[inst]'),
"33": ("ergodic",
    "avant-garde experimental soundscape, unpredictable non-linear time signatures, abstract prepared piano plucks, erratic typewriter clicks, tape loops, strange ambient glitch textures, academic avant-garde instrumental, 80 BPM",
    '[inst]'),
"34": ("transgressive",
    "raw transgressive punk instrumentation, aggressive distorted electric guitar garage riffs, driving fast messy rock drums, heavy industrial bass fuzz, chaotic counter-culture energy, instrumental, 140 BPM",
    '[inst]'),
"35": ("climate-fiction",
    "sweeping climate fiction soundscape, beautiful melting glass ambient synths, solemn acoustic woodwinds, rolling ocean wave sound effects, fragile environmental beauty theme, 70 BPM",
    '[verse]\naah... aah... ooh...\noooh... aaah...'),
"36": ("slipstream",
    "surreal slipstream music, dream-pop electric guitars with heavy chorus, swirling ethereal synthesizers, floating jazz fusion rhythms, blurring reality boundaries theme, 88 BPM",
    '[verse]\nooh aah ooh...\naah ooh aah...'),
"37": ("bangsian",
    "mystical bangsian afterlife score, celestial pipe organ, shimmering angelic harps, echoing limestone underworld cavern reverb, baroque classical instrumentation, 65 BPM",
    '[verse]\naah... aah... aah...\nooh... aah... ooh...'),
"38": ("black-comedy",
    "quirky black comedy score, jaunty pizzicato cello plucking, ironic cheerful whistling, macabre bassoon melodies, dry comedic tango percussion, dark humor instrumental, 90 BPM",
    '[inst]'),
"39": ("magical-realism",
    "whimsical magical realism score, sparkling warm acoustic piano runs, sudden surreal accordion swells, twinkling acoustic chimes, soft marimba accents, blending ordinary life with magic vibe, instrumental, 80 BPM",
    '[verse]\nmmm... la la... mmm...\nla la... mmm... la...'),
"40": ("epistolary",
    "intimate epistolary score, scratching fountain pen sound effects, soft emotional felt piano keys, warm acoustic cello background, old hand-written letter nostalgia, instrumental, 60 BPM",
    '[inst]'),
}


def queue(gid, slug, tags, lyrics):
    wf = {
        "1": {"class_type": "CheckpointLoaderSimple",
              "inputs": {"ckpt_name": "ace_step_v1_3.5b.safetensors"}},
        "2": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["1", 0], "shift": 5.0}},
        "3": {"class_type": "EmptyAceStepLatentAudio",
              "inputs": {"seconds": SECONDS, "batch_size": 1}},
        "4": {"class_type": "TextEncodeAceStepAudio",
              "inputs": {"clip": ["1", 1], "tags": tags,
                         "lyrics": lyrics, "lyrics_strength": 0.99}},
        "5": {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["4", 0]}},
        "6": {"class_type": "KSampler",
              "inputs": {"model": ["2", 0], "positive": ["4", 0], "negative": ["5", 0],
                         "latent_image": ["3", 0], "seed": random.randint(0, 2**32),
                         "steps": 50, "cfg": 5.0, "sampler_name": "euler",
                         "scheduler": "simple", "denoise": 1.0}},
        "7": {"class_type": "VAEDecodeAudio", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}},
        "8": {"class_type": "SaveAudioMP3",
              "inputs": {"audio": ["7", 0], "quality": "128k",
                         "filename_prefix": "genre_machine_mp3_v3/music_%s_%s" % (gid, slug)}},
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


if __name__ == "__main__":
    for gid, (slug, tags, lyrics) in GENRES.items():
        name = "music_%s_%s_00001.mp3" % (gid, slug)
        if os.path.exists(os.path.join(OUT, name)):
            print(gid, slug, "already done, skipping", flush=True)
            continue
        t0 = time.time()
        ok = wait(queue(gid, slug, tags, lyrics))
        print(gid, slug, "ok" if ok else "FAILED", "%.0fs" % (time.time() - t0), flush=True)
    print("batch complete", flush=True)
