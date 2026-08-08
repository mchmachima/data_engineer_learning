# Database Usage Patterns

`Tags: RDBMS, ORM, database tools, DBA`

| Field            | Value                                            |
| ---------------- | ------------------------------------------------ |
| **Certificate**  | IBM Data Engineering Professional Certificate    |
| **Course**       | C04 Introduction to Relational Databases (RDBMS) |
| **Module**       | M01 Relational Database Concepts                 |
| **Lesson**       | L02 Introducing Relational Database Products     |
| **Date studied** | 2026-07-30                                       |

---

## Table of Contents

- [Overview](#overview)
- [Three User Groups and Their Tools](#three-user-groups-and-their-tools)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้แบ่งผู้ใช้งานฐานข้อมูลออกเป็น 3 กลุ่มหลักตามลักษณะงาน คือ data engineer/DBA, data scientist/business analyst และ application developer พร้อมยกตัวอย่างเครื่องมือที่แต่ละกลุ่มใช้เข้าถึงฐานข้อมูล ซึ่งช่วยให้เข้าใจว่าทำไม RDBMS แต่ละตัวถึงต้องรองรับ interface ที่หลากหลาย

---

## Three User Groups and Their Tools

ผู้ใช้งานฐานข้อมูลแบ่งได้เป็น 3 กลุ่มหลัก แต่ละกลุ่มใช้เครื่องมือต่างกัน

| กลุ่มผู้ใช้ | งานที่ทำ | เครื่องมือ |
| ----------- | -------- | ---------- |
| **Data Engineers และ Database Administrators (DBAs)** | งาน admin เช่น สร้าง/ดูแล database object, กำหนด access control, monitor และปรับปรุง performance | GUI/web-based management tools (เช่น Oracle SQL Developer), command-line interfaces ทั้งคำสั่งตรง (`db2 create database sample`, `mysqldump sakila > sakila.sql`) และ interactive shell (`sqlplus`, `db2 clp`), APIs สำหรับ automation |
| **Data Scientists และ Business Analysts** | อ่านข้อมูลเพื่อวิเคราะห์และคาดการณ์ บางครั้งสร้าง object ใน sandbox ของตัวเอง | Jupyter, R Studio, Zeppelin, SAS, SPSS (ฝั่ง data science/ML) และ Excel, Power BI, Tableau, MicroStrategy (ฝั่ง reporting/BI) — ส่วนใหญ่เชื่อมกับฐานข้อมูลผ่าน SQL interface/API โดยซ่อนรายละเอียด SQL ไว้เบื้องหลัง |
| **Application Developers** | เขียนแอปพลิเคชันที่สื่อสารกับฐานข้อมูล มักไม่เข้าถึงฐานข้อมูลโดยตรง | ภาษาต่าง ๆ (C++, C#, Java, JavaScript, .NET, PHP, Perl, Python, Ruby) เชื่อมผ่าน SQL interface/API เช่น ODBC, JDBC หรือ REST API — ปัจจุบันนิยมใช้ **ORM framework** เช่น ActiveRecord (Ruby), Django (Python), Entity Framework (.NET), Hibernate (Java), Sequelize (JavaScript) เพื่อซ่อนความซับซ้อนของ SQL |

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| ORM (Object Relational Mapping) | framework ที่ช่วยให้ภาษาโปรแกรมมิ่งเชิงวัตถุทำงานกับ relational database ได้ง่ายขึ้นโดยซ่อน SQL ไว้เบื้องหลัง |

---

## ❓ My Questions & Gaps

- [ ] ORM framework มีข้อเสียหรือ trade-off อะไรบ้างเมื่อเทียบกับการเขียน SQL ตรง ๆ โดยเฉพาะเรื่อง query performance

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
