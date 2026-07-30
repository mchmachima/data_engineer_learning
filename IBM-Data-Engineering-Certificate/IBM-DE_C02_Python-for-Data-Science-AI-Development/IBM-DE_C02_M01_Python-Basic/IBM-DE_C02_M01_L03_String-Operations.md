# L03 String Formatting and Raw Strings

- **Certificate:** IBM Data Engineering Professional Certificate
- **Course:** C02 Python for Data Science, AI & Development
- **Module:** M01 Python Basics
- **Date studied:** 2026-06-13

---

## Table of Contents

- [Overview](#overview)
- [String Formatting Methods](#string-formatting-methods)
- [Raw Strings (r'')](#raw-strings-r)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

This lesson covers the three ways Python can inject variables into strings — f-strings, `str.format()`, and the legacy `%` operator — and compares them for readability and capability. It also introduces raw strings, which stop Python from interpreting backslashes as escape sequences, most useful for file paths and regex patterns.

---

## String Formatting Methods

Python provides three main ways to inject variables into strings.

### 1. F-strings (String Interpolation) — Recommended

Introduced in Python 3.6. Prefix the string with `f` and place variables or expressions inside `{}`.

```python
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
# My name is John and I am 30 years old.
```

F-strings can also **evaluate expressions** inline:

```python
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}.")
# The sum of 10 and 20 is 30.
```

### 2. `str.format()` Method

Uses `{}` as positional placeholders; values passed as arguments to `.format()`.

```python
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# My name is John and I am 30 years old.
```

### 3. `%` Operator (Legacy)

Oldest method. Uses `%s`, `%d`, etc. as format specifiers followed by a tuple of values.

```python
print("My name is %s and I am %d years old." % (name, age))
# My name is John and I am 30 years old.
```

Common specifiers:

- `%s` — string
- `%d` — integer
- `%f` — float

### Comparison

| Method         | Python Version | Readability | Supports Expressions |
| -------------- | -------------- | ----------- | -------------------- |
| f-string       | 3.6+           | Best        | Yes                  |
| `str.format()` | 2.6+           | Good        | No                   |
| `%` operator   | All            | Least       | No                   |

F-strings are the modern, preferred approach for readability and performance.

---

## Raw Strings (`r''`)

Prefixing a string with `r` tells Python to treat backslashes as **literal characters**, not escape sequences. Useful for file paths and regex patterns.

```python
regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)
# Regular String: C:
# ew_folder\file.txt   ← \n interpreted as newline
```

```python
raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)
# Raw String: C:\new_folder\file.txt   ← backslash treated literally
```

---

## 📖 Key Terms & Glossary

| Term            | Definition                                                                       |
| ---------------- | --------------------------------------------------------------------------------- |
| F-string          | Python 3.6+ string prefix (`f"..."`) that interpolates variables/expressions inline |
| `str.format()`    | String method that fills `{}` placeholders with arguments passed to `.format()`   |
| `%` Operator       | Legacy C-style string formatting using specifiers like `%s`, `%d`, `%f`           |
| Raw String        | A string prefixed with `r` where backslashes are treated as literal characters    |
| Escape Sequence   | A backslash-prefixed character (e.g. `\n`, `\t`) interpreted specially by Python  |

---

## ❓ My Questions & Gaps

- [ ] Are there performance differences between f-strings and `.format()` at scale?
- [ ] What are common regex use cases where raw strings are essential?

---

## 🔗 Resources

- [IBM Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-engineer)
