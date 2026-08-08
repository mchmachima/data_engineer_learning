# Data Repositories

Tags: RDBMS, NoSQL, data warehouse

| Field            | Value                                                                 |
| ---------------- | --------------------------------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate                         |
| **Course**       | C01 Introduction to Data Engineering                                  |
| **Module**       | M02 The Data Engineering Ecosystem                                    |
| **Lesson**       | L02 Data Repositories, Data Pipelines, and Data Integration Platforms |
| **Date studied** | 2026-06-13                                                            |

---

## Table of Contents

- [Overview](#overview)
- [RDBMS](#rdbms)
- [NoSQL](#nosql)
- [Data Warehouses, Marts, and Lakes](#data-warehouses-marts-and-lakes)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้ครอบคลุมที่จัดเก็บข้อมูลหลักที่ Data Engineer ต้องเลือกใช้ ได้แก่ RDBMS, NoSQL และกลุ่ม data warehouse/mart/lake/lakehouse พร้อมเปรียบเทียบข้อดีข้อเสียของแต่ละแบบ

---

## RDBMS

- จัดข้อมูลเป็นตารางที่มีแถวและคอลัมน์ เชื่อมโยงตารางกันด้วย key ร่วม
- รองรับ ACID transaction: **A**tomicity, **C**onsistency, **I**solation, **D**urability
- เหมาะกับ: OLTP, data warehousing, โซลูชัน IoT
- ข้อจำกัด: จัดการข้อมูล unstructured ได้ไม่ดี, มีข้อจำกัดความยาว field ที่ตายตัว, ย้ายข้ามระบบ RDBMS ได้ยาก
- ที่นิยม: IBM DB2, SQL Server, MySQL, Oracle, PostgreSQL; บน Cloud: Amazon RDS, Google Cloud SQL, SQL Azure

---

## NoSQL

| Type      | Description                      | Best For                               | Examples         |
| --------- | -------------------------------- | -------------------------------------- | ---------------- |
| Key-value | key เดียวจับคู่กับหนึ่งค่า       | session data, caching, ระบบแนะนำสินค้า | Redis, DynamoDB  |
| Document  | เก็บทั้ง record ไว้ในเอกสารเดียว | eCommerce, CRM, analytics              | MongoDB, CouchDB |
| Column    | จัดกลุ่มข้อมูลตาม column family  | time-series, IoT, งานเขียนหนักๆ        | Cassandra, HBase |
| Graph     | โหนดและความสัมพันธ์              | social network, ตรวจจับการทุจริต       | Neo4J, CosmosDB  |

**ข้อดีของ NoSQL:** รองรับข้อมูลปริมาณมากได้ทุกประเภท; ขยายตัวแบบ horizontal บนฮาร์ดแวร์ทั่วไปได้; schema ยืดหยุ่น

**RDBMS เทียบกับ NoSQL:**

- RDBMS: schema ตายตัว, รองรับ ACID, เป็นเทคโนโลยีที่เก่าแก่และเสถียร, ค่าใช้จ่ายสูงเมื่อขยายตัว
- NoSQL: ไม่ยึดติด schema, ไม่ได้รองรับ ACID เสมอไป, ค่าใช้จ่ายต่ำกว่า, เหมาะกับ big data มากกว่า

---

## Data Warehouses, Marts, and Lakes

| Repository     | Description                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------- |
| Data Warehouse | ศูนย์กลางข้อมูลพร้อมวิเคราะห์ เป็น single source of truth; แบ่งเป็น 3 ชั้น: DB layer → OLAP → client |
| Data Mart      | ส่วนย่อยของ Data Warehouse สำหรับหน่วยธุรกิจเฉพาะ (เช่น ฝ่ายขาย, ฝ่ายการเงิน)                        |
| Data Lake      | ข้อมูลดิบในรูปแบบดั้งเดิม; schema-on-read; เสี่ยงกลายเป็น Data Swamp หากไม่จัดการดี                  |
| Data Lakehouse | รวมความยืดหยุ่นของ Data Lake เข้ากับ performance และ governance ของ Data Warehouse                   |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์)   | คำอธิบาย (ภาษาไทย)                                                                           |
| -------------- | -------------------------------------------------------------------------------------------- |
| ACID           | Atomicity, Consistency, Isolation, Durability — การรับประกันสำหรับ transaction ของฐานข้อมูล  |
| OLTP           | ระบบที่ optimize สำหรับงาน transaction อ่าน/เขียนความเร็วสูง                                 |
| OLAP           | ระบบที่ optimize สำหรับ query วิเคราะห์ที่ซับซ้อนบนข้อมูลปริมาณมาก                           |
| Data Swamp     | Data Lake ที่ใช้งานไม่ได้เพราะขาดการทำ governance                                            |
| Data Lakehouse | สถาปัตยกรรมที่รวมความยืดหยุ่นของ Data Lake เข้ากับโครงสร้างและ governance ของ Data Warehouse |

---

## ❓ My Questions & Gaps

- [ ] How does a Data Lakehouse (e.g., Databricks Delta Lake) enforce ACID compliance on a data lake?

---

## 🔗 Resources

- [MongoDB University](https://university.mongodb.com/)
