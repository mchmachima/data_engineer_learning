# Data Movement Utilities

`Tags: backup, restore, import, export, load, RDBMS`

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
- [Three Ways to Move Data](#three-ways-to-move-data)
- [File Formats for Import and Export](#file-formats-for-import-and-export)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้แนะนำสามวิธีหลักในการย้ายข้อมูลเข้า-ออกจากฐานข้อมูล คือ backup/restore, import/export และ load ซึ่งแต่ละวิธีเหมาะกับสถานการณ์ต่างกัน เป็นทักษะสำคัญสำหรับ data engineer ที่ต้อง populate ตาราง สร้างฐานข้อมูลสำเนา หรือสำรองข้อมูลสำหรับ disaster recovery

---

## Three Ways to Move Data

Data engineer และ database administrator ต้องย้ายข้อมูลเข้า-ออกฐานข้อมูลด้วยเหตุผลหลายอย่าง เช่น การ populate ตารางครั้งแรก, สร้างฐานข้อมูลสำเนาสำหรับ development/testing, สร้าง snapshot สำหรับ disaster recovery, หรือนำข้อมูลจากแหล่งภายนอกเข้ามาสร้างตารางใหม่

| วิธี | ทำอะไร | เหมาะกับ |
| ---- | ------ | -------- |
| **Backup and restore** | backup สร้างไฟล์ที่รวบรวม database objects และข้อมูลทั้งหมด (schema, table, view, stored procedure, constraint, trigger, security setting ไปจนถึงความสัมพันธ์ระหว่าง object) ส่วน restore สร้างสำเนาฐานข้อมูลต้นฉบับขึ้นมาใหม่จากไฟล์ backup | disaster recovery และสร้างสำเนาสำหรับ dev/test |
| **Import and export** | import อ่านข้อมูลจากไฟล์แล้วทำ insert statement เข้าตารางเป้าหมาย ส่วน export ดึงข้อมูลจากตารางไปเก็บเป็นไฟล์ ทำได้ผ่าน command line utility, management API, GUI/web tool หรือ third-party tool | ตารางขนาดเล็กกว่าที่ต้องการความถูกต้องของ constraint |
| **Load** | จัดการข้อมูลเข้าฐานข้อมูลโดยตรง (format pages ลง database) แทนที่จะรัน SQL insert statement ทีละคำสั่งแบบ import ทำให้เร็วกว่า แต่ไม่ตรวจสอบ referential/table constraint และอาจข้าม database logging ไปด้วย | ข้อมูลปริมาณมาก |

---

## File Formats for Import and Export

รูปแบบไฟล์ที่พบบ่อยสำหรับ import/export ได้แก่ DEL (delimited ASCII เช่น CSV), ASC (non-delimited ASCII แบบ flat text คอลัมน์ตรงกัน), PC/IXF (integration exchange format ที่เก็บโครงสร้างตารางแบบสมบูรณ์) และ JSON

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Backup/Restore | การสำรองและกู้คืนฐานข้อมูลทั้งชุด รวมทุก object และข้อมูล |
| Import/Export | การนำข้อมูลเข้า/ออกจากตารางผ่านไฟล์ โดยใช้ SQL insert statement เบื้องหลัง |
| Load Utility | เครื่องมือโหลดข้อมูลปริมาณมากเข้าตารางโดยตรง เร็วกว่า import แต่ไม่ตรวจ constraint |
| DEL (Delimited ASCII) | รูปแบบไฟล์ที่คั่นค่าด้วย delimiter เช่น comma (CSV) |
| ASC (Non-delimited ASCII) | รูปแบบไฟล์ flat text ที่จัดคอลัมน์ให้ตรงกันแบบไม่มี delimiter |
| PC/IXF | รูปแบบไฟล์ integration exchange format ที่เก็บโครงสร้างตารางแบบสมบูรณ์ |

---

## ❓ My Questions & Gaps

- [ ] ความแตกต่างระหว่าง import กับ load utility ในแง่ performance และ use case ควรเลือกใช้แบบไหนเมื่อไหร่ในสถานการณ์จริง
- [ ] PC/IXF format ใช้งานจริงในเครื่องมือ/แพลตฟอร์มอื่นนอกจาก Db2 มากน้อยแค่ไหน

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
