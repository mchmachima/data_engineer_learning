# Inner Join

`Tags: SQL, JOIN, INNER JOIN, alias, ON clause`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C05 Databases and SQL with Python         |
| **Module**        | M06 Advance SQL                           |
| **Lesson**        | L02 Join Statements                       |
| **Date studied**  | 2026-08-16                                |

---

## Table of Contents

- [Overview](#overview)
- [What an Inner Join Is](#what-an-inner-join-is)
- [Inner Join Syntax](#inner-join-syntax)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบาย inner join ซึ่งเป็นประเภท JOIN ที่ใช้บ่อยที่สุดใน SQL เนื้อหาครอบคลุมความหมายของ inner join เมื่อไหร่ควรใช้ และ syntax ของคำสั่ง INNER JOIN พร้อมตัวอย่างจริงจากตาราง borrower และ loan

---

## What an Inner Join Is

Join operation คือการรวมแถวจากสองตารางขึ้นไป โดยอาศัยความสัมพันธ์ระหว่างคอลัมน์บางคอลัมน์ในตารางเหล่านั้น SQL มี join สองประเภทหลักคือ inner join และ outer join

Inner join ซึ่งเป็นประเภทที่ใช้บ่อยที่สุด จะแสดงเฉพาะแถวจากสองตารางที่มีค่าตรงกันในคอลัมน์ร่วม ซึ่งมักเป็น primary key ของตารางหนึ่งที่ปรากฏเป็น foreign key ในอีกตาราง แถวที่ไม่มีค่าตรงกันจะไม่ถูกแสดงในผลลัพธ์

---

## Inner Join Syntax

ตัวอย่าง: ต้องการดึงรายชื่อคนที่ยืมหนังสือทั้งหมด พร้อมวันที่ยืม ซึ่งต้องใช้ข้อมูลจากทั้งตาราง borrower และตาราง loan

ใน FROM clause ระบุ join ระหว่างตาราง borrower และ loan เป็น `BORROWER INNER JOIN LOAN` โดยตั้งชื่อย่อ (alias) ให้ตาราง borrower เป็น B และตาราง loan เป็น L การใช้ alias ช่วยให้ไม่ต้องเขียนชื่อตารางเต็มซ้ำ ๆ ตารางที่ระบุอยู่ทางซ้ายของ JOIN clause เรียกว่า left table ซึ่งในตัวอย่างนี้คือตาราง borrower

จากนั้นเลือกคอลัมน์ borrower ID, last name และ country จากตาราง borrower และคอลัมน์ borrower ID กับ loan date จากตาราง loan ใน ON clause จะระบุ JOIN predicate คือเงื่อนไขว่า borrower ID ในตาราง borrower ต้องเท่ากับ borrower ID ในตาราง loan แต่ละชื่อคอลัมน์ในการ join นี้จะมี prefix เป็น B หรือ L (alias) กำกับไว้

```sql
-- ดึงรายชื่อผู้ยืมพร้อมวันที่ยืม โดย join ตาราง borrower และ loan ผ่าน borrower ID
SELECT B.BORROWER_ID, B.LASTNAME, B.COUNTRY, L.BORROWER_ID, L.LOAN_DATE
FROM BORROWER B
INNER JOIN LOAN L
ON B.BORROWER_ID = L.BORROWER_ID;
```

ผลลัพธ์จะแสดงเฉพาะแถวที่ Borrower_Id ในทั้งสองตารางตรงกันเท่านั้น ส่วนแถวที่ Borrower_Id ไม่ตรงกันจะไม่ปรากฏในผลลัพธ์

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Inner Join | JOIN ที่แสดงเฉพาะแถวจากสองตารางที่มีค่าตรงกันในคอลัมน์ร่วม แถวที่ไม่ตรงกันจะไม่แสดงในผลลัพธ์ |
| Left Table | ตารางที่ระบุอยู่ทางซ้ายของ JOIN clause ใน FROM clause |
| ON clause | ส่วนของคำสั่ง JOIN ที่ใช้ระบุ JOIN predicate หรือเงื่อนไขการจับคู่แถวระหว่างตาราง |
| JOIN predicate | เงื่อนไขที่ใช้กำหนดว่าแถวจากสองตารางจะถูกจับคู่กันอย่างไรใน JOIN |
| Alias | ชื่อทางเลือกที่ใช้อ้างอิงตารางหรือคอลัมน์แทนชื่อเต็ม เพื่อให้เขียน query ได้กระชับขึ้น |

---

## ❓ My Questions & Gaps

- [ ] เขียน `INNER JOIN` แบบเดียวกับการเขียน `FROM table1, table2 WHERE table1.id = table2.id` (implicit join) ให้ผลลัพธ์เหมือนกันหรือไม่ และแบบไหนดีกว่ากัน
- [ ] จะเกิดอะไรขึ้นถ้า ON clause ระบุเงื่อนไขผิด หรือลืมใส่ ON clause ไปเลย

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมที่กล่าวถึงในวิดีโอนี้
