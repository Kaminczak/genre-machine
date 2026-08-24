# The Genre Machine

**[Open the live version →](https://kaminczak.github.io/genre-machine/)**

Four fairy tales. Forty genres. One grid.

Pick a story, pick a genre, and read what happens when *The Three Little Pigs*
is retold as film noir, cosmic horror, a courtroom transcript, or a 1950s
suburban mystery. Some cells are narrated aloud in a voice designed for that
genre — a weathered cowhand for the Western, a whisper for the cosmic horror.

Built as a classroom tool for teaching genre, voice, and craft.

---

## Why it exists

Ask a class what "genre" means and you get a list of shelves at a bookstore.
Genre is not a shelf. It is a set of promises about tone, pacing, what counts as
a threat, and what an ending is allowed to feel like. The fastest way to see that
is to hold the plot completely still and change nothing but the genre.

So the plot never changes. Three pigs, three houses, one wolf, every single time.
What changes is everything else — and once a student sees the same events become
a police procedural, a myth, and a slapstick cartoon, the concept stops being
vocabulary and starts being a tool they can use in their own writing.

## Classroom uses

- **Read two cells side by side.** What did the genre demand be added? What did it
  quietly delete?
- **Predict before revealing.** Give students the logline for a cell and have them
  draft the opening line, then compare against the version here.
- **Write it yourself first.** Give students a cell's logline and have them draft
  their own version before revealing the machine's — then argue about whose
  genre moves are stronger.
- **Hear the difference.** Every cell is narrated in a voice designed for its
  genre — in English and in Spanish — making tone audible for students who do
  not catch it on the page.
- **Print the two sheets.** The *Handout* explains what genre is and walks the
  machine's four lenses — Setting / World Building, Tone & Atmosphere, Character
  Traits & Motivation, Language / Syntax — with a word wall for the terms inside
  them. The *Genre Activity* then hands students a fable the machine deliberately
  does not carry, *The Tortoise and the Hare*: they explore five or six genres,
  choose the two that surprised them most, and describe each shift lens by lens
  against a worked Wilderness / Survival example. Both print on one landscape
  page.

## How it works

A static site — no build step, no framework, no dependencies. Open `index.html`
and it runs.

| Path | What it holds |
|---|---|
| `index.html` | The whole app: markup, styles hook-up, and app logic |
| `handout.html` | Printable handout: what genre is, the four lenses, a word wall |
| `activity.html` | Printable activity: shift *The Tortoise and the Hare* through the lenses |
| `data/stories.js` | Stories, genres, and loglines for all 164 cells |
| `Stories/` | One markdown file per story x genre — where the writing happens |
| `data/scripts-generated.js` | Generated: merges the markdown scripts over `stories.js` |
| `tools/sync_scripts.py` | Reads `Stories/` and regenerates the file above |
| `tools/narrate.py` | Sends a script to a local text-to-speech API and saves the audio |
| `assets/audio/` | Pre-rendered narration, played directly by the browser |

### The narration pipeline

Each markdown file carries a `voice_prompt` in its frontmatter — a plain-English
description of how that genre should sound. `tools/narrate.py` sends the prompt
and the script to [Voice Creator Pro](https://github.com/) running locally,
saves the resulting WAV into `assets/audio/`, saves the designed voice so it can
be reused, and writes the voice ID back into the markdown.

```bash
python tools/narrate.py 01 08 03   # narrate three genres of The Three Little Pigs
python tools/sync_scripts.py       # push markdown edits into the site
```

The hosted copy has no access to a local API, so it plays the pre-rendered files
and shows *Narration coming soon* for cells that do not have one yet. Run it
locally with the API up and any cell can be generated on demand.

## Running it locally

```bash
git clone https://github.com/Kaminczak/genre-machine.git
cd genre-machine
python -m http.server 8123
```

Then open <http://127.0.0.1:8123/index.html>. On Windows, `serve.cmd` does the
same thing with a double-click. Serving over HTTP rather than opening the file
directly matters only if you want live narration — browsers block a `file://`
page from calling a local API.

## Status

Complete. All four tales are written across all forty genres — 164 cells with
full prose, an illustration for every cell, and narration in both English and
Spanish for every cell. Two printable classroom sheets (the Handout and the
Create a Genre activity) ship alongside the machine.

## Credits

Written and built by Steve Kaminczak. Illustration prompts in `prompts.csv`.
