# Data Engineer Learning

A personal study repo for completing the **IBM Data Engineering Professional Certificate** (Coursera), tracked with lesson notes generated per video and a running study plan.

## Goal

- Build job-market-ready data engineering skills using SSIS/SSAS background as a foundation, and land a new role.
- Target completion of the IBM certificate: **Sep–Oct 2026**.
- Next up after the certificate: *Mastering Azure Databricks for Data Engineers*.

## Structure

```
data_engineer_learning/
├── CLAUDE.md                  # Claude Code instructions for this repo (note/plan generation rules)
├── INDEX.md                    # Link index to every note, grouped by Course/Module/Lesson/Video
├── Study-Plan.md              # Current study plan and weekly schedule
├── GLOSSARY.md                 # Master glossary aggregated from every note's Key Terms section
├── Cheat-Sheets-Index.md       # Index of cheat-sheet reference files
├── .claude/
│   ├── commands/
│   └── templates/              # Templates used to generate lesson notes and the study plan
└── IBM-Data-Engineering-Certificate/
    ├── C01_Introduction-to-Data-Engineering/
    ├── C02_Python-for-Data-Science-AI-Development/
    ├── C03_Python-Project-for-Data-Engineer/
    ├── C04_RDBMS/
    ├── C05_Databases-and-SQL-with-Python/
    └── C06_Linux-Commands-and-Shell-Scripting/
```

Each course folder is broken down as `C<NN>_<Course-Name>/M<NN>_<Module-Name>/L<NN>_<Lesson-Name>/V<NN>_<Video-Title>.md`, mirroring Coursera's Course → Module → Lesson → Video hierarchy. Lessons with only one video skip the lesson folder and video split (see `CLAUDE.md` for full naming rules).

## Notes format

Each lesson note is written from a video transcript and includes: an overview, topic sections (with diagrams/tables where useful), a glossary of key terms, a "Questions & Gaps" section, and resources. Note bodies are written in Thai; headings stay in English for consistent navigation. Cheat-sheet-style reference content (syntax/example tables) is saved as-is, without the note template, under `<language>-cheat-sheet-<topic>.md`.

## How notes/plan get generated

This repo is set up to work with Claude Code:
- Paste lesson content → generates one note per video (`note` skill), and updates `GLOSSARY.md` and `INDEX.md`.
- Paste cheat-sheet reference content → saves it faithfully (`cheat-sheet` skill), and updates `Cheat-Sheets-Index.md`.
- Ask about schedule/timeline → regenerates `Study-Plan.md` (`plan` skill).

See `CLAUDE.md` for the full rules these follow, and `INDEX.md` to browse all notes.
