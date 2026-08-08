# PostgreSQL

`Tags: RDBMS, PostgreSQL, replication, LAPP`

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
- [What Is PostgreSQL](#what-is-postgresql)
- [Replication](#replication)
- [Partitioning and Sharding](#partitioning-and-sharding)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้แนะนำ PostgreSQL ตั้งแต่ต้นกำเนิดจากโปรเจกต์ POSTGRES ไปจนถึงคุณสมบัติแบบ object-relational ที่รองรับทั้งฟีเจอร์มาตรฐานของ relational database และฟีเจอร์แบบ NoSQL รวมถึงรูปแบบ replication, partitioning และ sharding ที่ใช้รองรับ scalability

---

## What Is PostgreSQL

PostgreSQL มีต้นกำเนิดจากโปรเจกต์ POSTGRES ที่ University of California เมื่อกว่า 30 ปีก่อน ในปี 1994 มีการเปิดตัว Postgres95 แบบ open source พร้อม SQL interpreter ซึ่งภายหลังเปลี่ยนชื่อเป็น PostgreSQL (มักเรียกสั้น ๆ ว่า Postgres) ใช้เป็นส่วนหนึ่งของ **LAPP stack** (Linux, Apache, PostgreSQL, PHP) และรองรับ extension เพิ่มเติม เช่น PostGIS สำหรับข้อมูลภูมิสารสนเทศ

เป็น free open-source **object-relational** DBMS หมายถึงรองรับแนวคิดแบบ object-oriented เช่น inheritance และ overloading ทำงานได้บนระบบปฏิบัติการส่วนใหญ่ ดูแลรักษาง่าย รองรับหลายภาษาโปรแกรมมิ่งและมาตรฐาน ANSI-SQL

รองรับโครงสร้างมาตรฐานของ relational database (keys, transactions, views, functions, stored procedures) รวมถึงฟีเจอร์แบบ NoSQL เช่น JSON (ข้อมูลมีโครงสร้าง) และ HSTORE (ข้อมูลไม่มีลำดับชั้น)

---

## Replication

| แบบ | ลักษณะ |
| ---- | ------ |
| **Two-node synchronous replication** | เก็บสำเนาข้อมูลไว้ที่ node ที่สอง ทุกการเปลี่ยนแปลงที่ node 1 จะถูก apply ที่ node 2 ด้วย แชร์ read load ได้ และหาก node 1 ล่ม node 2 จะรับ traffic แทนได้ทันที |
| **Multi-node asynchronous replication** | master node กระจายการเปลี่ยนแปลงไปยัง read-only replica หลายตัวเพื่อ scalability หาก node หลักล่มก็แทนที่ด้วย replica ตัวใดตัวหนึ่งได้ |
| **Commercial extension** | เช่น EDB PostgreSQL Replication Server รองรับ multi-master read/write replication ให้หลาย database เขียน/replicate ข้อมูลระหว่างกันได้ |

---

## Partitioning and Sharding

รองรับ **partitioning** (แบ่งตารางใหญ่เป็นส่วนย่อยเพื่อเพิ่มประสิทธิภาพ query) และ **sharding** (กระจาย horizontal partition ไปยัง remote server หลายตัว) เพื่อรองรับ scalability และข้อมูลขนาดใหญ่

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Object-Relational DBMS | DBMS ที่รองรับแนวคิดแบบ object-oriented (inheritance, overloading) นอกเหนือจากโครงสร้าง relational มาตรฐาน |
| HSTORE | PostgreSQL extension สำหรับเก็บข้อมูลแบบ key-value ที่ไม่มีลำดับชั้น |
| Synchronous Replication | การ replicate ที่ทุกการเปลี่ยนแปลงต้องถูก apply ที่ replica ก่อนถือว่า transaction สำเร็จ |
| Asynchronous Replication | การ replicate ที่ไม่รอให้ replica apply การเปลี่ยนแปลงก่อนถือว่า transaction สำเร็จ |

---

## ❓ My Questions & Gaps

- [x] LAMP stack vs. LAPP stack
  - The primary difference between LAMP and LAPP stacks is the database system they use: LAMP uses MySQL, while LAPP uses PostgreSQL.
  - Both share Linux for the operating system, Apache for the web server, and PHP (along with Python or Perl) for scripting.
  - Database Comparison
    - MySQL (LAMP):
      - Faster and simpler setup for basic, standard web projects.
      - Highly popular with content management systems like WordPress
      - Great for standard relational data storage.
    - PostgreSQL (LAPP):
      - Advanced features for complex data queries, data integrity, and heavy workloads.
      - Better support for enterprise-level applications, custom data types, and high concurrency.
  - Use Cases
    - Choose LAMP when: Building standard blogs, e-commerce sites, or simple dynamic applications that rely on traditional MySQL databases
    - Choose LAPP when: Developing large-scale enterprise software that requires advanced database functions, strict data rules, or complex analytical processing.

---

## 🔗 Resources

- ไม่มีลิงก์อ้างอิงภายนอกในวิดีโอนี้
