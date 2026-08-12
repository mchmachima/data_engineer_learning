# Using String Patterns and Ranges

`Tags: SQL, WHERE clause, string patterns, ranges`

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
- [String Patterns with LIKE](#string-patterns-with-like)
- [Ranges with BETWEEN AND](#ranges-with-between-and)
- [Sets of Values with IN](#sets-of-values-with-in)
- [Key Terms & Glossary](#key-terms--glossary)
- [My Questions & Gaps](#my-questions--gaps)
- [Resources](#resources)

---

## Overview

วิดีโอนี้สอนเทคนิคขั้นสูงในการดึงข้อมูลด้วย SELECT statement เมื่อเราไม่ทราบค่าที่แน่นอนที่จะใส่ใน WHERE clause โดยใช้ string patterns, ranges และ sets of values แทนการระบุค่าตรงๆ ทำให้ query เขียนง่ายขึ้นและกระชับขึ้น เนื้อหาครอบคลุมการใช้ LIKE predicate กับ wildcard character, การใช้ BETWEEN AND เพื่อระบุช่วงตัวเลข และการใช้ IN operator เพื่อระบุชุดของค่าที่ต้องการเปรียบเทียบ

---

## String Patterns with LIKE

เมื่อเราไม่ทราบค่าที่แน่นอนสำหรับ predicate ใน WHERE clause เช่น จำชื่อผู้แต่งไม่ได้แต่จำได้ว่าชื่อขึ้นต้นด้วยตัวอักษร R เราสามารถใช้ LIKE predicate เพื่อค้นหา pattern ในคอลัมน์ได้ โดยใช้เครื่องหมาย percent sign (`%`) เป็น wildcard character สำหรับแทนตัวอักษรที่ขาดหายไป ซึ่งวางได้ทั้งก่อนหน้า pattern, หลัง pattern หรือทั้งสองด้าน

```sql
-- ดึง first name ของ author ที่ชื่อขึ้นต้นด้วยตัวอักษร R
SELECT firstname FROM author WHERE firstname LIKE 'R%';
```

---

## Ranges with BETWEEN AND

แทนที่จะเขียนเงื่อนไขช่วงตัวเลขด้วย comparison operator สองตัว (greater than or equal to และ less than or equal to) เราสามารถใช้ `BETWEEN AND` เพื่อเปรียบเทียบค่าสองค่าได้ในคำสั่งเดียว โดยค่าทั้งสองด้านของช่วง (range) นับรวมอยู่ในผลลัพธ์ด้วย (inclusive) ทำให้ query สั้นและเขียนได้เร็วขึ้น

```sql
-- ดึงหนังสือที่มีจำนวนหน้าอยู่ระหว่าง 290 ถึง 300 (รวมค่าทั้งสองด้าน)
SELECT * FROM book WHERE pages BETWEEN 290 AND 300;
```

| แบบเดิม | แบบใช้ BETWEEN AND |
| --- | --- |
| `WHERE pages >= 290 AND pages <= 300` | `WHERE pages BETWEEN 290 AND 300` |

---

## Sets of Values with IN

เมื่อค่าข้อมูลที่ต้องการไม่สามารถจัดกลุ่มเป็นช่วง (range) ได้ เช่น ต้องการดึงข้อมูล author จากหลายประเทศ การเขียน WHERE clause แบบระบุค่าซ้ำๆ ด้วย OR จะยาวและซับซ้อนขึ้นเรื่อยๆ เมื่อมีเงื่อนไขมากขึ้น จึงใช้ `IN` operator แทน ซึ่งรับ list ของค่าที่ต้องการเปรียบเทียบได้ในคำสั่งเดียว

```sql
-- ดึง author ที่มาจากประเทศ Australia หรือ Brazil โดยใช้ IN operator
SELECT * FROM author WHERE country IN ('Australia', 'Brazil');
```

---

## Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Predicate     | เงื่อนไขใน WHERE clause ที่ประเมินผลได้เป็น true, false หรือ unknown |
| LIKE          | predicate สำหรับค้นหา pattern ของข้อความในคอลัมน์ |
| Wildcard character | ตัวอักษรพิเศษ (เช่น `%`) ที่ใช้แทนตัวอักษรอื่นๆ ที่ไม่ทราบค่า |
| BETWEEN AND   | comparison operator สำหรับระบุช่วงค่า โดยรวมค่าทั้งสองด้านของช่วง (inclusive) |
| IN            | operator สำหรับระบุ set ของค่าที่ต้องการเปรียบเทียบใน WHERE clause แทนการเขียน OR ซ้ำๆ |

---

## My Questions & Gaps

- [ ] LIKE รองรับ wildcard character ตัวอื่นนอกจาก `%` หรือไม่ (เช่น underscore `_` สำหรับแทนตัวอักษรเดียว)
- [ ] BETWEEN AND ใช้กับข้อมูลประเภทวันที่ (date) ได้หรือไม่ และมี syntax ต่างจากตัวเลขอย่างไร
- [ ] IN operator รองรับการใช้ร่วมกับ subquery ได้หรือไม่

---

## Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมในวิดีโอนี้
