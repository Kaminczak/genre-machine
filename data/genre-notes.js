/* genre-notes.js — field notes for every genre in the machine.
   Keyed by genre id. Each entry:
     traits   : hallmark conventions of the genre (bullets)
     history  : two-or-three-sentence origin story
     examples : three landmark titles to hand a student
   Rendered by the "About this genre" panel in index.html. */

window.GENRE_MACHINE_NOTES = {
  "01": {
    traits: [
      "Oral-tradition simplicity: flat characters, fast plots",
      "The rule of three — three pigs, three houses, three attempts",
      "A moral baked into the ending",
      "Magic and talking animals accepted without explanation"
    ],
    history: "Folk tales passed mouth-to-mouth for centuries before Charles Perrault wrote them down in 1697 and the Brothers Grimm collected hundreds more in 1812. They were originally for adults — the nursery versions came later, scrubbed of the darker bits.",
    examples: ["Grimms' Fairy Tales", "Perrault's Tales of Mother Goose", "Andersen's Fairy Tales"]
  },
  "02": {
    traits: [
      "Cynical narrator in a corrupt city, usually first person",
      "Femme fatales, double-crosses, doomed fatalism",
      "Rain, neon, cigarette smoke, venetian-blind shadows",
      "Crime never really pays — but nobody's innocent either"
    ],
    history: "Born from 1930s hardboiled pulp fiction and 1940s Hollywood crime films shot in German-Expressionist shadow. French critics, seeing the backlog of dark American movies after WWII, named the style film noir — \"black film\" — in 1946.",
    examples: ["The Maltese Falcon", "Double Indemnity", "The Big Sleep"]
  },
  "03": {
    traits: [
      "Humanity is insignificant against vast, unknowable forces",
      "Forbidden knowledge that costs the knower their sanity",
      "Entities beyond human geometry, description, or morality",
      "Dread of the unknown over gore or jump scares"
    ],
    history: "H.P. Lovecraft crystallized the form in 1920s–30s pulp magazines like Weird Tales, building on Arthur Machen and Algernon Blackwood. His 'Cthulhu Mythos' became a shared universe other writers still expand today.",
    examples: ["The Call of Cthulhu", "The Colour Out of Space", "Annihilation"]
  },
  "04": {
    traits: [
      "Crumbling castles, manors, and family estates",
      "Ancestral curses and buried family secrets",
      "The sublime: beauty and terror tangled together",
      "Atmosphere of decay — fog, candlelight, locked rooms"
    ],
    history: "Horace Walpole's The Castle of Otranto (1764) invented the form, Ann Radcliffe perfected the atmosphere, and the 19th century gave it its monuments: Frankenstein, Dracula, and Poe's tales of decaying houses and minds.",
    examples: ["Frankenstein", "Dracula", "The Fall of the House of Usher"]
  },
  "05": {
    traits: [
      "Victorian retro-futurism: brass, gears, goggles, steam",
      "Gentleman inventors and impossible machines",
      "Airships as the signature vehicle",
      "Empire and industry admired and critiqued at once"
    ],
    history: "K.W. Jeter coined the word in 1987 as a joke about Victorian-flavored science fiction, riffing on 'cyberpunk.' The roots go back to Jules Verne and H.G. Wells; Gibson and Sterling's The Difference Engine (1990) made it a movement.",
    examples: ["The Difference Engine", "Perdido Street Station", "Leviathan"]
  },
  "06": {
    traits: [
      "High tech, low life — cutting-edge tools in gutter economies",
      "Megacorporations more powerful than governments",
      "Hackers, AIs, cybernetic bodies, virtual spaces",
      "Neon-noir mood: the future is here and it's rented"
    ],
    history: "Emerged in the early 1980s as a rebellion against clean, optimistic sci-fi, with Philip K. Dick as its patron saint. William Gibson's Neuromancer (1984) defined the genre in a single book and coined 'cyberspace' while at it.",
    examples: ["Neuromancer", "Snow Crash", "Do Androids Dream of Electric Sheep?"]
  },
  "07": {
    traits: [
      "Galactic scale: star empires, fleets, whole worlds at stake",
      "Larger-than-life heroes and operatic emotions",
      "Faster-than-light travel taken for granted",
      "Adventure first, scientific rigor second"
    ],
    history: "Born in 1920s–30s pulps with E.E. 'Doc' Smith's galaxy-spanning serials. The name was coined as an insult in 1941 — like 'soap opera,' but in space — and later reclaimed proudly by writers of the New Space Opera in the 1980s and 90s.",
    examples: ["Dune", "Foundation", "A Fire Upon the Deep"]
  },
  "08": {
    traits: [
      "The frontier: lawless space where character is tested",
      "Lone riders, homesteaders, and men with pasts",
      "Civilization versus wilderness as the core tension",
      "Laconic dialogue; violence that arrives slow, then fast"
    ],
    history: "Grew from dime novels of the 1860s into respectability with Owen Wister's The Virginian (1902) and Zane Grey's bestsellers. Revisionist writers later turned the myth inside out to examine the violence underneath it.",
    examples: ["True Grit", "Lonesome Dove", "Blood Meridian"]
  },
  "09": {
    traits: [
      "Civilization already fell; the story is what's left",
      "Scavenging, shelter, and the economics of scarcity",
      "Ruins of the old world as scenery and warning",
      "Hope measured out one can of food at a time"
    ],
    history: "Mary Shelley's The Last Man (1826) got there first, but the genre exploded after Hiroshima, when the end of the world stopped being hypothetical. Nuclear dread powered the 1950s–60s classics; climate anxiety powers today's.",
    examples: ["The Road", "A Canticle for Leibowitz", "Station Eleven"]
  },
  "10": {
    traits: [
      "A totalitarian state that runs on surveillance and fear",
      "Language, history, and memory under state control",
      "One individual's conscience against the system",
      "The regime presents itself as utopia"
    ],
    history: "The inverted utopia: Yevgeny Zamyatin's We (1924) set the template, Huxley and Orwell built the twin pillars, and Atwood proved the form could be aimed anywhere. A YA boom in the 2000s introduced it to a new generation.",
    examples: ["Nineteen Eighty-Four", "Brave New World", "The Handmaid's Tale"]
  },
  "11": {
    traits: [
      "Optimistic ecological futures — sunlight, not smog",
      "Renewable tech, green cities, repaired ecosystems",
      "Community and craft over corporations and conquest",
      "Conflict resolved by repair rather than destruction"
    ],
    history: "Coined on blogs around 2008 as a deliberate answer to cyberpunk's pessimism: what if the future actually worked? Grown through anthologies and art movements in the 2010s, it's the youngest genre in this machine.",
    examples: ["A Psalm for the Wild-Built", "Sunvault: Stories of Solarpunk", "Pacific Edge"]
  },
  "12": {
    traits: [
      "A fully invented secondary world with its own map and history",
      "Epic quests, chosen ones, ancient evils returning",
      "Magic with rules — swords, runes, and prophecy",
      "Good versus evil at civilizational scale"
    ],
    history: "Myth and saga are ancient, but J.R.R. Tolkien codified the modern form with The Lord of the Rings (1954), drawing on Beowulf and Norse legend. The 1970s–80s paperback boom built an entire publishing category on his foundations.",
    examples: ["The Lord of the Rings", "A Game of Thrones", "The Name of the Wind"]
  },
  "13": {
    traits: [
      "Heightened emotion — feelings drawn at maximum volume",
      "Named special techniques, shouted mid-battle",
      "Training arcs, rivals, and the power of friendship",
      "Tragic backstories revealed at the worst possible moment"
    ],
    history: "Japan's manga and anime tradition took shape under Osamu Tezuka in the 1950s–60s. Weekly Shonen Jump refined the battle-story formula in the 70s–80s — effort, friendship, victory — and the 90s exported it to the world.",
    examples: ["Dragon Ball", "Naruto", "My Hero Academia"]
  },
  "14": {
    traits: [
      "Costumed heroes with powers, codenames, and secret identities",
      "A city in peril and a villain with a monologue",
      "Splash-page action written in bold capitals",
      "Great power, great responsibility — the moral engine"
    ],
    history: "Superman's debut in Action Comics #1 (1938) invented the genre overnight. Marvel humanized it in the 1960s with flawed heroes, and 1986 — Watchmen and The Dark Knight Returns — proved it could interrogate itself.",
    examples: ["Watchmen", "The Dark Knight Returns", "The Amazing Spider-Man"]
  },
  "15": {
    traits: [
      "No spoken dialogue — title cards carry the words",
      "Pantomime acting: the body does the talking",
      "Sight gags, pratfalls, and impossible stunts",
      "Iris shots, cranked film speed, live musical score"
    ],
    history: "Cinema's first language, 1895–1929. Chaplin, Keaton, and Lloyd turned physical comedy into high art before synchronized sound ended the era almost overnight. Its grammar — the close-up, the cut, the chase — still underlies every film.",
    examples: ["Safety Last!", "The General", "City Lights"]
  },
  "16": {
    traits: [
      "Pastel perfection concealing rot — lawns, casseroles, secrets",
      "Conformity as both comfort and menace",
      "Nosy neighbors, block parties, and things unsaid",
      "The dread builds in broad daylight"
    ],
    history: "Postwar suburbia bred its own gothic: Shirley Jackson and Richard Matheson found horror in the cul-de-sac, and The Twilight Zone televised it. Ira Levin's The Stepford Wives (1972) named the fear that the neighbors might be right.",
    examples: ["The Stepford Wives", "The Lottery and Other Stories", "The Twilight Zone: The Monsters Are Due on Maple Street"]
  },
  "17": {
    traits: [
      "Divided cities, dead drops, and tradecraft",
      "Double agents — nobody is only what they seem",
      "Moral gray: our side lies too",
      "The quiet chess match, not the shootout"
    ],
    history: "The Cold War produced two rival schools at once: Ian Fleming's glamorous Bond fantasies and John le Carré's disillusioned realism, written by actual former intelligence officers. Le Carré's Berlin novels defined the serious form.",
    examples: ["The Spy Who Came in from the Cold", "Tinker Tailor Soldier Spy", "From Russia, with Love"]
  },
  "18": {
    traits: [
      "Talking-head interviews and archival footage",
      "Reconstruction of a timeline, piece by piece",
      "Unreliable memory — witnesses contradict each other",
      "The ending is often an open question"
    ],
    history: "Truman Capote's In Cold Blood (1966) invented literary true crime; Errol Morris's The Thin Blue Line (1988) invented the modern documentary form and actually freed its subject. Serial and the streaming boom made it the dominant nonfiction genre of the 2010s.",
    examples: ["In Cold Blood", "The Thin Blue Line", "Serial"]
  },
  "19": {
    traits: [
      "Testimony, cross-examination, objection, verdict",
      "The courtroom as theater — every question a trap",
      "Justice versus the letter of the law",
      "The late reveal that turns the case"
    ],
    history: "Trials have been drama since the Greeks, but the modern genre grew through Perry Mason's 1930s pulps into the American classics of the 1950s–60s. John Grisham's 1990s legal thrillers made it a bestseller category of its own.",
    examples: ["To Kill a Mockingbird", "Twelve Angry Men", "Anatomy of a Murder"]
  },
  "20": {
    traits: [
      "A central love story is the plot, not a subplot",
      "Obstacles: pride, class, distance, bad timing",
      "Emotional beats — the meet, the rift, the grand gesture",
      "An emotionally satisfying ending is the genre's promise"
    ],
    history: "Jane Austen perfected the courtship novel by 1813; Mills & Boon and Harlequin industrialized the form in the 20th century. Today romance is publishing's best-selling genre by a wide margin — and its most rule-aware.",
    examples: ["Pride and Prejudice", "Jane Eyre", "Outlander"]
  },
  "21": {
    traits: [
      "Assemble the crew — each member has one specialty",
      "The plan, shown step by step... then going wrong",
      "The double-cross and the reveal of the real plan",
      "Competence as spectacle: we root for the thieves"
    ],
    history: "A film-born genre: The Asphalt Jungle (1950) and the French classic Rififi (1955) — with its silent 30-minute burglary — set the template. Richard Stark's Parker novels carried it in print; Ocean's Eleven made it a party.",
    examples: ["The Asphalt Jungle", "Rififi", "Ocean's Eleven"]
  },
  "22": {
    traits: [
      "A brilliant sleuth and a baffling case",
      "Clues planted fairly — the reader can play along",
      "Red herrings, alibis, and least-likely suspects",
      "The parlor scene: all is explained"
    ],
    history: "Edgar Allan Poe invented the detective story in 1841 with Dupin; Conan Doyle's Holmes made it immortal. The Golden Age of the 1920s–30s — Christie above all — turned the whodunit into an elegant puzzle with rules.",
    examples: ["The Murders in the Rue Morgue", "The Hound of the Baskervilles", "Murder on the Orient Express"]
  },
  "23": {
    traits: [
      "One protagonist versus nature — no villain required",
      "Cold, hunger, and injury as the antagonists",
      "Competence and improvisation as the drama",
      "Nature is indifferent, which is scarier than cruel"
    ],
    history: "Robinson Crusoe (1719) is the ancestor; Jack London's Klondike naturalism gave the genre its teeth — survival as a test the universe doesn't care if you pass. Gary Paulsen's Hatchet made it a rite of passage for young readers.",
    examples: ["Robinson Crusoe", "To Build a Fire", "Hatchet"]
  },
  "24": {
    traits: [
      "Impossible physics: squash, stretch, and anvils",
      "Instant recovery — flattened, then fine",
      "Gag escalation: each attempt fails bigger",
      "Character is destiny: the schemer always loses"
    ],
    history: "Vaudeville slapstick jumped into animation in the 1930s, and the golden age of Looney Tunes and Tom and Jerry (1940s–50s) perfected the seven-minute gag symphony. Tex Avery pushed the logic to its beautiful breaking point.",
    examples: ["Looney Tunes", "Tom and Jerry", "Tex Avery's MGM shorts"]
  },
  "25": {
    traits: [
      "Gods, demigods, and mortals sharing a stage",
      "Elevated diction: invocations, epithets, formal speech",
      "Hubris punished; fate inescapable",
      "Deeds performed to be remembered in song"
    ],
    history: "The oldest storytelling we have: Gilgamesh is over four thousand years old, and Homer's epics were composed for oral performance around the 8th century BC. Every epic since — Virgil, Milton, modern fantasy — answers them.",
    examples: ["The Epic of Gilgamesh", "The Iliad", "The Odyssey"]
  },
  "26": {
    traits: [
      "A 'what if' premise extrapolated rigorously",
      "Technology and science drive the plot",
      "Aliens, AIs, and futures as mirrors for the present",
      "Sense of wonder anchored by internal logic"
    ],
    history: "Frankenstein (1818) is the usual starting gun; Verne and Wells built the tracks. Hugo Gernsback named 'scientifiction' in his 1926 pulps, and the Golden Age of the 1940s–50s turned it into the literature of ideas.",
    examples: ["Frankenstein", "The War of the Worlds", "The Left Hand of Darkness"]
  },
  "27": {
    traits: [
      "A quest, a map, a deadline",
      "Exotic locales, ancient traps, narrow escapes",
      "A rival hunting the same prize",
      "Physical courage and wit tested in equal measure"
    ],
    history: "The 19th century's gift: Dumas, Stevenson, and H. Rider Haggard sent heroes after treasure and made the journey the point. Pulp serials carried the torch to film, where Indiana Jones repaid the debt with interest.",
    examples: ["Treasure Island", "The Count of Monte Cristo", "King Solomon's Mines"]
  },
  "28": {
    traits: [
      "Ghosts, curses, and the restless dead",
      "The haunting escalates: sounds, sightings, contact",
      "Place with a memory — the house is a character",
      "Dread and atmosphere over gore"
    ],
    history: "The ghost story is ancient, but the Victorians made it an art — told at Christmas, refined by M.R. James into the classic form. Shirley Jackson's Hill House (1959) brought the haunting indoors, into the psyche.",
    examples: ["The Haunting of Hill House", "The Turn of the Screw", "Ghost Stories of an Antiquary"]
  },
  "29": {
    traits: [
      "A real (or realistically framed) life told in arc",
      "The voice of hindsight — older narrator, younger self",
      "Formative episodes chosen for meaning, not completeness",
      "Honesty about failure as the price of admission"
    ],
    history: "Plutarch paired noble lives two thousand years ago; Augustine's Confessions invented inner autobiography. The modern memoir boom of the 1990s onward made the ordinary life, well told, a literary event.",
    examples: ["The Confessions", "The Diary of a Young Girl", "Educated"]
  },
  "30": {
    traits: [
      "Real eras and events, invented lives inside them",
      "Period detail worn accurately but lightly",
      "Ordinary people caught in history's machinery",
      "Research in service of story, not on display"
    ],
    history: "Walter Scott's Waverley (1814) founded the genre; Tolstoy gave it its cathedral in War and Peace. Hilary Mantel's Cromwell trilogy showed a new century that the form could still win every prize in sight.",
    examples: ["War and Peace", "Wolf Hall", "All the Light We Cannot See"]
  },
  "31": {
    traits: [
      "Acts and scenes; stage directions in the text",
      "Dialogue does all the work — no narrator to help",
      "Dramatic irony: the audience knows what characters don't",
      "Written to be performed, not just read"
    ],
    history: "Born in Athens in the 5th century BC with Aeschylus and Sophocles, reborn with Shakespeare, and modernized by Ibsen's living-room realism. The script is the oldest continuously practiced literary form after the epic.",
    examples: ["Hamlet", "A Doll's House", "Death of a Salesman"]
  },
  "32": {
    traits: [
      "Panels, gutters, and the reader's eye doing the editing",
      "Words and pictures carrying meaning together",
      "Captions, balloons, and hand lettering as voice",
      "Time controlled by panel size and page turns"
    ],
    history: "Comic books grew from 1930s newspaper strips; Will Eisner's A Contract with God (1978) popularized the term 'graphic novel' for serious long-form work. Maus won a Pulitzer in 1992 and settled the argument for good.",
    examples: ["Maus", "Persepolis", "A Contract with God"]
  },
  "33": {
    traits: [
      "Reading requires real work — the book's form is an obstacle course",
      "Footnotes, indexes, redactions, and marginalia that contradict the text",
      "Typography as terrain: spiraling, mirrored, or vanishing type",
      "The document itself is a character, and it is not reliable"
    ],
    history: "Espen Aarseth coined the term in 1997 from the Greek ergon and hodos — 'work' and 'path' — for texts that demand nontrivial effort to traverse. The lineage runs from the I Ching through choose-your-own-adventure books to Mark Z. Danielewski's House of Leaves (2000), the genre's haunted cathedral.",
    examples: ["House of Leaves", "Pale Fire", "S."]
  },
  "34": {
    traits: [
      "Protagonists who violate social norms on principle or compulsion",
      "First-person confession — unreliable, uncomfortably intimate",
      "Aimed at consumerism, propriety, and polite institutions",
      "Shock deployed as critique, not just spectacle"
    ],
    history: "The label crystallized in the early 1990s, but the tradition is old: the Marquis de Sade, Baudelaire's obscenity trial, and the 1960s court battles over Burroughs' Naked Lunch all cleared the road. Chuck Palahniuk's Fight Club (1996) dragged the mode into the mainstream, swinging.",
    examples: ["Fight Club", "Trainspotting", "American Psycho"]
  },
  "35": {
    traits: [
      "Climate change as setting, antagonist, and moral question at once",
      "Near futures: floods, fire seasons, migration, adaptation",
      "Science kept plausible — the horror is the forecast",
      "Grief and hope held for the same coastline"
    ],
    history: "Journalist Dan Bloom coined 'cli-fi' around 2008, but J.G. Ballard's The Drowned World (1962) and Octavia Butler's Parable of the Sower (1993) got there decades early. Kim Stanley Robinson turned it into a literature of policy, repair, and stubborn hope.",
    examples: ["Parable of the Sower", "The Ministry for the Future", "Flight Behavior"]
  },
  "36": {
    traits: [
      "Reality slightly, unapologetically wrong",
      "The strangeness is never explained and never resolved",
      "Literary craft over genre plot mechanics",
      "Leaves the reader feeling 'very strange' — which is the point"
    ],
    history: "Bruce Sterling coined the term in a 1989 essay for fiction that 'makes you feel very strange, the way that living in the twentieth century makes you feel.' It names the borderland between literary fiction and the fantastic — Kafka's country, with Murakami and Kelly Link as later cartographers.",
    examples: ["The Metamorphosis", "Kafka on the Shore", "Magic for Beginners"]
  },
  "37": {
    traits: [
      "Set in the afterlife, which functions like a working society",
      "The famous dead mingle across eras as characters",
      "Death is the premise, not the tragedy — the tone stays light",
      "Celestial bureaucracy: gates, ledgers, waiting rooms, committees"
    ],
    history: "Named for John Kendrick Bangs, whose A House-Boat on the Styx (1895) ran the afterlife as a gentlemen's club where Shakespeare, Napoleon, and Dr. Johnson bicker eternally. The mode is older — Lucian's Dialogues of the Dead did it in the 2nd century — and it survives everywhere from Riverworld to The Good Place.",
    examples: ["A House-Boat on the Styx", "To Your Scattered Bodies Go", "The Brief History of the Dead"]
  },
  "38": {
    traits: [
      "Comedy mined from death, disaster, and taboo",
      "Deadpan delivery — the horror plays it absolutely straight",
      "Satire of institutions that process tragedy into paperwork",
      "Laughter as both defense and indictment"
    ],
    history: "André Breton coined 'humour noir' in 1940 and named Jonathan Swift its ancestor — A Modest Proposal (1729) remains the template. The mode flowered after World War II, when Heller's Catch-22 and Vonnegut's Slaughterhouse-Five decided the only sane answer to the machinery of death was a horrible laugh.",
    examples: ["Catch-22", "A Modest Proposal", "Slaughterhouse-Five"]
  },
  "39": {
    traits: [
      "Miracles narrated in the same tone as breakfast",
      "The fantastic is ordinary — nobody in the story is surprised",
      "Rooted in family, village, and generational memory",
      "Ghosts, prophecies, and time loops as everyday furniture"
    ],
    history: "Art critic Franz Roh coined the term in 1925 for painting; Latin American writers made it a literature. Gabriel García Márquez's One Hundred Years of Solitude (1967) is the defining book, and Toni Morrison, Isabel Allende, and Salman Rushdie proved the mode travels anywhere history leaves ghosts.",
    examples: ["One Hundred Years of Solitude", "Beloved", "The House of the Spirits"]
  },
  "40": {
    traits: [
      "Story told entirely through documents — letters, diaries, reports",
      "Multiple unreliable voices the reader must triangulate",
      "The intimacy of reading someone else's mail",
      "The gaps between documents carry the plot"
    ],
    history: "One of the novel's oldest forms: Samuel Richardson's Pamela (1740) helped invent the English novel as a stack of letters, and Dracula (1897) proved documents could do horror. Email, transcripts, and group chats keep reinventing it for every new medium.",
    examples: ["Dracula", "The Color Purple", "Frankenstein"]
  }
};
