# Views

`Tags: RDBMS, PostgreSQL, views, materialized-views, pgAdmin`

| Field            | Value                                            |
| ---------------- | ------------------------------------------------ |
| **Certificate**  | IBM Data Engineering Professional Certificate    |
| **Course**       | C04 Introduction to Relational Databases (RDBMS) |
| **Module**       | M03 MySQL and PostgreSQL                         |
| **Lesson**       | L02 PostgreSQL                                   |
| **Date studied** | 2026-08-09                                       |

---

## Table of Contents

- [Overview](#overview)
- [What Is a View](#what-is-a-view)
- [Creating and Using a View in pgAdmin](#creating-and-using-a-view-in-pgadmin)
- [Materialized Views](#materialized-views)
- [Creating and Using a Materialized View in pgAdmin](#creating-and-using-a-materialized-view-in-pgadmin)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบาย views ใน PostgreSQL ซึ่งเป็นอีกวิธีหนึ่งในการนำเสนอข้อมูลจากตารางหรือ view อื่น ๆ ตั้งแต่นิยาม ประโยชน์ ไปจนถึงขั้นตอนสร้างและใช้งานผ่าน pgAdmin นอกจากนี้ยังเปรียบเทียบ regular view กับ materialized view ซึ่งเก็บผลลัพธ์ query ไว้ล่วงหน้าเพื่อเพิ่มประสิทธิภาพการ query ในอนาคต

---

## What Is a View

View คือวิธีการนำเสนอข้อมูล (alternative method of presenting information) ที่ดึงมาจากตารางเดียวหรือหลายตาราง หรือแม้แต่จาก view อื่นก็ได้ สามารถโต้ตอบกับ view ได้เหมือนกับตาราง เช่น insert, update, delete ข้อมูลได้ตามต้องการ

ประโยชน์ของ view มี 3 ข้อหลัก:

- **จำกัดการเข้าถึงข้อมูลที่ sensitive** — เช่น สร้าง view ที่รวมเฉพาะคอลัมน์ name และ email จากสองตาราง ทำให้ user เข้าถึงข้อมูลที่ต้องการได้โดยไม่ต้องรู้ว่าข้อมูลจริงถูกเก็บอยู่ในตารางไหน และไม่ต้องให้สิทธิ์เข้าถึงข้อมูล salary ที่ sensitive
- **ทำให้การดึงข้อมูลง่ายขึ้น** (simplifying data retrieval)
- **ลดการเข้าถึงตารางต้นทางโดยตรง** (reducing access to underlying tables)

---

## Creating and Using a View in pgAdmin

ขั้นตอนสร้าง view ใน pgAdmin เริ่มจากใน tree view ด้านซ้าย view จะถูกสร้างภายใต้ schema:

```mermaid
flowchart TD
    A[Right-click "Views" ใน schema] --> B[คลิก "Create"]
    B --> C[คลิก "View"]
    C --> D[ตั้งชื่อ view]
    D --> E[ไปที่ Code page แล้วใส่ SQL ที่นิยาม view]
    E --> F[คลิก "Save"]
    F --> G[View ปรากฏใน Views folder]
    G --> H[Right-click view name → View/Edit Data → All rows]
    H --> I[แสดงข้อมูลทุกแถวใน view]
```

หลังสร้างเสร็จ สามารถ expand view ใน tree view เพื่อดูคอลัมน์ที่รวมอยู่ภายในได้

---

## Materialized Views

PostgreSQL รองรับ view อีกประเภทหนึ่งคือ **materialized view** ซึ่งต่างจาก regular view ตรงที่เมื่อ refresh ครั้งแรก ผลลัพธ์ของ query (result set) จะถูก materialize หรือบันทึกเก็บไว้ใช้งานในอนาคต

ผลจากการ materialize มีทั้งข้อดีและข้อจำกัด:

| ประเด็น | Regular View | Materialized View |
| --- | --- | --- |
| การเก็บข้อมูล | ไม่เก็บผลลัพธ์ ดึงข้อมูลใหม่ทุกครั้งที่ query | เก็บผลลัพธ์ไว้ (มักอยู่ใน memory) |
| การแก้ไขข้อมูล | insert, update, delete ได้ | **query ได้อย่างเดียว** ไม่สามารถ update หรือ delete ได้ |
| ประสิทธิภาพ | ขึ้นกับ query ต้นทางทุกครั้ง | เร็วกว่าสำหรับการ query ซ้ำ เพราะผลลัพธ์พร้อมใช้งานอยู่แล้ว |
| ความสดของข้อมูล | ข้อมูลล่าสุดเสมอ | ต้อง refresh เองเพื่ออัปเดตข้อมูลจากตารางต้นทาง |

---

## Creating and Using a Materialized View in pgAdmin

ขั้นตอนคล้ายกับการสร้าง regular view แต่ต้องเริ่มจาก folder "Materialized Views" ใน view tree แทน:

1. Right-click ที่ folder "Materialized Views" แล้วสร้าง materialized view ใหม่
2. ตั้งชื่อ view บน definition page
3. ใส่ SQL code ที่นิยาม view (เช่น ตัวอย่างในวิดีโอที่ดึงเฉพาะคอลัมน์ employee ID และ salary จากตาราง `employee_details` เพื่อ anonymize ข้อมูล salary)
4. คลิก "Save" — materialized view จะถูกเพิ่มเข้า folder

เนื่องจาก materialized view เก็บข้อมูลไว้ ก่อนใช้งานต้อง **refresh** ก่อนเพื่อดึงแถวข้อมูลปัจจุบันเข้ามา จากนั้นจึงใช้ view เพื่อเข้าถึงข้อมูลได้ และสามารถ refresh ซ้ำได้ทุกเมื่อเพื่ออัปเดตข้อมูลให้ตรงกับตารางต้นทาง

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| View | วิธีนำเสนอข้อมูลจากตารางหรือ view อื่นหนึ่งตารางขึ้นไป โต้ตอบได้เหมือนตาราง (insert, update, delete) |
| Materialized view | View ที่ผลลัพธ์ query ถูกบันทึกเก็บไว้จริง (materialize) หลังการ refresh ครั้งแรก query ได้อย่างเดียว update/delete ไม่ได้ |
| Refresh (materialized view) | คำสั่งอัปเดตข้อมูลใน materialized view ให้ตรงกับข้อมูลปัจจุบันในตารางต้นทาง |
| Underlying table | ตารางต้นทางที่ view หรือ materialized view ดึงข้อมูลมา |
| Anonymize | การซ่อน/ตัดข้อมูลที่ sensitive ออกจาก result set เช่น การไม่รวมคอลัมน์ salary ที่ระบุตัวตนได้ง่าย |

---

## ❓ My Questions & Gaps

- [ ] Materialized view ต้อง refresh ด้วยตนเองทุกครั้ง หรือ PostgreSQL มีวิธี auto-refresh ตามรอบเวลาได้หรือไม่
- [ ] การสร้าง index บน materialized view ทำได้หรือไม่ และช่วยเพิ่มประสิทธิภาพอย่างไร
- [ ] ความแตกต่างด้านสิทธิ์การเข้าถึง (permissions) ระหว่าง regular view กับการให้สิทธิ์ตรงบนตารางต้นทาง

---

## 🔗 Resources

- [PostgreSQL Documentation — Views (CREATE VIEW)](https://www.postgresql.org/docs/current/sql-createview.html)
- [PostgreSQL Documentation — Materialized Views](https://www.postgresql.org/docs/current/rules-materializedviews.html)
