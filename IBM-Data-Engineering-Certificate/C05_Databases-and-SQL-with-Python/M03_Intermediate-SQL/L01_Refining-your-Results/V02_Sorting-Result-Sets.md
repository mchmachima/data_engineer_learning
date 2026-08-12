# Sorting Result Sets

`Tags: SQL, ORDER BY, sorting`

| Field             | Value                                          |
| ----------------- | ----------------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate    |
| **Course**        | C05 Databases and SQL for Data Science with Python |
| **Module**        | M03 Intermediate SQL                             |
| **Lesson**        | L01 Refining your Results                        |
| **Date studied**  | 2026-08-12                                       |

---

## Table of Contents

- [Overview](#overview)
- [Sorting with ORDER BY](#sorting-with-order-by)
- [Ascending vs Descending Order](#ascending-vs-descending-order)
- [Sorting by Column Sequence Number](#sorting-by-column-sequence-number)
- [Key Terms & Glossary](#key-terms--glossary)
- [My Questions & Gaps](#my-questions--gaps)
- [Resources](#resources)

---

## Overview

วิดีโอนี้สอนวิธีจัดเรียงลำดับผลลัพธ์ (result set) ที่ได้จาก SELECT statement โดยใช้ ORDER BY clause เพื่อให้ผลลัพธ์แสดงในลำดับที่อ่านง่ายและใช้งานสะดวกขึ้น เนื้อหาครอบคลุมการเรียงลำดับแบบ ascending และ descending รวมถึงวิธีระบุคอลัมน์ที่ต้องการเรียงลำดับ ทั้งการระบุด้วยชื่อคอลัมน์และด้วยลำดับตำแหน่งของคอลัมน์ใน SELECT statement

---

## Sorting with ORDER BY

เมื่อดึงข้อมูลด้วย SELECT โดยไม่มีการระบุลำดับ ผลลัพธ์ที่ได้อาจไม่เรียงตามลำดับใดๆ เพื่อให้ผลลัพธ์แสดงเป็นระเบียบ เช่น เรียงตามตัวอักษร เราใช้ `ORDER BY` clause เพื่อจัดเรียง result set ตามคอลัมน์ที่ระบุ

> ตัวอย่างข้อมูลประกอบด้านล่างเป็นข้อมูลสมมติที่สร้างขึ้นให้ตรงกับพฤติกรรมที่วิดีโออธิบาย (ไม่ใช่ค่าตัวเลข/ชื่อจริงจากสไลด์ เนื่องจาก transcript ไม่ได้ระบุค่าที่แน่นอน) เพื่อให้เห็นภาพว่า ORDER BY ทำงานอย่างไร

```sql
-- ดึงชื่อหนังสือทั้งหมด และเรียงลำดับตามตัวอักษรของ title
SELECT title FROM book ORDER BY title;
```

| title |
| --- |
| Getting started with Db2 Express-C |
| Getting started with instances and databases |
| Getting started with SQL |
| Volcano Adventures |

---

## Ascending vs Descending Order

โดย default แล้ว ORDER BY จะเรียงผลลัพธ์แบบ ascending (จากน้อยไปมาก หรือ A ไป Z) หากต้องการเรียงแบบ descending (มากไปน้อย หรือ Z ไป A) ให้เพิ่มคำสั่ง `DESC` ต่อท้าย ในกรณีที่ค่าคอลัมน์ที่ใช้เรียงมีตัวอักษรเริ่มต้นเหมือนกันหลายตัว การเรียงลำดับจะพิจารณาจากจุดที่ตัวอักษรเริ่มต่างกัน

```sql
-- เรียงชื่อหนังสือจากมากไปน้อย (Z ไป A)
SELECT title FROM book ORDER BY title DESC;
```

| title |
| --- |
| Volcano Adventures |
| Getting started with SQL |
| Getting started with instances and databases |
| Getting started with Db2 Express-C |

สังเกตว่าสามแถวสุดท้ายขึ้นต้นด้วย "Getting started with" เหมือนกัน การเรียงลำดับจึงเทียบกันที่คำถัดไป (SQL > instances > Db2)

| คำสั่ง | ลำดับผลลัพธ์ |
| --- | --- |
| `ORDER BY title` (ไม่ระบุ) | ascending (default) |
| `ORDER BY title DESC` | descending |

---

## Sorting by Column Sequence Number

นอกจากระบุชื่อคอลัมน์ตรงๆ แล้ว ยังสามารถระบุคอลัมน์ที่ต้องการเรียงลำดับด้วยหมายเลขลำดับตำแหน่งของคอลัมน์ใน column list ของ SELECT statement ได้ เช่น ถ้าคอลัมน์ที่สองใน SELECT คือ pages ก็สามารถใช้ `ORDER BY 2` แทนการพิมพ์ชื่อคอลัมน์ pages ได้

```sql
-- เรียงลำดับตามคอลัมน์ที่ 2 ในผลลัพธ์ (pages) แบบ ascending
SELECT title, pages FROM book ORDER BY 2;
```

| title | pages |
| --- | --- |
| Getting started with SQL | 150 |
| Getting started with Db2 Express-C | 210 |
| Volcano Adventures | 275 |
| Getting started with instances and databases | 390 |

---

## Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| ORDER BY      | clause ที่ใช้จัดเรียงลำดับ result set ตามคอลัมน์ที่ระบุ |
| Ascending order | การเรียงจากน้อยไปมาก หรือ A ไป Z (ค่า default ของ ORDER BY) |
| Descending order | การเรียงจากมากไปน้อย หรือ Z ไป A ระบุด้วยคำสั่ง DESC |
| Column sequence number | หมายเลขลำดับตำแหน่งของคอลัมน์ใน column list ของ SELECT statement ที่ใช้แทนชื่อคอลัมน์ใน ORDER BY ได้ |

---

## My Questions & Gaps

- [ ] สามารถ ORDER BY หลายคอลัมน์พร้อมกันได้หรือไม่ และแต่ละคอลัมน์กำหนด ASC/DESC แยกกันได้หรือไม่
- [ ] ORDER BY ด้วยชื่อคอลัมน์กับด้วยหมายเลขลำดับตำแหน่ง มีข้อดีข้อเสียต่างกันอย่างไรในการเขียน production query

---

## Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมในวิดีโอนี้
