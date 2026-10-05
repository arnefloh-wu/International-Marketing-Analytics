"""Render the Quarto demo (slides/quarto_demo/report.qmd) to HTML, PDF (Typst), Word and
reveal.js, and save one thumbnail per format to slides/figures/quarto_*.png for the set-up deck.

usage: python slides/make_quarto_figures.py   (repository root, course .venv; needs quarto,
LibreOffice for Word, pdftoppm, and headless Chromium at $CHROMIUM or /opt/pw-browsers/chromium)
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures"
CHROMIUM = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
env = dict(os.environ, QUARTO_PYTHON=sys.executable)

work = Path(tempfile.mkdtemp())
shutil.copy(ROOT / "quarto_demo" / "report.qmd", work / "report.qmd")
(work / "data").symlink_to(ROOT.parent / "data")          # the qmd reads data/ like a project root
for fmt in ("html", "typst", "docx", "revealjs"):
    subprocess.run(["quarto", "render", "report.qmd", "--to", fmt, "-M", "embed-resources:true"],
                   cwd=work, env=env, check=True, capture_output=True)
    if fmt in ("html", "revealjs"):                       # both write report.html
        shutil.move(work / "report.html", work / ("page.html" if fmt == "html" else "slides.html"))


def shot(html, png, size):
    subprocess.run([CHROMIUM, "--headless", "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=1.5",
                    f"--window-size={size}", "--virtual-time-budget=4000", f"--screenshot={png}", f"file://{html}"],
                   check=True, capture_output=True)


shot(work / "page.html", OUT / "quarto_html.png", "1000,750")
shot(work / "slides.html#/weekly-sales", OUT / "quarto_revealjs.png", "1000,625")
subprocess.run(["pdftoppm", "-png", "-r", "80", "-f", "1", "-l", "1", work / "report.pdf", work / "pdf"], check=True)
shutil.move(next(work.glob("pdf*.png")), OUT / "quarto_pdf.png")
subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", work / "docx", work / "report.docx"],
               check=True, capture_output=True, env=dict(os.environ, SAL_USE_VCLPLUGIN="svp"))
subprocess.run(["pdftoppm", "-png", "-r", "80", "-f", "1", "-l", "1", work / "docx" / "report.pdf", work / "docx" / "p"],
               check=True)
shutil.move(next((work / "docx").glob("p*.png")), OUT / "quarto_docx.png")
for f in ("html", "revealjs", "pdf", "docx"):
    print(f, Image.open(OUT / f"quarto_{f}.png").size)
