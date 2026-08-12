# DDL Statements

`Tags: SQL, DDL, CREATE TABLE, ALTER TABLE, DROP TABLE, TRUNCATE TABLE`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C05 Databases and SQL with Python         |
| **Module**        | M02 Intro to RDBMS and Tables             |
| **Lesson**        | L03 DDL Statements                        |
| **Date studied**  | 2026-08-12                                |

---

## Table of Contents

- [Overview](#overview)
- [CREATE](#create)
- [ALTER](#alter)
- [DROP](#drop)
- [TRUNCATE](#truncate)
- [CREATE vs ALTER vs DROP vs TRUNCATE](#create-vs-alter-vs-drop-vs-truncate)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

บทเรียนนี้รวมสองวิดีโอที่อธิบาย DDL statement หลักสี่ตัวที่ใช้จัดการโครงสร้างของ table ในฐานข้อมูลเชิงสัมพันธ์ ได้แก่ `CREATE` สำหรับสร้าง table ใหม่, `ALTER` สำหรับแก้ไขโครงสร้าง table ที่มีอยู่, `DROP` สำหรับลบ table ทั้งตัว และ `TRUNCATE` สำหรับลบข้อมูลทั้งหมดในตารางโดยยังคง table ไว้ เนื้อหาแสดง syntax ของแต่ละคำสั่งพร้อมตัวอย่างจาก library database (table `author`) และข้อควรระวังเมื่อใช้งาน

---

## CREATE

`CREATE TABLE` เป็น DDL statement ที่ใช้บ่อยที่สุดสำหรับสร้าง table เริ่มด้วย `CREATE TABLE` ตามด้วยชื่อ table จากนั้นครอบส่วนที่เหลือด้วยวงเล็บ โดยแต่ละบรรทัดในวงเล็บระบุชื่อ column ตามด้วย data type และค่าเสริม (optional value) เช่น constraint คั่นแต่ละ column ด้วยเครื่องหมายจุลภาค

```sql
-- Create a table with 2 columns: id (fixed-length code) and name (full name)
CREATE TABLE provinces (
    id CHAR(2) PRIMARY KEY NOT NULL,
    name VARCHAR(24)
);
```

ตัวอย่างที่ซับซ้อนขึ้นจาก library database แปลง entity `AUTHOR` เป็น table `author` โดยกำหนดให้ `author_id` เป็น PRIMARY KEY เพื่อป้องกันค่าซ้ำ และกำหนด NOT NULL ให้กับ `lastname` และ `firstname` เพราะ author ต้องมีชื่อเสมอ

```sql
-- Create the AUTHOR table with a primary key and NOT NULL constraints
CREATE TABLE author (
    author_id CHAR(2) PRIMARY KEY NOT NULL,
    lastname VARCHAR(15) NOT NULL,
    firstname VARCHAR(15) NOT NULL,
    email VARCHAR(40),
    city VARCHAR(15),
    country CHAR(2)
);
```

---

## ALTER

`ALTER TABLE` ใช้เพิ่ม หรือลบ column จาก table แก้ไข data type ของ column หรือเพิ่ม/ลบ key และ constraint ต่างจาก `CREATE TABLE` ตรงที่ไม่ใช้วงเล็บครอบ parameter และแต่ละบรรทัดของคำสั่งระบุการเปลี่ยนแปลง 1 อย่างที่ต้องการทำกับ table

```sql
-- Add a telephone_number column (up to 19 digits) to the author table
ALTER TABLE author
ADD COLUMN telephone_number BIGINT;
```

ใช้ clause `MODIFY` เพื่อเปลี่ยน data type ของ column ที่มีอยู่แล้ว เช่น เปลี่ยน `telephone_number` จาก BIGINT ไปเป็น CHAR เพื่อให้เก็บรูปแบบเบอร์โทรที่มีสัญลักษณ์ปนได้

```sql
-- Change telephone_number's data type from BIGINT to CHAR(20)
ALTER TABLE author
MODIFY telephone_number CHAR(20);
```

**ข้อควรระวัง**: การเปลี่ยน data type ของ column ที่มีข้อมูลอยู่แล้วอาจทำให้เกิด error ได้ ถ้าข้อมูลเดิมไม่เข้ากันกับ data type ใหม่ — คำสั่งจะไม่ทำงานและขึ้น error message ใน notification log

ใช้ clause `DROP COLUMN` เพื่อลบ column ที่ไม่ต้องการออกจาก table

```sql
-- Remove the telephone_number column from the author table
ALTER TABLE author
DROP COLUMN telephone_number;
```

---

## DROP

`DROP TABLE` ใช้ลบ table ทั้งตัวออกจากฐานข้อมูล ถ้า table มีข้อมูลอยู่ ข้อมูลนั้นจะถูกลบไปพร้อมกับ table โดย default

```sql
-- Delete the author table entirely, including its data
DROP TABLE author;
```

---

## TRUNCATE

บางครั้งต้องการลบเฉพาะข้อมูลใน table โดยไม่ลบ table เอง แม้จะใช้ `DELETE` โดยไม่ใส่ `WHERE` ได้ แต่การใช้ `TRUNCATE TABLE` จะรวดเร็วและมีประสิทธิภาพกว่าสำหรับลบข้อมูลทั้งหมด คำสั่งนี้ต้องระบุ `IMMEDIATE` เพื่อสั่งให้ประมวลผลทันทีและไม่สามารถ undo ได้

```sql
-- Delete all rows from the author table immediately (cannot be undone)
TRUNCATE TABLE author IMMEDIATE;
```

---

## CREATE vs ALTER vs DROP vs TRUNCATE

| Statement | ทำอะไรกับ table | ทำอะไรกับข้อมูล | Undo ได้หรือไม่ |
| --- | --- | --- | --- |
| CREATE | สร้าง table ใหม่พร้อม column | ยังไม่มีข้อมูล | ใช้ DROP TABLE เพื่อลบสิ่งที่สร้างไป |
| ALTER | แก้ไขโครงสร้าง table ที่มีอยู่ (เพิ่ม/ลบ/แก้ column, key, constraint) | ข้อมูลเดิมยังอยู่ (ยกเว้นถ้า DROP COLUMN ที่มีข้อมูล) | ขึ้นกับชนิดการเปลี่ยนแปลง โดยทั่วไป undo ยาก |
| DROP | ลบ table ทั้งตัวออกจากฐานข้อมูล | ลบข้อมูลทั้งหมดไปพร้อม table | ไม่ได้ |
| TRUNCATE | table ยังอยู่ ไม่เปลี่ยนโครงสร้าง | ลบข้อมูลทุก row ใน table | ไม่ได้ (เมื่อระบุ IMMEDIATE) |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| CREATE TABLE | DDL statement ใช้สร้าง entity หรือ table ในฐานข้อมูล พร้อมกำหนด column |
| CHAR | data type สำหรับ character string ความยาวคงที่ |
| VARCHAR | data type สำหรับ character string ความยาวไม่คงที่ (variable length) |
| PRIMARY KEY | constraint ที่ระบุ column ให้เป็นตัวระบุแต่ละ row แบบไม่ซ้ำกัน |
| NOT NULL | constraint ที่บังคับว่า column นั้นห้ามมีค่าว่าง (NULL) |
| ALTER TABLE | DDL statement ใช้แก้ไขโครงสร้างของ table ที่มีอยู่แล้ว |
| ADD COLUMN | clause ของ ALTER TABLE ใช้เพิ่ม column ใหม่เข้า table |
| MODIFY | clause ของ ALTER TABLE ใช้เปลี่ยน data type ของ column ที่มีอยู่ |
| DROP COLUMN | clause ของ ALTER TABLE ใช้ลบ column ออกจาก table |
| DROP TABLE | DDL statement ใช้ลบ table ทั้งตัวออกจากฐานข้อมูล พร้อมข้อมูลภายใน |
| TRUNCATE TABLE | DDL statement ใช้ลบข้อมูลทุก row ใน table โดยยังคง table ไว้ |
| IMMEDIATE | คำที่ระบุใน TRUNCATE TABLE เพื่อสั่งประมวลผลทันทีและไม่สามารถ undo ได้ |
| BIGINT | data type ตัวเลขจำนวนเต็มขนาดใหญ่ เก็บได้สูงสุดประมาณ 19 หลัก |

---

## ❓ My Questions & Gaps

- [ ] สามารถกำหนด PRIMARY KEY ได้มากกว่า 1 column พร้อมกัน (composite primary key) ในคำสั่ง CREATE TABLE เดียวกันได้อย่างไร
- [ ] นอกจาก PRIMARY KEY และ NOT NULL มี constraint อื่นที่ใช้ใน CREATE TABLE ได้อีกหรือไม่ เช่น UNIQUE, FOREIGN KEY, CHECK
- [ ] ถ้า DROP COLUMN กับ column ที่มี foreign key reference อยู่ จะเกิดอะไรขึ้น
- [ ] TRUNCATE TABLE ต่างจาก DELETE โดยไม่มี WHERE clause อย่างไรในแง่การ reset auto-increment/identity column

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารเพิ่มเติมที่กล่าวถึงในวิดีโอนี้
