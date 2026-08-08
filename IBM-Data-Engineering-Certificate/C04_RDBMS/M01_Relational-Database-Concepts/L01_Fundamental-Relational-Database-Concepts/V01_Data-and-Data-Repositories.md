# Data and Data Repositories

`Tags: RDBMS, database, data-types, OLTP, OLAP`

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
- [Data and Data Structures](#data-and-data-structures)
- [Common File Formats for Data Transfer](#common-file-formats-for-data-transfer)
- [Data Repositories: Relational vs Non-Relational Databases](#data-repositories-relational-vs-non-relational-databases)
- [OLTP vs OLAP](#oltp-vs-olap)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้ปูพื้นฐานว่าข้อมูลมีกี่ประเภท (structured, unstructured, semi-structured) รูปแบบไฟล์ที่ใช้ถ่ายโอนข้อมูลระหว่างระบบ และความแตกต่างระหว่าง relational กับ non-relational database รวมถึงแนวคิด OLTP กับ OLAP ซึ่งเป็นพื้นฐานสำคัญก่อนจะเข้าใจว่า relational database ทำงานอย่างไรในระบบจริง

---

## Data and Data Structures

Data คือข้อมูลดิบที่ยังไม่ผ่านการจัดระเบียบ — ข้อเท็จจริง, การสังเกตการณ์, ตัวเลข, ตัวอักษร, สัญลักษณ์, รูปภาพ หรือรวมกันหลายแบบ — ซึ่งจะมีความหมายก็ต่อเมื่อผ่านการประมวลผลแล้ว วิธีจัดโครงสร้างของข้อมูลส่งผลต่อประสิทธิภาพในการจัดเก็บ จัดการ และวิเคราะห์

| ประเภทข้อมูล | ลักษณะ | ตัวอย่าง |
| ------------- | ------ | -------- |
| **Structured data** | มีการจัดระเบียบสูง เป็นไปตาม schema ที่กำหนดไว้ล่วงหน้า มักอยู่ในรูปแบบแถว/คอลัมน์ | Excel spreadsheet, SQL database, ฟอร์มออนไลน์ที่มีช่องกรอกกำหนดไว้ชัดเจน (ชื่อ, ที่อยู่, หมายเลขบัตรเครดิต) |
| **Unstructured data** | ไม่มีรูปแบบหรือโครงสร้างชัดเจน ไม่เป็นไปตามกฎที่กำหนดไว้ล่วงหน้า ประมวลผลด้วยวิธีดั้งเดิมได้ยาก | text file, media file (รูปภาพ/เสียง/วิดีโอ), เว็บเพจ, เนื้อหาบน social media |
| **Semi-structured data** | มีคุณสมบัติการจัดระเบียบบางส่วน (โครงสร้างแบบลำดับชั้นหรือ tag) แต่ไม่ใช่ตารางที่เคร่งครัด สร้างสมดุลระหว่างความยืดหยุ่นและโครงสร้าง | JSON file (array/object ที่มี key), XML document (tag, attribute, schema), email (มีช่องที่มีโครงสร้าง เช่น to/from/subject แต่เนื้อหาข้อความเป็น unstructured) |

---

## Common File Formats for Data Transfer

ธุรกิจดึงข้อมูลมาจากหลายแหล่ง — ฐานข้อมูลแบบดั้งเดิม, flat file, ชุดข้อมูล XML, web scraping, data stream/feed, social media, IoT sensor — และต้องการรูปแบบมาตรฐานสำหรับจัดเก็บหรือถ่ายโอนข้อมูลระหว่างระบบ:

- **Delimited text files** — ข้อมูลเรียงเป็นแถว โดยแต่ละตัวแปรคั่นด้วยอักขระเฉพาะ (comma หรือ tab) ได้แก่ CSV (comma-separated values) และ TSV (tab-separated values)
- **Spreadsheets** — ข้อมูลจัดเรียงเป็นแถวและคอลัมน์คล้ายตาราง ทำให้เข้าถึงและจัดการข้อมูลได้ง่าย และสามารถใช้สร้างไฟล์ CSV ได้
- **Language files** — รูปแบบอย่าง XML และ JSON ที่มีกฎและโครงสร้างชัดเจนสำหรับ encode ข้อมูลเพื่อส่งผ่านอินเทอร์เน็ต

---

## Data Repositories: Relational vs Non-Relational Databases

Data repository ทำหน้าที่จัดเก็บ จัดการ และจัดระเบียบข้อมูลแบบรวมศูนย์ ให้กรอบโครงสร้างสำหรับการเรียกใช้และบริหารจัดการข้อมูลอย่างมีประสิทธิภาพ แบ่งเป็น 2 ประเภทหลัก:

- **Relational databases** — จัดเก็บ structured data ในตารางที่เชื่อมโยงกัน การเชื่อมโยงระหว่างตารางช่วยลดความซ้ำซ้อนของข้อมูล เรียกรวมกันว่า Relational Database Management System (RDBMS) ตัวอย่างที่รู้จักกันดี ได้แก่ IBM DB2, Microsoft SQL Server, Oracle, MySQL
- **Non-relational databases** — ให้ความยืดหยุ่นในการจัดการข้อมูลที่หลากหลายและเป็น unstructured/semi-structured เช่น MongoDB (document-oriented), Cassandra, Redis

---

## OLTP vs OLAP

| ระบบ | ลักษณะ |
| ---- | ------ |
| **OLTP (Online Transaction Processing)** | relational database ส่วนใหญ่เป็นระบบ OLTP รองรับกิจกรรมทางธุรกิจประจำวัน เช่น การทำธุรกรรมของลูกค้า, งาน HR และ workflow ต่าง ๆ โครงสร้างที่ผ่านการ normalize ช่วยรักษาความถูกต้องของ transaction และรองรับการเข้าถึงพร้อมกันสำหรับงานประจำวัน |
| **OLAP (Online Analytical Processing)** | ครอบคลุมรูปแบบการจัดเก็บข้อมูลหลากหลาย (relational/non-relational database, data warehouse, data lake, big data store) เน้นการ query และวิเคราะห์ข้อมูลปริมาณมากเพื่อดึง insight เช่น การนำข้อมูลจาก CRM มาใช้วิเคราะห์เพื่อคาดการณ์ยอดขาย |

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

---

## ❓ My Questions & Gaps

- [ ] อะไรคือความแตกต่างที่ชัดเจนระหว่าง data warehouse กับ data lake ในกลุ่มระบบ OLAP
- [ ] ในทางปฏิบัติ ใช้เกณฑ์อะไรตัดสินใจว่าเมื่อไรควรใช้ non-relational database (เช่น MongoDB) แทน relational database

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
