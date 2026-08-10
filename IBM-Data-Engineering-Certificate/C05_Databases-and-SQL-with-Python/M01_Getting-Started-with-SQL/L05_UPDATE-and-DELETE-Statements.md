# UPDATE and DELETE Statements

`Tags: SQL, UPDATE, DELETE, DML`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C05 Databases and SQL for Data Science with Python |
| **Module**        | M01 Getting Started with SQL              |
| **Lesson**        | L05 UPDATE and DELETE Statements          |
| **Date studied**  | 2026-08-10                                |

---

## Table of Contents

- [Overview](#overview)
- [UPDATE Statement](#update-statement)
- [DELETE Statement](#delete-statement)
- [Importance of the WHERE Clause](#importance-of-the-where-clause)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้สอนเรื่องการแก้ไข (alter) และลบ (delete) ข้อมูลในตารางที่มีข้อมูลอยู่แล้ว ด้วยคำสั่ง UPDATE และ DELETE ซึ่งเป็น DML statement เช่นเดียวกับ SELECT และ INSERT พร้อมทั้งเน้นย้ำความสำคัญของ WHERE clause ในทั้งสองคำสั่งนี้ เพราะถ้าไม่ระบุ WHERE clause จะส่งผลกระทบต่อทุกแถวในตาราง

---

## UPDATE Statement

หลังจากสร้างตารางและเติมข้อมูลแล้ว ข้อมูลในตารางสามารถถูกแก้ไขได้ด้วยคำสั่ง UPDATE ซึ่งเป็นหนึ่งใน DML statement syntax ของ UPDATE ประกอบด้วย table name, คอลัมน์ที่จะเปลี่ยนค่าใน SET clause, และเงื่อนไขใน WHERE clause ที่ระบุว่าจะแก้ไขแถวไหน

```sql
-- General syntax of the UPDATE statement
UPDATE table_name
SET column_name = value
WHERE condition;
```

ตัวอย่าง: เปลี่ยนชื่อ-นามสกุลของ author ที่มี AUTHOR_ID เท่ากับ A2 จาก Rav Ahuja เป็น Lakshmi Katta

```sql
-- Update the first name and last name for AUTHOR_ID A2
UPDATE AUTHOR
SET LASTNAME = 'KATTA', FIRSTNAME = 'LAKSHMI'
WHERE AUTHOR_ID = 'A2';
```

---

## DELETE Statement

เมื่อต้องการลบแถวหนึ่งแถวหรือมากกว่าออกจากตาราง ใช้คำสั่ง DELETE ซึ่งเป็น DML statement เช่นกัน syntax ประกอบด้วย table name และ WHERE clause ที่ระบุแถวที่จะถูกลบ

```sql
-- General syntax of the DELETE statement
DELETE FROM table_name
WHERE condition;
```

ตัวอย่าง: ลบแถวของ author ที่มี AUTHOR_ID เท่ากับ A2 และ A3

```sql
-- Delete rows for AUTHOR_ID A2 and A3
DELETE FROM AUTHOR
WHERE AUTHOR_ID IN ('A2', 'A3');
```

---

## Importance of the WHERE Clause

WHERE clause สำคัญมากทั้งใน UPDATE และ DELETE เพราะเป็นตัวกำหนดว่าคำสั่งจะมีผลกับแถวไหนบ้าง ถ้าไม่ระบุ WHERE clause คำสั่งนั้นจะมีผลกับ **ทุกแถว** ในตาราง

| Statement | ไม่มี WHERE clause |
| --------- | ------------------- |
| UPDATE | ทุกแถวในตารางจะถูกเปลี่ยนค่าตาม SET ที่ระบุ |
| DELETE | ทุกแถวในตารางจะถูกลบทั้งหมด |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| UPDATE statement | คำสั่ง DML ที่ใช้แก้ไขค่าข้อมูลในแถวที่มีอยู่แล้วของตาราง |
| DELETE statement | คำสั่ง DML ที่ใช้ลบแถวออกจากตาราง |
| SET clause | ส่วนของ UPDATE statement ที่ระบุคอลัมน์และค่าใหม่ที่จะเปลี่ยน |
| WHERE clause | ส่วนที่ระบุเงื่อนไขว่าคำสั่งจะมีผลกับแถวไหน ถ้าไม่ระบุจะมีผลกับทุกแถว |

---

## ❓ My Questions & Gaps

- [ ] ถ้า UPDATE หรือ DELETE โดยไม่ตั้งใจลืมใส่ WHERE clause แล้วรันไปแล้ว มีวิธี rollback หรือกู้ข้อมูลคืนได้อย่างไร (transaction, backup)
- [ ] WHERE ... IN ('A2', 'A3') ใน DELETE ทำงานต่างจากการเขียน WHERE AUTHOR_ID = 'A2' OR AUTHOR_ID = 'A3' หรือไม่

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงที่กล่าวถึงในวิดีโอนี้
