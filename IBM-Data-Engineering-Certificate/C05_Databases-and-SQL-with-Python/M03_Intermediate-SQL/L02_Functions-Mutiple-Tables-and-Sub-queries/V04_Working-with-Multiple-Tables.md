# Working with Multiple Tables

`Tags: SQL, multiple-tables, sub-queries, implicit-join, table-alias, full-join`

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
- [The EMPLOYEES and DEPARTMENTS Tables](#the-employees-and-departments-tables)
- [Accessing Multiple Tables with Sub-Queries](#accessing-multiple-tables-with-sub-queries)
- [Implicit Join via the FROM Clause](#implicit-join-via-the-from-clause)
- [Filtering the Implicit Join with WHERE](#filtering-the-implicit-join-with-where)
- [Table Aliases](#table-aliases)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้สอนวิธีเขียน query ที่เข้าถึงมากกว่าหนึ่งตารางพร้อมกัน โดยมี 3 วิธีหลัก ได้แก่ sub-query, implicit join, และ join operator (เช่น inner join, outer join) วิดีโอนี้เน้นสองวิธีแรกคือ sub-query และ implicit join ส่วน join operator จะอธิบายละเอียดในวิดีโอถัดไป โดยใช้ตาราง `employees` และ `departments` เป็นตัวอย่างประกอบการอธิบาย

---

## The EMPLOYEES and DEPARTMENTS Tables

ตาราง `employees` มีคอลัมน์ เช่น employee ID, first name, last name, salary ส่วนตาราง `departments` มีคอลัมน์ department ID, department name, manager ID, และ location ID

> ⚠️ ทรานสคริปต์ที่ paste มาไม่ได้แนบตารางข้อมูลตัวอย่างจริง (ในวิดีโอมีสไลด์แสดงข้อมูลแต่ไม่ได้ถูกแปลงเป็นข้อความ) ตารางด้านล่างเป็นข้อมูลตัวอย่างที่สร้างขึ้นเพื่อสาธิตผลลัพธ์ของแต่ละ query เท่านั้น ควรเทียบกับสไลด์จริงในวิดีโอเพื่อยืนยันชื่อคอลัมน์และค่าที่ถูกต้อง (ดู [My Questions & Gaps](#-my-questions--gaps))

**employees**

| EMP_ID | FIRST_NAME | LAST_NAME | SALARY | DEP_ID |
| ------ | ---------- | --------- | ------ | ------ |
| E1001  | John       | Smith     | 60000  | D01    |
| E1002  | Emma       | Johnson   | 70000  | D02    |
| E1003  | Michael    | Brown     | 80000  | D01    |
| E1004  | Sarah      | Davis     | 90000  | D03    |
| E1005  | David      | Wilson    | 70000  | D02    |
| E1006  | Laura      | Miller    | 80000  | D01    |

**departments**

| DEP_ID_DEP | DEP_NAME | MANAGER_ID | LOC_ID |
| ---------- | -------- | ---------- | ------ |
| D01        | Support  | 30001      | L0001  |
| D02        | Design   | 30002      | L0002  |
| D03        | Test     | 30003      | L0002  |

---

## Accessing Multiple Tables with Sub-Queries

การใช้ sub-query เพื่อเข้าถึงหลายตารางทำได้โดยให้ outer query อ้างอิงตารางหนึ่ง แล้วใช้ sub-query บนอีกตารางหนึ่งเพื่อกรองผลลัพธ์

```sql
-- ดึงพนักงานที่ Department ID ของเขาปรากฏอยู่ในตาราง departments จริง
SELECT * FROM employees
WHERE dep_id IN (SELECT dep_id_dep FROM departments);
```

| EMP_ID | FIRST_NAME | LAST_NAME | SALARY | DEP_ID |
| ------ | ---------- | --------- | ------ | ------ |
| E1001  | John       | Smith     | 60000  | D01    |
| E1002  | Emma       | Johnson   | 70000  | D02    |
| E1003  | Michael    | Brown     | 80000  | D01    |
| E1004  | Sarah      | Davis     | 90000  | D03    |
| E1005  | David      | Wilson    | 70000  | D02    |
| E1006  | Laura      | Miller    | 80000  | D01    |

> ในตัวอย่างนี้ dep_id ของพนักงานทุกคนตรงกับ dep_id_dep ที่มีอยู่ในตาราง departments อยู่แล้ว ผลลัพธ์จึงได้ทุกแถวเหมือนตาราง employees เดิม

ถ้าต้องการกรองตามที่ตั้ง (location) ซึ่งไม่มีอยู่ในตาราง `employees` โดยตรง แต่มีอยู่ในตาราง `departments` (คอลัมน์ location ID) ก็ใช้ sub-query จาก `departments` เป็น input ให้ query บน `employees` ได้

```sql
-- ดึงพนักงานที่สังกัดแผนกซึ่งตั้งอยู่ที่ location L0002
SELECT * FROM employees
WHERE dep_id IN (SELECT dep_id_dep FROM departments WHERE loc_id = 'L0002');
```

| EMP_ID | FIRST_NAME | LAST_NAME | SALARY | DEP_ID |
| ------ | ---------- | --------- | ------ | ------ |
| E1002  | Emma       | Johnson   | 70000  | D02    |
| E1005  | David      | Wilson    | 70000  | D02    |

> เฉพาะแผนก D02 (Design) เท่านั้นที่ตั้งอยู่ที่ location L0002 พนักงานที่เหลือจึงถูกกรองออก

อีกตัวอย่างคือดึงรหัสและชื่อแผนกของพนักงานที่มีเงินเดือนมากกว่า 70,000 โดยต้องใช้ sub-query บนตาราง `employees` เพื่อกรองเงื่อนไขเงินเดือนก่อน แล้วนำผลลัพธ์ไปเป็น input ให้ outer query บนตาราง `departments`

```sql
-- ดึง department ID และ department name ของแผนกที่มีพนักงานเงินเดือนมากกว่า 70,000
SELECT dep_id_dep, dep_name FROM departments
WHERE dep_id_dep IN (SELECT dep_id FROM employees WHERE salary > 70000);
```

| DEP_ID_DEP | DEP_NAME |
| ---------- | -------- |
| D01        | Support  |
| D03        | Test     |

> พนักงานที่เงินเดือนมากกว่า 70,000 สังกัดแผนก D01 และ D03 เท่านั้น จึงเหลือแค่สองแผนกนี้ในผลลัพธ์

---

## Implicit Join via the FROM Clause

นอกจาก sub-query แล้ว ยังเข้าถึงหลายตารางได้โดยระบุหลายตารางไว้ใน `FROM` clause พร้อมกัน วิธีนี้ทำให้เกิด table join แต่ไม่ได้ใช้ join operator อย่างชัดเจน (implicit join)

```sql
-- full join ระหว่าง employees และ departments — ทุกแถวของตารางหนึ่งจับคู่กับทุกแถวของอีกตารางหนึ่ง
SELECT * FROM employees, departments;
```

| EMP_ID | FIRST_NAME | DEP_ID | DEP_ID_DEP | DEP_NAME |
| ------ | ---------- | ------ | ---------- | -------- |
| E1001  | John       | D01    | D01        | Support  |
| E1001  | John       | D01    | D02        | Design   |
| E1001  | John       | D01    | D03        | Test     |
| E1002  | Emma       | D02    | D01        | Support  |
| E1002  | Emma       | D02    | D02        | Design   |
| ...    | ...        | ...    | ...        | ...      |

> ตารางข้างต้นแสดงเพียงบางแถวเป็นตัวอย่าง (ตัดคอลัมน์ LAST_NAME, SALARY, MANAGER_ID, LOC_ID ออกเพื่อความกระชับ) ผลลัพธ์เต็มมี 6 แถว (employees) × 3 แถว (departments) = 18 แถว เพราะพนักงานทุกคนถูกจับคู่กับทุกแผนก ไม่ใช่แค่แผนกของตัวเอง

ผลลัพธ์ที่ได้เรียกว่า **full join** เพราะทุกแถวในตารางแรกถูกจับคู่กับทุกแถวในตารางที่สอง ทำให้จำนวนแถวในผลลัพธ์มากกว่าจำนวนแถวของทั้งสองตารางรวมกันเมื่อพิจารณาแบบตารางเดียว (จริงๆ คือ จำนวนแถวตาราง 1 × จำนวนแถวตาราง 2)

---

## Filtering the Implicit Join with WHERE

เพื่อจำกัดผลลัพธ์ของ full join ให้เหลือเฉพาะแถวที่มี department ID ตรงกัน จะเพิ่มเงื่อนไขใน `WHERE` clause โดยต้อง fully qualify ชื่อคอลัมน์ด้วยชื่อตาราง (table.column) เพราะบางตารางอาจมีชื่อคอลัมน์ซ้ำกัน

```sql
-- จำกัด full join ให้เหลือเฉพาะแถวที่ department ID ของทั้งสองตารางตรงกัน
SELECT * FROM employees, departments
WHERE employees.dep_id = departments.dep_id_dep;
```

| EMP_ID | FIRST_NAME | LAST_NAME | SALARY | DEP_ID | DEP_ID_DEP | DEP_NAME | MANAGER_ID | LOC_ID |
| ------ | ---------- | --------- | ------ | ------ | ---------- | -------- | ---------- | ------ |
| E1001  | John       | Smith     | 60000  | D01    | D01        | Support  | 30001      | L0001  |
| E1002  | Emma       | Johnson   | 70000  | D02    | D02        | Design   | 30002      | L0002  |
| E1003  | Michael    | Brown     | 80000  | D01    | D01        | Support  | 30001      | L0001  |
| E1004  | Sarah      | Davis     | 90000  | D03    | D03        | Test     | 30003      | L0002  |
| E1005  | David      | Wilson    | 70000  | D02    | D02        | Design   | 30002      | L0002  |
| E1006  | Laura      | Miller    | 80000  | D01    | D01        | Support  | 30001      | L0001  |

> เมื่อเทียบกับ full join ก่อนหน้า เงื่อนไข `WHERE` ตัดจาก 18 แถวเหลือเพียง 6 แถว คือเฉพาะคู่ที่ department ID ของพนักงานตรงกับ department ID ของแผนกจริงเท่านั้น

---

## Table Aliases

เนื่องจากชื่อตารางบางครั้งยาว จึงใช้ alias (ชื่อย่อ) แทนชื่อตารางเต็มได้ ทั้งใน `WHERE` clause และในรายการคอลัมน์ที่ select

```sql
-- ใช้ alias E แทน employees และ D แทน departments
SELECT * FROM employees E, departments D
WHERE E.dep_id = D.dep_id_dep;
```

> ผลลัพธ์เหมือนกับตัวอย่างในหัวข้อก่อนหน้าทุกประการ (6 แถว) เพราะ alias เป็นเพียงชื่อย่อของตารางเดิม ไม่เปลี่ยนตรรกะของ query

```sql
-- ดึง employee ID พร้อมชื่อแผนกของแต่ละพนักงาน โดยใช้ alias ทั้งใน SELECT และ WHERE
SELECT E.emp_id, D.dep_name FROM employees E, departments D
WHERE E.dep_id = D.dep_id_dep;
```

| EMP_ID | DEP_NAME |
| ------ | -------- |
| E1001  | Support  |
| E1002  | Design   |
| E1003  | Support  |
| E1004  | Test     |
| E1005  | Design   |
| E1006  | Support  |

> ตัวอย่างนี้เลือกเฉพาะคอลัมน์ emp_id (จาก alias E) และ dep_name (จาก alias D) แทนการ select ทุกคอลัมน์ด้วย `*`

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Sub-query | query ที่ซ้อนอยู่ในอีก query หนึ่ง ใช้เป็นตัวกรอง (filter) หรือ input ให้ outer query เมื่อทำงานข้ามตาราง |
| Implicit join | การ join ตารางโดยระบุหลายตารางไว้ใน `FROM` clause พร้อมกัน โดยไม่ใช้ join operator อย่าง `JOIN` ชัดเจน |
| Full join | ผลลัพธ์ของ implicit join ที่ยังไม่มีเงื่อนไขกรอง ทำให้ทุกแถวของตารางหนึ่งจับคู่กับทุกแถวของอีกตารางหนึ่ง |
| Fully qualified column name | การระบุชื่อคอลัมน์โดยมี prefix เป็นชื่อตาราง (เช่น `employees.dep_id`) เพื่อไม่ให้กำกวมเมื่อหลายตารางมีชื่อคอลัมน์ซ้ำกัน |
| Table alias | ชื่อย่อที่ตั้งให้กับตารางในคำสั่ง SQL เพื่อใช้แทนชื่อตารางเต็มที่อาจยาวเกินไป |
| Join operator | คำสั่งเช่น `INNER JOIN`, `OUTER JOIN` ที่ใช้ join ตารางอย่างชัดเจน (จะอธิบายในวิดีโอถัดไป) |

---

## ❓ My Questions & Gaps

- [ ] ตารางข้อมูล employees และ departments ในโน้ตนี้เป็นข้อมูลตัวอย่างที่สร้างขึ้นเอง (ไม่ได้อยู่ในทรานสคริปต์ที่ paste มา) — ควรเทียบกับสไลด์จริงในวิดีโอเพื่อยืนยันว่าค่าคอลัมน์และผลลัพธ์ของแต่ละ query ตรงกับของจริง
- [ ] วิดีโอกล่าวถึง join operator (inner join, outer join) ว่าจะอธิบายในวิดีโอถัดไป — ควรตามไปดูว่า implicit join กับ explicit `JOIN` ให้ผลลัพธ์เหมือนกันหรือต่างกันอย่างไรในเชิง performance และ readability
- [ ] ยังไม่ชัดเจนว่า full join แบบ implicit (ไม่มี WHERE กรอง) ต่างจาก `CROSS JOIN` แบบ explicit หรือไม่

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารเพิ่มเติมที่กล่าวถึงในวิดีโอนี้
