---
name: polish-slides
description: Polish a PowerPoint deck so it looks finished and consistent, especially one built on a corporate template such as the WU template. Use this whenever the user asks to polish, clean up, tidy, fix the layout of, or QA a .pptx or slide deck, or says slides look cramped, overflow, are inconsistent, or "not appealing", and also right after you generate or edit any deck, before presenting it to the user. Covers rendering the deck to images, finding overflow and leftover template text, fixing layout and typography inside the template's placeholders, and validating the file.
---

# Polish slides

A deck is polished when it looks like one person designed it, nothing overflows, nothing is left over from the template, and every slide earns its place. The way to get there is to look at the rendered slides, fix what you see, and look again. Reading the XML alone misses most problems, because overflow, odd wrapping and empty space only show up when rendered.

Use the `pptx` skill for the mechanics of editing OOXML (unzip, edit slide XML, zip, validate). This skill is the quality pass on top of it.

## Workflow

1. **Render and measure.** Run `python scripts/check_deck.py deck.pptx <outdir>` (path relative to this skill). It converts the deck to PDF, writes contact sheets (`sheet-N.jpg`, six slides each) and per-slide PNGs, and lists likely problems: text running off the slide, fonts below 10.5 pt, leftover placeholder text, nearly empty slides. Treat the list as hints; the images are the ground truth.
2. **Look at every sheet.** Check the items under "What to look for". Note each fix as a short list before editing, so you change things deliberately instead of nudging at random.
3. **Fix inside the template.** Work through the template's placeholders and layouts (see "Templates"); if a slide uses free text boxes or the wrong layout, move its content into the right layout from `assets/template.pptx`. Re-render after the fixes and look again; the first fix often shifts something else.
4. **Validate the file.** Run the `pptx` skill's `validate.py` with `--original <template>` for template-derived decks. A deck that renders fine can still be refused by PowerPoint.
5. **Report honestly.** Say what you changed, what you could not check (fonts that were substituted in the preview, content you did not verify), and anything that needs a human decision.

## What to look for

- **Overflow and cut-off text.** Fix by cutting words first, then splitting the slide, and shrinking the font last. A slide that needs 10 pt text has too much on it.
- **Title wrapping to two lines** where the layout expects one: shorten the title rather than shrinking it. A two-line title is acceptable only if the layout has room for it.
- **Big empty areas.** A bullet list that fills the top third of a slide looks unfinished. Prefer a two-column layout, a table, a picture, or a larger body size (14 to 16 pt) before adding filler. Leave space where it helps reading; fix space that looks accidental.
- **Wrapped numbers and units.** Use a non-breaking space (U+00A0) between a number and its unit or percent sign ("20 %", "15 min") so it never splits across lines.
- **Inconsistent patterns.** Same kind of content, same layout: all section dividers alike, all two-column slides built the same way, bullet depth no deeper than two levels. Vary layouts across *different* kinds of content, not randomly.
- **Leftover template content.** Sample text, "Sample Footer", slide numbers or footers that still describe the template, unused placeholders showing prompt text, stray pictures. Delete the whole unused shape, not just its text, or it keeps its frame and prompt.
- **Weak slides.** Text-only slides with a long paragraph are the usual culprit. Turn paragraphs into 3 to 5 short bullets with a bold lead-in ("**Positioning:** ...") or move them to speaker notes. Add a picture or logo when the source material provides one that fits.
- **Links and contact details.** Check each hyperlink is attached to the intended text and points to the right target; mailto links for e-mail addresses.
- **Language and spelling.** One language and one spelling variant (for example British English) throughout, with the language tag set accordingly so spell-check does not underline everything.

## Templates

Corporate templates (WU, university or company masters) define fonts, colours, logo, footer and slide numbers on the master and layouts. Respect them; this is what makes the deck look official.

**Default template.** For WU decks, start from `assets/template.pptx` in this skill folder (`assets/template.potx` is the same master without sample slides). Open its sample slides to see what each layout looks like, copy the one you need, and fill in its placeholders. Layout names are German because the template's are.

| Purpose | Layout |
|---|---|
| Title slide | Titelfolie, or Titelfolie Kontakt, whose info box already shows the presenter's name, e-mail and office-hours link; the "kurz" variants suit one-line titles |
| Section divider (short text only) | Kapitelfolie, Kapitelfolie kurz |
| Bullets | Titel und Inhalt |
| Two columns | Zwei Inhalte; with a coloured heading over each column: Zwei Inhalte Vergleich |
| Text with a photo, optionally a logo in the photo's corner (company, product or person introductions) | Inhalt und Bild mit Logo |
| Table | Titel und Tabelle (insert the table through the placeholder) |
| Large chart or graphic | Nur Titel |
| Closing / contact card | Abschlussfolie Kontakt (business card already filled in); plain Abschlussfolie for another person |

**Presenter details.** Titelfolie Kontakt and Abschlussfolie Kontakt carry these as fixed text, so a new deck needs no typing. The layouts hold the text as fixed shapes, not placeholders, because PowerPoint shows placeholder text only as a grey prompt that disappears on new slides.

- Dr Arne Floh, Senior Lecturer in Marketing, WU Vienna, Institute for International Business, Welthandelsplatz 1, 1020 Vienna, Austria
- E-mail `arne.floh@wu.ac.at`, web `https://www.wu.ac.at/en/welthandel/arne-floh/`, phone labelled "F" +43-31336-6367 (as in the syllabus), office hours via the booking calendar `https://calendar.app.google/o4FuKoF1YcarRfnC8`
- Use only these details on slides; do not add private numbers or addresses found elsewhere (for example in e-mails). If a detail changes, edit it in both `assets/template.pptx` and `assets/template.potx` (layouts 16 and 19) and update this list.

Rules that keep the result consistent:

- Fill the layout's own placeholders (title, content, the two headings of a comparison layout, the picture and logo placeholders). Avoid free text boxes, which ignore the template's fonts and spacing.
- Do not edit the master or layouts to make one slide fit. Change the content or pick a different layout. If the same need keeps coming back, add a layout to the template once, in both `assets/template.pptx` and `assets/template.potx`, instead of fixing it slide by slide. If the template says not to touch the footer on the master (the WU one does), set footer text per slide.
- Copy a template slide for each new slide instead of building shapes by hand, and finish all adding, deleting and reordering before filling in text, because copies clone whatever is on the source slide. A copied sample slide can carry its own position or size overrides that mask the layout; clear them (an empty `<p:spPr/>`) when the layout should decide.
- Keep the template's typography. For WU that means Georgia titles and Verdana body, with 16 pt running text as the default; go down to 14 pt for dense two-column slides and do not go below 12 pt for body text.

## Fonts and the preview

The preview is rendered by LibreOffice, which substitutes fonts it does not have (Georgia and Verdana among them). Substitutes are often wider, so a slide that fits in the preview will usually fit in PowerPoint, but exact line breaks differ. Say so when you hand over the deck, and leave a little slack in tight boxes instead of fitting them to the pixel.

## Hand-over

Save the `.pptx` and a PDF export together. If the user cannot open a preview inline, they can download the files; avoid spaces in file names when a preview fails. When the deck goes to the repository, commit both files and mention what was not verified.
