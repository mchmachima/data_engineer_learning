# Information Models and Data Models

`Tags: RDBMS, information model, data model, ER model, data independence`

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
- [Information Models vs Data Models](#information-models-vs-data-models)
- [The Hierarchical Model](#the-hierarchical-model)
- [Types of Data Models: Relational and Entity-Relationship (ER)](#types-of-data-models-relational-and-entity-relationship-er)
- [Data Independence Concepts](#data-independence-concepts)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายความแตกต่างระหว่าง information model ที่เป็นแนวคิดเชิงนามธรรม กับ data model ที่เป็น blueprint ทางเทคนิค พร้อมแนะนำ hierarchical model ในฐานะตัวอย่างการ implement ยุคแรก และเปรียบเทียบ relational model กับ ER model ซึ่งเป็น data model สองแบบที่พบบ่อยที่สุด ปิดท้ายด้วยแนวคิด data independence สามแบบที่ช่วยให้ระบบฐานข้อมูลปรับตัวได้โดยไม่กระทบส่วนอื่น

---

## Information Models vs Data Models

Information model คือกรอบแนวคิดที่แสดง entity, property, relationship และ function ในระดับนามธรรม ให้ stakeholder มองเห็นภาพรวมของข้อมูลโดยไม่ต้องลงรายละเอียดการนำไปใช้งานจริง ส่วน data model ทำงานในระดับที่จับต้องได้มากกว่า โดยแปลงมุมมองเชิงแนวคิดนั้นให้เป็น blueprint ทางเทคนิค: schema, ตาราง, คอลัมน์, data type, index และความสัมพันธ์ (มักผ่านการปรับปรุงด้วย normalization)

| Aspect | Information Model | Data Model |
| --- | --- | --- |
| ระดับความเป็นนามธรรม | สูง — เชิงแนวคิด ไม่ผูกกับเทคโนโลยี | ต่ำ — จับต้องได้ เชิงเทคนิค |
| จุดเน้น | แนวคิดทางธุรกิจและความสัมพันธ์ในภาพกว้าง | การจัดเก็บ, schema และวิธีจัดการเชิงเทคนิค |
| รายละเอียด | รายละเอียดน้อยกว่า | ละเอียด (ตาราง, คอลัมน์, data type, constraint) |
| ผูกกับ DBMS เฉพาะเจาะจงหรือไม่ | ไม่ | ส่วนใหญ่ผูก |
| ผู้ใช้งาน | Business analyst และ stakeholder | Database designer และ developer |
| จุดประสงค์ | ตกลงแนวคิดทางธุรกิจโดยไม่ต้องลงรายละเอียดเทคนิค | สร้างและ implement ระบบฐานข้อมูลจริง |

ในการพัฒนาระบบ information model จะจับภาพประเภทข้อมูลทางธุรกิจที่จำเป็นก่อน จากนั้นจึงถูกแปลงเป็น data model ซึ่งเป็น blueprint ทางเทคนิคสำหรับระบบฐานข้อมูล

---

## The Hierarchical Model

Hierarchical model เป็นการ implement ทางกายภาพของระบบข้อมูล โดยเก็บความสัมพันธ์ในรูปแบบ tree — ต่างจาก information model ที่เป็นเพียงแนวคิดความสัมพันธ์โดยไม่ระบุการจัดเก็บ

| Aspect | Information Model | Hierarchical Model |
| --- | --- | --- |
| ความเป็นนามธรรม | สูง — เป็นแนวคิดโดยไม่ระบุการจัดเก็บ | ต่ำกว่า — จัดโครงสร้างข้อมูลแบบ tree ทางกายภาพ |
| การจัดการความสัมพันธ์ | แสดงความสัมพันธ์ของ entity ได้ชัดเจนสำหรับสถานการณ์จริง | มีปัญหากับความสัมพันธ์แบบ many-to-many |
| ผลลัพธ์ | ไม่มี (เป็นแนวคิดล้วน ๆ) | ข้อจำกัดเชิงโครงสร้างอาจนำไปสู่ความซ้ำซ้อนของข้อมูล |
| บทบาททางประวัติศาสตร์ | ไม่มี | มีรากฐานจากระบบฐานข้อมูลยุคแรก เชื่อมโยงกับช่วงเริ่มต้นของ information model |

---

## Types of Data Models: Relational and Entity-Relationship (ER)

Data model ที่พบบ่อยที่สุด 2 ประเภทคือ **relational model** และ **entity-relationship (ER) model**

- **Relational model** — data model ที่ใช้กันแพร่หลายที่สุดสำหรับฐานข้อมูล จัดเก็บข้อมูลในตาราง และให้ logical, physical และ storage independence ข้อดีคือความเรียบง่าย ยืดหยุ่น และใช้งานง่าย
- **ER model** — ทางเลือกที่มองฐานข้อมูลเป็นกลุ่มของ entity และ object ที่มีอยู่อย่างเป็นอิสระต่อกัน entity แสดงเป็นสี่เหลี่ยม attribute แสดงเป็นวงรี (เช่น ในฐานข้อมูลห้องสมุด `Author` เป็น entity ที่มี attribute อย่าง last name, first name, email) ER diagram (ERD) ใช้สำหรับขั้นตอนออกแบบเชิงแนวคิด แล้วจึงถูกแปลงเป็นตาราง — แต่ละ entity กลายเป็นตาราง และ attribute กลายเป็นคอลัมน์

| Aspect | Relational Model | Entity-Relationship (ER) Model |
| --- | --- | --- |
| การนำเสนอ | ข้อมูลถูกเก็บในตารางโดยตรง | Entity (สี่เหลี่ยม) และ attribute (วงรี) ใน diagram |
| การใช้งานทั่วไป | การจัดเก็บ/implement ฐานข้อมูลจริง | ขั้นตอนออกแบบเชิงแนวคิด ก่อน implement |
| Independence | ให้ logical, physical และ storage independence | ไม่มี — เป็นเครื่องมือออกแบบ/สร้างโมเดล |
| ความสัมพันธ์ระหว่างกัน | เป็นเป้าหมายปลายทางของการ implement | ถูกแปลงเป็นตาราง (entity → table, attribute → column) |
| ตัวอย่าง | ตารางเช่น `Books`, `Authors`, `Borrowers` | ERD แสดง entity `Book`, `Author`, `Borrower` และความสัมพันธ์ระหว่างกัน |

---

## Data Independence Concepts

มีแนวคิด 3 อย่างที่ช่วยให้ระบบฐานข้อมูลปรับตัวและมีประสิทธิภาพ โดยแต่ละอย่างจะแยกชั้นหนึ่งของระบบออกจากการเปลี่ยนแปลงในอีกชั้นหนึ่ง:

| Independence Type | สิ่งที่เปลี่ยนแปลงได้ | สิ่งที่ไม่ได้รับผลกระทบ |
| --- | --- | --- |
| Logical data independence | โครงสร้างฐานข้อมูล (เช่น เปลี่ยน data type, เพิ่ม field) | การเข้าถึงข้อมูลของผู้ใช้ |
| Physical data independence | การจัดระเบียบภายในฐานข้อมูล (เช่น ประเภทการจัดเก็บ, กลยุทธ์ indexing) | View หรือแอปพลิเคชันของผู้ใช้ |
| Physical storage independence | ตำแหน่ง/การจัดระเบียบข้อมูลบนอุปกรณ์จัดเก็บทางกายภาพ | โปรแกรมแอปพลิเคชันที่ประมวลผลข้อมูล |

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Information model | การนำเสนอเชิงแนวคิดแบบนามธรรมของ entity, property, relationship และ function |
| Data model | Blueprint ทางเทคนิคที่แปลง information model ให้เป็นโครงสร้างฐานข้อมูล |
| Hierarchical model | Data model ยุคแรกที่จัดโครงสร้างข้อมูลแบบ tree ทางกายภาพ |
| Relational model | Data model ที่ใช้กันแพร่หลายที่สุด จัดเก็บข้อมูลในตาราง พร้อม logical/physical/storage independence |
| Entity-Relationship (ER) model | Model เชิงแนวคิดที่แสดงฐานข้อมูลเป็น entity และความสัมพันธ์ระหว่างกัน |
| Logical data independence | ความสามารถในการเปลี่ยนโครงสร้างฐานข้อมูลโดยไม่กระทบการเข้าถึงข้อมูลของผู้ใช้ |
| Physical data independence | ความสามารถในการเปลี่ยนการจัดเก็บ/indexing ภายในโดยไม่กระทบ view หรือแอปพลิเคชันของผู้ใช้ |
| Physical storage independence | ความสามารถในการย้าย/จัดระเบียบข้อมูลบนอุปกรณ์จัดเก็บโดยไม่กระทบแอปพลิเคชัน |

---

## ❓ My Questions & Gaps

- [ ] ข้อจำกัดเชิงโครงสร้างแบบไหนที่ทำให้ hierarchical model มีปัญหากับความสัมพันธ์ many-to-many
- [ ] ในทางปฏิบัติ independence ทั้งสามแบบต่างกันอย่างไรเมื่อมีการเปลี่ยนแปลง schema จริง (เช่น เพิ่ม index เทียบกับเพิ่มคอลัมน์)

---

## 🔗 Resources

- https://www.geeksforgeeks.org/dbms/what-is-data-independence-in-dbms/
