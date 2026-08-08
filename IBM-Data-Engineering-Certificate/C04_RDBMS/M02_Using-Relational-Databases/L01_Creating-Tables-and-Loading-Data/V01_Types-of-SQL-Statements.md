# Types of SQL Statements (DDL vs. DML)

`Tags: SQL, DDL, DML, RDBMS`

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
- [DDL vs. DML](#ddl-vs-dml)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้แยกประเภทคำสั่ง SQL ออกเป็นสองกลุ่มหลักตามหน้าที่การใช้งาน คือ DDL สำหรับสร้าง/แก้ไข/ลบ database object เช่น table และ DML สำหรับอ่านและแก้ไขข้อมูลในตาราง เป็นพื้นฐานที่ต้องเข้าใจก่อนลงมือสร้างตารางจริงในวิดีโอถัดไป

---

## DDL vs. DML

คำสั่ง SQL แบ่งออกเป็นสองกลุ่มหลัก ตามหน้าที่การใช้งานกับ entities (tables), attributes (columns) และ tuples (rows)

| กลุ่มคำสั่ง | ใช้ทำอะไร | คำสั่งหลัก |
| ----------- | --------- | ---------- |
| **DDL** (Data Definition Language) | define, change หรือ drop database objects เช่น table | `CREATE` สร้างตารางและกำหนด columns · `ALTER` แก้ไขตาราง (เพิ่ม/ลบ column, เปลี่ยน data type) · `TRUNCATE` ลบข้อมูลทั้งหมดแต่ไม่ลบตัวตาราง · `DROP` ลบตารางทั้งหมด |
| **DML** (Data Manipulation Language) | อ่านและแก้ไขข้อมูลในตาราง หรือที่เรียกว่า CRUD operations | `INSERT` (Create) เพิ่มแถวข้อมูล · `SELECT` (Read) อ่าน/เลือกแถวข้อมูล · `UPDATE` (Update) แก้ไขแถวข้อมูล · `DELETE` (Delete) ลบแถวข้อมูล |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| DDL (Data Definition Language) | กลุ่มคำสั่ง SQL สำหรับ define/change/drop database object เช่น table (CREATE, ALTER, TRUNCATE, DROP) |
| DML (Data Manipulation Language) | กลุ่มคำสั่ง SQL สำหรับอ่านและแก้ไขข้อมูลในตาราง (INSERT, SELECT, UPDATE, DELETE) / CRUD |
| CRUD | ตัวย่อของ Create, Read, Update, Delete — การดำเนินการพื้นฐานสี่แบบกับข้อมูล |

---

## ❓ My Questions & Gaps

- [ ] มีคำสั่ง SQL กลุ่มอื่นนอกจาก DDL/DML อีกหรือไม่ (เช่น DCL สำหรับ permission, TCL สำหรับ transaction) และเกี่ยวข้องกับงาน data engineer แค่ไหน

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
