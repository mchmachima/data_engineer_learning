# Understanding Relational Model Constraints

`Tags: SQL, constraints, entity integrity, referential integrity, domain integrity`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C05 Databases and SQL with Python         |
| **Module**        | M02 Intro to RDBMS and Tables             |
| **Lesson**        | L04 Understanding Relational Model Constraints |
| **Date studied**  | 2026-08-12                                |

---

## Table of Contents

- [Overview](#overview)
- [Entity Integrity Constraint](#entity-integrity-constraint)
- [Referential Integrity Constraint](#referential-integrity-constraint)
- [Domain Integrity Constraint](#domain-integrity-constraint)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

Reading นี้อธิบาย relational model constraint 3 ประเภทหลักที่ใช้รักษา data integrity ในฐานข้อมูลเชิงสัมพันธ์ ได้แก่ entity integrity, referential integrity และ domain integrity โดยใช้ตัวอย่าง database `BookShopDB` ที่มี table `BookShop` และ `BookShop_AuthorDetails` เพื่อแสดงว่าแต่ละ constraint ช่วยให้ข้อมูลมีความถูกต้อง สอดคล้อง และเชื่อถือได้อย่างไร พร้อมตัวอย่างการ implement ผ่าน SQL

---

## Entity Integrity Constraint

Constraint นี้รับประกันว่าทุก table ในฐานข้อมูลเชิงสัมพันธ์ต้องมี primary key ซึ่งทำหน้าที่ระบุแต่ละ row แบบไม่ซ้ำกัน โดย primary key column ต้อง:
- ไม่มีค่า NULL
- มีค่าไม่ซ้ำกันในทุก row

Constraint นี้ช่วยรับประกันว่าแต่ละ record (หรือ entity) ใน table มีความแตกต่างและระบุตัวตนได้ ป้องกันข้อมูลซ้ำซ้อนและการขาด identifier

```sql
-- BOOK_ID is the primary key: must be unique and cannot be NULL
CREATE TABLE BookShop (
    BOOK_ID INT PRIMARY KEY,
    TITLE VARCHAR(100),
    AUTHOR_ID INT
);
```

ทุก table ในฐานข้อมูลเชิงสัมพันธ์ควรมี primary key เพื่อให้เป็นไปตาม entity integrity

---

## Referential Integrity Constraint

Constraint นี้รับประกันว่า foreign key ใน table หนึ่งต้องอ้างอิงไปยัง primary key ที่มีอยู่จริงใน table อื่นเสมอ ช่วยรักษาความสัมพันธ์ระหว่าง table ให้สอดคล้องและมีความหมาย ป้องกันการเกิด reference ที่ไม่ถูกต้องหรือ "orphaned" record

```sql
-- AUTHOR_ID in BookShop references AUTHOR_ID in BookShop_AuthorDetails
CREATE TABLE BookShop_AuthorDetails (
    AUTHOR_ID INT PRIMARY KEY,
    AUTHOR_NAME VARCHAR(100)
);

CREATE TABLE BookShop (
    BOOK_ID INT PRIMARY KEY,
    TITLE VARCHAR(100),
    AUTHOR_ID INT,
    FOREIGN KEY (AUTHOR_ID) REFERENCES BookShop_AuthorDetails(AUTHOR_ID)
);
```

- `AUTHOR_ID` ใน `BookShop` อ้างอิงไปยัง `AUTHOR_ID` ใน `BookShop_AuthorDetails`
- ทุกค่า `AUTHOR_ID` ใน `BookShop` ต้องมีอยู่จริงใน `BookShop_AuthorDetails`
- หากพยายาม insert หนังสือที่มี `AUTHOR_ID` ที่ไม่มีอยู่ใน `BookShop_AuthorDetails` คำสั่งจะล้มเหลว

---

## Domain Integrity Constraint

Constraint นี้รับประกันว่าค่าที่เก็บใน column แต่ละตัวอยู่ภายใน domain ที่กำหนดไว้ ครอบคลุมกฎเรื่อง data type, format, ค่าที่อนุญาต และ nullability ช่วยให้ข้อมูลใน column มีความถูกต้อง สมเหตุสมผล และสอดคล้องกับการใช้งานที่ตั้งใจไว้

```sql
-- PRICE must not be negative; TITLE cannot be left empty
CREATE TABLE BookShop (
    BOOK_ID INT PRIMARY KEY,
    TITLE VARCHAR(100) NOT NULL,
    PRICE DECIMAL(5, 2) CHECK (PRICE >= 0),
    PUBLISHED_DATE DATE
);
```

กลไกหลัก 2 แบบที่ใช้บังคับ domain integrity:
- **CHECK constraint**: บังคับกฎเรื่องช่วงค่าหรือรูปแบบของค่าที่ยอมรับได้ใน column เช่น `PRICE` ต้องไม่ติดลบ
- **NOT NULL constraint**: บังคับกฎเรื่อง nullability ว่า column นั้นต้องมีค่าเสมอ ห้ามเป็นค่าว่าง เช่น `TITLE` ต้องมีค่าเสมอ

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Entity integrity | constraint ที่รับประกันว่าทุก table ต้องมี primary key ที่ไม่ซ้ำและไม่เป็น NULL |
| Referential integrity | constraint ที่รับประกันว่า foreign key ต้องอ้างอิงไปยัง primary key ที่มีอยู่จริงในอีก table |
| Domain integrity | constraint ที่รับประกันว่าค่าใน column อยู่ภายใน data type, format และช่วงค่าที่กำหนดไว้ |
| Primary key | column ที่ระบุแต่ละ row ในตารางแบบไม่ซ้ำกัน และห้ามเป็นค่าว่าง |
| Foreign key | column ที่อ้างอิงไปยัง primary key ของอีก table เพื่อสร้างความสัมพันธ์ระหว่างตาราง |
| Orphaned reference | ข้อมูลที่มี foreign key ชี้ไปยังค่าที่ไม่มีอยู่จริงในตารางที่ถูกอ้างอิง |
| CHECK constraint | constraint ที่บังคับให้ค่าใน column ต้องผ่านเงื่อนไขที่กำหนด เช่น ต้องไม่ติดลบ |
| NOT NULL constraint | constraint ที่บังคับว่า column ต้องมีค่าเสมอ ห้ามเป็นค่าว่าง (NULL) |

---

## ❓ My Questions & Gaps

- [ ] ถ้าลบ row ใน table ที่ถูกอ้างอิงโดย foreign key (เช่นลบ author ที่ยังมีหนังสืออยู่) จะเกิดอะไรขึ้น — มี option เช่น CASCADE หรือ RESTRICT อย่างไรบ้าง
- [ ] domain integrity ครอบคลุมแค่ CHECK กับ NOT NULL หรือมีกลไกอื่นเพิ่มเติม เช่น ENUM หรือ custom data type

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารเพิ่มเติมที่กล่าวถึงใน reading นี้
