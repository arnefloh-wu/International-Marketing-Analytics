#!/usr/bin/env python3
"""Insert the "Module Convenor" and "Work Experience" slides into a WU-template deck.

Usage:
    python add_instructor_slides.py TARGET.pptx [-o OUT.pptx] [--after N] [--footer TEXT] [--force]

The two slides (with photo, logos, book covers, hyperlinks) come from
../assets/instructor-slides.pptx. They are placed on the target deck's own
"Titel und Inhalt" layout, so they take on the target's fonts, colours and logo.
Without -o the target file is overwritten (keep it under version control).
Only the standard library is used.
"""
import argparse, posixpath, re, sys, zipfile
from pathlib import Path

ASSET = Path(__file__).resolve().parent.parent / "assets" / "instructor-slides.pptx"
NS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
CT_SLIDE = "application/vnd.openxmlformats-officedocument.presentationml.slide+xml"
IMG_CT = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
          "tif": "image/tiff", "tiff": "image/tiff", "gif": "image/gif"}
LAYOUT_NAMES = ("titel und inhalt", "title and content")


def read_all(path):
    with zipfile.ZipFile(path) as z:
        return {n: z.read(n) for n in z.namelist()}


def text(parts, name):
    return parts[name].decode("utf-8")


def slide_order(parts):
    """Slide part names in presentation order."""
    pres = text(parts, "ppt/presentation.xml")
    rels = text(parts, "ppt/_rels/presentation.xml.rels")
    target = {}
    for r in re.findall(r"<Relationship [^>]*>", rels):
        target[re.search(r'Id="([^"]+)"', r).group(1)] = re.search(r'Target="([^"]+)"', r).group(1)
    return [posixpath.normpath(posixpath.join("ppt", target[i])) for i in
            re.findall(r'<p:sldId [^>]*r:id="([^"]+)"', pres)]


def slide_size(parts):
    m = re.search(r'<p:sldSz cx="(\d+)" cy="(\d+)"', text(parts, "ppt/presentation.xml"))
    return m.groups()


def find_layout(parts):
    found = {}
    for n in parts:
        if re.fullmatch(r"ppt/slideLayouts/slideLayout\d+\.xml", n):
            name = re.search(r'<p:cSld name="([^"]*)"', text(parts, n))
            if name:
                found[n] = name.group(1)
    for exact in (True, False):
        for n, name in sorted(found.items()):
            norm = re.sub(r"^\d+_", "", name).strip().lower()
            if (name.strip().lower() in LAYOUT_NAMES) if exact else (norm in LAYOUT_NAMES):
                return n
    sys.exit('No layout named "Titel und Inhalt" in the target. Layouts: ' + ", ".join(sorted(set(found.values()))))


def target_footer(parts, order):
    for n in order:
        x = text(parts, n)
        for sp in re.findall(r"<p:sp>.*?</p:sp>", x, re.S):
            if re.search(r'<p:ph[^>]*type="ftr"', sp):
                t = "".join(re.findall(r"<a:t>([^<]*)</a:t>", sp)).strip()
                if t:
                    return t
    return ""


def set_footer(xml, footer):
    def fix(m):
        sp = m.group(0)
        if not re.search(r'<p:ph[^>]*type="ftr"', sp):
            return sp
        runs = list(re.finditer(r"<a:t>[^<]*</a:t>", sp))
        if not runs:
            return sp
        first = True
        for r in reversed(runs):
            sp = sp[:r.start()] + (f"<a:t>{footer}</a:t>" if r is runs[0] else "<a:t></a:t>") + sp[r.end():]
        return sp
    return re.sub(r"<p:sp>.*?</p:sp>", fix, xml, flags=re.S)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target"); ap.add_argument("-o", "--output")
    ap.add_argument("--after", type=int, default=1, help="insert after this slide number (default 1, the title slide)")
    ap.add_argument("--footer", help="footer text for the new slides (default: the target's own footer text)")
    ap.add_argument("--force", action="store_true", help="insert even if a Module Convenor slide exists or the slide size differs")
    a = ap.parse_args()

    tgt = read_all(a.target); src = read_all(ASSET)
    t_order = slide_order(tgt)
    if not a.force:
        if slide_size(tgt) != slide_size(src):
            sys.exit(f"Slide size differs (target {slide_size(tgt)}, assets {slide_size(src)}); the slides would not fit. Use --force to insert anyway.")
        for n in t_order:
            if "ModuleConvenor" in "".join(re.findall(r"<a:t>([^<]*)</a:t>", text(tgt, n))).replace(" ", ""):
                sys.exit(f"{n} already contains a Module Convenor slide; nothing to do (use --force to add again).")
    if not 0 <= a.after <= len(t_order):
        sys.exit(f"--after must be between 0 and {len(t_order)}")

    layout = find_layout(tgt)
    footer = a.footer if a.footer is not None else target_footer(tgt, t_order)
    s_order = slide_order(src)

    n_slide = max([int(re.search(r"slide(\d+)\.xml", n).group(1)) for n in tgt if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)] + [0])
    ct = text(tgt, "[Content_Types].xml")
    prel = text(tgt, "ppt/_rels/presentation.xml.rels"); pres = text(tgt, "ppt/presentation.xml")
    rid_n = max(int(i) for i in re.findall(r'Id="rId(\d+)"', prel))
    sld_id = max(int(i) for i in re.findall(r'<p:sldId id="(\d+)"', pres))
    new_ids, media_done = [], {}

    for sname in s_order:
        n_slide += 1; rid_n += 1; sld_id += 1
        new = f"ppt/slides/slide{n_slide}.xml"
        xml = text(src, sname)
        if footer is not None:
            xml = set_footer(xml, footer)
        tgt[new] = xml.encode("utf-8")
        srels = text(src, f"ppt/slides/_rels/{posixpath.basename(sname)}.rels")
        out = []
        for r in re.findall(r"<Relationship [^>]*/>", srels):
            typ = re.search(r'Type="([^"]+)"', r).group(1).rsplit("/", 1)[-1]
            if typ == "slideLayout":
                r = re.sub(r'Target="[^"]+"', f'Target="../slideLayouts/{posixpath.basename(layout)}"', r)
            elif typ == "image":
                old = posixpath.normpath(posixpath.join("ppt/slides", re.search(r'Target="([^"]+)"', r).group(1)))
                if old not in media_done:
                    base = posixpath.basename(old)
                    media_done[old] = "ppt/media/instr_" + base
                    tgt[media_done[old]] = src[old]
                    ext = base.rsplit(".", 1)[-1].lower()
                    if ext in IMG_CT and f'Extension="{ext}"' not in ct:
                        ct = ct.replace("<Override", f'<Default Extension="{ext}" ContentType="{IMG_CT[ext]}"/><Override', 1)
                r = re.sub(r'Target="[^"]+"', f'Target="../media/{posixpath.basename(media_done[old])}"', r)
            elif typ == "hyperlink":
                pass
            else:                       # notes, charts etc. are not carried over
                continue
            out.append(r)
        tgt[f"ppt/slides/_rels/slide{n_slide}.xml.rels"] = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + "".join(out) + "</Relationships>").encode("utf-8")
        ct = ct.replace("</Types>", f'<Override PartName="/{new}" ContentType="{CT_SLIDE}"/></Types>')
        prel = prel.replace("</Relationships>", f'<Relationship Id="rId{rid_n}" Type="{NS_REL}/slide" Target="slides/slide{n_slide}.xml"/></Relationships>')
        new_ids.append(f'<p:sldId id="{sld_id}" r:id="rId{rid_n}"/>')

    ids = re.findall(r"<p:sldId [^>]*/>", pres)
    ids[a.after:a.after] = new_ids
    pres = re.sub(r"<p:sldIdLst>.*?</p:sldIdLst>", "<p:sldIdLst>" + "".join(ids) + "</p:sldIdLst>", pres, flags=re.S)
    tgt["[Content_Types].xml"] = ct.encode("utf-8"); tgt["ppt/_rels/presentation.xml.rels"] = prel.encode("utf-8"); tgt["ppt/presentation.xml"] = pres.encode("utf-8")

    out_path = Path(a.output or a.target)
    tmp = out_path.with_suffix(out_path.suffix + ".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", tgt.pop("[Content_Types].xml"))
        for n, b in tgt.items():
            if not n.endswith("/"):
                z.writestr(n, b)
    tmp.replace(out_path)
    print(f"added 2 slides after slide {a.after} of {len(t_order)} using layout {posixpath.basename(layout)}; footer {footer!r}; wrote {out_path}")


if __name__ == "__main__":
    main()
