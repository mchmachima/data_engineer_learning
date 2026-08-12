# Date and Time Built-in Functions

`Tags: SQL, date-functions, time-functions, date-arithmetic`

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
- [Date, Time, and Timestamp Data Types](#date-time-and-timestamp-data-types)
- [Extracting Date and Time Parts](#extracting-date-and-time-parts)
- [Date and Time Functions in the WHERE Clause](#date-and-time-functions-in-the-where-clause)
- [Date and Time Arithmetic](#date-and-time-arithmetic)
- [Special Registers: CURRENT_DATE and CURRENT_TIME](#special-registers-current_date-and-current_time)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้ต่อยอดจากเรื่อง built-in functions โดยเจาะลึกเฉพาะฟังก์ชันที่เกี่ยวกับวันที่และเวลา (date and time functions) ครอบคลุมชนิดข้อมูล DATE, TIME, TIMESTAMP ของ SQL วิธีดึงส่วนประกอบของวันที่/เวลาออกมา (เช่น day, month) การใช้ฟังก์ชันเหล่านี้ร่วมกับ `WHERE` clause และการทำ date/time arithmetic เช่น การบวกวันเข้าไปในวันที่ หรือหาผลต่างระหว่างวันที่ปัจจุบันกับวันที่ในตาราง ยังคงใช้ตาราง `PETRESCUE` เป็นตัวอย่างเช่นเดิม

---

## Date, Time, and Timestamp Data Types

SQL มีชนิดข้อมูลสำหรับวันที่และเวลาโดยเฉพาะ 3 แบบ ได้แก่ DATE, TIME, และ TIMESTAMP ซึ่งแต่ละแบบมีจำนวนหลัก (digit) และรูปแบบ (format) ต่างกัน

| Type      | Digits | Format                | คำอธิบาย |
| --------- | ------ | ---------------------- | -------- |
| DATE      | 8      | `YYYYMMDD`              | ปี, เดือน, วัน |
| TIME      | 6      | `HHMMSS`                | ชั่วโมง, นาที, วินาที |
| TIMESTAMP | 20     | `YYYYXXDDHHMMSSZZZZZZ`  | วันที่และเวลารวมกัน โดย XX คือเดือน และ ZZZZZZ คือ microseconds |

นอกจากนี้ยังมีฟังก์ชันสำหรับดึงส่วนประกอบต่าง ๆ ออกมาได้ เช่น DAY, MONTH, DAYOFMONTH, DAYOFWEEK, DAYOFYEAR, WEEK, HOUR, MINUTE, SECOND

---

## Extracting Date and Time Parts

ฟังก์ชัน `DAY()` ใช้ดึงเฉพาะส่วนวันที่ (day) ออกจากค่า date

```sql
-- ดึงเฉพาะส่วนวัน (day) ของ RESCUEDATE สำหรับแถวที่เป็น cat
SELECT DAY(RESCUEDATE), RESCUEDATE FROM PETRESCUE WHERE ANIMAL = 'Cat';
```

| 1   | RESCUEDATE |
| --- | ---------- |
| 29  | 2018-05-29 |
| 11  | 2018-06-11 |
| 13  | 2018-06-13 |

> ⚠️ ผลลัพธ์คำนวณจากชุดข้อมูล PETRESCUE มาตรฐานของ IBM course ที่ใช้ในโน้ต V01 (ทรานสคริปต์วิดีโอนี้ไม่ได้แนบข้อมูลตารางมาด้วย) ควรเทียบกับสไลด์จริงของคุณ

---

## Date and Time Functions in the WHERE Clause

Date/time functions ใช้ใน `WHERE` clause ได้เช่นเดียวกับ scalar function อื่น ๆ

```sql
-- นับจำนวนธุรกรรมที่เกิดขึ้นในเดือนพฤษภาคม (month = 5)
SELECT COUNT(*) FROM PETRESCUE WHERE MONTH(RESCUEDATE) = 5;
```

| 1   |
| --- |
| 1   |

> มีเพียงแถวเดียวที่ RESCUEDATE อยู่ในเดือน 5 คือ ID 1 (2018-05-29)

---

## Date and Time Arithmetic

สามารถบวก/ลบช่วงเวลา (interval) เข้ากับค่า date ได้โดยตรงด้วยฟังก์ชันอย่าง `DATE_ADD`

```sql
-- หาว่าวันที่ 3 วันหลังจากแต่ละ RESCUEDATE คือวันที่เท่าไร
SELECT RESCUEDATE, DATE_ADD(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE;
```

| RESCUEDATE | 1          |
| ---------- | ---------- |
| 2018-05-29 | 2018-06-01 |
| 2018-06-01 | 2018-06-04 |
| 2018-06-04 | 2018-06-07 |
| 2018-06-04 | 2018-06-07 |
| 2018-06-10 | 2018-06-13 |
| 2018-06-11 | 2018-06-14 |
| 2018-06-11 | 2018-06-14 |
| 2018-06-12 | 2018-06-15 |
| 2018-06-13 | 2018-06-16 |
| 2018-06-15 | 2018-06-18 |

ตัวอย่างการใช้งานจริงคือ กรณีต้องประมวลผลคำสั่งซื้อภายใน 3 วันหลังวันที่บันทึกไว้

---

## Special Registers: CURRENT_DATE and CURRENT_TIME

Database มี special register อย่าง `CURRENT_DATE` และ `CURRENT_TIME` ที่คืนค่าวันที่/เวลาปัจจุบันของระบบ ใช้คำนวณระยะเวลาที่ผ่านไปได้ เช่น จำนวนวันตั้งแต่ RESCUEDATE จนถึงตอนนี้

```sql
-- หาว่าผ่านมากี่ปี/เดือน/วัน นับจากแต่ละ RESCUEDATE จนถึงวันปัจจุบัน
SELECT CURRENT_DATE - RESCUEDATE FROM PETRESCUE;
```

| RESCUEDATE | CURRENT_DATE | ผลต่าง (ปี-เดือน-วัน) |
| ---------- | ------------ | ---------------------- |
| 2018-05-29 | 2026-08-12   | 8 ปี 2 เดือน 14 วัน     |

> ⚠️ ตัวอย่างนี้แสดงเฉพาะ 1 แถวเพื่อความชัดเจน เพราะผลลัพธ์เป็นค่าที่**เปลี่ยนแปลงตามวันที่รันคำสั่งจริง** (คำนวณโดยอิงวันปัจจุบัน 2026-08-12 ตาม session นี้) — รูปแบบผลลัพธ์ในหลาย database (เช่น Db2) จะแสดงเป็นตัวเลขรูปแบบปี-เดือน-วันต่อกัน ไม่ใช่ค่าจำนวนวันตรง ๆ ควรทดสอบรันจริงเพื่อดูรูปแบบผลลัพธ์ที่ database ของคุณใช้

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| DATE          | ชนิดข้อมูลวันที่ มี 8 หลัก รูปแบบ `YYYYMMDD` |
| TIME          | ชนิดข้อมูลเวลา มี 6 หลัก รูปแบบ `HHMMSS` |
| TIMESTAMP     | ชนิดข้อมูลวันที่+เวลารวมกัน มี 20 หลัก รูปแบบ `YYYYXXDDHHMMSSZZZZZZ` |
| DAY / MONTH / DAYOFMONTH / DAYOFWEEK / DAYOFYEAR / WEEK / HOUR / MINUTE / SECOND | ฟังก์ชันสำหรับดึงส่วนประกอบย่อยของค่า date/time |
| Date/time arithmetic | การบวกหรือลบช่วงเวลา (interval) เข้ากับค่า date/time โดยตรงในคำสั่ง SQL |
| `INTERVAL`    | keyword ใช้ระบุช่วงเวลาที่จะบวกหรือลบ เช่น `INTERVAL 3 DAY` |
| Special register | ตัวแปรพิเศษที่ database เตรียมไว้ให้ เช่น `CURRENT_DATE`, `CURRENT_TIME` ซึ่งคืนค่าปัจจุบันของระบบ |

---

## ❓ My Questions & Gaps

- [ ] ผลลัพธ์ของ `CURRENT_DATE - RESCUEDATE` ในตัวอย่างนี้อ้างอิงวันที่ปัจจุบันของ session (2026-08-12) — ควรทดลองรันจริงบน database เพื่อดูรูปแบบผลลัพธ์ที่แท้จริง (บาง database คืนค่าเป็น DECIMAL รูปแบบปี-เดือน-วัน บางที่คืนเป็นจำนวนวันตรง ๆ)
- [ ] Syntax ของ `DATE_ADD` และการดึงส่วนประกอบวันที่ (เช่น `MONTH()`) อาจต่างกันในแต่ละ database (Db2, MySQL, PostgreSQL) — ควรตรวจสอบ syntax ที่ตรงกับ database ที่ใช้จริงในหลักสูตร

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารเพิ่มเติมที่กล่าวถึงในวิดีโอนี้
