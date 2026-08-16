# Getting Table and Column Details

`Tags: SQL, SQLite3, MySQL, system catalog`

| Field            | Value                                                            |
| ---------------- | ---------------------------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate                    |
| **Course**       | C05 Databases and SQL for Data Science with Python               |
| **Module**       | M05 Final Project                                                |
| **Lesson**       | L01 Working with Real-World Data Sets and Built-in SQL Functions |
| **Date studied** | 2026-08-15                                                       |

---

## Table of Contents

- [Overview](#overview)
- [Listing Tables via System Catalogs](#listing-tables-via-system-catalogs)
- [Getting Column Details](#getting-column-details)
- [Counting Columns in a Table](#counting-columns-in-a-table)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายวิธีตรวจสอบว่าฐานข้อมูลมี table อะไรบ้าง และแต่ละ table มี column อะไรบ้าง โดยอาศัย system หรือ catalog table ที่ database engine แต่ละตัวมีให้ ซึ่งมีชื่อและ syntax แตกต่างกันไปในแต่ละ database system เนื้อหานี้สำคัญเมื่อทำงานกับฐานข้อมูลที่ไม่คุ้นเคย และจำชื่อ table หรือโครงสร้าง column ไม่ได้แน่ชัด

---

## Listing Tables via System Catalogs

Database system ส่วนใหญ่มี system หรือ catalog table ที่เก็บ metadata ของ table ทั้งหมดในฐานข้อมูล ชื่อ catalog table นี้แตกต่างกันไปตามแต่ละระบบ

| Database System | Catalog / Command สำหรับ list table |
| --------------- | ----------------------------------- |
| DB2             | `SYSCAT.TABLES`                     |
| SQL Server      | `INFORMATION_SCHEMA.TABLES`         |
| SQLite3         | `sqlite_master`                     |
| MySQL           | `SHOW TABLES`                       |

```sql
-- ดึงรายชื่อ table ทั้งหมดใน SQLite3 database
SELECT name FROM sqlite_master WHERE type='table';
```

```sql
-- ดึงรายชื่อ table ทั้งหมดใน MySQL
SHOW TABLES;
```

---

## Getting Column Details

การดึงชื่อ attribute หรือ column header ของ table ใช้คำสั่งเฉพาะของแต่ละ database server เช่นกัน ใน SQLite3 ใช้คำสั่ง `PRAGMA table_info` ส่วนใน MySQL ใช้คำสั่ง `DESCRIBE table_name`

```sql
-- ดึงรายละเอียด column ของ table ใน SQLite3
PRAGMA table_info(table_name);
```

```sql
-- ดึงรายละเอียด column ของ table ใน MySQL
DESCRIBE table_name;
```

---

## Counting Columns in a Table

นอกจากดึงรายละเอียด column ทั้งหมดด้วย `PRAGMA table_info` แล้ว ยังสามารถใช้ `PRAGMA_TABLE_INFO` เป็น table-valued function ใน SQLite3 คือเรียกใช้เหมือน table ปกติใน `FROM` clause ได้ ทำให้นำไป query ต่อได้ เช่นนับจำนวน column ทั้งหมดของ table ด้วย `count()`

```sql
-- นับจำนวน column ทั้งหมดของตาราง table_name
SELECT count(name) FROM PRAGMA_TABLE_INFO('table_name');
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์)         | คำอธิบาย (ภาษาไทย)                                                                                                                       |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| System/Catalog table | table พิเศษที่ database system สร้างไว้ให้อัตโนมัติ เก็บ metadata เช่นรายชื่อ table และ column ในฐานข้อมูล                               |
| sqlite_master        | catalog table ของ SQLite3 ที่เก็บข้อมูลของ object ทั้งหมดในฐานข้อมูล รวมถึง table                                                        |
| SHOW TABLES          | คำสั่งของ MySQL ใช้แสดงรายชื่อ table ทั้งหมดในฐานข้อมูลปัจจุบัน                                                                          |
| PRAGMA table_info    | คำสั่งของ SQLite3 ใช้ดึงรายละเอียด column ของ table ที่ระบุ                                                                              |
| PRAGMA_TABLE_INFO()  | table-valued function ของ SQLite3 ที่คืนรายละเอียด column ของ table เป็น result set นำไป query ต่อได้ เช่นนับจำนวน column ด้วย `count()` |
| DESCRIBE             | คำสั่งของ MySQL ใช้ดึงรายละเอียด column ของ table ที่ระบุ                                                                                |

---

## ❓ My Questions & Gaps

- [ ] `INFORMATION_SCHEMA.TABLES` ของ SQL Server ให้ข้อมูลอะไรเพิ่มเติมนอกจากชื่อ table บ้าง (เช่น schema, ประเภท)
- [ ] มีคำสั่งเทียบเท่า `DESCRIBE` หรือ `PRAGMA table_info` ใน PostgreSQL หรือ DB2 หรือไม่

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารเพิ่มเติมที่กล่าวถึงในวิดีโอ
