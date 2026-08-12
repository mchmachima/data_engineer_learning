# Grouping Result Sets

`Tags: SQL, DISTINCT, GROUP BY, HAVING`

| Field            | Value                                              |
| ---------------- | -------------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate      |
| **Course**       | C05 Databases and SQL for Data Science with Python |
| **Module**       | M03 Intermediate SQL                               |
| **Lesson**       | L01 Refining your Results                          |
| **Date studied** | 2026-08-12                                         |

---

## Table of Contents

- [Overview](#overview)
- [Eliminating Duplicates with DISTINCT](#eliminating-duplicates-with-distinct)
- [Grouping Rows with GROUP BY](#grouping-rows-with-group-by)
- [Naming Derived Columns with AS](#naming-derived-columns-with-as)
- [Restricting Groups with HAVING](#restricting-groups-with-having)
- [Key Terms & Glossary](#key-terms--glossary)
- [My Questions & Gaps](#my-questions--gaps)
- [Resources](#resources)

---

## Overview

วิดีโอนี้สอนวิธีจัดการกับข้อมูลที่ซ้ำกันใน result set และการจัดกลุ่มข้อมูลเพื่อสรุปผล โดยใช้ DISTINCT เพื่อกำจัดค่าซ้ำ และใช้ GROUP BY ร่วมกับฟังก์ชัน aggregate เช่น COUNT เพื่อสรุปจำนวนข้อมูลในแต่ละกลุ่ม นอกจากนี้ยังครอบคลุมการตั้งชื่อคอลัมน์ที่คำนวณได้ด้วย AS และการจำกัดผลลัพธ์ของกลุ่มด้วย HAVING clause ซึ่งทำงานร่วมกับ GROUP BY เท่านั้น ต่างจาก WHERE ที่ทำงานกับทั้ง result set

---

## Eliminating Duplicates with DISTINCT

เมื่อ result set มีค่าซ้ำกันจากหลายแถว เช่น author หลายคนมาจากประเทศเดียวกัน ทำให้ column country มีค่าซ้ำ หากต้องการดูแค่รายชื่อประเทศที่ไม่ซ้ำกัน สามารถใช้ keyword `DISTINCT` เพื่อกำจัดค่าซ้ำออกจาก result set ได้

> ตัวอย่างข้อมูลประกอบด้านล่างเป็นข้อมูลสมมติที่สร้างขึ้นให้ตรงกับตัวเลขที่วิดีโอกล่าวถึง (20 authors จาก 6 ประเทศ, China และ India มี 6 authors) เนื่องจาก transcript ไม่ได้ระบุค่าจริงทั้งหมด

```sql
-- ดึงรายชื่อประเทศที่ไม่ซ้ำกันของ author ทั้งหมด เรียงตามลำดับตัวอักษร
SELECT DISTINCT country FROM author;
```

| country |
| --- |
| AU |
| BR |
| CA |
| CN |
| IN |
| US |

---

## Grouping Rows with GROUP BY

หากต้องการทราบจำนวน author ที่มาจากแต่ละประเทศ ไม่ใช่แค่รายชื่อประเทศ ต้องใช้ `GROUP BY` clause ซึ่งจัดกลุ่ม result set ออกเป็น subset ตามค่าที่ตรงกันในคอลัมน์ที่ระบุ แล้วใช้ฟังก์ชัน aggregate อย่าง `COUNT` เพื่อนับจำนวนแถวในแต่ละกลุ่ม

```sql
-- นับจำนวน author ในแต่ละประเทศ
SELECT country, COUNT(country) FROM author GROUP BY country;
```

| country | 2 |
| --- | --- |
| AU | 2 |
| BR | 2 |
| CA | 2 |
| CN | 6 |
| IN | 6 |
| US | 2 |

---

## Naming Derived Columns with AS

เมื่อคอลัมน์ในผลลัพธ์ถูกคำนวณขึ้นมาจากฟังก์ชัน (เช่น COUNT) ชื่อคอลัมน์ที่แสดงจะเป็นตัวเลขลำดับตำแหน่ง (เช่น "2") แทนที่จะเป็นชื่อที่สื่อความหมาย เราสามารถตั้งชื่อคอลัมน์ที่คำนวณได้นี้ด้วย keyword `AS` เพื่อให้ผลลัพธ์อ่านเข้าใจง่ายขึ้น

```sql
-- ตั้งชื่อคอลัมน์ที่คำนวณจาก COUNT ว่า "Count"
SELECT country, COUNT(country) AS Count FROM author GROUP BY country;
```

| country | Count |
| --- | --- |
| AU | 2 |
| BR | 2 |
| CA | 2 |
| CN | 6 |
| IN | 6 |
| US | 2 |

---

## Restricting Groups with HAVING

หลังจากจัดกลุ่มและนับจำนวนแล้ว หากต้องการกรองเฉพาะกลุ่มที่ตรงตามเงื่อนไข เช่น เฉพาะประเทศที่มี author มากกว่า 4 คน ต้องใช้ `HAVING` clause ร่วมกับ GROUP BY ข้อแตกต่างสำคัญคือ WHERE clause ใช้กรองทั้ง result set ก่อนจัดกลุ่ม ในขณะที่ HAVING clause ใช้กรองเฉพาะกลุ่มที่เกิดจาก GROUP BY เท่านั้น

```sql
-- แสดงเฉพาะประเทศที่มี author มากกว่า 4 คน
SELECT country, COUNT(country) AS Count
FROM author
GROUP BY country
HAVING COUNT(country) > 4;
```

| country | Count |
| --- | --- |
| CN | 6 |
| IN | 6 |

| Clause | ใช้กรองกับ                     |
| ------ | ------------------------------ |
| WHERE  | ทั้ง result set (ก่อนจัดกลุ่ม) |
| HAVING | เฉพาะกลุ่มที่เกิดจาก GROUP BY  |

---

## Key Terms & Glossary

| Term (ศัพท์)       | คำอธิบาย (ภาษาไทย)                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| DISTINCT           | keyword ที่ใช้กำจัดค่าซ้ำออกจาก result set                                                                   |
| GROUP BY           | clause ที่จัดกลุ่ม result set ตามค่าที่ตรงกันในคอลัมน์ที่ระบุ                                                |
| Aggregate function | ฟังก์ชันที่คำนวณค่าสรุปจากหลายแถว เช่น COUNT                                                                 |
| AS                 | keyword สำหรับตั้งชื่อ (alias) ให้กับคอลัมน์ที่คำนวณได้                                                      |
| HAVING             | clause สำหรับกำหนดเงื่อนไขกรองผลลัพธ์ที่ผ่านการ GROUP BY แล้วเท่านั้น (ต่างจาก WHERE ที่กรองทั้ง result set) |

---

## My Questions & Gaps

- [ ] GROUP BY สามารถจัดกลุ่มด้วยหลายคอลัมน์พร้อมกันได้หรือไม่ และผลลัพธ์จะเป็นอย่างไร
- [ ] นอกจาก COUNT ยังมี aggregate function อื่นที่ใช้ร่วมกับ GROUP BY ได้อีกหรือไม่ เช่น SUM, AVG, MAX, MIN
- [ ] สามารถใช้ทั้ง WHERE และ HAVING ในคำสั่งเดียวกันได้หรือไม่ และลำดับการทำงานเป็นอย่างไร

---

## Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมในวิดีโอนี้
