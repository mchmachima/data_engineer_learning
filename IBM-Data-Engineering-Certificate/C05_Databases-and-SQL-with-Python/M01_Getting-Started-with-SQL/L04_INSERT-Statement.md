# INSERT Statement

`Tags: SQL, INSERT, DML`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C05 Databases and SQL for Data Science with Python |
| **Module**        | M01 Getting Started with SQL              |
| **Lesson**        | L04 INSERT Statement                      |
| **Date studied**  | 2026-08-10                                |

---

## Table of Contents

- [Overview](#overview)
- [INSERT Statement Syntax](#insert-statement-syntax)
- [Inserting a Single Row](#inserting-a-single-row)
- [Inserting Multiple Rows](#inserting-multiple-rows)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้สอนเรื่องการเติมข้อมูล (populate) เข้าตารางหลังจากที่สร้างตารางแล้ว ด้วยคำสั่ง INSERT ซึ่งเป็นหนึ่งใน Data Manipulation Language (DML) statement ครอบคลุม syntax ของ INSERT statement และวิธีการเพิ่มข้อมูล 2 แบบ คือเพิ่มทีละแถว และเพิ่มหลายแถวพร้อมกันในคำสั่งเดียว

---

## INSERT Statement Syntax

หลังจากสร้างตารางแล้ว ตารางนั้นต้องถูกเติมข้อมูล (populate) ซึ่งทำได้ด้วยคำสั่ง INSERT ใช้สำหรับเพิ่มแถวใหม่เข้าไปในตาราง INSERT เป็นหนึ่งใน DML statement ซึ่งใช้อ่านและแก้ไขข้อมูล

syntax ของ INSERT statement ประกอบด้วย 3 ส่วน: table name (ระบุตารางเป้าหมาย), column name list (ระบุแต่ละคอลัมน์ในตาราง), และ values clause (ระบุค่าข้อมูลที่จะใส่ลงในแต่ละคอลัมน์)

```sql
-- General syntax of the INSERT statement
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

---

## Inserting a Single Row

ตัวอย่างจากตาราง author ที่มี 6 คอลัมน์ การเพิ่มข้อมูลของ Raul Chong หนึ่งแถวต้องระบุชื่อคอลัมน์ทั้ง 6 คอลัมน์คั่นด้วย comma ตามด้วยค่าของแต่ละคอลัมน์คั่นด้วย comma เช่นกัน จำนวนค่าใน values clause ต้องเท่ากับจำนวนคอลัมน์ที่ระบุไว้เสมอ เพื่อให้แต่ละคอลัมน์มีค่าครบ

```sql
-- Insert one row into the author table
INSERT INTO author (author_id, lastname, firstname, email, city, country)
VALUES ('A1', 'Chong', 'Raul', 'RFC@IBM.com', 'Toronto', 'CA');
```

---

## Inserting Multiple Rows

ตารางไม่จำเป็นต้องเติมข้อมูลทีละแถว สามารถ insert หลายแถวพร้อมกันได้ โดยระบุแต่ละแถวใน values clause คั่นด้วย comma

```sql
-- Insert two rows into the author table in a single statement
INSERT INTO author (author_id, lastname, firstname, email, city, country)
VALUES
    ('A1', 'Chong', 'Raul', 'RFC@IBM.com', 'Toronto', 'CA'),
    ('A2', 'Ahuja', 'Rav', 'RA@IBM.com', 'Toronto', 'CA');
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| INSERT statement | คำสั่ง DML ที่ใช้เพิ่มแถวใหม่เข้าไปในตาราง |
| DML (Data Manipulation Language) | กลุ่มคำสั่งที่ใช้อ่านและแก้ไขข้อมูล เช่น SELECT, INSERT |
| Column name list | รายชื่อคอลัมน์ในตารางที่ระบุใน INSERT statement เพื่อบอกว่าจะใส่ค่าลงคอลัมน์ไหนบ้าง |
| Values clause | ส่วนของ INSERT statement ที่ระบุค่าข้อมูลจริงที่จะใส่ลงในแต่ละคอลัมน์ |

---

## ❓ My Questions & Gaps

- [ ] ถ้าไม่ระบุ column name list เลย (INSERT INTO table_name VALUES (...)) จะมีข้อกำหนดหรือความเสี่ยงอะไรบ้าง
- [ ] ถ้าคอลัมน์ใดไม่มีค่าที่ต้องการใส่ (เช่นยังไม่รู้ email) จะ insert แบบเว้นคอลัมน์นั้นไว้เป็น NULL ได้อย่างไร

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงที่กล่าวถึงในวิดีโอนี้
