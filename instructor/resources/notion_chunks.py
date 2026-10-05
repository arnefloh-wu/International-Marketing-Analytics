"""Turn <topic>-notion.json into Notion-flavoured Markdown table chunks, one file per category."""
import json, re, sys
from pathlib import Path
topic = sys.argv[1]
ROOT = Path(__file__).resolve().parent
rows = json.loads((ROOT / f"{topic}-notion.json").read_text())
ORDER = ["Bücher", "Journal Articles", "Reports", "Websites / Blogs", "(Video-) Tutorials", "Cases for Teaching",
         "Praxisbeispiele", "Software", "stat. Methoden", "Data", "Personenkontakte", "Communities & Events"]
def esc(s):
    s = re.sub(r"\s+", " ", s or "").strip().replace("`", "")
    return re.sub(r"([\\*~`$\[\]<>{}|^])", r"\\\1", s)
def link(u):
    u = (u or "").strip()
    if not u:
        return ""
    if re.search(r"[\s()<>\[\]]", u):
        return esc(u)
    return f"[{esc(u)}]({u})"
out = ROOT / f"{topic}-notion-chunks"; out.mkdir(exist_ok=True)
for f in out.glob("*.md"): f.unlink()
cats = [c for c in ORDER if any(r["category"] == c for r in rows)] + sorted({r["category"] for r in rows} - set(ORDER))
for i, cat in enumerate(cats, 1):
    rs = [r for r in rows if r["category"] == cat]
    lines = [f"### {esc(cat)} ({len(rs)})", '<table fit-page-width="true" header-row="true">',
             "\t<tr>", "\t\t<td>Kategorie</td>", "\t\t<td>Titel / Name</td>", "\t\t<td>Autor / Quelle / Firma</td>",
             "\t\t<td>Link</td>", "\t\t<td>Notiz</td>", "\t\t<td>Verwendung im Kurs</td>", "\t\t<td>Status</td>", "\t</tr>"]
    for r in rs:
        lines += ["\t<tr>", f"\t\t<td>{esc(cat)}</td>", f"\t\t<td>{esc(r['title'])}</td>", f"\t\t<td>{esc(r['source'])}</td>",
                  f"\t\t<td>{link(r['link'])}</td>", f"\t\t<td>{esc(r['note'])}</td>", f"\t\t<td>{esc(r['use'])}</td>", f"\t\t<td>{esc(r['status'])}</td>", "\t</tr>"]
    lines.append("</table>")
    (out / f"{i:02d}-{re.sub(r'[^a-z0-9]+','-',cat.lower()).strip('-')}.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"{i:02d} {cat}: {len(rs)} rows, {sum(len(l) for l in lines)} chars")
