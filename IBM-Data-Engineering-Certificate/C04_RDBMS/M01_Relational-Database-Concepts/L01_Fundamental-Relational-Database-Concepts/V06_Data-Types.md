# Data Types

`Tags: RDBMS, data types, VARCHAR, CHAR, SQL`

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
- [What Is a Data Type](#what-is-a-data-type)
- [Varchar](#varchar)
- [Common Data Types](#common-data-types)
- [Advantages of Using Appropriate Data Types](#advantages-of-using-appropriate-data-types)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายว่า data type คืออะไรและทำไมแต่ละคอลัมน์ในตารางต้องมี data type กำกับ พร้อมเจาะลึก VARCHAR ในฐานะตัวอย่าง แล้วสรุป data type พื้นฐานที่พบบ่อยในฐานข้อมูล (date/time, float, decimal, integer, binary, char) และปิดท้ายด้วยประโยชน์ของการเลือก data type ให้เหมาะสม

---

## What Is a Data Type

ตารางฐานข้อมูลแทน entity หนึ่งตัว โดยแต่ละคอลัมน์แทน attribute ของ entity นั้น (เช่น ตาราง `Book` ที่มีคอลัมน์ `title`, `publish date`, `pages`) ค่าทุกค่าในคอลัมน์เดียวกันควรเป็นข้อมูลชนิดเดียวกัน — data type ที่กำหนดให้คอลัมน์เป็นตัวควบคุมว่าคอลัมน์นั้นเก็บอะไรได้บ้าง คอลัมน์ text เก็บข้อมูล alphanumeric, คอลัมน์ date รับเฉพาะวันที่ที่ถูกต้อง และคอลัมน์ numeric รับเฉพาะตัวเลข

---

## Varchar

Varchar เป็น data type สำหรับเก็บ character string ที่มีความยาวไม่แน่นอน จนถึงค่าสูงสุดที่กำหนด เช่น `VARCHAR(100)` จองพื้นที่ไว้สูงสุด 100 ตัวอักษร แต่ string ที่มี 50 ตัวอักษรจะใช้พื้นที่เท่าที่จำเป็นสำหรับ 50 ตัวอักษรนั้นเท่านั้น — ไม่ใช่เต็ม 100

ข้อพิจารณาสำคัญ:

- **Efficiency** — Varchar จองพื้นที่เท่าที่ใช้จริงเท่านั้น จึงประหยัดพื้นที่กว่า fixed-length type อย่าง Char
- **Flexibility** — เหมาะกับ string ที่มีความยาวแตกต่างกันมาก เช่น ชื่อ, ที่อยู่ หรือคำอธิบาย

---

## Common Data Types

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

## Advantages of Using Appropriate Data Types

- ป้องกันไม่ให้ข้อมูลที่ไม่ถูกต้องถูกใส่เข้าไปในคอลัมน์ เนื่องจาก data type จำกัดว่าอะไรคือ input ที่ถูกต้อง
- ทำให้ข้อมูลวันที่ เวลา และตัวเลขถูกเรียงลำดับได้อย่างแม่นยำ
- ทำให้เลือกช่วงข้อมูลได้อย่างแม่นยำ (เช่น กรองวันที่หรือตัวเลขในช่วงที่กำหนด)
- รองรับการคำนวณเชิงตัวเลขบนข้อมูลที่มี type ถูกต้อง เช่น การคำนวณยอดรวมของคำสั่งซื้อ

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
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

---

## ❓ My Questions & Gaps

- [ ] ความแตกต่างเชิงปฏิบัติระหว่าง DATETIME กับ TIMESTAMP ในแต่ละระบบฐานข้อมูลมีอะไรบ้าง (เช่น การจัดการ time zone, ขอบเขตค่า)
- [ ] การเลือก VARCHAR ที่มีความยาวสูงสุดมาก (เช่น VARCHAR(255) เทียบกับ VARCHAR(50)) มีผลด้าน performance หรือ indexing จริงหรือไม่ ทั้งที่พื้นที่จัดเก็บใช้เท่าที่จำเป็นเท่านั้น
- [ ] ในทางปฏิบัติ เมื่อไรที่ Float เป็นตัวเลือกที่ยอมรับได้มากกว่า Decimal นอกเหนือจากงานการเงิน มี performance tradeoff หรือไม่
- [ ] มีขีดจำกัดขนาดหรือ best practice ในการเก็บไฟล์ขนาดใหญ่ในคอลัมน์ BLOB เทียบกับการเก็บ path/reference ของไฟล์แทนหรือไม่

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
