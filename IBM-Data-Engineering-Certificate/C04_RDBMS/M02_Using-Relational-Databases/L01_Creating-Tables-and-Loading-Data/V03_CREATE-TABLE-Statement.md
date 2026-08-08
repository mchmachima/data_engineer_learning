# CREATE TABLE Statement

`Tags: SQL, CREATE TABLE, primary key, data types, RDBMS`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C04 Introduction to Relational Databases (RDBMS) |
| **Module**        | M02 Using Relational Databases            |
| **Lesson**        | L01 Creating Tables and Loading Data      |
| **Date studied**  | 2026-07-31                                |

---

## Table of Contents

- [Overview](#overview)
- [CREATE TABLE Syntax](#create-table-syntax)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้เจาะลึกคำสั่ง `CREATE TABLE` ซึ่งเป็น DDL statement ที่ใช้บ่อยที่สุดสำหรับสร้างตารางในฐานข้อมูล ครอบคลุมรูปแบบ syntax, data type ที่พบบ่อยอย่าง CHAR และ VARCHAR และวิธีกำหนด primary key กับ NOT NULL constraint ผ่านตัวอย่างตาราง provinces และ author

---

## CREATE TABLE Syntax

`CREATE TABLE` เป็น DDL statement ที่ใช้บ่อยที่สุดสำหรับสร้าง entity หรือ table ในฐานข้อมูล รูปแบบ syntax คือเริ่มด้วย `CREATE TABLE` ตามด้วยชื่อตาราง แล้วเปิดวงเล็บเพื่อระบุ column แต่ละตัว โดยแต่ละแถวในวงเล็บระบุชื่อ column, data type และค่า optional อื่น ๆ (เช่น constraint) คั่นแต่ละ column ด้วยเครื่องหมายจุลภาค (comma)

data type ที่พบบ่อยได้แก่ `CHAR(n)` (character string ความยาวคงที่) และ `VARCHAR(n)` (character string ความยาวไม่เกิน n ตัวอักษร) ตัวอย่างเช่นการสร้างตาราง provinces ที่มี column `Id` เป็น primary key แบบ CHAR(2) และ column `name` เป็น VARCHAR(24)

**Primary key** ใช้ระบุว่า column นั้นเป็นตัวระบุ (identify) แต่ละ tuple/row แบบไม่ซ้ำกัน (unique) ในตัวอย่างตาราง author ของ library database จะกำหนดให้ `Author_ID` เป็น primary key เพื่อป้องกันค่าซ้ำ และกำหนด `NOT NULL` ให้กับ column ที่ต้องมีค่าเสมอ เช่น first name และ last name

```sql
-- Create a simple table with a primary key column
CREATE TABLE provinces (
    Id CHAR(2) PRIMARY KEY NOT NULL,
    name VARCHAR(24)
);

-- Create the author table with primary key and NOT NULL constraints
CREATE TABLE author (
    Author_ID CHAR(2) PRIMARY KEY NOT NULL,
    Lastname VARCHAR(15) NOT NULL,
    Firstname VARCHAR(15) NOT NULL,
    Email VARCHAR(40),
    City VARCHAR(15),
    Country CHAR(2)
);
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Primary Key | column หรือชุด column ที่ใช้ระบุแต่ละ row แบบไม่ซ้ำกัน |
| CHAR(n) | data type แบบ character string ความยาวคงที่ n ตัวอักษร |
| VARCHAR(n) | data type แบบ character string ความยาวไม่เกิน n ตัวอักษร |
| NOT NULL | constraint ที่บังคับว่า column นั้นต้องมีค่าเสมอ ห้ามเป็นค่าว่าง |

---

## ❓ My Questions & Gaps

- [ ] เลือกใช้ CHAR กับ VARCHAR ต่างกันตอนไหน ในแง่ performance และพื้นที่จัดเก็บ

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
