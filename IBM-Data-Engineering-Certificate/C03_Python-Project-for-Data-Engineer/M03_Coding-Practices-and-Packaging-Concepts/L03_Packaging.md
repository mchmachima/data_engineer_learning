# Packaging

`Tags: Python, module, package, library, __init__.py`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C03 Python Project for Data Engineer      |
| **Module**        | M03 Coding Practices and Packaging Concepts |
| **Lesson**        | L03 Packaging                             |
| **Date studied**  | 2026-08-09                                |

---

## Table of Contents

- [Overview](#overview)
- [Module vs Package vs Library](#module-vs-package-vs-library)
- [Creating a Python Package](#creating-a-python-package)
- [Verifying and Using a Package](#verifying-and-using-a-package)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายความแตกต่างระหว่าง module, package และ library ใน Python พร้อมสอนขั้นตอนการสร้าง package, การตรวจสอบว่า package ถูกสร้างขึ้นถูกต้อง (verify) และการนำ package ไปใช้งานในไฟล์อื่น ๆ

---

## Module vs Package vs Library

- **Module** คือไฟล์ `.py` ที่มี definition, statement, function หรือ class อยู่ภายใน สามารถ import ไปใช้ในสคริปต์หรือ notebook อื่นได้ ถ้าไฟล์นั้นอยู่ใน directory เดียวกัน
- **Package** คือกลุ่มของ module หลาย ๆ ไฟล์ที่รวมอยู่ใน directory เดียวกัน โดยต้องมีไฟล์ `__init__.py` อยู่ด้วย ซึ่งเป็นสิ่งที่แยก package ออกจาก directory ธรรมดาที่มีแค่ไฟล์ Python เก็บอยู่ ทั้งนี้ความแตกต่างระหว่าง module กับ package เป็นเพียงระดับ file system เท่านั้น เมื่อ import ทั้งสองแบบ object ที่ได้จาก Python จะมี type เป็น `module` เหมือนกัน
- **Library** คือกลุ่มของ package (หรืออาจเป็น package เดียวก็ได้) เช่น NumPy, PyTorch, Pandas โดยคำว่า package และ library มักใช้แทนกันได้ในทางปฏิบัติ

```python
# module.py — ตัวอย่าง module ที่มี 2 function
def square(number):
    return number ** 2


def doubler(number):
    return number * 2


# การเรียกใช้ function จาก module ในไฟล์เดียวกัน directory
print(square(4))   # 4 ** 2 = 16
print(doubler(4))  # 2 * 4 = 8
```

| ระดับ (Level) | นิยาม                                             | ตัวอย่าง                  |
| --------------- | ---------------------------------------------------- | ---------------------------- |
| Module           | ไฟล์ `.py` ไฟล์เดียว                                | `module.py`                  |
| Package           | directory ที่รวม module หลายไฟล์ + มี `__init__.py` | `myproject/`                 |
| Library            | กลุ่มของ package (หรือ package เดียว)              | NumPy, PyTorch, Pandas       |

---

## Creating a Python Package

ขั้นตอนการสร้าง Python package มีดังนี้

1. สร้าง folder ที่ตั้งชื่อตาม package ที่ต้องการ
2. สร้างไฟล์ `__init__.py` แบบว่างเปล่าไว้ใน folder นั้น
3. สร้าง module ที่ต้องการให้อยู่ใน package
4. เพิ่มโค้ดใน `__init__.py` เพื่ออ้างอิง (reference) module ที่ต้องการให้ package นี้เข้าถึงได้

ตัวอย่างเช่น package ชื่อ `myproject` มี `module1.py` (มี function `square`, `doubler`) และ `module2.py` (มี function `mean`)

```
myproject/
├── __init__.py
├── module1.py
└── module2.py
```

```python
# __init__.py — อ้างอิง module ที่ต้องการให้ package เข้าถึงได้
from . import module1
from . import module2
```

---

## Verifying and Using a Package

การตรวจสอบว่า package ถูกสร้างขึ้นถูกต้อง (verify) ทำได้โดย

1. เปิด bash terminal แล้วเข้าไปยัง directory เดียวกับ folder ของ package
2. เปิด Python interpreter ด้วยคำสั่ง `python`
3. ทดลอง `import` ชื่อ package เช่น `import myproject` — ถ้าไม่มี error แสดงว่า package โหลดสำเร็จ
4. เรียกใช้ function ในรูปแบบ `package.module.function(parameter)`

```python
# ทดสอบเรียก function จาก package myproject
import myproject

myproject.module1.square(4)  # ได้ผลลัพธ์ 16
```

หลังจากสร้าง package แล้ว สามารถนำไปใช้ในสคริปต์อื่นได้ ถ้า package folder อยู่ใน directory เดียวกันกับสคริปต์นั้น

```python
# test.py — import function จาก package myproject มาใช้
from myproject.module1 import square, doubler
from myproject.module2 import mean

print(4 ** 2 == square(4))          # 16 == 16
print(2 * 4 == doubler(4))          # 8 == 8
print((2 + 1 + 3) / 3 == mean([2, 1, 3]))  # 2.0 == 2.0
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์)      | คำอธิบาย (ภาษาไทย)                                                    |
| --------------------- | -------------------------------------------------------------------------- |
| Module                  | ไฟล์ `.py` ที่มี definition, statement, function หรือ class               |
| Package                   | directory ที่รวม module หลายไฟล์ และมี `__init__.py`                    |
| Library                     | กลุ่มของ package หรือ package เดียว เช่น NumPy, Pandas                 |
| `__init__.py`                 | ไฟล์ที่บ่งบอกว่า directory นั้นเป็น package และใช้อ้างอิง module ภายใน |
| Verify (package)                | การตรวจสอบว่า package ถูกสร้างและ import ได้ถูกต้อง                    |

---

## ❓ My Questions & Gaps

- [ ] `__init__.py` แบบว่างเปล่า (ไม่มีการ reference module) ยังทำให้ folder เป็น package ได้หรือไม่
- [ ] ความแตกต่างระหว่าง relative import (`from . import module1`) กับ absolute import ใน package คืออะไร
- [ ] การทำ package ให้ติดตั้งผ่าน `pip install` ได้ (เช่นด้วย `setup.py`) ต้องทำอย่างไรเพิ่มเติม

---

## 🔗 Resources

- Python Packages documentation (Python.org)
