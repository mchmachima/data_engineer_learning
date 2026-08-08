# Database Objects

`Tags: RDBMS, database objects, schema`

| Field             | Value                                            |
| ----------------- | ------------------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate    |
| **Course**        | C04 Introduction to Relational Databases (RDBMS) |
| **Module**        | M01 Relational Database Concepts                 |
| **Lesson**        | L01 Fundamental Relational Database Concepts     |
| **Date studied**  | 2026-07-12                                       |

---

## Table of Contents

- [Overview](#overview)
- [What Is a Database Object](#what-is-a-database-object)
- [Common Database Objects](#common-database-objects)
- [Why Database Objects Matter](#why-database-objects-matter)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายว่า database object คืออะไร พร้อมยกตัวอย่าง object แต่ละประเภทที่พบบ่อยในฐานข้อมูล (table, view, index, constraint, stored procedure, trigger, schema, sequence) โดยเปรียบเทียบกับสิ่งปลูกสร้างในอาคารเพื่อให้เข้าใจง่ายขึ้น และปิดท้ายด้วยเหตุผลว่าทำไมความเข้าใจเรื่อง object เหล่านี้ถึงสำคัญต่อการออกแบบและดูแลฐานข้อมูล

---

## What Is a Database Object

ใน Database Management System (DBMS) คำว่า **Object (ออบเจกต์ในฐานข้อมูล)** หมายถึง **องค์ประกอบเชิงโครงสร้างต่าง ๆ ที่ถูกสร้าง จัดเก็บ และใช้งานภายในฐานข้อมูล** เพื่อจัดเก็บ จัดการ ค้นหา หรือควบคุมความปลอดภัยของข้อมูล

ถ้าเปรียบฐานข้อมูลเป็น "เมืองใหญ่" หรือ "อาคารสำนักงาน" database object ก็เปรียบเสมือนสิ่งปลูกสร้างและระบบภายในนั้น เช่น ห้องเก็บของ, ตู้เอกสาร, ถนน หรือกุญแจล็อคห้อง — แต่ละอย่างมีหน้าที่เฉพาะตัว แต่ทำงานร่วมกันเพื่อให้ทั้งระบบใช้งานได้จริง

---

## Common Database Objects

| Object | เปรียบเทียบ | หน้าที่ |
| --- | --- | --- |
| **Table** | ตู้เอกสาร/ชั้นวางของ | จัดเก็บข้อมูลจริงเป็นแถวและคอลัมน์ เป็น object พื้นฐานที่สุด |
| **View** | หน้าต่างมองเข้าไปในตู้เอกสาร | มุมมองเสมือนที่สร้างจาก query บนตารางหนึ่งตัวหรือมากกว่า โดยไม่เก็บข้อมูลซ้ำ |
| **Index** | สารบัญหรือป้ายบอกทาง | โครงสร้างช่วยให้ค้นหาแถวข้อมูลในตารางได้เร็วขึ้น โดยไม่ต้องไล่อ่านทั้งตาราง |
| **Primary/Foreign Key (Constraint)** | กุญแจล็อคห้อง | บังคับกฎความถูกต้องของข้อมูล เช่น ห้ามซ้ำ (primary key) หรือบังคับความสัมพันธ์ระหว่างตาราง (foreign key) |
| **Stored Procedure** | คู่มือขั้นตอนการทำงานที่เก็บไว้ใช้ซ้ำ | ชุดคำสั่ง SQL ที่เขียนไว้ล่วงหน้าและเรียกใช้งานซ้ำได้ |
| **Trigger** | ระบบเซนเซอร์อัตโนมัติ | ชุดคำสั่งที่ทำงานอัตโนมัติเมื่อมีเหตุการณ์เกิดขึ้นกับตาราง (เช่น insert, update, delete) |
| **Schema** | ผังของอาคารทั้งหลัง | พื้นที่เชิงตรรกะที่ใช้จัดกลุ่ม object ต่าง ๆ (ตาราง, view, index ฯลฯ) ไว้ด้วยกัน |
| **Sequence** | เครื่องออกบัตรคิว | สร้างค่าตัวเลขที่เพิ่มขึ้นเรื่อย ๆ โดยอัตโนมัติ มักใช้เป็นค่า primary key |

---

## Why Database Objects Matter

- ช่วยแยกหน้าที่ของแต่ละองค์ประกอบในฐานข้อมูลให้ชัดเจน (จัดเก็บข้อมูล, ควบคุมความปลอดภัย, เพิ่มประสิทธิภาพการค้นหา, บังคับใช้กฎของข้อมูล)
- เป็นหน่วยที่ DBA และ data engineer ใช้อ้างอิงเมื่อกำหนดสิทธิ์การเข้าถึง (access control) เช่น อนุญาตให้ user เข้าถึงเฉพาะ view แทนที่จะเข้าถึงตารางต้นฉบับโดยตรง
- การเข้าใจว่า object แต่ละประเภททำหน้าที่อะไร เป็นพื้นฐานสำคัญก่อนจะออกแบบและ implement โครงสร้างฐานข้อมูลจริง

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Database Object | องค์ประกอบเชิงโครงสร้างที่ถูกสร้าง จัดเก็บ และใช้งานภายในฐานข้อมูล เช่น table, view, index, stored procedure |
| Index | โครงสร้างที่ช่วยให้ค้นหาแถวข้อมูลในตารางได้เร็วขึ้น โดยไม่ต้องไล่อ่านทั้งตาราง |
| Stored Procedure | ชุดคำสั่ง SQL ที่เขียนไว้ล่วงหน้าและเรียกใช้งานซ้ำได้ |
| Trigger | ชุดคำสั่งที่ทำงานอัตโนมัติเมื่อมีเหตุการณ์เกิดขึ้นกับตาราง เช่น insert, update, delete |
| Schema (object) | พื้นที่เชิงตรรกะที่ใช้จัดกลุ่ม database object ต่าง ๆ ไว้ด้วยกัน |
| Sequence | Object ที่สร้างค่าตัวเลขเพิ่มขึ้นเรื่อย ๆ โดยอัตโนมัติ มักใช้เป็นค่า primary key |

---

## ❓ My Questions & Gaps

- [ ] Primary key ต่างจาก unique identifier แบบอื่นอย่างไร และเมื่อไรที่ตารางต้องใช้ composite primary key

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
