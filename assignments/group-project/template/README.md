# Group XX: Alpenglow 2027 media budget

Group project for *International Marketing Analytics* (WU Vienna, CEMS, winter 2026/27).
Brief and rubric: `assignments/group-project/` in the course repository.

## Team

| Name | GitHub username | Main responsibility |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |

## What is in this repository

```
README.md             this file
report.qmd            the board report (renders to report.html / report.pdf, max 12 pages)
report.pdf            rendered report (committed for the final submission)
pitch.pdf             the 8-slide pitch deck shown in Session 5
allocation_2027.csv   our recommended weekly 2027 spend per country x channel (30 rows)
code/
  00_load.py          loads the course data (course repo cloned next to this one)
  01_explore.py       milestone 1: data exploration
  02_mmm_country.py   per-country MMMs
  03_mmm_pooled.py    pooled / hierarchical MMM
  04_forecast.py      2026 baseline forecast
  05_geolift.py       geo-lift calibration of paid social
  06_allocation.py    budget scenarios and allocation_2027.csv
results/              model tables and figures written by the scripts
```

The course data are **not** copied into this repository. `code/00_load.py` reads them from
`../International-Marketing-Analytics/data/` (clone the course repository next to this one)
or, as a fallback, from the raw GitHub URL in that file.

## How to reproduce

```bash
# from the root of this repository, with the course virtual environment active
python code/00_load.py          # checks the data are found, writes a placeholder allocation if none exists
python code/02_mmm_country.py   # ... and so on, in numerical order
quarto render report.qmd
```

Rendering `report.qmd` end to end must take less than ten minutes on a laptop
(PyMC: `draws=500, tune=500, chains=2, random_seed=42`).

## Check the allocation file

From the course repository:

```bash
PROJECT_CSV=../group-XX-alpenglow/allocation_2027.csv pytest assignments/checks/test_project.py
```

## Milestones

| Milestone | Due | Content |
|---|---|---|
| Group formation | Session 1 (6 Oct) | repository created, all members added, README filled |
| M1 data exploration | before Session 2 (13 Oct) | `code/01_explore.py`, first figures in `results/` |
| M2 first model table | before Session 4 (27 Oct) | per-country ROAS table in `results/`, skeleton report renders |
| Final submission | Mon 2 Nov 2026, 18:00 | report, allocation file, pitch deck, prompt log, contribution statement |
| Pitches | Tue 3 Nov 2026 | board meeting, 10 minutes per group plus 5 minutes Q&A |

## AI use

AI coding assistants are expected. Every non-trivial prompt is logged in the prompt-log
appendix of `report.qmd`, and every number in the report was verified by a team member.
