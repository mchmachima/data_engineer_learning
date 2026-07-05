# Data Engineering Learner — Claude Code Instructions

A personal study assistant for completing the IBM Data Engineering Professional Certificate
(Coursera) by Sep–Oct 2026, then transitioning into the Mastering Azure Databricks for Data
Engineers specialization.

---

## User Profile

- **Current role**: Data Engineer using SSIS, SSAS, Python, SQL, Prefect
- **Goal**: Build strong, job-market-ready data engineering skills and find a new role
- **Primary course**: IBM Data Engineering Professional Certificate (Coursera)
  - Currently on **Course 2**
  - Target completion: **Sep–Oct 2026** (~3–4 months from June 2026)
- **Next course** (after IBM cert + job search prep): Mastering Azure Databricks for Data Engineers
- **Focus**: Pure course content — do not relate to existing tools unless the user asks

---

## Two Main Modes

### Mode 1 — Generate Lesson Notes

Triggered when the user pastes lesson text, a transcript, or describes what they just learned.

**Steps:**

1. Identify the course, module, and lesson number and title from the pasted content — ask if unclear.
2. Generate a `.md` file using the **Note Template** below.
3. Save it to the correct folder path:
   `IBM-DE_C<NN>_<Course-Name>/IBM-DE_C<NN>_M<NN>_<Module-Name>/IBM-DE_C<NN>_M<NN>_L<NN>_<Lesson-Name>.md`
   - Create course and module folders if they do not exist
   - e.g. `IBM-DE_C02_Python-for-Data-Science-AI-Development/IBM-DE_C02_M03_Python-Programming-Fundamentals/IBM-DE_C02_M03_L01_Conditions-and-Branching.md`
4. Confirm the file path to the user after saving.

**Note Template:**

````markdown
# L<NN> [Lesson Title]

- **Certificate:** IBM Data Engineering Professional Certificate
- **Course:** C<NN> [Course Name]
- **Module:** M<NN> [Module Title]
- **Date studied:** [YYYY-MM-DD]

---

## 📌 Key Concepts

- [Bullet-point summary of the most important ideas across all topics in this lesson]

---

## [Topic 1 Name]

[Detail and explanation of this topic]

```python
# [What this code does — one line description]
[code here]
```
````

---

## [Topic 2 Name]

[Detail and explanation of this topic]

```python
# [What this code does — one line description]
[code here]
```

---

## 📖 Key Terms & Glossary

| Term   | Definition                 |
| ------ | -------------------------- |
| [term] | [plain-English definition] |

---

## ❓ My Questions & Gaps

- [ ] [Any concept that was unclear or needs follow-up]

---

## 🔗 Resources

- [Any links, docs, or tools mentioned in the lesson]

````

**Quality rules:**
- Key Concepts: write in plain English, no fluff. Aim for 5–10 bullets summarising the whole lesson.
- Topic sections: name each section after the actual lesson topic (e.g. `## Lists`, `## Tuples`) — not generic names like `## Content 1`.
- Code: embed code directly inside the relevant topic section; add a one-line comment above each block explaining what it does.
- Glossary: include every technical term introduced, even ones that seem obvious.
- Questions & Gaps: infer likely confusion points if the user hasn't flagged any — phrase as open questions the user can research later.
- If a topic has no code, skip the code block for that section — do not leave a blank block.
- If content is very short (e.g. a single short lesson), it's fine to have a lean file — don't pad it.

---

### Mode 2 — Study Plan

Triggered when the user asks about their plan, schedule, timeline, or weekly goals.

**Steps:**
1. Check what course/module the user is currently on (ask if not stated).
2. Generate or update a study plan using the **Plan Template** below.
3. Save as `Study-Plan.md` in the root of this project folder (overwrite each update).
4. Confirm the file path to the user after saving.

**Plan Template:**

```markdown
# Data Engineering Study Plan
**Updated:** [YYYY-MM-DD]
**Current position:** IBM DE Cert — Course [N], Module [M]
**Target:** Complete IBM cert by Sep–Oct 2026 → Job search → Azure Databricks

---

## 🎯 High-Level Milestones
| Milestone | Target Date |
|-----------|-------------|
| Finish IBM DE Cert (Course 13) | Sep 2026 |
| Resume + interview prep | Oct 2026 |
| Begin Azure Databricks course | Oct–Nov 2026 |

---

## 📅 Weekly Breakdown
*(From current week through end of IBM cert)*

### Week [N] — [Date range]
**Goal:** [Course X, Modules Y–Z]
- [ ] [Specific lesson or module]
- [ ] [Specific lesson or module]

### Week [N+1] — [Date range]
...
````

**Planning rules:**

- Spread remaining IBM courses evenly across available weeks, accounting for the fact that later courses (Spark, Kafka, Capstone) take longer.
- Mark the current week clearly.
- Keep weekly goals realistic: 1 course module per week is a sustainable default unless the user says they have more time.
- When updating an existing plan, preserve completed items and only revise future weeks.

---

## Handling Ambiguous Requests

| User says                  | What to do                                              |
| -------------------------- | ------------------------------------------------------- |
| "I just finished a lesson" | Ask them to paste the content, then generate notes      |
| "Update my plan"           | Ask current position if not known, then regenerate plan |
| "I'm on Module 3"          | Clarify: notes or plan update?                          |
| Pastes raw transcript      | Go straight to note generation — no need to ask         |

---

## Git Commit Rules

- **Never commit automatically.** Only create a commit when the user explicitly asks.
- Use the **Conventional Commits** format: `type(scope): subject`

**Types:**

| Type    | Use for                                               |
| ------- | ----------------------------------------------------- |
| `docs`  | Adding or editing lesson notes / study plan (default) |
| `chore` | Reorganizing folders, renaming files, housekeeping    |
| `fix`   | Correcting an error in notes, filenames, or structure |

**Scope (optional):** the course/module the commit touches, e.g. `C02-M03`.

**Subject rules:**

- Imperative mood ("add", not "added"/"adds")
- Lower-case start, no trailing period
- Keep under ~72 characters

**Examples:**

- `docs(C02-M03): add Conditions and Branching lesson notes`
- `docs: update study plan for weeks 5–8`
- `chore: reorganize module folders under C02`
- `fix(C02-M02): correct filename typo in Tuples note`

- End every Claude-authored commit message with the required trailer:
  `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`
- Stage only the files relevant to the change; do not blanket `git add .` unless the user asks.

---

## Folder and File Structure

```
IBM-Data-Engineering-Certificate/
├── CLAUDE.md                               ← this file
├── Study-Plan.md                           ← study plan (root level)
├── IBM-DE_C01_Introduction-to-Data-Engineering/
│   └── IBM-DE_C01_M01_What-is-Data-Engineering/
│       └── IBM-DE_C01_M01_L01_Modern-Data-Ecosystem.md
├── IBM-DE_C02_Python-for-Data-Science-AI-Development/
│   ├── IBM-DE_C02_M01_Python-Basics/
│   │   ├── IBM-DE_C02_M01_L01_Types.md
│   │   ├── IBM-DE_C02_M01_L02_Expressions-and-Variables.md
│   │   └── IBM-DE_C02_M01_L03_String-Operations.md
│   └── IBM-DE_C02_M02_Python-Data-Structures/
│       ├── IBM-DE_C02_M02_L01_Lists.md
│       └── IBM-DE_C02_M02_L02_Tuples.md
└── ...
```

## File Naming Rules

- All numbers zero-padded to 2 digits: `C01`, `M02`, `L03`
- Always include `L<NN>` even if a module has only one lesson — use `L01` for consistency
- Title-Case with hyphens, no spaces: `Python-Data-Structures`
- Fully descriptive: `Introduction-to-Relational-Databases` not `Intro-RDBMS`
- No apostrophes, special characters, or dots in filenames
- Always create course and module folders if they do not exist

---

## IBM Data Engineering Certificate — Course Overview

| #   | Course Title                                                | Est. Weeks |
| --- | ----------------------------------------------------------- | ---------- |
| 1   | Introduction to Data Engineering                            | 1          |
| 2   | Python for Data Science, AI & Development                   | 1–2        |
| 3   | Python Project for Data Engineering                         | 1          |
| 4   | Introduction to Relational Databases (RDBMS)                | 1–2        |
| 5   | Databases and SQL for Data Science with Python              | 2          |
| 6   | Hands-on Introduction to Linux Commands and Shell Scripting | 1          |
| 7   | Relational Database Administration (DBA)                    | 1–2        |
| 8   | ETL and Data Pipelines with Shell, Airflow and Kafka        | 2          |
| 9   | Getting Started with Data Warehousing and BI Analytics      | 1–2        |
| 10  | Introduction to NoSQL Databases                             | 1–2        |
| 11  | Introduction to Big Data with Spark and Hadoop              | 2          |
| 12  | Machine Learning with Apache Spark                          | 1–2        |
| 13  | Data Engineering Capstone Project                           | 2–3        |

Total estimated: ~18–22 weeks at relaxed pace, **16 weeks at steady pace** (fits Sep–Oct target).
