# SELECT Statement

`Tags: SQL, SELECT, DML, WHERE-clause`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C05 Databases and SQL for Data Science with Python |
| **Module**        | M01 Getting Started with SQL              |
| **Lesson**        | L02 SELECT Statement                      |
| **Date studied**  | 2026-08-10                                |

---

## Table of Contents

- [Overview](#overview)
- [SELECT Statement Basics](#select-statement-basics)
- [Selecting Specific Columns](#selecting-specific-columns)
- [Filtering with WHERE and Predicates](#filtering-with-where-and-predicates)
- [Comparison Operators](#comparison-operators)
- [SELECT Examples](#select-examples)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้สอนเรื่องการดึงข้อมูล (retrieve data) จากตารางใน relational database ด้วยคำสั่ง SELECT ซึ่งเป็นหนึ่งใน Data Manipulation Language (DML) statement ครอบคลุมตั้งแต่การ SELECT ทุกคอลัมน์ การเลือกเฉพาะบางคอลัมน์ ไปจนถึงการใช้ WHERE clause ร่วมกับ predicate เพื่อกรองผลลัพธ์ พร้อมทั้งแนะนำ comparison operators ที่ RDBMS รองรับ

---

## SELECT Statement Basics

หน้าที่หลักของ database management system ไม่ใช่แค่จัดเก็บข้อมูล แต่ต้องช่วยให้ดึงข้อมูล (retrieve) กลับมาดูได้ด้วย หลังจากสร้างตารางและ insert ข้อมูลแล้ว เราใช้คำสั่ง SELECT เพื่อดูข้อมูลนั้น

SELECT statement เป็น DML statement ซึ่งใช้อ่านและแก้ไขข้อมูล คำสั่ง SELECT เรียกว่า query และผลลัพธ์ที่ได้จากการรัน query เรียกว่า result set หรือ result table รูปแบบง่ายที่สุดของ SELECT คือ `SELECT * FROM table_name` ซึ่งจะดึงข้อมูลทุกแถวทุกคอลัมน์ในตารางนั้นออกมา

```sql
-- Retrieve all columns and all rows from a table
SELECT * FROM TABLE_1;
```

---

## Selecting Specific Columns

ไม่จำเป็นต้องดึงทุกคอลัมน์เสมอไป เราสามารถระบุเฉพาะคอลัมน์ที่ต้องการได้ เช่น จากตาราง book ถ้าต้องการแค่คอลัมน์ book_id กับ title ก็เขียนเป็น `select book_id, title from book` ลำดับคอลัมน์ที่แสดงผลจะตรงกับลำดับที่ระบุใน SELECT statement เสมอ

```sql
-- Retrieve only the listed columns from a table
SELECT COLUMN1, COLUMN2, ... FROM TABLE_1;
```

---

## Filtering with WHERE and Predicates

ถ้าต้องการจำกัดผลลัพธ์ให้แคบลง เช่น หา title ของหนังสือที่ book_id เท่ากับ B1 ต้องใช้ WHERE clause ซึ่งต้องมี predicate เสมอ predicate คือเงื่อนไขที่ประเมินผลได้เป็น true, false หรือ unknown และถูกใช้ใน search condition ของ WHERE clause

```sql
-- Filter rows using a predicate in the WHERE clause
SELECT <COLUMNS> FROM TABLE_1 WHERE <predicate>;
```

---

## Comparison Operators

RDBMS รองรับ comparison operators ต่อไปนี้ใน WHERE clause:

| Operator | ความหมาย |
| -------- | -------- |
| = | เท่ากับ |
| > | มากกว่า |
| < | น้อยกว่า |
| >= | มากกว่าหรือเท่ากับ |
| <= | น้อยกว่าหรือเท่ากับ |
| <> | ไม่เท่ากับ |

---

## SELECT Examples

ตัวอย่างทั้งหมดใช้ตาราง `COUNTRY` เดียวกัน (คอลัมน์ ID, Name, CCode) เป็นข้อมูลตั้งต้น

**Table: COUNTRY**

| ID | Name | CCode |
| -- | ---- | ----- |
| 1 | United States of America | US |
| 2 | China | CH |
| 3 | Japan | JA |
| 4 | Germany | GE |
| 5 | India | IN |
| 6 | United Kingdom | UK |
| 7 | France | FR |
| 8 | Italy | IT |
| 9 | Canada | CA |
| 10 | Brazil | BR |

### Example #1 — SELECT all columns

```sql
SELECT * FROM COUNTRY;
```

`SELECT *` คือดึงทุกคอลัมน์ `FROM COUNTRY` คือระบุตารางต้นทาง ผลลัพธ์คือทั้งตาราง COUNTRY ทุกแถวทุกคอลัมน์

**Result set:**

| ID | Name | CCode |
| -- | ---- | ----- |
| 1 | United States of America | US |
| 2 | China | CH |
| 3 | Japan | JA |
| 4 | Germany | GE |
| 5 | India | IN |
| 6 | United Kingdom | UK |
| 7 | France | FR |
| 8 | Italy | IT |
| 9 | Canada | CA |
| 10 | Brazil | BR |

### Example #2 — SELECT specific columns

```sql
SELECT ID, Name FROM COUNTRY;
```

`SELECT ID, Name` คือดึงเฉพาะสองคอลัมน์นี้จากทุกแถวที่ตรงเงื่อนไข (ในที่นี้ไม่มี WHERE จึงได้ทุกแถว)

**Result set:**

| ID | Name |
| -- | ---- |
| 1 | United States of America |
| 2 | China |
| 3 | Japan |
| 4 | Germany |
| 5 | India |
| 6 | United Kingdom |
| 7 | France |
| 8 | Italy |
| 9 | Canada |
| 10 | Brazil |

### Example #3 — SELECT with WHERE (numeric comparison)

```sql
SELECT * FROM COUNTRY WHERE ID <= 5;
```

`WHERE ID <= 5` กรองเฉพาะแถวที่ค่า ID น้อยกว่าหรือเท่ากับ 5

**Result set:**

| ID | Name | CCode |
| -- | ---- | ----- |
| 1 | United States of America | US |
| 2 | China | CH |
| 3 | Japan | JA |
| 4 | Germany | GE |
| 5 | India | IN |

### Example #4 — SELECT with WHERE (string comparison)

```sql
SELECT * FROM COUNTRY WHERE CCode = 'CA';
```

`WHERE CCode = 'CA'` กรองเฉพาะแถวที่ค่า CCode เท่ากับ 'CA' พอดี ได้ผลลัพธ์เพียงแถวเดียวคือ Canada

**Result set:**

| ID | Name | CCode |
| -- | ---- | ----- |
| 9 | Canada | CA |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| SELECT statement | คำสั่งดึงข้อมูล (query) จากตารางใน database |
| DML (Data Manipulation Language) | กลุ่มคำสั่งที่ใช้อ่านและแก้ไขข้อมูล เช่น SELECT |
| Result set / result table | ผลลัพธ์ที่ได้จากการรัน query |
| Predicate | เงื่อนไขที่ประเมินผลเป็น true, false หรือ unknown ใช้ใน WHERE clause |
| WHERE clause | ส่วนของ SELECT statement ที่ใช้กรองผลลัพธ์ตาม predicate |
| Comparison operator | ตัวดำเนินการเปรียบเทียบ เช่น =, >, <, >=, <=, <> ที่ใช้ใน predicate |

---

## ❓ My Questions & Gaps

- [ ] ถ้าต้องการใช้เงื่อนไขหลายอันพร้อมกันใน WHERE clause (AND/OR) ต้องเขียนอย่างไร — วิดีโอยังไม่ได้พูดถึง
- [ ] comparison operator กับ string (เช่น CCode = 'CA') ต่างจากกับตัวเลขอย่างไรในแง่ syntax และ case sensitivity

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงที่กล่าวถึงในวิดีโอนี้ (มี hands-on lab ในโมดูลนี้ที่ให้ฝึกใช้ SELECT query เพิ่มเติม)
