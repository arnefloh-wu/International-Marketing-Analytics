"""Merge research-agent parts into one guide, a CSV source list and Notion table rows.

usage: python instructor/resources/build_guide.py <topic> <part-file> [<part-file> ...]
topic: mmm | positron | python | regression

Writes:
  instructor/resources/<topic>-resource-guide.md   (merged guide)
  instructor/resources/<topic>-sources.csv         (Kategorie, Titel, Autor/Quelle, Link, Notiz, Verwendung im Kurs, Status)
  instructor/resources/<topic>-notion.json         (rows for the Notion table, deduplicated against existing-<topic>.json if present)
"""
import csv
import json
import re
import sys
from pathlib import Path

topic, *parts = sys.argv[1:]
ROOT = Path(__file__).resolve().parent
TITLES = {
    "mmm": "Marketing mix modelling: resource guide",
    "positron": "Positron and AI-assisted analytics: resource guide",
    "python": "Python data-analysis stack (polars, plotnine, Great Tables, Quarto): resource guide",
    "regression": "Regression analysis in Python: resource guide",
}
# map section headings (lower-case substrings) to the Notion category labels
CATS = [
    ("teaching case", "Cases for Teaching"), ("course example", "Cases for Teaching"),
    ("book", "Bücher"), ("journal", "Journal Articles"), ("report", "Reports"),
    ("website", "Websites / Blogs"), ("documentation", "Websites / Blogs"), ("blog", "Websites / Blogs"),
    ("video", "(Video-) Tutorials"), ("tutorial", "(Video-) Tutorials"), ("course", "(Video-) Tutorials"),
    ("teaching case", "Cases for Teaching"), ("cases", "Cases for Teaching"), ("case", "Cases for Teaching"),
    ("practice", "Praxisbeispiele"), ("real-world", "Praxisbeispiele"), ("real world", "Praxisbeispiele"), ("example", "Praxisbeispiele"),
    ("software", "Software"), ("statistical method", "stat. Methoden"), ("method", "stat. Methoden"),
    ("people", "Personenkontakte"), ("guest", "Personenkontakte"), ("communit", "Communities & Events"), ("conference", "Communities & Events"),
    ("dataset", "Data"), ("data", "Data"),
]


def category_for(heading: str) -> str:
    h = heading.lower()
    for key, label in CATS:
        if key in h:
            return label
    return heading.strip("# ").strip()


def norm_url(u: str) -> str:
    u = u.strip().lower()
    u = re.sub(r"^https?://(www\.)?", "", u)
    base, _, query = u.partition("?")
    base = base.split("#")[0].rstrip("/")
    keep = [kv for kv in query.split("&") if kv and not re.match(r"^(utm_|si=|rlkey=|trackingid=|st=|dl=|pvs=|ref=|fbclid=)", kv)]
    return base + ("?" + "&".join(sorted(keep)) if keep else "")


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def first_url(s: str) -> str:
    m = re.search(r"https?://[^\s)\]>]+", s)
    return m.group(0).rstrip(".,;") if m else ""


entries, guide_body = [], []
for part in parts:
    text = Path(part).read_text(encoding="utf-8")
    guide_body.append(text)
    section, sub = "", ""
    cur = None
    for line in text.splitlines():
        if re.match(r"^#{1,2} ", line) and not line.startswith("# Part") and line.lstrip("#").strip().lower() not in ("", TITLES[topic].lower()):
            section, sub = line.lstrip("#").strip(), ""
            cur = None
        elif line.startswith("### ") and not re.match(r"^### \d[a-z]?\.", line):
            cat = category_for(section)
            if cat == section.strip("# ").strip() and sub:
                cat = category_for(sub)
            cur = {"category": cat, "section": sub or section, "title": line[4:].strip(),
                   "source": "", "link": "", "why": "", "use": ""}
            entries.append(cur)
        elif cur is not None and line.startswith("- **"):
            m = re.match(r"- \*\*(.+?):\*\*\s*(.*)", line)
            if not m:
                continue
            key, val = m.group(1).lower(), m.group(2).strip()
            if key.startswith("source"):
                cur["source"] = val
            elif key.startswith("link"):
                cur["link"] = first_url(val) or val
                cur["link_raw"] = val
            elif key.startswith("why"):
                cur["why"] = val
            elif key.startswith("use"):
                cur["use"] = val
        elif line.startswith("### ") and cur is None:
            # numbered sub-heading like "### 1a. Global thought leaders": treat as sub-section
            sub = line[4:].strip()

# verification status from the text
for e in entries:
    blob = " ".join([e.get("link_raw", ""), e["source"], e["why"], e["use"]]).lower()
    if "unverified" in blob or "doi unverified" in blob:
        e["status"] = "neu; Link ungeprüft"
    elif "search-confirmed" in blob or "confirmed in search" in blob or "search result" in blob:
        e["status"] = "neu; in Suchergebnis bestätigt"
    else:
        e["status"] = "neu; Link geprüft"
    e["note"] = re.sub(r"\s+", " ", e["why"])[:400]
    e["use"] = re.sub(r"\s+", " ", e["use"])[:300]

# dedupe within and against existing Notion rows
existing_path = ROOT / f"existing-{topic}.json"
existing = json.loads(existing_path.read_text()) if existing_path.exists() else []
seen_urls = {norm_url(x["link"]) for x in existing if x.get("link")}
seen_titles = {norm_title(x["title"]) for x in existing if x.get("title")}
existing_titles = set(seen_titles)
kept, dropped, run_titles = [], [], set()
for e in entries:
    nu, nt = norm_url(e["link"]), norm_title(e["title"])
    dup_existing = (nu and nu in seen_urls) or (nt in existing_titles) or any((nt in t or t in nt) for t in existing_titles if len(nt) > 25 and len(t) > 25)
    dup_run = nt in run_titles
    if dup_existing or dup_run:
        dropped.append(e["title"] + ("  [already in Notion]" if dup_existing else "  [twice in parts]"))
        continue
    run_titles.add(nt)
    kept.append(e)

# outputs
guide = [f"# {TITLES[topic]}", "",
         "Compiled on 5 October 2026 by parallel research agents for the course International Marketing Analytics (WU Vienna). "
         "Entries are ranked best first within each section. Links marked (unverified) or search-confirmed could not be fetched from the build environment and should be checked once before use.",
         "", f"Total entries: {len(entries)}; new relative to the existing Notion list: {len(kept)}.", "", "---", ""]
guide += guide_body
(ROOT / f"{topic}-resource-guide.md").write_text("\n".join(guide), encoding="utf-8")

with (ROOT / f"{topic}-sources.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Kategorie", "Titel", "Autor / Quelle", "Link", "Notiz", "Verwendung im Kurs", "Status"])
    for e in entries:
        w.writerow([e["category"], e["title"], e["source"], e["link"], e["note"], e["use"], e["status"]])

(ROOT / f"{topic}-notion.json").write_text(json.dumps(kept, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"entries {len(entries)}, new for Notion {len(kept)}, duplicates dropped {len(dropped)}")
for d in dropped:
    print("  dup:", d)
from collections import Counter
print(Counter(e["category"] for e in kept))
