# Sub-Queries and Nested Selects

`Tags: SQL, subqueries, nested-select, aggregate-functions, derived-tables`

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
- [The EMPLOYEES Table](#the-employees-table)
- [Why Sub-Queries: The Aggregate Function Problem](#why-sub-queries-the-aggregate-function-problem)
- [Sub-Query in the WHERE Clause](#sub-query-in-the-where-clause)
- [Sub-Query as a Column Expression](#sub-query-as-a-column-expression)
- [Sub-Query in the FROM Clause (Derived Tables)](#sub-query-in-the-from-clause-derived-tables)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้สอนการเขียน sub-query (หรือ nested select) ซึ่งคือ query ที่ซ้อนอยู่ภายใน query อีกอันหนึ่งโดยใช้วงเล็บครอบ ช่วยให้เขียน query ที่ซับซ้อนและทรงพลังกว่าเดิมได้ โดยเฉพาะการแก้ปัญหาข้อจำกัดของ aggregate function ที่ใช้ตรงๆ ใน `WHERE` clause ไม่ได้ วิดีโอนี้ครอบคลุม 3 ตำแหน่งที่ใส่ sub-query ได้ ได้แก่ ใน `WHERE` clause, ในรายการคอลัมน์ที่ select (Column Expression), และใน `FROM` clause (Derived Table) โดยใช้ตาราง `employees` เป็นตัวอย่าง

---

## The EMPLOYEES Table

ตัวอย่างในบทเรียนใช้ตาราง `employees` ต่อเนื่องมาจากวิดีโอก่อนหน้า (V01/V02) ซึ่งมีคอลัมน์ employee ID, first name, last name, salary เป็นต้น

> ⚠️ ทรานสคริปต์ที่ paste มาไม่ได้แนบตารางข้อมูลจริง (ในวิดีโอมีสไลด์แสดงข้อมูลแต่ไม่ได้ถูกแปลงเป็นข้อความ) ตารางด้านล่างเป็นข้อมูลตัวอย่างที่สร้างขึ้นเพื่อสาธิตผลลัพธ์ของแต่ละ query เท่านั้น ควรเทียบกับสไลด์จริงในวิดีโอเพื่อยืนยันค่าที่ถูกต้อง (ดู [My Questions & Gaps](#-my-questions--gaps))

| EMP_ID | FIRST_NAME | LAST_NAME | SALARY | DEP_ID |
| ------ | ---------- | --------- | ------ | ------ |
| E1001  | John       | Smith     | 60000  | D01    |
| E1002  | Emma       | Johnson   | 70000  | D02    |
| E1003  | Michael    | Brown     | 80000  | D01    |
| E1004  | Sarah      | Davis     | 90000  | D03    |
| E1005  | David      | Wilson    | 70000  | D02    |
| E1006  | Laura      | Miller    | 80000  | D01    |

---

## Why Sub-Queries: The Aggregate Function Problem

ปัญหาเริ่มต้นคือถ้าต้องการดึงพนักงานที่มีเงินเดือนมากกว่าค่าเฉลี่ย จะเขียน aggregate function อย่าง `AVG()` ตรงๆ ใน `WHERE` clause ไม่ได้ เพราะ built-in aggregate function มีข้อจำกัดว่าไม่สามารถ evaluate ใน `WHERE` clause ได้โดยตรง

```sql
-- วิธีนี้ผิด: ใช้ AVG() ตรงๆ ใน WHERE clause จะทำให้เกิด error "invalid use of aggregate function"
SELECT * FROM employees WHERE salary > AVG(salary);
```

Sub-query คือทางออก โดยการนำ query ที่คำนวณค่าเฉลี่ยไปซ้อนไว้ในวงเล็บแทน

---

## Sub-Query in the WHERE Clause

วิธีแก้ปัญหาด้านบนคือใส่ sub-select ที่คำนวณ `AVG(salary)` ไว้ในวงเล็บภายใน `WHERE` clause แทนการเรียก aggregate function ตรงๆ

```sql
-- ดึงพนักงานที่เงินเดือนน้อยกว่าค่าเฉลี่ยเงินเดือนของพนักงานทั้งหมด
SELECT employee_id, first_name, last_name, salary
FROM employees
WHERE salary < (SELECT AVG(salary) FROM employees);
```

| EMP_ID | FIRST_NAME | LAST_NAME | SALARY |
| ------ | ---------- | --------- | ------ |
| E1001  | John       | Smith     | 60000  |
| E1002  | Emma       | Johnson   | 70000  |
| E1005  | David      | Wilson    | 70000  |

> ค่าเฉลี่ยเงินเดือน (`AVG(salary)`) จากตาราง EMPLOYEES ตัวอย่างคือ 75000 จึงเหลือเฉพาะแถวที่ SALARY น้อยกว่า 75000

sub-query ส่วนใน `AVG(salary)` จะถูกประมวลผลก่อน ได้ค่าเฉลี่ยออกมาเป็นตัวเลขค่าเดียว แล้วนำไปเทียบกับ `salary` ของแต่ละแถวใน outer query

---

## Sub-Query as a Column Expression

Sub-query ไม่จำเป็นต้องอยู่ใน `WHERE` clause เท่านั้น ยังใส่ในรายการคอลัมน์ที่ select ได้ด้วย เรียกว่า **Column Expression** ตัวอย่างเช่น ถ้าต้องการเทียบเงินเดือนของแต่ละพนักงานกับค่าเฉลี่ย การเขียน `AVG(salary) AS average_salary` ตรงๆ ในรายการคอลัมน์ (โดยไม่มี `GROUP BY`) จะเกิด error เพราะต้องมี `GROUP BY` clause กำกับ

```sql
-- วิธีนี้ผิด: จะเกิด error เพราะไม่มี GROUP BY clause
SELECT employee_id, salary, AVG(salary) AS average_salary FROM employees;
```

การแก้ไขคือนำ `AVG(salary)` ไปไว้ในวงเล็บเป็น sub-query แทน

```sql
-- แสดงเงินเดือนของแต่ละพนักงานเทียบกับค่าเฉลี่ยเงินเดือนทั้งหมด โดยไม่ต้องใช้ GROUP BY
SELECT employee_id, salary,
    (SELECT AVG(salary) FROM employees) AS average_salary
FROM employees;
```

| EMP_ID | SALARY | AVERAGE_SALARY |
| ------ | ------ | --------------- |
| E1001  | 60000  | 75000           |
| E1002  | 70000  | 75000           |
| E1003  | 80000  | 75000           |
| E1004  | 90000  | 75000           |
| E1005  | 70000  | 75000           |
| E1006  | 80000  | 75000           |

> คอลัมน์ AVERAGE_SALARY เป็นค่าเดียวกันทุกแถว (75000) เพราะ sub-query คำนวณค่าเฉลี่ยจากทั้งตาราง แล้วนำมาแปะซ้ำในทุกแถวของ outer query

---

## Sub-Query in the FROM Clause (Derived Tables)

Sub-query ยังใส่ใน `FROM` clause ได้ด้วย โดย outer query จะใช้ผลลัพธ์ของ sub-query เป็นแหล่งข้อมูล (data source) แทนการอ้างถึงตารางจริงโดยตรง sub-query แบบนี้เรียกว่า **Derived Table** หรือ **Table Expression**

```sql
-- สร้าง derived table ที่มีเฉพาะข้อมูลพนักงานที่ไม่ sensitive (ไม่รวม date of birth และ salary)
SELECT * FROM
    (SELECT employee_id, first_name, last_name, department_id FROM employees) AS employee_for_all;
```

| EMP_ID | FIRST_NAME | LAST_NAME | DEP_ID |
| ------ | ---------- | --------- | ------ |
| E1001  | John       | Smith     | D01    |
| E1002  | Emma       | Johnson   | D02    |
| E1003  | Michael    | Brown     | D01    |
| E1004  | Sarah      | Davis     | D03    |
| E1005  | David      | Wilson    | D02    |
| E1006  | Laura      | Miller    | D01    |

> ผลลัพธ์ไม่มีคอลัมน์ SALARY เพราะ derived table (sub-query ใน FROM clause) ไม่ได้ select คอลัมน์นั้นมาตั้งแต่ต้น

ตัวอย่างนี้เป็นตัวอย่างง่ายๆ ที่จริงแล้วสามารถเลือกคอลัมน์ใน outer query ตรงๆ ได้เลยโดยไม่ต้องใช้ derived table แต่เทคนิคนี้จะมีประโยชน์มากขึ้นในสถานการณ์ที่ซับซ้อนกว่า เช่น การทำงานกับหลายตารางและการทำ join

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Sub-query (Nested query / Sub-select) | query ที่ซ้อนอยู่ภายใน query อีกอันหนึ่ง โดยครอบด้วยวงเล็บ |
| Aggregate function | ฟังก์ชันที่คำนวณค่าจากหลายแถวรวมเป็นค่าเดียว เช่น `AVG()`, `SUM()` มีข้อจำกัดว่าใช้ตรงๆ ใน `WHERE` clause ไม่ได้ |
| Column Expression | sub-query ที่วางอยู่ในรายการคอลัมน์ที่ select |
| Derived Table (Table Expression) | sub-query ที่วางอยู่ใน `FROM` clause ซึ่ง outer query จะใช้ผลลัพธ์เป็นแหล่งข้อมูล |
| Outer query | query หลักที่ครอบ sub-query ไว้ |

---

## ❓ My Questions & Gaps

- [ ] ตารางข้อมูล EMPLOYEES ในโน้ตนี้เป็นข้อมูลตัวอย่างที่สร้างขึ้นเอง (ไม่ได้อยู่ในทรานสคริปต์ที่ paste มา) — ควรเทียบกับสไลด์จริงในวิดีโอเพื่อยืนยันว่าค่า EMP_ID, ชื่อ, และ SALARY ตรงกับของจริง โดยเฉพาะผลลัพธ์ของ query ที่เทียบกับค่าเฉลี่ยเงินเดือน
- [ ] Sub-query แบบ correlated (ที่อ้างอิงคอลัมน์จาก outer query) ยังไม่ได้พูดถึงในวิดีโอนี้ — ควรตามไปดูว่าต่างจาก sub-query ธรรมดาที่เห็นในวิดีโอนี้อย่างไร
- [ ] Derived table ในตัวอย่างนี้ยังไม่ได้แสดงร่วมกับ `JOIN` — ควรลองดูตัวอย่างที่ใช้ derived table ร่วมกับหลายตารางตามที่วิดีโอกล่าวถึงว่า "มีประโยชน์มากขึ้น"

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารเพิ่มเติมที่กล่าวถึงในวิดีโอนี้
