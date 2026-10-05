"""Check the course set-up: Python version, course packages, Quarto and Git.

Run it from the course folder, in the Positron terminal:

    uv run --no-project python setup/check_setup.py

or open this file in Positron and press the Run button (top right of the editor).
It prints one line per item and ends with "ready" when everything is in place.
"""
import importlib
import shutil
import subprocess
import sys
import warnings

warnings.filterwarnings("ignore")  # library notices are not set-up problems

PACKAGES = [  # (import name, what it is for)
    ("polars", "data wrangling"),
    ("pandas", "data frames for statsmodels and PyMC"),
    ("pyarrow", "polars to pandas conversion"),
    ("plotnine", "charts"),
    ("great_tables", "tables"),
    ("statsmodels", "regression"),
    ("sklearn", "machine learning helpers"),
    ("pymc_marketing", "Bayesian MMM (Session 5)"),
]

problems = []


def show(ok, label, detail):
    print(f"  [{'ok' if ok else '!!'}] {label:<16} {detail}")
    if not ok:
        problems.append(label)


print("Python")
in_venv = sys.prefix != sys.base_prefix
show(sys.version_info >= (3, 11), "version", sys.version.split()[0] + " (3.11 or newer needed)")
show(in_venv, "environment", sys.prefix if in_venv else "not the course .venv: select it in Positron")

print("Packages")
for name, purpose in PACKAGES:
    try:
        mod = importlib.import_module(name)
        show(True, name, f"{getattr(mod, '__version__', '?'):<10} {purpose}")
    except Exception as err:  # ImportError, or a broken install
        show(False, name, f"missing ({type(err).__name__}): run  uv pip install -r requirements.txt")

print("Tools")
for tool in ("quarto", "git"):
    path = shutil.which(tool)
    if path is None:
        show(False, tool, "not found on PATH: install it, then restart Positron")
        continue
    out = subprocess.run([tool, "--version"], capture_output=True, text=True).stdout.strip().splitlines()
    show(True, tool, out[0] if out else path)

print()
print("ready" if not problems else "not ready yet, fix: " + ", ".join(problems))
sys.exit(1 if problems else 0)
