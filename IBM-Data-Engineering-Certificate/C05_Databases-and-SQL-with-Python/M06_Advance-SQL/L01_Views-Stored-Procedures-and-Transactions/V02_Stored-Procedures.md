# Stored Procedures

`Tags: SQL, stored procedure, CREATE PROCEDURE, CALL, delimiter`

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
- [What a Stored Procedure Is](#what-a-stored-procedure-is)
- [Benefits of Stored Procedures](#benefits-of-stored-procedures)
- [Creating and Calling a Stored Procedure](#creating-and-calling-a-stored-procedure)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายเรื่อง stored procedure ซึ่งเป็นชุดคำสั่ง SQL ที่ถูกเก็บและรันบน database server แทนที่จะส่งหลาย statement จาก client ไปยัง server ทีละคำสั่ง เนื้อหาครอบคลุมความหมาย ประโยชน์ของการใช้ stored procedure และวิธีสร้าง/เรียกใช้งานด้วย syntax จริง

---

## What a Stored Procedure Is

Stored procedure คือชุดคำสั่ง SQL ที่ถูกเก็บไว้และรันบน database server แทนที่จะส่งหลาย SQL statement จาก client ไปยัง server ทีละคำสั่ง เราสามารถ encapsulate คำสั่งเหล่านั้นไว้เป็น stored procedure บน server แล้วส่งแค่คำสั่งเดียวจาก client เพื่อเรียกใช้งานทั้งหมด

สามารถเขียน stored procedure ได้หลายภาษา เช่นสำหรับ DB2 on Cloud และ DB2 สามารถเขียนด้วย SQL PL, PL/SQL, Java, C หรือภาษาอื่น ๆ stored procedure สามารถรับ parameter, ทำ CRUD operation (Create, Read, Update, Delete) และคืนผลลัพธ์กลับไปยัง client application ได้

---

## Benefits of Stored Procedures

| ประโยชน์ | คำอธิบาย |
| --- | --- |
| ลด network traffic | client ส่ง call เดียวเพื่อรันหลาย statement แทนที่จะส่งทีละคำสั่ง |
| เพิ่ม performance | การประมวลผลเกิดขึ้นบน server ที่เก็บข้อมูลอยู่ ส่งกลับแค่ผลลัพธ์สุดท้ายให้ client |
| นำโค้ดกลับมาใช้ซ้ำได้ | หลาย application สามารถเรียกใช้ stored procedure เดียวกันสำหรับงานเดียวกัน |
| เพิ่มความปลอดภัย | ไม่ต้องเปิดเผยข้อมูล table/column ทั้งหมดให้ client-side developer เห็น และสามารถใช้ server-side logic ตรวจสอบข้อมูลก่อนรับเข้าระบบได้ |

ควรระวังว่า SQL ไม่ใช่ fully fledged programming language จึงไม่ควรพยายามเขียน business logic ทั้งหมดไว้ใน stored procedure

---

## Creating and Calling a Stored Procedure

การสร้าง stored procedure ใช้คำสั่ง `CREATE PROCEDURE` ระบุชื่อ procedure และ parameter ที่จะรับ จากนั้น declare ภาษาที่ใช้ และเขียน procedural logic ไว้ระหว่าง `BEGIN` กับ `END`

เนื่องจาก stored procedure จะมีหลาย statement รวมกัน จึงควรเปลี่ยน delimiter (ตัวอักษรที่บ่งบอกจุดสิ้นสุดของ statement) ก่อนเริ่ม define procedure เพื่อไม่ให้ semicolon ภายใน procedure ถูกตีความว่าจบคำสั่งก่อนเวลา แล้วค่อยเปลี่ยน delimiter กลับเป็น semicolon เมื่อ define เสร็จ

```sql
-- เปลี่ยน delimiter เป็น $$ ก่อนเริ่ม define procedure ที่มีหลาย statement
DELIMITER $$

-- สร้าง procedure update_sal รับ employee number และ rating เพื่อปรับ salary
CREATE PROCEDURE update_sal (IN empID INT, IN rating INT)
LANGUAGE SQL
BEGIN
    IF rating = 1 THEN
        UPDATE employees SET salary = salary * 1.10 WHERE emp_id = empID;
    ELSE
        UPDATE employees SET salary = salary * 1.05 WHERE emp_id = empID;
    END IF;
END $$

-- เปลี่ยน delimiter กลับเป็น semicolon เมื่อ define เสร็จแล้ว
DELIMITER ;

-- เรียกใช้ stored procedure ที่สร้างไว้ โดยส่ง employee ID และ rating
CALL update_sal(20001, 1);
```

เรียกใช้ stored procedure ได้ทั้งจาก external application และจาก dynamic SQL statement โดยใช้คำสั่ง `CALL` ตามด้วยชื่อ procedure และ parameter ที่ต้องการ

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Stored Procedure | ชุดคำสั่ง SQL ที่ถูกเก็บไว้และรันบน database server แทนที่จะรันฝั่ง client |
| CREATE PROCEDURE | คำสั่ง SQL สำหรับสร้าง stored procedure พร้อมระบุชื่อและ parameter |
| CALL | คำสั่งที่ใช้เรียกใช้งาน stored procedure |
| Delimiter | ตัวอักษรที่บ่งบอกจุดสิ้นสุดของ SQL statement โดย default คือ semicolon แต่ต้องเปลี่ยนชั่วคราวเมื่อ define procedure ที่มีหลาย statement |
| CRUD | ตัวย่อของ Create, Read, Update, Delete — การดำเนินการพื้นฐานสี่แบบกับข้อมูล |
| SQL PL | ภาษา procedural extension ของ SQL ที่ใช้เขียน stored procedure บน DB2 |

---

## ❓ My Questions & Gaps

- [ ] การจัดการ error ภายใน stored procedure (เช่น exception handling) ทำอย่างไรใน SQL PL
- [ ] stored procedure ต่างจาก function อย่างไร ในแง่การคืนค่าและการใช้งานใน SELECT statement
- [ ] การเปลี่ยน delimiter จำเป็นในทุก database engine หรือเฉพาะบางตัว เช่น MySQL/DB2

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมที่กล่าวถึงในวิดีโอนี้
