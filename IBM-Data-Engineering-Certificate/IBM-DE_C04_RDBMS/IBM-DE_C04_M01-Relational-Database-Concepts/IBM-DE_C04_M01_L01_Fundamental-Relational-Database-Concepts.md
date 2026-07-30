# L01 Fundamental Relational Database Concepts

`Tags: RDBMS, database, data-model, ERD, normalization, data-types`

| Field             | Value                                            |
| ----------------- | ------------------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate    |
| **Course**        | C04 Introduction to Relational Databases (RDBMS) |
| **Module**        | M01 Relational Database Concepts                 |
| **Date studied**  | 2026-07-12                                       |

---

## Table of Contents

- [Overview](#overview)
- [Data and Data Repositories](#data-and-data-repositories)
- [Database Objects](#database-objects)
- [Information Models and Data Models](#information-models-and-data-models)
- [ERDs and Types of Relationships](#erds-and-types-of-relationships)
- [Mapping Entities to Tables](#mapping-entities-to-tables)
- [Data Types](#data-types)
- [Relational Model Concepts](#relational-model-concepts)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

บทเรียนนี้ปูพื้นฐานแนวคิดของฐานข้อมูลเชิงสัมพันธ์ (relational database) ตั้งแต่ประเภทของข้อมูล (structured, unstructured, semi-structured), data repository และความหมายของ database object (table, view, index, stored procedure ฯลฯ) ที่ประกอบกันขึ้นเป็นฐานข้อมูล ไปจนถึงความแตกต่างระหว่าง information model กับ data model รวมถึงวิธีใช้ ERD (Entity Relationship Diagram) เพื่อออกแบบฐานข้อมูลและแปลงเป็นตารางจริง นอกจากนี้ยังครอบคลุม data type ที่ใช้กำหนดชนิดข้อมูลในแต่ละคอลัมน์ และปิดท้ายด้วยรากฐานทางคณิตศาสตร์ของ relational model อย่าง set และ relation ซึ่งเป็นพื้นฐานสำคัญก่อนจะเข้าสู่เรื่อง normalization ในบทเรียนถัดไป

---

## Data and Data Repositories

### Data and Data Structures

Data คือข้อมูลดิบที่ยังไม่ผ่านการจัดระเบียบ — ข้อเท็จจริง, การสังเกตการณ์, ตัวเลข, ตัวอักษร, สัญลักษณ์, รูปภาพ หรือรวมกันหลายแบบ — ซึ่งจะมีความหมายก็ต่อเมื่อผ่านการประมวลผลแล้ว วิธีจัดโครงสร้างของข้อมูลส่งผลต่อประสิทธิภาพในการจัดเก็บ จัดการ และวิเคราะห์ แบ่งเป็น 3 ประเภทหลัก:

- **Structured data** — ข้อมูลที่มีการจัดระเบียบสูง เป็นไปตาม schema ที่กำหนดไว้ล่วงหน้า มักอยู่ในรูปแบบแถว/คอลัมน์ เช่น Excel spreadsheet, SQL database, ฟอร์มออนไลน์ที่มีช่องกรอกกำหนดไว้ชัดเจน (ชื่อ, ที่อยู่, หมายเลขบัตรเครดิต)
- **Unstructured data** — ข้อมูลที่ไม่มีรูปแบบหรือโครงสร้างชัดเจน ไม่เป็นไปตามกฎที่กำหนดไว้ล่วงหน้า ประมวลผลด้วยวิธีดั้งเดิมได้ยาก เช่น text file, media file (รูปภาพ/เสียง/วิดีโอ), เว็บเพจ, เนื้อหาบน social media
- **Semi-structured data** — มีคุณสมบัติการจัดระเบียบบางส่วน (โครงสร้างแบบลำดับชั้นหรือ tag) แต่ไม่ใช่ตารางที่เคร่งครัด สร้างสมดุลระหว่างความยืดหยุ่นและโครงสร้าง เช่น JSON file (array/object ที่มี key), XML document (tag, attribute, schema), email (มีช่องที่มีโครงสร้าง เช่น to/from/subject แต่เนื้อหาข้อความเป็น unstructured)

---

### Common File Formats for Data Transfer

ธุรกิจดึงข้อมูลมาจากหลายแหล่ง — ฐานข้อมูลแบบดั้งเดิม, flat file, ชุดข้อมูล XML, web scraping, data stream/feed, social media, IoT sensor — และต้องการรูปแบบมาตรฐานสำหรับจัดเก็บหรือถ่ายโอนข้อมูลระหว่างระบบ:

- **Delimited text files** — ข้อมูลเรียงเป็นแถว โดยแต่ละตัวแปรคั่นด้วยอักขระเฉพาะ (comma หรือ tab) ได้แก่ CSV (comma-separated values) และ TSV (tab-separated values)
- **Spreadsheets** — ข้อมูลจัดเรียงเป็นแถวและคอลัมน์คล้ายตาราง ทำให้เข้าถึงและจัดการข้อมูลได้ง่าย และสามารถใช้สร้างไฟล์ CSV ได้
- **Language files** — รูปแบบอย่าง XML และ JSON ที่มีกฎและโครงสร้างชัดเจนสำหรับ encode ข้อมูลเพื่อส่งผ่านอินเทอร์เน็ต

---

### Data Repositories: Relational vs Non-Relational Databases

Data repository ทำหน้าที่จัดเก็บ จัดการ และจัดระเบียบข้อมูลแบบรวมศูนย์ ให้กรอบโครงสร้างสำหรับการเรียกใช้และบริหารจัดการข้อมูลอย่างมีประสิทธิภาพ แบ่งเป็น 2 ประเภทหลัก:

- **Relational databases** — จัดเก็บ structured data ในตารางที่เชื่อมโยงกัน การเชื่อมโยงระหว่างตารางช่วยลดความซ้ำซ้อนของข้อมูล เรียกรวมกันว่า Relational Database Management System (RDBMS) ตัวอย่างที่รู้จักกันดี ได้แก่ IBM DB2, Microsoft SQL Server, Oracle, MySQL
- **Non-relational databases** — ให้ความยืดหยุ่นในการจัดการข้อมูลที่หลากหลายและเป็น unstructured/semi-structured เช่น MongoDB (document-oriented), Cassandra, Redis

---

### OLTP vs OLAP

- **OLTP (Online Transaction Processing)** — relational database ส่วนใหญ่เป็นระบบ OLTP รองรับกิจกรรมทางธุรกิจประจำวัน เช่น การทำธุรกรรมของลูกค้า, งาน HR และ workflow ต่าง ๆ โครงสร้างที่ผ่านการ normalize ช่วยรักษาความถูกต้องของ transaction และรองรับการเข้าถึงพร้อมกันสำหรับงานประจำวัน
- **OLAP (Online Analytical Processing)** — ครอบคลุมรูปแบบการจัดเก็บข้อมูลหลากหลาย (relational/non-relational database, data warehouse, data lake, big data store) เน้นการ query และวิเคราะห์ข้อมูลปริมาณมากเพื่อดึง insight เช่น การนำข้อมูลจาก CRM มาใช้วิเคราะห์เพื่อคาดการณ์ยอดขาย

---

## Database Objects

### ความหมายของ Object ในฐานข้อมูล

ใน Database Management System (DBMS) คำว่า **Object (ออบเจกต์ในฐานข้อมูล)** หมายถึง **องค์ประกอบเชิงโครงสร้างต่าง ๆ ที่ถูกสร้าง จัดเก็บ และใช้งานภายในฐานข้อมูล** เพื่อจัดเก็บ จัดการ ค้นหา หรือควบคุมความปลอดภัยของข้อมูล

ถ้าเปรียบฐานข้อมูลเป็น "เมืองใหญ่" หรือ "อาคารสำนักงาน" database object ก็เปรียบเสมือนสิ่งปลูกสร้างและระบบภายในนั้น เช่น ห้องเก็บของ, ตู้เอกสาร, ถนน หรือกุญแจล็อคห้อง — แต่ละอย่างมีหน้าที่เฉพาะตัว แต่ทำงานร่วมกันเพื่อให้ทั้งระบบใช้งานได้จริง

---

### ตัวอย่าง Database Object ที่พบบ่อย

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

### ทำไม Database Object ถึงสำคัญ

- ช่วยแยกหน้าที่ของแต่ละองค์ประกอบในฐานข้อมูลให้ชัดเจน (จัดเก็บข้อมูล, ควบคุมความปลอดภัย, เพิ่มประสิทธิภาพการค้นหา, บังคับใช้กฎของข้อมูล)
- เป็นหน่วยที่ DBA และ data engineer ใช้อ้างอิงเมื่อกำหนดสิทธิ์การเข้าถึง (access control) เช่น อนุญาตให้ user เข้าถึงเฉพาะ view แทนที่จะเข้าถึงตารางต้นฉบับโดยตรง
- การเข้าใจว่า object แต่ละประเภททำหน้าที่อะไร เป็นพื้นฐานสำคัญก่อนจะออกแบบและ implement โครงสร้างฐานข้อมูลจริงในหัวข้อถัดไป

---

## Information Models and Data Models

### Information Models vs Data Models

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

### The Hierarchical Model

Hierarchical model เป็นการ implement ทางกายภาพของระบบข้อมูล โดยเก็บความสัมพันธ์ในรูปแบบ tree — ต่างจาก information model ที่เป็นเพียงแนวคิดความสัมพันธ์โดยไม่ระบุการจัดเก็บ

| Aspect | Information Model | Hierarchical Model |
| --- | --- | --- |
| ความเป็นนามธรรม | สูง — เป็นแนวคิดโดยไม่ระบุการจัดเก็บ | ต่ำกว่า — จัดโครงสร้างข้อมูลแบบ tree ทางกายภาพ |
| การจัดการความสัมพันธ์ | แสดงความสัมพันธ์ของ entity ได้ชัดเจนสำหรับสถานการณ์จริง | มีปัญหากับความสัมพันธ์แบบ many-to-many |
| ผลลัพธ์ | ไม่มี (เป็นแนวคิดล้วน ๆ) | ข้อจำกัดเชิงโครงสร้างอาจนำไปสู่ความซ้ำซ้อนของข้อมูล |
| บทบาททางประวัติศาสตร์ | ไม่มี | มีรากฐานจากระบบฐานข้อมูลยุคแรก เชื่อมโยงกับช่วงเริ่มต้นของ information model |

---

### Types of Data Models: Relational and Entity-Relationship (ER)

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

### Data Independence Concepts

มีแนวคิด 3 อย่างที่ช่วยให้ระบบฐานข้อมูลปรับตัวและมีประสิทธิภาพ โดยแต่ละอย่างจะแยกชั้นหนึ่งของระบบออกจากการเปลี่ยนแปลงในอีกชั้นหนึ่ง:

| Independence Type | สิ่งที่เปลี่ยนแปลงได้ | สิ่งที่ไม่ได้รับผลกระทบ |
| --- | --- | --- |
| Logical data independence | โครงสร้างฐานข้อมูล (เช่น เปลี่ยน data type, เพิ่ม field) | การเข้าถึงข้อมูลของผู้ใช้ |
| Physical data independence | การจัดระเบียบภายในฐานข้อมูล (เช่น ประเภทการจัดเก็บ, กลยุทธ์ indexing) | View หรือแอปพลิเคชันของผู้ใช้ |
| Physical storage independence | ตำแหน่ง/การจัดระเบียบข้อมูลบนอุปกรณ์จัดเก็บทางกายภาพ | โปรแกรมแอปพลิเคชันที่ประมวลผลข้อมูล |

---

## ERDs and Types of Relationships

### What is an ERD?

ERD (Entity Relationship Diagram) คือการนำเสนอเชิงภาพที่แสดงความสัมพันธ์และปฏิสัมพันธ์ระหว่าง entity ในฐานข้อมูล แสดงโครงสร้างเชิงตรรกะของระบบฐานข้อมูล โดยแสดง entity และความสัมพันธ์ระหว่างกันเป็นเส้นเชื่อมระหว่างกล่อง

---

### Fundamental Components of an ERD

ERD ประกอบด้วยองค์ประกอบพื้นฐาน 3 อย่าง:

- **Entities** — แทนบุคคล, วัตถุ หรือแนวคิดที่จัดเก็บข้อมูลในฐานข้อมูล เป็นส่วนประกอบพื้นฐาน แสดงเป็นสี่เหลี่ยม และมี attribute (คุณสมบัติ) ที่อธิบายคุณลักษณะเฉพาะ (เช่น entity `Book` มี attribute อย่าง title, edition, year, price; entity `Author` มี attribute อย่าง last name, first name, email, city, country, author ID) แต่ละ attribute เชื่อมกับ entity เพียงตัวเดียวเท่านั้น entity เป็นพื้นฐานสำหรับความสัมพันธ์ในโมเดลฐานข้อมูล
- **Relationship sets** — แสดงว่า entity เชื่อมโยงหรือสัมพันธ์กันอย่างไร แสดงว่า instance ของ entity หนึ่งสัมพันธ์กับ instance ของอีก entity อย่างไร แทนด้วยรูปสี่เหลี่ยมข้าวหลามตัด (diamond) พร้อมเส้นเชื่อมไปยัง entity ที่เกี่ยวข้อง diagram ที่แสดงประเภทความสัมพันธ์มักมีแค่ entity เท่านั้น (ไม่มี attribute) เพื่อไม่ให้ดูรก
- **Crow's foot notation** — สัญลักษณ์เชิงภาพที่บ่งบอกลักษณะและปริมาณของความสัมพันธ์ระหว่าง entity: สี่เหลี่ยมสำหรับ entity set, สี่เหลี่ยมข้าวหลามตัดสำหรับ relationship set และสัญลักษณ์อย่าง `>`, `<` และเส้นแนวตั้ง เพื่อบ่งบอกว่าความสัมพันธ์เป็นแบบ one-to-one, one-to-many หรือ many-to-many

---

### Types of Relationships

ใช้ตัวอย่าง Book/Author: หนังสือหนึ่งเล่มต้องมีผู้แต่งอย่างน้อยหนึ่งคน (และอาจมีมากกว่านั้น) และผู้แต่งหนึ่งคนสามารถเขียนหนังสือได้หนึ่งเล่มหรือมากกว่า ลักษณะของความเชื่อมโยงนี้เป็นตัวกำหนดประเภทความสัมพันธ์

| Relationship Type | นิยาม | สัญลักษณ์ Crow's Foot | ตัวอย่าง Book/Author |
| --- | --- | --- | --- |
| One-to-one | Entity แต่ละตัวใน set มีความสัมพันธ์เพียงหนึ่งเดียว | เส้นหนา/เรียบ ไม่มี crow's foot | หนังสือแต่ละเล่มเขียนโดยผู้แต่งคนเดียว ("Authored by") |
| One-to-many (หรือ many-to-one) | Entity หนึ่งตัวมีส่วนร่วมในความสัมพันธ์หลายรายการภายใน set | สัญลักษณ์ less-than (`<`) ด้านหนึ่ง | หนังสือหนึ่งเล่มมีผู้แต่งหลายคน; มองอีกมุมคือผู้แต่งหลายคนร่วมเขียนหนังสือเล่มเดียว |
| Many-to-many | Instance หลายตัวของ entity หนึ่งสัมพันธ์กับ instance หลายตัวของอีก entity | สัญลักษณ์ greater-than และ less-than (`>` ... `<`) ทั้งสองด้าน | ผู้แต่งหลายคนเขียนหนังสือหลายเล่ม |

แผนภาพอย่างง่ายของแต่ละประเภท (Book–Author):

```
One-to-One:      [ Book ] ──────── [ Author ]
                  (หนังสือแต่ละเล่มมีผู้แต่งเพียงคนเดียว)

One-to-Many:      [ Book ] ───────≺ [ Author ]
                  (หนังสือหนึ่งเล่ม มีผู้แต่งหลายคน)

Many-to-Many:     [ Book ] ≻─────≺ [ Author ]
                  (หนังสือหลายเล่ม ผู้แต่งหลายคน)
```

---

## Mapping Entities to Tables

### From ERD to Relational Database

ERD คือการนำเสนอเชิงภาพของ entity และความสัมพันธ์ระหว่างกันในฐานข้อมูล เป็นเทคนิคการสร้างโมเดลที่ใช้แสดงโครงสร้างของระบบฐานข้อมูลเชิงภาพ องค์ประกอบหลักได้แก่:

- **Entities** — วัตถุ แนวคิด หรือสิ่งของในโลกจริงที่จัดเก็บและจัดการข้อมูล แสดงเป็นสี่เหลี่ยม (เช่น `Book`)
- **Attributes** — คุณลักษณะที่เกี่ยวข้องกับ entity แสดงเป็นวงรีภายในสี่เหลี่ยมของ entity (เช่น ISBN, title, author, published year สำหรับ `Book`)
- **Relationships** — แสดงว่า entity สัมพันธ์กันอย่างไร แสดงเป็นเส้นเชื่อมระหว่างสี่เหลี่ยมของ entity (เช่น `Author` "writes" `Book`)

Relational database ให้กรอบโครงสร้างที่ชัดเจนสำหรับจัดการและปรับแต่ง structured data โดยจัดข้อมูลเป็นตาราง ซึ่งความสัมพันธ์ระหว่างตารางขึ้นอยู่กับ field ที่ใช้ร่วมกัน

---

### Steps for Mapping Entities to Tables

การออกแบบ relational database เริ่มจาก ERD แล้วจึงแปลงเป็นตาราง:

1. **Entity → Table** — entity กลายเป็นตารางที่มีชื่อเดียวกัน (เช่น entity `Book` กลายเป็นตาราง `Book`) ขั้นตอนนี้ให้เพียงโครงสร้างของแถว/คอลัมน์ ตารางยังว่างเปล่าอยู่
2. **Attributes → Columns** — attribute ของ entity กลายเป็นคอลัมน์ในตาราง (เช่น ISBN, title และ author กลายเป็นคอลัมน์ในตาราง `Book`)
3. **Add data values** — นำข้อมูลจริงมาใส่ในคอลัมน์ของตาราง เป็นการเปลี่ยนจาก entity เชิงแนวคิดให้กลายเป็นตารางที่จับต้องได้พร้อมข้อมูลจริง

ทำซ้ำ 3 ขั้นตอนนี้กับทุก entity ใน ERD (เช่น เปลี่ยน entity `Author` ให้กลายเป็นตาราง `Author`)

---

### Best Practices for Relational Database Design

- **Primary key designation** — กำหนด primary key (เช่น `Book ID`) เพื่อระบุแต่ละ entry ในตารางอย่างไม่ซ้ำกัน
- **Data validation** — ตรวจสอบ data type, ช่วงค่า และรูปแบบ เพื่อความถูกต้องและความสอดคล้องของข้อมูล (เช่น กำหนดให้คอลัมน์ `published year` รับเฉพาะค่าตัวเลขในช่วงที่กำหนด)
- **Default values** — กำหนดค่าเริ่มต้นให้บางคอลัมน์เพื่อให้การกรอกข้อมูลสะดวกขึ้น (เช่น ตั้งค่า default ของคอลัมน์ `author` เป็น "Unknown" เมื่อไม่มีข้อมูลผู้แต่ง)
- **Use of views** — ใช้ view เพื่อนำเสนอมุมมองข้อมูลที่ปรับแต่งและเรียบง่ายขึ้น โดยเฉพาะสำหรับ query ที่ซับซ้อนหรือรายงาน (เช่น view ที่รวมตาราง `Book` และ `Author` เป็นรายการเดียวโดยไม่ต้องเปิดเผยความซับซ้อนเบื้องหลัง)
- **Concurrency control** — ใช้กลไกจัดการผู้ใช้หลายคนที่เข้าถึงและแก้ไขฐานข้อมูลพร้อมกัน เพื่อป้องกันความไม่สอดคล้องและความขัดแย้งของข้อมูล (เช่น คอลัมน์ "Last modified" ในตาราง `Book`)

---

## Data Types

### What Is a Data Type

ตารางฐานข้อมูลแทน entity หนึ่งตัว โดยแต่ละคอลัมน์แทน attribute ของ entity นั้น (เช่น ตาราง `Book` ที่มีคอลัมน์ `title`, `publish date`, `pages`) ค่าทุกค่าในคอลัมน์เดียวกันควรเป็นข้อมูลชนิดเดียวกัน — data type ที่กำหนดให้คอลัมน์เป็นตัวควบคุมว่าคอลัมน์นั้นเก็บอะไรได้บ้าง คอลัมน์ text เก็บข้อมูล alphanumeric, คอลัมน์ date รับเฉพาะวันที่ที่ถูกต้อง และคอลัมน์ numeric รับเฉพาะตัวเลข

---

### Varchar

Varchar เป็น data type สำหรับเก็บ character string ที่มีความยาวไม่แน่นอน จนถึงค่าสูงสุดที่กำหนด เช่น `VARCHAR(100)` จองพื้นที่ไว้สูงสุด 100 ตัวอักษร แต่ string ที่มี 50 ตัวอักษรจะใช้พื้นที่เท่าที่จำเป็นสำหรับ 50 ตัวอักษรนั้นเท่านั้น — ไม่ใช่เต็ม 100

ข้อพิจารณาสำคัญ:

- **Efficiency** — Varchar จองพื้นที่เท่าที่ใช้จริงเท่านั้น จึงประหยัดพื้นที่กว่า fixed-length type อย่าง Char
- **Flexibility** — เหมาะกับ string ที่มีความยาวแตกต่างกันมาก เช่น ชื่อ, ที่อยู่ หรือคำอธิบาย

---

### Common Data Types

ระบบฐานข้อมูลแต่ละแบบจัดการ data type พื้นฐานเหล่านี้แตกต่างกันเล็กน้อย:

| Category | Type(s) | คำอธิบาย | ตัวอย่าง |
| --- | --- | --- | --- |
| Date / Time | DATE, TIME, DATETIME, TIMESTAMP | DATE เก็บปี เดือน วัน; TIME เก็บเวลาในหนึ่งวัน; DATETIME/TIMESTAMP รวมทั้งวันที่และเวลา | ใน MySQL, DATE ใช้รูปแบบปี-เดือน-วัน ขณะที่ TIMESTAMP รวมทั้งวันที่และเวลา |
| Float | FLOAT | ตัวเลขทศนิยมแบบประมาณค่า ใช้เมื่อไม่ต้องการความแม่นยำสูง | `FLOAT(24)` ใน SQL Server |
| Decimal | DECIMAL | ตัวเลขแบบแม่นยำ เหมาะกับการคำนวณที่ต้องแม่นยำ เช่นงานการเงิน | `DECIMAL(5,2)` เก็บทั้งหมด 5 หลัก มีทศนิยม 2 ตำแหน่ง |
| Integer | INT, SMALLINT | ตัวเลขจำนวนเต็ม แต่ละชนิดมีช่วงค่าที่รองรับต่างกัน | INT มีช่วงประมาณ -2,147,483,648 ถึง 2,147,483,647 |
| Binary | BLOB | Binary Large Object; เก็บข้อมูลเป็นลำดับ byte เหมาะกับข้อมูลที่ไม่ใช่ข้อความ | รูปภาพ, ไฟล์ |
| Char | CHAR | ตัวอักษรความยาวคงที่ ใช้จำนวนตัวอักษรตามที่กำหนดเสมอ โดยเติม space หากค่าสั้นกว่า | `CHAR(10)` เก็บ 10 ตัวอักษรเสมอ |

---

### Advantages of Using Appropriate Data Types

- ป้องกันไม่ให้ข้อมูลที่ไม่ถูกต้องถูกใส่เข้าไปในคอลัมน์ เนื่องจาก data type จำกัดว่าอะไรคือ input ที่ถูกต้อง
- ทำให้ข้อมูลวันที่ เวลา และตัวเลขถูกเรียงลำดับได้อย่างแม่นยำ
- ทำให้เลือกช่วงข้อมูลได้อย่างแม่นยำ (เช่น กรองวันที่หรือตัวเลขในช่วงที่กำหนด)
- รองรับการคำนวณเชิงตัวเลขบนข้อมูลที่มี type ถูกต้อง เช่น การคำนวณยอดรวมของคำสั่งซื้อ

---

## Relational Model Concepts

### Sets and Set Operations

Set คือกลุ่มของ element ที่ไม่ซ้ำกันและไม่มีลำดับ ประกอบด้วยรายการที่เป็นชนิดเดียวกัน มักเขียนแทนด้วยวงเล็บปีกกา (ระบุ element ไว้ข้างใน) หรือ set-builder notation (เงื่อนไขที่อธิบายการเป็นสมาชิก) Set เป็นรากฐานของคณิตศาสตร์สมัยใหม่หลายแขนง รวมถึง algebra, geometry และ probability

แนวคิดและ operation พื้นฐานของ set:

| Concept | Notation | ความหมาย |
| --- | --- | --- |
| Membership | `a ∈ A` | `a` เป็นสมาชิกของ set `A` |
| Subset | `A ⊆ B` | ทุก element ของ `A` เป็น element ของ `B` ด้วย |
| Union | `A ∪ B` | Element ที่อยู่ใน `A`, ใน `B`, หรือทั้งคู่ |
| Intersection | `A ∩ B` | Element ที่อยู่ทั้งใน `A` และ `B` |
| Difference | `A − B` (หรือ `A / B`) | Element ที่อยู่ใน `A` แต่ไม่อยู่ใน `B` |
| Empty set | `{}` หรือ `∅` | Set ที่ไม่มี element ใด ๆ เป็น subset ของทุก set |
| Power set | `P(A)` | Set ของ subset ที่เป็นไปได้ทั้งหมดของ `A` รวมถึง `∅` และ `A` เอง |
| Universal set | `U` | Set ที่รวมทุก object ที่พิจารณา; set อื่นทั้งหมดเป็น subset ของมัน |
| Disjoint sets | — | สอง set ที่ไม่มี element ร่วมกันเลย |

Venn diagram เป็นการนำเสนอเชิงภาพที่ใช้แสดงความสัมพันธ์เชิงตรรกะระหว่าง set

---

### Relations and Their Properties

Relation คือแนวคิดทางคณิตศาสตร์ที่สร้างบนแนวคิดของ set — อธิบายความเชื่อมโยงระหว่าง element ของ set และเป็นแนวคิดสำคัญของ set theory และ logic ประเภทที่พบบ่อยได้แก่:

- **Binary relation** — ความเชื่อมโยงระหว่าง element สองตัว (เช่น relation "less than" อย่าง 3 < 5)
- **Ordered pairs** — subset ของ Cartesian product `A × B` แทน binary relation บน set `A` และ `B` เขียนแทนด้วย `(a, b)`

Relation อาจมีคุณสมบัติดังนี้:

| Property | นิยาม | ตัวอย่าง |
| --- | --- | --- |
| Reflexivity | Element แต่ละตัวสัมพันธ์กับตัวมันเอง | Equality — `A = A` สำหรับทุก element `A` |
| Symmetry | ถ้า `A` สัมพันธ์กับ `B` แล้ว `B` ก็สัมพันธ์กับ `A` ด้วย | "Is a sibling of" |
| Transitivity | ถ้า `A` สัมพันธ์กับ `B` และ `B` สัมพันธ์กับ `C` แล้ว `A` สัมพันธ์กับ `C` | "Less than" — ถ้า `A < B` และ `B < C` แล้ว `A < C` |
| Anti-symmetry | ถ้า `A` สัมพันธ์กับ `B` และ `B` สัมพันธ์กับ `A` แล้ว `A` ต้องเท่ากับ `B` | "Less than or equal to" |

---

### Relation Schema vs. Relation Instance

Relation ประกอบด้วยองค์ประกอบสำคัญ 2 อย่าง:

- **Relation schema** — ระบุโครงสร้าง: ชื่อของ relation และชื่อ/data type ของแต่ละคอลัมน์ (attribute) เช่น สำหรับ relation `Author`: `Author_ID` (CHAR — string ความยาวคงที่), `last_name`, `first_name`, `email` (VARCHAR — string ความยาวไม่คงที่) และ `country` (CHAR)
- **Relation instance** — ข้อมูลจริงในโลกจริงที่จัดเก็บในตาราง ประกอบด้วยแถวและคอลัมน์ คอลัมน์สอดคล้องกับ attribute ที่กำหนดใน schema และแถวแทน tuple (record แต่ละรายการ)

---

### Degree and Cardinality

- **Degree** — จำนวน attribute (คอลัมน์) ใน relation
- **Cardinality** — จำนวน tuple (แถว) ใน relation

ในตัวอย่าง `Author` ของบทเรียน: degree เท่ากับ 6 (หกคอลัมน์: `Author_ID`, `last_name`, `first_name`, `email`, `city`, `country`) และ cardinality เท่ากับ 5 (ห้าแถวของข้อมูล)

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Structured data | ข้อมูลที่มีการจัดระเบียบสูง เป็นไปตาม schema ที่กำหนดไว้ล่วงหน้า มักอยู่ในรูปแบบแถวและคอลัมน์ |
| Unstructured data | ข้อมูลที่ไม่มีรูปแบบหรือการจัดระเบียบเฉพาะเจาะจง |
| Semi-structured data | ข้อมูลที่มีคุณสมบัติการจัดระเบียบบางส่วน (tag/hierarchy) แต่ไม่ใช่โครงสร้างตารางที่เคร่งครัด |
| CSV | Comma-separated values — รูปแบบ delimited text file |
| TSV | Tab-separated values — รูปแบบ delimited text file |
| XML | Extensible Markup Language — encode ข้อมูลด้วย tag, attribute และ schema |
| JSON | JavaScript Object Notation — encode ข้อมูลด้วย array และ object ที่มี key |
| Data repository | ระบบรวมศูนย์ที่จัดเก็บ จัดการ และจัดระเบียบข้อมูล |
| RDBMS | Relational Database Management System — ซอฟต์แวร์จัดการฐานข้อมูลเชิงสัมพันธ์ |
| OLTP | Online Transaction Processing — ระบบรองรับ transaction เชิงปฏิบัติการประจำวัน |
| OLAP | Online Analytical Processing — ระบบสำหรับ query/วิเคราะห์ข้อมูลปริมาณมากเพื่อหา insight |
| MongoDB | ฐานข้อมูล non-relational แบบ document-oriented เหมาะกับข้อมูล semi-structured/unstructured |
| Database Object | องค์ประกอบเชิงโครงสร้างที่ถูกสร้าง จัดเก็บ และใช้งานภายในฐานข้อมูล เช่น table, view, index, stored procedure |
| Index | โครงสร้างที่ช่วยให้ค้นหาแถวข้อมูลในตารางได้เร็วขึ้น โดยไม่ต้องไล่อ่านทั้งตาราง |
| Stored Procedure | ชุดคำสั่ง SQL ที่เขียนไว้ล่วงหน้าและเรียกใช้งานซ้ำได้ |
| Trigger | ชุดคำสั่งที่ทำงานอัตโนมัติเมื่อมีเหตุการณ์เกิดขึ้นกับตาราง เช่น insert, update, delete |
| Schema (object) | พื้นที่เชิงตรรกะที่ใช้จัดกลุ่ม database object ต่าง ๆ ไว้ด้วยกัน |
| Sequence | Object ที่สร้างค่าตัวเลขเพิ่มขึ้นเรื่อย ๆ โดยอัตโนมัติ มักใช้เป็นค่า primary key |
| Information model | การนำเสนอเชิงแนวคิดแบบนามธรรมของ entity, property, relationship และ function |
| Data model | Blueprint ทางเทคนิคที่แปลง information model ให้เป็นโครงสร้างฐานข้อมูล |
| Hierarchical model | Data model ยุคแรกที่จัดโครงสร้างข้อมูลแบบ tree ทางกายภาพ |
| Relational model | Data model ที่ใช้กันแพร่หลายที่สุด จัดเก็บข้อมูลในตาราง พร้อม logical/physical/storage independence |
| Entity-Relationship (ER) model | Model เชิงแนวคิดที่แสดงฐานข้อมูลเป็น entity และความสัมพันธ์ระหว่างกัน |
| Entity | วัตถุ แนวคิด หรือสิ่งของในโลกจริงที่จัดเก็บและจัดการข้อมูล แสดงเป็นสี่เหลี่ยมใน ERD |
| Attribute | คุณลักษณะ (property) ของ entity แสดงเป็นวงรี เชื่อมกับ entity เพียงตัวเดียว |
| ERD | Entity Relationship Diagram — การนำเสนอเชิงภาพ/graphical ของ entity และความสัมพันธ์ในฐานข้อมูล |
| Normalization | กระบวนการจัดระเบียบข้อมูลเพื่อลดความซ้ำซ้อนและรักษาความถูกต้องของข้อมูล |
| Foreign key | Field ที่เชื่อมโยงตารางหนึ่งไปยัง primary key ของอีกตาราง แทนความสัมพันธ์ |
| Logical data independence | ความสามารถในการเปลี่ยนโครงสร้างฐานข้อมูลโดยไม่กระทบการเข้าถึงข้อมูลของผู้ใช้ |
| Physical data independence | ความสามารถในการเปลี่ยนการจัดเก็บ/indexing ภายในโดยไม่กระทบ view หรือแอปพลิเคชันของผู้ใช้ |
| Physical storage independence | ความสามารถในการย้าย/จัดระเบียบข้อมูลบนอุปกรณ์จัดเก็บโดยไม่กระทบแอปพลิเคชัน |
| Relationship set | องค์ประกอบรูปสี่เหลี่ยมข้าวหลามตัดที่แสดงว่า entity สองตัวเชื่อมโยงกันอย่างไร |
| Crow's foot notation | Notation ที่ใช้สัญลักษณ์ (>, <, เส้นแนวตั้ง) เพื่อบ่งบอกชนิดและปริมาณของความสัมพันธ์ |
| One-to-one relationship | Instance ของ entity หนึ่งเชื่อมกับ instance เพียงหนึ่งเดียวของอีก entity |
| One-to-many relationship | Instance ของ entity หนึ่งเชื่อมกับ instance หลายตัวของอีก entity |
| Many-to-many relationship | Instance หลายตัวของ entity หนึ่งเชื่อมกับ instance หลายตัวของอีก entity |
| Cardinality (ในความหมาย ERD) | ลักษณะเชิงตัวเลขของความสัมพันธ์ (one vs many) ระหว่าง entity ที่เชื่อมกัน |
| Relational database | โมเดลฐานข้อมูลที่จัดข้อมูลเป็นตาราง โดยความสัมพันธ์ระหว่างตารางขึ้นอยู่กับ field ที่ใช้ร่วมกัน |
| Relationship | ความเชื่อมโยงที่แสดงว่า entity สัมพันธ์กันอย่างไร แสดงเป็นเส้นระหว่างสี่เหลี่ยมของ entity |
| Primary key | ตัวระบุเฉพาะที่กำหนดให้แต่ละ entry ในตาราง เพื่อระบุอย่างไม่ซ้ำกัน |
| Data validation | กลไกตรวจสอบ data type, ช่วงค่า และรูปแบบ เพื่อความถูกต้องและความสอดคล้องของข้อมูลที่ป้อนเข้ามา |
| Default value | ค่าที่กำหนดไว้ล่วงหน้าให้กับคอลัมน์ เพื่อให้การกรอกข้อมูลสะดวกขึ้นเมื่อไม่มีการระบุค่า |
| View | database object ที่เป็นมุมมองเสมือนสร้างจาก query บนตารางหนึ่งตัวหรือมากกว่า ไม่เก็บข้อมูลซ้ำจากตารางต้นฉบับ มักใช้เพื่อลดความซับซ้อนของ query หรือรายงาน |
| Concurrency control | กลไกจัดการผู้ใช้หลายคนที่เข้าถึงและแก้ไขฐานข้อมูลพร้อมกัน เพื่อป้องกันความไม่สอดคล้องและความขัดแย้ง |
| Data type | คุณสมบัติที่กำหนดให้คอลัมน์ ระบุว่าคอลัมน์นั้นเก็บข้อมูลชนิดใดได้บ้าง และตรวจสอบข้อมูลที่ป้อนเข้ามา |
| Varchar | Variable character — data type ที่เก็บ character string ความยาวไม่แน่นอน จนถึงค่าสูงสุดที่กำหนด |
| Char | Data type ตัวอักษรความยาวคงที่ เติม space ให้ครบตามจำนวนที่กำหนดเสมอ |
| DATE | Data type ที่เก็บวันที่ตามปฏิทิน (ปี เดือน วัน) |
| TIME | Data type ที่เก็บเวลาในหนึ่งวัน |
| DATETIME / TIMESTAMP | Data type ที่เก็บค่าวันที่และเวลารวมกัน |
| Float | Data type ตัวเลขทศนิยมแบบประมาณค่า ใช้เมื่อไม่ต้องการความแม่นยำสูง |
| Decimal | Data type ตัวเลขแบบแม่นยำ ใช้สำหรับการคำนวณที่ต้องแม่นยำ เช่นงานการเงิน |
| Integer (INT, SMALLINT) | Data type ที่เก็บตัวเลขจำนวนเต็ม แต่ละชนิดมีช่วงค่าที่รองรับของตัวเอง |
| Binary / BLOB | Binary Large Object — data type ที่เก็บข้อมูลที่ไม่ใช่ข้อความ (เช่น รูปภาพ, ไฟล์) เป็นลำดับ byte |
| Set | กลุ่มของ element ที่ไม่ซ้ำกันและไม่มีลำดับ |
| Relation | แนวคิดทางคณิตศาสตร์ที่สร้างบนแนวคิดของ set อธิบายความเชื่อมโยงระหว่าง element |
| Binary relation | Relation ที่สร้างความเชื่อมโยงระหว่าง element สองตัว |
| Ordered pair | Subset ของ Cartesian product ของสอง set แทน binary relation |
| Reflexivity | คุณสมบัติของ relation ที่ element แต่ละตัวสัมพันธ์กับตัวมันเอง |
| Symmetry | คุณสมบัติของ relation ที่ A สัมพันธ์กับ B แล้วนัยว่า B สัมพันธ์กับ A |
| Transitivity | คุณสมบัติของ relation ที่ A สัมพันธ์กับ B และ B สัมพันธ์กับ C แล้วนัยว่า A สัมพันธ์กับ C |
| Anti-symmetry | คุณสมบัติของ relation ที่ A สัมพันธ์กับ B และ B สัมพันธ์กับ A แล้วนัยว่า A เท่ากับ B |
| Relation schema | โครงสร้างของ relation — ชื่อและชื่อ/type ของแต่ละ attribute |
| Relation instance | ข้อมูลจริง (แถวและคอลัมน์) ที่จัดเก็บสำหรับ relation |
| Tuple | แถวหนึ่งใน relation instance |
| Degree | จำนวน attribute (คอลัมน์) ใน relation |
| Cardinality (ในความหมาย relational model) | จำนวน tuple (แถว) ใน relation |
| CHAR | Data type ที่เก็บ character string ความยาวคงที่ |
| VARCHAR | Data type ที่เก็บ character string ความยาวไม่คงที่ |

---

## ❓ My Questions & Gaps

- [ ] อะไรคือความแตกต่างที่ชัดเจนระหว่าง data warehouse กับ data lake ในกลุ่มระบบ OLAP
- [ ] Normalization ใน RDBMS ช่วยลดความซ้ำซ้อนของข้อมูลได้อย่างเป็นรูปธรรมอย่างไร (อยากได้ตัวอย่างประกอบ)
- [ ] ในทางปฏิบัติ ใช้เกณฑ์อะไรตัดสินใจว่าเมื่อไรควรใช้ non-relational database (เช่น MongoDB) แทน relational database
- [ ] ขั้นตอนที่เป็นรูปธรรมในการแปลง ER diagram เป็นตาราง relational มีอะไรบ้าง (นอกเหนือจาก entity → table, attribute → column)
- [ ] ข้อจำกัดเชิงโครงสร้างแบบไหนที่ทำให้ hierarchical model มีปัญหากับความสัมพันธ์ many-to-many
- [ ] ในทางปฏิบัติ independence ทั้งสามแบบต่างกันอย่างไรเมื่อมีการเปลี่ยนแปลง schema จริง (เช่น เพิ่ม index เทียบกับเพิ่มคอลัมน์)
- [ ] Crow's foot notation แยกความแตกต่างระหว่าง optional participation (zero-or-many) กับ mandatory participation (one-or-many) ได้อย่างไร
- [ ] ความสัมพันธ์แบบ many-to-many ถูก implement จริงในระดับ schema อย่างไร (เช่นผ่าน junction/associative table) — บทเรียนนี้ยังไม่ครอบคลุม
- [ ] เหตุใด attribute มักถูกละไว้ใน diagram ที่แสดงประเภทความสัมพันธ์ และควรใส่กลับเมื่อไร
- [ ] ความสัมพันธ์ (เช่น one-to-many ระหว่าง `Author` กับ `Book`) ถูก implement ในระดับตารางอย่างไร — ผ่าน foreign key — เนื่องจากบทเรียนนี้ครอบคลุมแค่การ map entity และ attribute ยังไม่รวมความสัมพันธ์
- [ ] Primary key ต่างจาก unique identifier แบบอื่นอย่างไร และเมื่อไรที่ตารางต้องใช้ composite primary key
- [ ] View มีปฏิสัมพันธ์กับ concurrency control อย่างไร — สะท้อนข้อมูลที่เปลี่ยนแปลงแบบ live หรือเป็นแค่ snapshot ณ เวลาที่ query
- [ ] ความแตกต่างเชิงปฏิบัติระหว่าง DATETIME กับ TIMESTAMP ในแต่ละระบบฐานข้อมูลมีอะไรบ้าง (เช่น การจัดการ time zone, ขอบเขตค่า)
- [ ] การเลือก VARCHAR ที่มีความยาวสูงสุดมาก (เช่น VARCHAR(255) เทียบกับ VARCHAR(50)) มีผลด้าน performance หรือ indexing จริงหรือไม่ ทั้งที่พื้นที่จัดเก็บใช้เท่าที่จำเป็นเท่านั้น
- [ ] ในทางปฏิบัติ เมื่อไรที่ Float เป็นตัวเลือกที่ยอมรับได้มากกว่า Decimal นอกเหนือจากงานการเงิน มี performance tradeoff หรือไม่
- [ ] มีขีดจำกัดขนาดหรือ best practice ในการเก็บไฟล์ขนาดใหญ่ในคอลัมน์ BLOB เทียบกับการเก็บ path/reference ของไฟล์แทนหรือไม่
- [ ] คุณสมบัติของ relation (reflexivity, symmetry, transitivity, anti-symmetry) เชื่อมโยงกับการตัดสินใจออกแบบฐานข้อมูลจริงอย่างไร หรือเป็นเพียงรากฐานเชิงทฤษฎี
- [ ] แนวคิด "relation" ของ relational model ต่างจาก SQL "table" ในทางปฏิบัติอย่างไร มี edge case ที่ต่างกันหรือไม่ (เช่น แถวที่ซ้ำกัน)
- [ ] Cardinality ในความหมายของ relational model (จำนวนแถว) สับสนกับ cardinality ในความสัมพันธ์แบบ ER diagram (one-to-many ฯลฯ) หรือไม่ ควรแยกสองความหมายนี้อย่างไร

---

## 🔗 Resources

- https://www.geeksforgeeks.org/dbms/what-is-data-independence-in-dbms/
- https://www.geeksforgeeks.org/dbms/introduction-of-er-model/