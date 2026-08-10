# COUNT, DISTINCT, LIMIT

`Tags: SQL, COUNT, DISTINCT, LIMIT`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C05 Databases and SQL for Data Science with Python |
| **Module**        | M01 Getting Started with SQL              |
| **Lesson**        | L03 COUNT, DISTINCT, LIMIT                |
| **Date studied**  | 2026-08-10                                |

---

## Table of Contents

- [Overview](#overview)
- [COUNT](#count)
- [DISTINCT](#distinct)
- [LIMIT](#limit)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้แนะนำ expression ที่มีประโยชน์อีก 3 ตัวที่ใช้ร่วมกับ SELECT statement ได้แก่ COUNT สำหรับนับจำนวนแถว, DISTINCT สำหรับตัดค่าที่ซ้ำกันออกจาก result set, และ LIMIT สำหรับจำกัดจำนวนแถวที่ดึงกลับมา ทั้งสามตัวช่วยให้ทำงานกับ result set ได้สะดวกขึ้นโดยเฉพาะเมื่อข้อมูลมีขนาดใหญ่

---

## COUNT

COUNT เป็น built-in database function ที่ใช้นับจำนวนแถวที่ตรงกับเงื่อนไขของ query เช่น ถ้าต้องการนับจำนวนแถวทั้งหมดในตาราง ใช้ `select COUNT(*) from tablename`

ตัวอย่าง: จากตาราง MEDALS ที่มีคอลัมน์ COUNTRY ถ้าต้องการนับจำนวนแถวที่ผู้ได้รับเหรียญมาจากประเทศ Canada

```sql
-- Count rows in MEDALS where COUNTRY is 'CANADA'
SELECT COUNT(COUNTRY) FROM MEDALS WHERE COUNTRY = 'CANADA';
```

---

## DISTINCT

DISTINCT ใช้ตัดค่าที่ซ้ำกันออกจาก result set เพื่อดึงเฉพาะค่าที่ไม่ซ้ำ (unique values) ในคอลัมน์นั้น เช่น ในตาราง MEDALS ประเทศหนึ่งอาจได้เหรียญทองหลายครั้ง ถ้าต้องการดึงรายชื่อประเทศที่ได้เหรียญทองแบบไม่ซ้ำ ก็ใช้ DISTINCT ร่วมกับ WHERE

```sql
-- Retrieve unique countries that won a gold medal
SELECT DISTINCT COUNTRY FROM MEDALS WHERE MEDALTYPE = 'GOLD';
```

---

## LIMIT

LIMIT ใช้จำกัดจำนวนแถวที่ดึงกลับมาจาก database มีประโยชน์มากเมื่อต้องการดูตัวอย่างผลลัพธ์เพียงบางส่วนแทนที่จะดึง result set ทั้งหมดซึ่งอาจมีขนาดใหญ่มาก

```sql
-- Retrieve just the first 10 rows in a table
SELECT * FROM tablename LIMIT 10;

-- Retrieve just a few rows in MEDALS for a particular year
SELECT * FROM MEDALS WHERE YEAR = 2018 LIMIT 5;
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| COUNT | built-in function ที่นับจำนวนแถวที่ตรงกับเงื่อนไขของ query |
| DISTINCT | keyword ที่ใช้ตัดค่าที่ซ้ำกันออกจาก result set เหลือแต่ค่าที่ไม่ซ้ำ |
| LIMIT | keyword ที่ใช้จำกัดจำนวนแถวสูงสุดที่ดึงกลับมาจาก query |

---

## ❓ My Questions & Gaps

- [x] COUNT(*) กับ COUNT(columnname) ต่างกันอย่างไรเมื่อคอลัมน์นั้นมีค่า NULL — `COUNT(*)` นับทุกแถวโดยไม่สนใจว่าค่าในคอลัมน์ใดเป็น NULL หรือไม่ ในขณะที่ `COUNT(columnname)` นับเฉพาะแถวที่คอลัมน์นั้นมีค่าไม่เป็น NULL เท่านั้น (แถวที่คอลัมน์นั้นเป็น NULL จะไม่ถูกนับ)
- [x] LIMIT ใช้ร่วมกับ ORDER BY ได้หรือไม่ และจำเป็นต้องมี ORDER BY ก่อนเสมอเพื่อให้ผลลัพธ์คงที่หรือไม่ — ใช้ร่วมกันได้และเป็น pattern ที่นิยมมาก (เช่น หา top N แถว) หากไม่ใส่ ORDER BY, ลำดับแถวที่ database ส่งกลับมาไม่มีการรับประกัน (implementation-defined) ดังนั้นผลลัพธ์ของ LIMIT อาจไม่คงที่ในแต่ละครั้งที่รัน query — ถ้าต้องการผลลัพธ์ที่ทำซ้ำได้ (deterministic) ควรใส่ ORDER BY เสมอ

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงที่กล่าวถึงในวิดีโอนี้
