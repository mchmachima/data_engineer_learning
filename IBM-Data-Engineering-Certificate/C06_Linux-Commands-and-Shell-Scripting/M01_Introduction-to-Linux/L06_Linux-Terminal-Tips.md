# Linux Terminal Tips - Tab Completion, Command History

`Tags: Linux, Terminal, tab-completion, command-history`

| Field            | Value                                                    |
| ---------------- | --------------------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate            |
| **Course**       | C06 Linux Commands and Shell Scripting                   |
| **Module**       | M01 Introduction to Linux                                |
| **Lesson**       | L06 Linux Terminal Tips - Tab Completion, Command History |
| **Date studied** | 2026-08-16                                                |

---

## Table of Contents

- [Overview](#overview)
- [Tab Completion](#tab-completion)
- [Command History](#command-history)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

Reading นี้แนะนำ shortcut สองอย่างที่ช่วยให้ทำงานกับ Linux terminal ได้เร็วขึ้น ได้แก่ **tab completion** สำหรับ autocomplete คำสั่งและชื่อไฟล์/directory และ **command history** สำหรับย้อนกลับไปใช้คำสั่งที่เคยพิมพ์ไปแล้วโดยไม่ต้องพิมพ์ใหม่

---

## Tab Completion

Tab completion คือฟีเจอร์ของ shell สมัยใหม่ส่วนใหญ่ ที่ให้กด **Tab** ขณะพิมพ์คำสั่งหรือ path เพื่อให้ shell เติมคำที่เหลือให้อัตโนมัติ — ใช้ได้เมื่อมีคำที่ตรงกันเพียงตัวเดียว (unique match) หากมีมากกว่าหนึ่งตัวที่ตรงกัน การกด Tab สองครั้งจะแสดงตัวเลือกทั้งหมดให้ดู

**ตัวอย่าง:** สมมติอยู่ใน home directory (`~`) ซึ่งมี subdirectory คือ `Pictures`, `Videos`, `Documents`, `Downloads` และภายใน `Documents` มี folder เดียวคือ `python-examples`

```bash
# พิมพ์ cd P แล้วกด Tab หนึ่งครั้ง
# shell จะเติมให้อัตโนมัติเพราะ Pictures เป็นตัวเดียวที่ขึ้นต้นด้วย P
cd Pictures/

# พิมพ์ cd Do แล้วกด Tab — จะไม่มีอะไรเกิดขึ้น
# เพราะมีทั้ง Documents และ Downloads ที่ขึ้นต้นด้วย Do (ไม่ unique)
cd Do

# พิมพ์ cd Doc แล้วกด Tab — shell เติมให้เป็น Documents/ ทันที
# เพราะมีแค่ Documents ตัวเดียวที่ขึ้นต้นด้วย Doc
cd Documents/

# กด Tab ซ้ำอีกครั้งที่ปลายคำสั่งเดิม
# shell เติมต่อเป็น Documents/python-examples/
# เพราะ python-examples เป็น folder เดียวที่อยู่ใน ~/Documents
cd Documents/python-examples/
```

---

## Command History

Command history ให้ย้อนดูคำสั่งที่เคยพิมพ์ไปแล้วโดยใช้ปุ่ม **ลูกศรขึ้น (Up Arrow)** และ **ลูกศรลง (Down Arrow)**

**สถานการณ์ตัวอย่าง:** เคยรันคำสั่งตามลำดับนี้มาก่อน

```bash
cd ~/Documents/python-examples
python3 myprogram.py
# ผลลัพธ์: Hello, World!
cd /
```

```bash
# กด Up Arrow หนึ่งครั้ง — shell เติมคำสั่งล่าสุดให้อัตโนมัติ
cd /

# กด Up Arrow เพิ่มอีกสองครั้ง (รวมเป็นสามครั้ง) — shell ย้อนกลับไปสามคำสั่งก่อนหน้า
# หมายเหตุ: บรรทัดผลลัพธ์ (เช่น "Hello, World!") ไม่ถูกนับเป็นคำสั่ง
cd ~/Documents/python-examples
```

> **Tip:** ถ้ากดลูกศรขึ้นเกินจุดที่ต้องการ ใช้ลูกศรลง (Down Arrow) เพื่อย้อนกลับมาในทิศตรงข้ามได้

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Tab completion | ฟีเจอร์ของ shell ที่เติมคำสั่ง ชื่อไฟล์ หรือชื่อ directory ให้อัตโนมัติเมื่อกดปุ่ม Tab |
| Unique match | กรณีที่มีตัวเลือกเดียวที่ตรงกับข้อความที่พิมพ์ไว้ ทำให้ tab completion เติมคำให้ได้ทันที |
| Command history | รายการคำสั่งที่เคยพิมพ์ไปแล้ว ที่สามารถเรียกย้อนกลับมาใช้ได้ด้วยปุ่มลูกศรขึ้น/ลง |
| Up Arrow / Down Arrow | ปุ่มที่ใช้เลื่อนไปมาใน command history เพื่อเรียกคำสั่งเก่ากลับมาแสดงที่ command line |

---

## ❓ My Questions & Gaps

- [ ] command history เก็บคำสั่งไว้ได้กี่รายการ และเก็บข้ามการปิด-เปิด terminal ใหม่ได้หรือไม่ (เกี่ยวข้องกับไฟล์ `.bash_history` หรือไม่)

---

## 🔗 Resources

- (ไม่มีลิงก์ระบุใน reading)
