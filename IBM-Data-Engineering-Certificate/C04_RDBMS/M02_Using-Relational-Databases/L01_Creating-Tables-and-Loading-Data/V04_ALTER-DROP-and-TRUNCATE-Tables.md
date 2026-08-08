# ALTER, DROP, and TRUNCATE Tables

`Tags: SQL, ALTER TABLE, DROP TABLE, TRUNCATE, RDBMS`

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
- [ALTER TABLE](#alter-table)
- [DROP TABLE vs. TRUNCATE TABLE](#drop-table-vs-truncate-table)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายคำสั่ง DDL อีกสามตัวที่ใช้จัดการตารางที่มีอยู่แล้ว คือ `ALTER TABLE` สำหรับแก้ไขโครงสร้างตาราง และ `DROP TABLE` กับ `TRUNCATE TABLE` สำหรับลบตารางหรือลบข้อมูล ซึ่งทั้งสองคำสั่งหลังนี้มีผลทำลายข้อมูลแบบย้อนกลับไม่ได้ จึงต้องเข้าใจความต่างให้ชัดก่อนใช้งานจริง

---

## ALTER TABLE

**ALTER TABLE** ใช้สำหรับเพิ่ม/ลบ column, เปลี่ยน data type ของ column, หรือเพิ่ม/ลบ key และ constraint จากตารางที่มีอยู่แล้ว ต่างจาก CREATE TABLE ตรงที่ไม่ต้องใช้วงเล็บครอบพารามิเตอร์ และแต่ละแถวระบุการเปลี่ยนแปลงหนึ่งอย่างที่ต้องการทำ

การเปลี่ยน data type ของ column ที่มีข้อมูลอยู่แล้วอาจเกิดปัญหาได้ถ้าข้อมูลเดิมไม่ compatible กับ data type ใหม่ (เช่น เปลี่ยนจาก CHAR เป็น numeric แต่มีข้อมูลที่ไม่ใช่ตัวเลขอยู่ จะเกิด error และคำสั่งจะไม่ทำงาน)

```sql
-- Add a new column to an existing table
ALTER TABLE author ADD COLUMN telephone_number BIGINT;

-- Change the data type of an existing column
ALTER TABLE author ALTER COLUMN telephone_number SET DATA TYPE CHAR(20);

-- Remove a column from a table
ALTER TABLE author DROP COLUMN telephone_number;
```

---

## DROP TABLE vs. TRUNCATE TABLE

ทั้งสองคำสั่งลบข้อมูลแบบย้อนกลับไม่ได้ แต่ขอบเขตของการลบต่างกัน:

| คำสั่ง | ลบอะไร | ตัวตารางยังอยู่ไหม |
| ------ | ------ | -------------------- |
| **DROP TABLE** | ลบตารางทั้งหมดออกจากฐานข้อมูล และข้อมูลในตารางจะถูกลบไปพร้อมกันโดย default | ไม่อยู่ |
| **TRUNCATE TABLE** | ลบข้อมูล (rows) ทั้งหมดในตาราง | ยังอยู่ — มีประสิทธิภาพกว่าการใช้ `DELETE` โดยไม่มี WHERE clause |

คำ `IMMEDIATE` ในคำสั่ง TRUNCATE บ่งบอกว่าเป็นการประมวลผลทันทีและ**ไม่สามารถย้อนกลับได้**

```sql
-- Delete an entire table from the database
DROP TABLE author;

-- Delete all rows in a table without deleting the table itself
TRUNCATE TABLE author IMMEDIATE;
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| ALTER TABLE | คำสั่งแก้ไขโครงสร้างตารางที่มีอยู่แล้ว เช่น เพิ่ม/ลบ column, เปลี่ยน data type |
| DROP TABLE | คำสั่งลบตารางทั้งหมดออกจากฐานข้อมูล พร้อมข้อมูลในตาราง |
| TRUNCATE | คำสั่งลบข้อมูลทั้งหมดในตารางโดยไม่ลบตัวตาราง และไม่สามารถย้อนกลับได้ |

---

## ❓ My Questions & Gaps

- [ ] การเปลี่ยน data type ของ column ที่มีข้อมูลไม่ compatible ควรมีขั้นตอน migrate ข้อมูลอย่างไรให้ปลอดภัย

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
