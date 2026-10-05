---
name: add-instructor-slide
description: Add the instructor's two profile slides, "Module Convenor – Dr Arne Floh" (personal and contact information with photo) and "Work Experience" (background, teaching, research, private interests, with logos and book covers), to a PowerPoint deck. Use this whenever the user wants an instructor, convenor, "about me", lecturer-introduction, profile, bio or work-experience slide added to a slide deck or lecture, or wants the same two intro slides in the decks of another course or repository, even if they only say "add my intro slides" or "put my slides at the start of the deck". Works on decks built on the WU template.
---

# Add instructor slides

Two ready-made slides live in `assets/instructor-slides.pptx`, designed by the instructor on the WU template:

1. **Module Convenor – Dr Arne Floh:** photo at the top right, two cards. *Personal information* (Senior Lecturer in International Marketing, WU Vienna; Deputy Program Director Export- und Internationalisierungsmanagement; web page; LinkedIn) and *Contact information* (telephone, e-mail, room, office hours).
2. **Work Experience:** an outline (international and industry background, teaching, research, private interests) with the logos of the universities worked with, book covers, and pictures of research topics and hobbies.

`scripts/add_instructor_slides.py` copies them, with pictures and links, into any deck on the WU template. It needs only Python 3.

## Workflow

1. **Find the target deck** (a `.pptx` in the repository). It must use the WU 16:10 template; the script stops if the slide size differs. If the deck is not on the WU template, build it on the template first (see the `polish-slides` skill).
2. **Run the script** from this skill's folder:
   `python scripts/add_instructor_slides.py path/to/deck.pptx --after 1`
   - `--after N` inserts after slide N; the default 1 puts the profile slides right behind the title slide. Use `--after 0` to open the deck with them.
   - Without `-o out.pptx` the deck is overwritten. That is safe in a git repository because history keeps the old version; add `-o` to keep the original untouched.
   - The slides use the target deck's own layout "Titel und Inhalt" (found by name), so they take on that deck's fonts, colours and logo. Their footer takes the footer text of the target deck's other slides; pass `--footer "text"` to set it.
   - Running it twice does nothing; the script reports that the Module Convenor slide already exists. `--force` adds them again.
3. **Validate and look.** Run the `pptx` skill's `scripts/office/validate.py deck.pptx --original <deck before the change>`, then render the deck (for example with `polish-slides/scripts/check_deck.py`) and look at the two new slides. The preview uses substitute fonts, so judge text fit with some tolerance. Known point to check: the title "Module Convenor – Dr Arne Floh" shares its line with the photo; if the last letters touch the photo in PowerPoint, shorten the title to "Dr Arne Floh" or move the photo slightly left on both slides.
4. **Commit** the changed deck. The photos are large; the slides added about 2 MB to the deck.

## Changing the content

The content is the asset itself. To update a phone number, role or the pictures, open `assets/instructor-slides.pptx` in PowerPoint, edit the two slides, and save it under the same name. Everything the script copies comes from that file, so the next deck gets the new version. Keep these fixed: two slides only, in the order Module Convenor, Work Experience, on the layout "Titel und Inhalt". Do not shrink the pictures further; they are already downscaled to keep the skill small.

Use only details that are on the slides. Do not add private contact data found elsewhere (for example in e-mails) to a deck.

## Using this skill in another repository

Copy the whole folder `.claude/skills/add-instructor-slide/` (SKILL.md, `scripts/`, `assets/`) into that repository's `.claude/skills/` and commit it. Nothing else is needed; the script finds the asset next to itself. For all repositories on one machine, copy the folder to `~/.claude/skills/` instead. When the slides change in one place, copy the updated `assets/instructor-slides.pptx` to the other copies so the decks stay consistent.
