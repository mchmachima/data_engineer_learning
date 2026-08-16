# Views

`Tags: SQL, view, CREATE VIEW, DROP VIEW`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C05 Databases and SQL with Python         |
| **Module**        | M06 Advance SQL                           |
| **Lesson**        | L01 Views, Stored Procedures and Transactions |
| **Date studied**  | 2026-08-16                                |

---

## Table of Contents

- [Overview](#overview)
- [What a View Is](#what-a-view-is)
- [Why Use a View](#why-use-a-view)
- [Creating and Querying a View](#creating-and-querying-a-view)
- [Dropping a View](#dropping-a-view)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายเรื่อง view ซึ่งเป็นอีกวิธีหนึ่งในการเข้าถึงข้อมูลที่มีอยู่แล้วในหนึ่งหรือหลาย table โดย view ไม่ได้เก็บข้อมูลของตัวเอง แต่เก็บแค่ definition ของ query ที่ใช้สร้างมัน เนื้อหาครอบคลุมตั้งแต่ความหมายของ view เหตุผลที่ควรใช้ view ไปจนถึง syntax ของ CREATE VIEW และ DROP VIEW

---

## What a View Is

View คือมุมมองทางเลือกในการแสดงข้อมูลที่มีอยู่ในหนึ่งหรือหลาย table หรือ view อื่นอยู่แล้ว โดย view สามารถรวม column ทั้งหมดหรือบางส่วนจาก base table หรือ view ที่มีอยู่ก็ได้

เมื่อสร้าง view จะได้ named specification ของ results table ที่สามารถ query ได้เหมือน table ปกติ และยังสามารถรัน insert, update, delete ผ่าน view เพื่อเปลี่ยนแปลงข้อมูลใน base table ได้ด้วย

จุดสำคัญคือ เมื่อ define view แล้ว สิ่งที่ถูกเก็บไว้คือ definition ของ view เท่านั้น ส่วนข้อมูลจริงยังคงถูกเก็บอยู่ใน base table ไม่ใช่ใน view เอง

---

## Why Use a View

View มีประโยชน์หลายด้าน:

- แสดงข้อมูลเฉพาะบางส่วนของ table เพื่อซ่อนข้อมูล sensitive เช่น tax information, birth date, หรือ salary
- รวมข้อมูลจากหลาย table เข้าด้วยกันในรูปแบบที่มีความหมาย
- ลดความซับซ้อนในการเข้าถึงข้อมูล โดยให้สิทธิ์เข้าถึง view แทนที่จะให้สิทธิ์เข้าถึง underlying table โดยตรง
- แสดงเฉพาะส่วนของข้อมูลที่เกี่ยวข้องกับ process ที่ใช้ view นั้น

ตัวอย่างเช่น การสร้าง view ที่แสดงเฉพาะข้อมูลที่ไม่ sensitive จาก table Employees เช่น Employee ID, name, address, job ID, manager ID, department ID โดยไม่แสดง salary หรือ birthdate

---

## Creating and Querying a View

การสร้าง view ใช้คำสั่ง `CREATE VIEW` ตามด้วยชื่อ view (ยาวได้สูงสุด 128 ตัวอักษร) จากนั้นระบุ column ที่ต้องการรวมไว้ในวงเล็บ (สามารถตั้ง alias ให้ column ได้) แล้วใช้ `AS SELECT` เพื่อระบุ column และ `FROM` เพื่อระบุชื่อ base table สามารถเพิ่ม `WHERE` clause แบบ optional เพื่อกรองแถวที่ต้องการได้

View มีลักษณะ dynamic คือข้อมูลที่ได้จะเป็นผลลัพธ์จาก SELECT statement ที่ใช้สร้าง view นั้นเสมอ เมื่อนำ view ไปใช้ใน SQL statement อื่น จะทำงานเหมือนใช้ SELECT statement ที่คืนค่าเนื้อหาของ view นั้น

SELECT statement ที่ใช้สร้าง view สามารถอ้างอิงถึง view หรือ table อื่นได้ และสามารถใช้ `WHERE`, `GROUP BY`, `HAVING` ได้ แต่ **ห้ามใช้ `ORDER BY`** และห้ามอ้างอิง host variable

```sql
-- สร้าง view ชื่อ EMPINFO จาก table Employees โดยเลือกเฉพาะ column ที่ไม่ sensitive
CREATE VIEW EMPINFO (EMP_ID, F_NAME, L_NAME, ADDRESS, JOB_ID, MANAGER_ID, DEP_ID) AS
    SELECT EMP_ID, F_NAME, L_NAME, ADDRESS, JOB_ID, MANAGER_ID, DEP_ID
    FROM EMPLOYEES;

-- query ข้อมูลจาก view เหมือน query table ปกติ
SELECT * FROM EMPINFO;

-- สร้าง view ที่กรองเฉพาะแถวที่ MANAGER_ID เท่ากับ 30002 ด้วย WHERE clause
CREATE VIEW EMPINFO (EMP_ID, F_NAME, L_NAME, ADDRESS, JOB_ID, MANAGER_ID, DEP_ID) AS
    SELECT EMP_ID, F_NAME, L_NAME, ADDRESS, JOB_ID, MANAGER_ID, DEP_ID
    FROM EMPLOYEES
    WHERE MANAGER_ID = 30002;

-- ตรวจสอบว่า view กรองเฉพาะแถวที่ MANAGER_ID = 30002 จริง
SELECT * FROM EMPINFO;
```

---

## Dropping a View

หากต้องการลบ view ออกจากฐานข้อมูลทั้งหมด ใช้คำสั่ง `DROP VIEW`

```sql
-- ลบ view EMPINFO ออกจากฐานข้อมูล
DROP VIEW EMPINFO;
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| View | มุมมองทางเลือกในการเข้าถึงข้อมูลที่มีอยู่ใน table หรือ view อื่น เก็บแค่ definition ของ query ไม่ได้เก็บข้อมูลจริง |
| Base table | table ต้นฉบับที่ view ถูกสร้างขึ้นมาจากมัน |
| CREATE VIEW | คำสั่ง SQL สำหรับสร้าง view ใหม่จาก SELECT statement |
| DROP VIEW | คำสั่ง SQL สำหรับลบ view ออกจากฐานข้อมูล |
| Dynamic (ในบริบท view) | คุณสมบัติของ view ที่ข้อมูลจะเปลี่ยนไปตามผลลัพธ์ล่าสุดของ SELECT statement ที่ใช้สร้างมันเสมอ ไม่ใช่ข้อมูล snapshot ที่ตายตัว |

---

## ❓ My Questions & Gaps

- [ ] ทำไม view ถึงห้ามใช้ `ORDER BY` ใน definition — ต่างจากการ query view แล้วเติม `ORDER BY` ภายนอกอย่างไร
- [ ] การ insert/update/delete ผ่าน view ที่มาจากหลาย table (join) จะมีข้อจำกัดอะไรเพิ่มเติมหรือไม่
- [ ] view แบบ updatable กับ read-only ต่างกันอย่างไร มีเงื่อนไขอะไรที่ทำให้ view กลาย เป็น read-only

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมที่กล่าวถึงในวิดีโอนี้
