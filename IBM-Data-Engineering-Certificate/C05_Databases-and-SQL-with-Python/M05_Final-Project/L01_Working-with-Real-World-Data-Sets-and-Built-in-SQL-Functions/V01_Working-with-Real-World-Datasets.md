# Working with Real World Datasets

`Tags: SQL, CSV, phpMyAdmin, Pandas, DB-API`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C05 Databases and SQL for Data Science with Python |
| **Module**        | M05 Final Project                         |
| **Lesson**        | L01 Working with Real-World Data Sets and Built-in SQL Functions |
| **Date studied**  | 2026-08-15                                |

---

## Table of Contents

- [Overview](#overview)
- [CSV Files as Real-World Datasets](#csv-files-as-real-world-datasets)
- [Loading CSV Data with phpMyAdmin](#loading-csv-data-with-phpmyadmin)
- [Querying Columns with Special Characters](#querying-columns-with-special-characters)
- [Splitting Long Queries](#splitting-long-queries)
- [Querying with Pandas read_sql](#querying-with-pandas-read_sql)
- [Restricting Result Set Size with LIMIT](#restricting-result-set-size-with-limit)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้ให้เทคนิคปฏิบัติสำหรับการทำงานกับ dataset จริงที่มักมาในรูปแบบไฟล์ CSV ตั้งแต่การทำความเข้าใจโครงสร้างไฟล์ การโหลดข้อมูลเข้าฐานข้อมูลผ่าน phpMyAdmin ไปจนถึงการ query column ที่มีชื่อซับซ้อน และการจัดการ query ยาวๆ ทั้งใน SQL cell magic และ Python เนื้อหานี้สำคัญเพราะ dataset จริงมักไม่สะอาดเรียบร้อยเหมือนตัวอย่างในบทเรียน ต้องรู้เทคนิคเสริมเหล่านี้เพื่อโหลดและ query ได้ถูกต้อง

---

## CSV Files as Real-World Datasets

Dataset จริงส่วนใหญ่มักถูกแจกจ่ายเป็นไฟล์ CSV (Comma-Separated Values) ซึ่งเป็น text file ที่คั่นค่าด้วยเครื่องหมายจุลภาค (comma) แต่บางครั้งอาจใช้ separator อื่น เช่น semicolon แทน โดยทั่วไปแถวแรกของไฟล์ CSV มักเป็น header row ที่เก็บชื่อ attribute ซึ่งจะถูก map ไปเป็นชื่อ column ของ table เมื่อโหลดเข้าฐานข้อมูล เช่นไฟล์ตัวอย่าง `DOGS.csv` ที่มี attribute คือ ID, Name of dog, และ Breed

---

## Loading CSV Data with phpMyAdmin

เมื่อ import ไฟล์ CSV เข้าฐานข้อมูลผ่าน phpMyAdmin ต้อง browse ไปเลือกไฟล์ แล้วเลือก format เป็น CSV จาก dropdown ซึ่งจะแสดง section "Format Specific Options" มี checkbox ให้ระบุว่าแถวแรกของไฟล์เป็นชื่อ column หรือไม่ ถ้าไฟล์มี header ให้ติ๊ก checkbox นี้ก่อนกด Go แล้ว MySQL จะ auto-detect ชื่อ header เป็นชื่อ column และสร้าง CREATE/INSERT statement ให้อัตโนมัติ โดย default ชื่อ table จะถูกตั้งเป็นชื่อไฟล์แบบตัวพิมพ์เล็กทั้งหมด

---

## Querying Columns with Special Characters

ชื่อ column จากไฟล์ CSV มักมี space หรือ special character ปนอยู่ เช่น "Name of dog" การจะ query column แบบนี้ ต้องใช้ backtick (`` ` ``) ครอบชื่อ column ไม่ใช่ single quote หรือ double quote เพราะจะใช้ไม่ได้กับชื่อ column

```sql
-- query column ที่มี space ในชื่อโดยใช้ backtick
SELECT `Name of dog` FROM dogs;
```

---

## Splitting Long Queries

Query ที่ยาว เช่น join query หรือ nested query ควรแบ่งเป็นหลายบรรทัดเพื่อให้อ่านง่ายขึ้น ใน Python notebook ที่ใช้ line magic (`%sql`) ต้องใช้ backslash (`\`) ต่อท้ายบรรทัดเพื่อบอกว่าบรรทัดถัดไปเป็น query เดียวกัน ไม่เช่นนั้นอาจเจอ error แต่ถ้าใช้ SQL cell magic (`%%sql`) เนื้อหาทั้ง cell จะถูกตีความเป็น SQL code อยู่แล้ว จึงไม่จำเป็นต้องใช้ backslash

```sql
-- ตัวอย่าง line magic ที่ต้องใช้ backslash เพื่อขึ้นบรรทัดใหม่
%sql SELECT * FROM dogs \
WHERE breed = 'Labrador'
```

---

## Querying with Pandas read_sql

ใน Python สามารถ query table ในฐานข้อมูลได้โดยใช้ `read_sql` method จาก Pandas library ซึ่งจะสะดวกขึ้นถ้าเก็บ query ไว้ในตัวแปร เช่น `query_statement` และหาก query มี double quote (เพื่อระบุชื่อ column ที่มี space) ให้ใช้ single quote ครอบตัวแปร Python เพื่อแยกจาก double quote ของชื่อ column ส่วนถ้าต้องระบุ single quote ภายใน query เอง (เช่นค่าใน WHERE clause) ให้ใช้ backslash เป็น escape character

```python
# เก็บ query ไว้ในตัวแปรแล้วใช้ single quote ครอบ เพื่อแยกจาก double quote ของชื่อ column
query_statement = 'SELECT "Name of dog" FROM dogs WHERE breed = \'Labrador\''
df = pandas.read_sql(query_statement, connection)
```

---

## Restricting Result Set Size with LIMIT

Table ในฐานข้อมูลอาจมีข้อมูลหลักพันหรือหลักล้านแถว การดึงข้อมูลทั้งหมดด้วย `SELECT *` แล้วนำมา `.head()` ใน Pandas อาจใช้เวลานาน แนะนำให้ใช้ `LIMIT` clause เพื่อจำกัดจำนวนแถวที่ดึงมาแทน

```sql
-- ดึงมาแค่ 3 แถวแรกจากตาราง census_data
SELECT * FROM census_data LIMIT 3;
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| CSV | Comma-Separated Values — text file ที่เก็บข้อมูลโดยคั่นค่าด้วยเครื่องหมายจุลภาค (หรือ separator อื่น เช่น semicolon) |
| Header row | แถวแรกของไฟล์ CSV ที่เก็บชื่อ attribute ซึ่งจะถูก map เป็นชื่อ column ของ table |
| phpMyAdmin | เครื่องมือ web-based สำหรับจัดการฐานข้อมูล MySQL รวมถึงการ import ไฟล์ CSV |
| Backtick | เครื่องหมาย `` ` `` ที่ใช้ครอบชื่อ column ที่มี space หรือ special character แทนการใช้ single/double quote |
| Line magic | คำสั่ง magic ของ Jupyter ที่ขึ้นต้นด้วย `%` เดียว ใช้กับหนึ่งบรรทัด |
| SQL cell magic | คำสั่ง magic ที่ขึ้นต้นด้วย `%%sql` ทำให้ทั้ง cell ถูกตีความเป็น SQL code โดยไม่ต้องใช้ backslash ต่อบรรทัด |
| read_sql | method จาก Pandas library ใช้ query ข้อมูลจากฐานข้อมูลแล้วคืนผลลัพธ์เป็น DataFrame |
| Escape character | อักขระ (เช่น backslash) ที่ใช้ระบุว่าตัวอักษรถัดไปควรถูกตีความตามตัวอักษร ไม่ใช่ตามความหมายพิเศษ เช่นใช้ escape single quote ภายใน string |
| LIMIT | clause ที่ใช้จำกัดจำนวนแถวสูงสุดที่ query จะคืนกลับมา |

---

## ❓ My Questions & Gaps

- [ ] ถ้า separator ในไฟล์ CSV ไม่ใช่ comma (เช่น semicolon) ต้องตั้งค่าอะไรเพิ่มใน phpMyAdmin ตอน import
- [ ] ชื่อ table ที่ auto-generate จากชื่อไฟล์ (lowercase) จะจัดการกับ space หรือ special character ในชื่อไฟล์อย่างไร
- [ ] มีวิธีโหลด CSV เข้าฐานข้อมูลแบบ programmatic (ไม่ผ่าน phpMyAdmin) ด้วย Python ไหม เช่นผ่าน Pandas `to_sql`

---

## 🔗 Resources

- phpMyAdmin — เครื่องมือ import CSV ที่กล่าวถึงในวิดีโอ
- Pandas `read_sql` documentation
