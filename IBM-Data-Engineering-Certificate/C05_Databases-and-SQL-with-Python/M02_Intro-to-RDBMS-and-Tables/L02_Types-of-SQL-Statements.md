# Types of SQL Statements

`Tags: SQL, DDL, DML, CRUD`

| Field            | Value                                         |
| ---------------- | --------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate |
| **Course**       | C05 Databases and SQL with Python             |
| **Module**       | M02 Intro to RDBMS and Tables                 |
| **Lesson**       | L02 Types of SQL Statements                   |
| **Date studied** | 2026-08-12                                    |

---

## Table of Contents

- [Overview](#overview)
- [Data Definition Language (DDL)](#data-definition-language-ddl)
- [Data Manipulation Language (DML)](#data-manipulation-language-dml)
- [DDL vs DML](#ddl-vs-dml)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้แบ่งประเภทของ SQL statement ที่ใช้จัดการ entity (table), attribute (column) และ tuple (row) ในฐานข้อมูลเชิงสัมพันธ์ออกเป็น 2 กลุ่มหลัก คือ Data Definition Language (DDL) สำหรับนิยามหรือเปลี่ยนแปลงโครงสร้างของ object ในฐานข้อมูล และ Data Manipulation Language (DML) สำหรับอ่านและแก้ไขข้อมูลภายใน table เนื้อหาครอบคลุม statement type หลักของแต่ละกลุ่ม พร้อมหน้าที่ของแต่ละคำสั่ง

---

## Data Definition Language (DDL)

DDL statement ใช้สำหรับนิยาม (define), เปลี่ยนแปลง (change) หรือลบ (drop) object ในฐานข้อมูล เช่น table

| Statement | หน้าที่                                                                    |
| --------- | -------------------------------------------------------------------------- |
| CREATE    | สร้าง table และกำหนด column ของ table นั้น                                 |
| ALTER     | แก้ไขโครงสร้าง table เช่น เพิ่ม/ลบ column หรือเปลี่ยน data type ของ column |
| TRUNCATE  | ลบข้อมูลทั้งหมดใน table แต่ไม่ลบตัว table                                  |
| DROP      | ลบ table ทิ้งทั้งหมด                                                       |

---

## Data Manipulation Language (DML)

DML statement ใช้สำหรับอ่านและแก้ไขข้อมูลใน table เรียกอีกชื่อว่า CRUD operation (Create, Read, Update, Delete)

| Statement | หน้าที่                                          |
| --------- | ------------------------------------------------ |
| INSERT    | เพิ่มข้อมูล 1 row หรือหลาย row เข้าไปใน table    |
| SELECT    | อ่านหรือเลือกข้อมูล 1 row หรือหลาย row จาก table |
| UPDATE    | แก้ไขข้อมูล 1 row หรือหลาย row ใน table          |
| DELETE    | ลบข้อมูล 1 row หรือหลาย row ออกจาก table         |

---

## DDL vs DML

| แง่มุม          | DDL (Data Definition Language)                          | DML (Data Manipulation Language)                             |
| --------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| จุดประสงค์      | นิยาม เปลี่ยนแปลง หรือลบ object ในฐานข้อมูล (โครงสร้าง) | อ่านและแก้ไขข้อมูลภายใน table (เนื้อหาข้อมูล)                |
| ผลกระทบ         | เปลี่ยนแปลง schema/โครงสร้างของ table                   | เปลี่ยนแปลง row/ค่าข้อมูลใน table โดยโครงสร้างเดิมไม่เปลี่ยน |
| Statement หลัก  | CREATE, ALTER, TRUNCATE, DROP                           | INSERT, SELECT, UPDATE, DELETE                               |
| เรียกอีกชื่อว่า | —                                                       | CRUD operation                                               |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์)                     | คำอธิบาย (ภาษาไทย)                                                           |
| -------------------------------- | ---------------------------------------------------------------------------- |
| DDL (Data Definition Language)   | กลุ่มคำสั่ง SQL ที่ใช้นิยาม เปลี่ยนแปลง หรือลบ object ในฐานข้อมูล เช่น table |
| DML (Data Manipulation Language) | กลุ่มคำสั่ง SQL ที่ใช้อ่านและแก้ไขข้อมูลใน table                             |
| CRUD                             | ตัวย่อของ Create, Read, Update, Delete ซึ่งเป็นการดำเนินการพื้นฐานกับข้อมูล  |
| CREATE                           | คำสั่งสร้าง table และกำหนด column                                            |
| ALTER                            | คำสั่งแก้ไขโครงสร้าง table                                                   |
| TRUNCATE                         | คำสั่งลบข้อมูลทั้งหมดใน table โดยยังคงตัว table ไว้                          |
| DROP                             | คำสั่งลบ table ทั้งหมด                                                       |
| INSERT                           | คำสั่งเพิ่ม row ข้อมูลเข้า table                                             |
| SELECT                           | คำสั่งอ่านข้อมูลจาก table                                                    |
| UPDATE                           | คำสั่งแก้ไขข้อมูลใน table                                                    |
| DELETE                           | คำสั่งลบ row ข้อมูลออกจาก table                                              |

---

## ❓ My Questions & Gaps

- [x] ความแตกต่างระหว่าง TRUNCATE กับ DELETE (ทั้งคู่ลบข้อมูลแต่ต่างกันอย่างไรในแง่ performance และ transaction log)
  - `TRUNCATE` เป็น DDL statement ที่ลบข้อมูลทั้งหมดใน table ทีเดียวโดยไม่บันทึก log ของแต่ละ row (บันทึกแค่การจัดสรร page) จึงเร็วกว่าและใช้ transaction log น้อยกว่ามาก แต่ไม่สามารถใส่ `WHERE` เพื่อลบเฉพาะบาง row ได้
  - ส่วน `DELETE` เป็น DML statement ที่ลบทีละ row พร้อมบันทึก log ของแต่ละ row (จึง rollback ได้ละเอียดกว่าและใช้ trigger ได้) และสามารถใส่ `WHERE` เพื่อลบเฉพาะบาง row ได้ แต่ช้ากว่าเมื่อลบข้อมูลจำนวนมาก
- [x] มี SQL statement กลุ่มอื่นนอกจาก DDL/DML อีกหรือไม่ (เช่น DCL, TCL) และครอบคลุมคำสั่งอะไรบ้าง
  - กลุ่มหลักที่พบบ่อย ได้แก่ **DCL (Data Control Language)** ใช้จัดการสิทธิ์การเข้าถึงข้อมูล เช่น `GRANT` (ให้สิทธิ์) และ `REVOKE` (เพิกถอนสิทธิ์)
  - และ **TCL (Transaction Control Language)** ใช้จัดการ transaction เช่น `COMMIT` (บันทึกการเปลี่ยนแปลงถาวร), `ROLLBACK` (ยกเลิกการเปลี่ยนแปลง) และ `SAVEPOINT` (ตั้งจุดย้อนกลับระหว่าง transaction)

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารเพิ่มเติมที่กล่าวถึงในวิดีโอนี้
