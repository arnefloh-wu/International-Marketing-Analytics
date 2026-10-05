"""Adapt the instructor profile slides added by the add-instructor-slide skill to this deck.

- Type sizes: slide titles 16 pt, card heading 15 pt.
- Module Convenor slide: the two cards (personal, contact) are merged into one card,
  with a thin divider between the two columns, and the contact column gets a link
  to the online office-hours calendar next to the e-mail address.

The skill's asset is not changed; this only edits the deck passed in.

usage: python slides/finish_profile_slides.py DECK.pptx
"""
import copy
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, PP_PLACEHOLDER
from pptx.util import Emu, Pt

CALENDAR = "https://calendar.app.google/o4FuKoF1YcarRfnC8"


def I(x):
    return Emu(int(round(x * 914400)))


path = sys.argv[1]
prs = Presentation(path)
done = 0
for slide in prs.slides:
    titles = [sh for sh in slide.placeholders
              if sh.placeholder_format.type in (PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE)]
    title = titles[0] if titles else None     # the asset's title placeholder has a non-zero idx
    if title is None or not title.text_frame.text.startswith("Module Convenor"):
        continue
    for p in title.text_frame.paragraphs:
        for r in p.runs:
            r.font.size = Pt(16)
    shapes = {sh.name: sh for sh in slide.shapes}
    if "Card header Contact Information" in shapes:
        # merge: widen the personal card over both columns, drop the contact card frame
        for name in ("Card body Contact Information", "Card header Contact Information"):
            shapes[name]._element.getparent().remove(shapes[name]._element)
        body, head = shapes["Card body Personal Information"], shapes["Card header Personal Information"]
        right = I(9.5)
        body.width = right - body.left
        head.width = right - head.left
        body.name, head.name = "Card body Convenor", "Card header Convenor"
        p = head.text_frame.paragraphs[0]
        p.runs[0].text = "Personal and contact information"
        for r in p.runs[1:]:
            r._r.getparent().remove(r._r)
        # thin white divider between the two columns, drawn right after the card body
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, I(5.6), body.top + I(0.75), I(0.02), body.height - I(0.95))
        div.name = "Card divider"
        div.fill.solid(); div.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        div.line.fill.background()
        body._element.addnext(div._element)
        # contact column: office hours with the online booking link
        contact = shapes["Contact text"]
        paras = contact.text_frame.paragraphs
        email = next(pp for pp in paras if "@" in pp.text)
        office = next(pp for pp in paras if "ffice" in pp.text)
        new = copy.deepcopy(email._p)
        office._p.addnext(new)
        office._p.getparent().remove(office._p)
        np_ = [pp for pp in contact.text_frame.paragraphs if pp._p is new][0]
        np_.runs[0].text = "Office hours: "
        np_.runs[1].text = "book online (Google Calendar)"
        np_.runs[1].hyperlink.address = CALENDAR
    for sh in slide.shapes:
        if sh.name.startswith("Card header") and sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(15)
    done += 1
prs.save(path)
print(f"profile slides adjusted: {done}")
