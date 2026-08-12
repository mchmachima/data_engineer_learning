# Built-in DB Functions

`Tags: SQL, aggregate-functions, scalar-functions, string-functions`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C05 Databases-and-SQL-with-Python         |
| **Module**        | M03 Intermediate-SQL                      |
| **Lesson**        | L02 Functions-Mutiple-Tables-and-Sub-queries |
| **Date studied**  | 2026-08-12                                |

---

## Table of Contents

- [Overview](#overview)
- [Why Use Built-in Functions](#why-use-built-in-functions)
- [The PETRESCUE Table](#the-petrescue-table)
- [Aggregate (Column) Functions](#aggregate-column-functions)
- [Scalar and String Functions](#scalar-and-string-functions)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้พูดถึงฟังก์ชันที่มากับ database โดยตรง (built-in functions) ซึ่งช่วยให้เราประมวลผลข้อมูลได้ตั้งแต่อยู่ใน database เลย แทนที่จะดึงข้อมูลทั้งหมดออกมาประมวลผลใน application ก่อน ทำให้ลด network traffic และเร็วขึ้นเมื่อข้อมูลมีขนาดใหญ่ บทเรียนนี้ใช้ตาราง PETRESCUE เป็นตัวอย่างเพื่อสาธิต aggregate functions (เช่น SUM, MIN, MAX, AVG) และ scalar/string functions (เช่น ROUND, LENGTH, UPPER, LOWER)

---

## Why Use Built-in Functions

การใช้ built-in functions ของ database มีข้อดีคือลดปริมาณข้อมูลที่ต้องดึงออกจาก database ลดการใช้ bandwidth และ network traffic และมักจะเร็วกว่าการดึงข้อมูลทั้งหมดมาประมวลผลใน application เมื่อข้อมูลมีขนาดใหญ่ นอกจากนี้ database ยังรองรับการสร้าง user-defined function ได้เองด้วย แต่เป็นหัวข้อขั้นสูงที่ไม่ได้ลงรายละเอียดในบทเรียนนี้

---

## The PETRESCUE Table

ตัวอย่างในบทเรียนใช้ตาราง `PETRESCUE` ของหน่วยงานช่วยเหลือสัตว์ ซึ่งเก็บข้อมูลธุรกรรมการช่วยเหลือสัตว์ ประกอบด้วยคอลัมน์ ID, ANIMAL, QUANTITY, COST, และ RESCUEDATE

> ⚠️ ทรานสคริปต์ที่ paste มาไม่ได้แนบตารางข้อมูลจริง (ในวิดีโอมีสไลด์แสดงข้อมูลแต่ไม่ได้ถูกแปลงเป็นข้อความ) ตารางด้านล่างเป็นชุดข้อมูลมาตรฐานที่ใช้ในบทเรียนนี้ของ IBM course — ใช้เพื่อคำนวณผลลัพธ์ตัวอย่างประกอบแต่ละ query ควรเทียบกับสไลด์จริงของคุณเพื่อยืนยันความถูกต้อง (ดู [My Questions & Gaps](#-my-questions--gaps))

| ID  | ANIMAL | QUANTITY | COST | RESCUEDATE |
| --- | ------ | -------- | ---- | ---------- |
| 1   | Cat    | 9        | 450  | 2018-05-29 |
| 2   | Dog    | 3        | 666  | 2018-06-01 |
| 3   | Dog    | 3        | 100  | 2018-06-04 |
| 4   | Parrot | 2        | 50   | 2018-06-04 |
| 5   | Dog    | 1        | 75   | 2018-06-10 |
| 6   | Cat    | 6        | 600  | 2018-06-11 |
| 7   | Parrot | 1        | 200  | 2018-06-11 |
| 8   | Dog    | 2        | 100  | 2018-06-12 |
| 9   | Cat    | 1        | 45   | 2018-06-13 |
| 10  | Dog    | 1        | 150  | 2018-06-15 |

---

## Aggregate (Column) Functions

Aggregate function (หรือ column function) รับค่าชุดหนึ่งจากคอลัมน์เป็น input แล้วคืนค่าเดียว (หรือ null) กลับมา ตัวอย่างเช่น SUM, MIN, MAX, AVG

| Function | ใช้ทำอะไร |
| -------- | ---------- |
| SUM      | รวมค่าทั้งหมดในคอลัมน์ |
| MIN      | หาค่าต่ำสุด |
| MAX      | หาค่าสูงสุด |
| AVG      | หาค่าเฉลี่ย |

ตัวคอลัมน์ที่ได้จาก aggregate function จะถูกตั้งชื่อ default เป็นหมายเลขคอลัมน์ แต่สามารถตั้งชื่อเองได้ด้วย `AS`

```sql
-- รวมค่า COST ทั้งหมด
SELECT SUM(COST) FROM PETRESCUE;
```

| 1    |
| ---- |
| 2436 |

```sql
-- รวมค่า COST ทั้งหมด และตั้งชื่อคอลัมน์ผลลัพธ์เป็น SUM_OF_COST
SELECT SUM(COST) AS SUM_OF_COST FROM PETRESCUE;
```

| SUM_OF_COST |
| ----------- |
| 2436        |

```sql
-- หาจำนวนสัตว์สูงสุดที่ถูกช่วยเหลือในธุรกรรมเดียว
SELECT MAX(QUANTITY) FROM PETRESCUE;
```

| 1   |
| --- |
| 9   |

Aggregate function สามารถใช้กับข้อมูลบางส่วน (subset) ได้ ไม่จำเป็นต้องเป็นทั้งคอลัมน์ โดยใช้ร่วมกับ `WHERE`

```sql
-- หาค่า ID ต่ำสุดของแถวที่เป็นสุนัข (Dog)
SELECT MIN(ID) FROM PETRESCUE WHERE ANIMAL = 'Dog';
```

| 1   |
| --- |
| 2   |

```sql
-- หาค่าเฉลี่ยของ COST ทั้งหมด
SELECT AVG(COST) FROM PETRESCUE;
```

| 1     |
| ----- |
| 243.6 |

สามารถทำ mathematical operation ระหว่างคอลัมน์ก่อน แล้วค่อยใส่ aggregate function ครอบอีกทีได้

```sql
-- หาค่าเฉลี่ยต้นทุนต่อตัวของสุนัข (cost หารด้วย quantity ก่อน แล้วค่อยเฉลี่ย)
SELECT AVG(COST / QUANTITY) FROM PETRESCUE WHERE ANIMAL = 'Dog';
```

| 1              |
| -------------- |
| 106.07 (ประมาณ) |

---

## Scalar and String Functions

Scalar function ทำงานกับค่าแต่ละค่า (individual value) ไม่ใช่ทั้งคอลัมน์เหมือน aggregate function เช่น การปัดเศษตัวเลข ส่วน string function เป็น scalar function ประเภทหนึ่งที่ทำงานกับค่าประเภท char/varchar

```sql
-- ปัดเศษค่า COST ของทุกแถวให้เป็นจำนวนเต็มที่ใกล้ที่สุด
SELECT ROUND(COST) FROM PETRESCUE;
```

| 1   |
| --- |
| 450 |
| 666 |
| 100 |
| 50  |
| 75  |
| 600 |
| 200 |
| 100 |
| 45  |
| 150 |

> ในชุดข้อมูลนี้ COST เป็นจำนวนเต็มอยู่แล้ว ROUND จึงไม่เปลี่ยนค่า

```sql
-- หาความยาวของ string ในคอลัมน์ ANIMAL แต่ละแถว
SELECT LENGTH(ANIMAL) FROM PETRESCUE;
```

| ANIMAL | 1   |
| ------ | --- |
| Cat    | 3   |
| Dog    | 3   |
| Dog    | 3   |
| Parrot | 6   |
| Dog    | 3   |
| Cat    | 3   |
| Parrot | 6   |
| Dog    | 3   |
| Cat    | 3   |
| Dog    | 3   |

```sql
-- แปลงค่าคอลัมน์ ANIMAL ทั้งหมดเป็นตัวพิมพ์ใหญ่
SELECT UPPER(ANIMAL) FROM PETRESCUE;
```

| 1      |
| ------ |
| CAT    |
| DOG    |
| DOG    |
| PARROT |
| DOG    |
| CAT    |
| PARROT |
| DOG    |
| CAT    |
| DOG    |

Scalar function ยังใช้ใน `WHERE` clause ได้ ซึ่งมีประโยชน์เมื่อไม่แน่ใจว่าข้อมูลในตารางถูกเก็บเป็นตัวพิมพ์ใหญ่ เล็ก หรือผสมกัน

```sql
-- ดึงทุกแถวที่ค่า ANIMAL แปลงเป็นตัวพิมพ์เล็กแล้วเท่ากับ 'cat'
SELECT * FROM PETRESCUE WHERE LOWER(ANIMAL) = 'cat';
```

| ID  | ANIMAL | QUANTITY | COST | RESCUEDATE |
| --- | ------ | -------- | ---- | ---------- |
| 1   | Cat    | 9        | 450  | 2018-05-29 |
| 6   | Cat    | 6        | 600  | 2018-06-11 |
| 9   | Cat    | 1        | 45   | 2018-06-13 |

สามารถใช้ function ซ้อน function ได้ เช่น การใช้ `DISTINCT` ครอบ `UPPER` เพื่อหาค่าที่ไม่ซ้ำกัน

```sql
-- หาค่าที่ไม่ซ้ำกันของคอลัมน์ ANIMAL ในรูปแบบตัวพิมพ์ใหญ่
SELECT DISTINCT(UPPER(ANIMAL)) FROM PETRESCUE;
```

| 1      |
| ------ |
| CAT    |
| DOG    |
| PARROT |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Built-in function | ฟังก์ชันที่มากับ database engine โดยตรง ใช้ประมวลผลข้อมูลภายใน database ได้เลยโดยไม่ต้องดึงข้อมูลออกมาก่อน |
| User-defined function | ฟังก์ชันที่ผู้ใช้สร้างขึ้นเองใน database (หัวข้อขั้นสูง ไม่ได้ลงรายละเอียดในบทเรียนนี้) |
| Aggregate function (Column function) | ฟังก์ชันที่รับค่าชุดหนึ่งจากคอลัมน์เป็น input แล้วคืนค่าเดียว (หรือ null) เช่น SUM, MIN, MAX, AVG |
| Scalar function | ฟังก์ชันที่ทำงานกับค่าแต่ละค่า (individual value) ไม่ใช่ทั้งชุดข้อมูล |
| String function | scalar function ประเภทหนึ่งที่ทำงานกับค่า char/varchar เช่น LENGTH, UPPER, LOWER |
| `AS` | keyword ใช้ตั้งชื่อ (alias) ให้คอลัมน์ผลลัพธ์ |
| `DISTINCT` | keyword ใช้กรองค่าที่ซ้ำกันออก ให้เหลือแต่ค่าที่ไม่ซ้ำ |

---

## ❓ My Questions & Gaps

- [ ] ตารางข้อมูล PETRESCUE ในโน้ตนี้ดึงมาจากชุดข้อมูลมาตรฐานของ IBM course (ไม่ได้อยู่ในทรานสคริปต์ที่ paste มา) — ควรเทียบกับสไลด์จริงในวิดีโอเพื่อยืนยันว่าค่าตรงกัน โดยเฉพาะผลลัพธ์ของ SUM, AVG, MIN ที่คำนวณจากตารางนี้
- [ ] ฟังก์ชัน `UPPER`/`LOWER` ในทรานสคริปต์เรียกว่า UPPERCASE/LOWERCASE — ควรตรวจสอบว่า database ที่ใช้จริง (เช่น Db2, PostgreSQL) รองรับชื่อฟังก์ชันแบบไหนบ้าง เพราะ syntax อาจต่างกันในแต่ละ database

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารเพิ่มเติมที่กล่าวถึงในวิดีโอนี้
