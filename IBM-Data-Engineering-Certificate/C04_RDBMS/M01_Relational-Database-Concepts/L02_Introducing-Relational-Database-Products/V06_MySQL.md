# MySQL

`Tags: RDBMS, MySQL, storage engine, LAMP`

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
- [What Is MySQL](#what-is-mysql)
- [Storage Engines](#storage-engines)
- [Clustering Options](#clustering-options)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้แนะนำ MySQL ตั้งแต่ประวัติความเป็นมาและบทบาทใน LAMP stack ไปจนถึง storage engine หลักสามตัว (InnoDB, MyISAM, NDB) ที่แต่ละตัวเหมาะกับ workload ต่างกัน และวิธี cluster MySQL สองแบบสำหรับงานที่ต้องการ availability สูง

---

## What Is MySQL

MySQL เป็น object-relational database management system ที่มีบทบาทสำคัญในงาน web development พัฒนาโดยบริษัท MySQL AB จากสวีเดน (ตั้งชื่อตามลูกสาวของผู้ร่วมก่อตั้ง Monty Widenius) ต่อมาถูก Sun Microsystems ซื้อกิจการ แล้ว Oracle Corporation ซื้อ Sun Microsystems อีกทอดหนึ่ง โลโก้เป็นรูปโลมาชื่อ Sakila ได้รับความนิยมมากในช่วงปลายปี 1990s-ต้น 2000s จากบทบาทใน **LAMP stack** (Linux, Apache, MySQL, PHP)

**License**: ใช้ dual licensing คือ open source GNU GPL และ commercial license สำหรับ application ที่ต้องการ embed MySQL การเป็น open source ทำให้เกิด fork เช่น MariaDB

**คุณสมบัติ**: รองรับ Unix, Windows, Linux เขียน client application ได้หลายภาษา ใช้ SQL มาตรฐานพร้อม extension เพิ่มเติม (เช่นคำสั่ง `LOAD DATA` สำหรับ import ข้อมูลจากไฟล์ text) รองรับทั้งข้อมูลเชิงสัมพันธ์และ JSON

---

## Storage Engines

| Storage Engine | เหมาะกับ | ลักษณะเด่น |
| --------------- | -------- | ----------- |
| **InnoDB** (ค่า default) | workload ที่ต้องการสมดุลระหว่าง performance และ reliability | รองรับ transaction, row-level locking, clustered index บน primary key, foreign key constraint |
| **MyISAM** | workload ที่อ่านมากกว่าเขียน (เช่น data warehouse, web application) | ใช้ table-level locking ซึ่งลดประสิทธิภาพในสภาพแวดล้อมที่ read-write พร้อมกันมาก |
| **NDB** | งานที่ต้องการ availability และ redundancy สูง | รองรับการรัน MySQL server หลาย instance เป็น cluster |

---

## Clustering Options

1. **InnoDB + Group Replication** — มี primary server เดียวสำหรับ read-write และ secondary server หลายตัว ใช้ MySQL Router ทำ load balancing และ reconnect client อัตโนมัติเมื่อ server ล่ม
2. **MySQL Cluster Edition + NDB storage engine** — หลาย MySQL server node เข้าถึงชุด data node ที่มักเก็บใน memory เพิ่ม redundancy (หลาย data node) และ scalability (หลาย server node)

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Storage Engine | ส่วนประกอบของ MySQL ที่จัดการ SQL operation บนตารางและกำหนดฟีเจอร์ที่ตารางนั้นใช้ได้ |
| InnoDB | storage engine ค่า default ของ MySQL รองรับ transaction, row-level locking, foreign key |
| MyISAM | storage engine ของ MySQL เหมาะกับ workload ที่อ่านมากกว่าเขียน ใช้ table-level locking |
| NDB | storage engine ของ MySQL สำหรับรองรับการรันเป็น cluster |

---

## ❓ My Questions & Gaps

- [ ] Storage engine ของ MySQL แต่ละตัว (InnoDB, MyISAM, NDB) เหมาะกับ use case แบบไหนมากที่สุดในงาน data engineering

---

## 🔗 Resources

- ไม่มีลิงก์อ้างอิงภายนอกในวิดีโอนี้
