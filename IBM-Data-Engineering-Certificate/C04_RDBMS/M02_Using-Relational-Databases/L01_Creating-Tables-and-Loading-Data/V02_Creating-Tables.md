# Creating Tables

`Tags: SQL, schema, ERD, Db2, RDBMS`

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
- [Preparing to Create a Table](#preparing-to-create-a-table)
- [Ways to Create a Table](#ways-to-create-a-table)
- [Creating a Table via Db2 on Cloud Console](#creating-a-table-via-db2-on-cloud-console)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายสิ่งที่ต้องเตรียมก่อนสร้างตารางในฐานข้อมูล ทั้งการเลือก schema และรายละเอียด column ต่าง ๆ พร้อมเปรียบเทียบสามวิธีหลักในการสร้างตาราง และเดินผ่านขั้นตอนจริงในการสร้างตารางผ่าน Db2 on Cloud console ซึ่งเป็นวิธีที่เป็นมิตรกับผู้เริ่มต้นที่ยังไม่คุ้นเคย SQL

---

## Preparing to Create a Table

การสร้างตารางต้องเตรียมข้อมูลและพิจารณาหลายอย่างล่วงหน้า ได้แก่ การเลือก schema ที่จะเก็บตาราง (schema ช่วยจัดระเบียบ database objects อย่างเป็นระบบ), การรวบรวมรายละเอียดที่จำเป็น เช่น ชื่อตาราง ชื่อ column และ data type ของแต่ละ column, การพิจารณาว่า column ใดอนุญาตให้มีค่าซ้ำ (duplicate) หรือค่าว่าง (null) ได้หรือไม่ และการใช้ Entity Relationship Diagram (ERD) ที่ทำไว้ตอนออกแบบฐานข้อมูลเป็นตัวอ้างอิง

---

## Ways to Create a Table

วิธีสร้างตารางมีสามแบบหลัก ๆ ซึ่งเหมาะกับสถานการณ์ต่างกัน:

| วิธี | เหมาะกับ | ตัวอย่างเครื่องมือ |
| ---- | -------- | ------------------- |
| **Visual interface / UI tools** | งานขนาดเล็กหรือไม่บ่อยนัก และผู้ที่ไม่คุ้นเคย SQL | Db2 on Cloud console, MySQL phpMyAdmin, PostgreSQL PGAdmin |
| **SQL statements** | งานที่ต้องการ automate การสร้างตารางหลายตาราง | `CREATE TABLE` เขียนเป็น script file |
| **Administrative APIs** | การสร้างและจัดการตารางแบบ programmatic | MongoDB กับ pymongo (Python driver) |

---

## Creating a Table via Db2 on Cloud Console

ขั้นตอนการสร้างตารางผ่าน Db2 on Cloud console มี 3 ส่วนหลัก: เลือก schema (default schema มักเป็นชื่อ username ของผู้ใช้), สร้างตารางใหม่และตั้งชื่อ (fully qualified name จะอยู่ในรูป `schema_name.table_name`), และกำหนด column ต่าง ๆ (data type, การอนุญาต null, ความยาว/scale) จากนั้นกด create เพื่อยืนยัน หลังสร้างตารางแล้วยังสามารถ alter โครงสร้าง, drop ตาราง, generate SQL code (select, insert, update, delete) หรือสำรวจ dependencies ของตารางได้

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Schema | พื้นที่จัดระเบียบ database objects อย่างเป็นระบบ (เหมือน namespace ของตาราง) |
| ERD (Entity Relationship Diagram) | แผนภาพแสดงความสัมพันธ์ระหว่าง entity ที่ใช้อ้างอิงตอนออกแบบฐานข้อมูล |
| Fully Qualified Name | ชื่อเต็มของตารางในรูป `schema_name.table_name` |

---

## ❓ My Questions & Gaps

- [ ] Administrative API สำหรับ RDBMS (ไม่ใช่ MongoDB) มีตัวอย่างการใช้งานจริงอย่างไรบ้าง เพราะตัวอย่างในวิดีโอเป็น NoSQL

---

## 🔗 Resources

- Db2 on Cloud console (IBM) — visual interface สำหรับสร้างและจัดการตาราง
