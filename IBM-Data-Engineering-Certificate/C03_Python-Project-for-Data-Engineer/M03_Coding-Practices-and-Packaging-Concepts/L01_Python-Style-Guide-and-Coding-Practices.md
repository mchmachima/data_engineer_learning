# Python Style Guide and Coding Practices

`Tags: Python, PEP-8, code style, static analysis`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C03 Python Project for Data Engineer      |
| **Module**        | M03 Coding Practices and Packaging Concepts |
| **Lesson**        | L01 Python Style Guide and Coding Practices |
| **Date studied**  | 2026-08-09                                |

---

## Table of Contents

- [Overview](#overview)
- [PEP-8 Readability Guidelines](#pep-8-readability-guidelines)
- [Coding Conventions for Consistency](#coding-conventions-for-consistency)
- [Static Code Analysis](#static-code-analysis)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้พูดถึงความสำคัญของการเขียนโค้ดที่อ่านง่ายและเข้าใจได้ง่ายสำหรับทีม โดยอ้างอิงจากเอกสาร PEP-8 (Python Enhancement Proposal 8) ซึ่งเป็นแนวทางมาตรฐานของ Python.org สำหรับจัดรูปแบบโค้ดให้สม่ำเสมอ เนื้อหาครอบคลุมทั้งแนวทางด้าน readability, coding convention สำหรับการตั้งชื่อ function/class/constant และการใช้ static code analysis เพื่อตรวจสอบว่าโค้ดเป็นไปตามมาตรฐานหรือไม่

---

## PEP-8 Readability Guidelines

PEP-8 คือเอกสารแนวทาง (guideline) จาก Python.org ที่กำหนด convention เพื่อให้โค้ด Python อ่านง่ายและมีรูปแบบสม่ำเสมอ ประเด็นหลักด้าน readability มีดังนี้

- **ใช้ space แทน tab สำหรับ indentation** — เพราะ text editor และ IDE แต่ละตัวตีความจำนวน space ใน 1 tab ไม่เท่ากัน (บางตัวตีความเป็น 3 space บางตัวเป็น 4 space) การใช้ tab จึงทำให้โค้ดจัดรูปแบบไม่สม่ำเสมอและเกิด formatting error ได้ แนวทางคือใช้ **4 space ต่อ 1 ระดับ indentation**
- **เว้นบรรทัดว่าง (blank line) คั่นระหว่าง function และ class** — ช่วยให้เห็นจุดเริ่มต้นและจุดสิ้นสุดของแต่ละส่วนโค้ดได้ชัดเจน
- **ใช้ space รอบ operator และหลัง comma** — เช่นเขียน `a = b + c` แทน `a=b+c` เพื่อให้คำสั่งอ่านง่ายและไม่แน่นจนเกินไป

| แนวทาง (Guideline)        | ตัวอย่างที่ไม่ถูกต้อง | ตัวอย่างที่ถูกต้อง |
| -------------------------- | ---------------------- | -------------------- |
| Indentation                | ใช้ tab (interpret ไม่ตรงกันแต่ละ editor) | ใช้ 4 space          |
| เว้นบรรทัดระหว่าง function/class | ไม่มีบรรทัดว่างคั่น    | เว้น 1 บรรทัดว่างก่อนนิยาม class/function ถัดไป |
| Space รอบ operator/comma   | `a=b+c`                | `a = b + c`           |

---

## Coding Conventions for Consistency

นอกจากเรื่อง readability แล้ว PEP-8 ยังแนะนำ convention เพื่อให้โค้ดสม่ำเสมอและดูแลรักษาง่าย (manageability)

- **แยกโค้ดก้อนใหญ่ออกเป็น function** — แทนที่จะเขียนโค้ด if-else ซ้ำทุกครั้งที่ต้องใช้ ให้ห่อ logic นั้นไว้ใน function แล้วเรียกใช้จากโปรแกรมหลัก ช่วยเพิ่มความเร็วในการทำงานของโค้ดและสนับสนุนการนำโค้ดกลับมาใช้ซ้ำ (code reuse)
- **ตั้งชื่อ function และไฟล์ด้วยตัวพิมพ์เล็กคั่นด้วย underscore** (lowercase with underscores) — เพราะ built-in library และ predefined function ของ Python ส่วนใหญ่ใช้ convention นี้ ยกเว้น **ชื่อ package ที่ไม่แนะนำให้ใช้ underscore** (เช่นใช้ `mypackage` แทน `my_package`)
- **ตั้งชื่อ class ด้วย camel case** (หรือ cap word case) — ช่วยแยกความแตกต่างระหว่าง class กับ function ในโค้ดได้ชัดเจน
- **ตั้งชื่อ constant ด้วยตัวพิมพ์ใหญ่ทั้งหมดคั่นด้วย underscore** — ชื่อควรสื่อถึงจุดประสงค์ของค่านั้น

```python
# ตัวอย่าง: ห่อ logic ไว้ใน function แทนการเขียนซ้ำ
def function_1(a, b):
    if a > b:
        return a
    else:
        return b

c = function_1(a, b)


# ตัวอย่างการตั้งชื่อตาม convention
def comp_surface_radiation(a, b):  # function/file: lowercase_with_underscores
    pass


class LambSquirrelCage:  # class: CamelCase
    pass


MAX_FILE_UPLOAD_SIZE = 10  # constant: ALL_CAPS_WITH_UNDERSCORES
```

| องค์ประกอบ (Element) | Convention             | ตัวอย่าง                     |
| ---------------------- | ----------------------- | ------------------------------ |
| Function / File name   | lowercase_with_underscores | `comp_surface_radiation`    |
| Package name            | lowercase ไม่มี underscore | `mypackage`                 |
| Class name               | CamelCase              | `LambSquirrelCage`             |
| Constant name            | ALL_CAPS_WITH_UNDERSCORES | `MAX_FILE_UPLOAD_SIZE`     |

---

## Static Code Analysis

Static code analysis คือวิธีการตรวจสอบโค้ดเทียบกับ style และ standard ที่กำหนดไว้ล่วงหน้า **โดยไม่ต้อง execute โค้ดจริง** ช่วยตรวจจับปัญหาต่าง ๆ เช่น programming error, การละเมิด coding standard, undefined value, syntax violation และช่องโหว่ด้านความปลอดภัย (security vulnerability)

เครื่องมือที่ใช้ตรวจสอบ Python code ให้เป็นไปตาม PEP-8 คือ library ชื่อ **PyLint**

---

## 📖 Key Terms & Glossary

| Term (ศัพท์)              | คำอธิบาย (ภาษาไทย)                                                        |
| --------------------------- | ---------------------------------------------------------------------------- |
| PEP-8                        | เอกสาร Python Enhancement Proposal 8 จาก Python.org ที่กำหนดแนวทางการเขียนโค้ดให้อ่านง่ายและสม่ำเสมอ |
| Indentation                   | การเยื้องบรรทัดโค้ดเพื่อแสดงลำดับชั้นของ block (แนะนำให้ใช้ 4 space)         |
| Coding convention              | ข้อตกลงร่วมในการตั้งชื่อและจัดรูปแบบโค้ดเพื่อความสม่ำเสมอ                    |
| Camel case                      | รูปแบบการตั้งชื่อที่ขึ้นต้นแต่ละคำด้วยตัวพิมพ์ใหญ่ ใช้กับชื่อ class          |
| Static code analysis             | การตรวจสอบโค้ดตาม style/standard โดยไม่ต้อง execute โค้ด                   |
| PyLint                            | library สำหรับตรวจสอบว่าโค้ด Python เป็นไปตาม PEP-8 หรือไม่                |

---

## ❓ My Questions & Gaps

- [ ] PyLint ตั้งค่า custom rule เพื่อ override PEP-8 บางข้อได้หรือไม่ และทำอย่างไร
- [ ] มี tool อื่นนอกจาก PyLint ที่ใช้ตรวจสอบ PEP-8 compliance ได้บ้าง (เช่น flake8, black) ต่างกันอย่างไร
- [ ] static code analysis ตรวจจับ security vulnerability ประเภทไหนได้บ้างโดยเฉพาะ

---

## 🔗 Resources

- PEP-8 — Style Guide for Python Code (Python.org)
- PyLint library
