# Loading Data

`Tags: load utility, Db2 Web Console, CSV, RDBMS`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C04 Introduction to Relational Databases (RDBMS) |
| **Module**        | M02 Using Relational Databases            |
| **Lesson**        | L01 Creating Tables and Loading Data      |
| **Date studied**  | 2026-07-31                                |

---

## Table of Contents

- [Overview](#overview)
- [When to Use a Load Utility](#when-to-use-a-load-utility)
- [Loading a CSV File in Db2 Web Console](#loading-a-csv-file-in-db2-web-console)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้ลงรายละเอียดการใช้ load utility เพื่อโหลดข้อมูลจำนวนมากเข้าตาราง และเดินผ่านขั้นตอนจริง 4 ขั้นตอนของการโหลดไฟล์ CSV ผ่าน Db2 Web Console ตั้งแต่ระบุแหล่งข้อมูลไปจนถึงตรวจสอบผลลัพธ์หลังโหลดเสร็จ

---

## When to Use a Load Utility

การใช้ `INSERT` เหมาะกับข้อมูลไม่กี่แถวหรือช่วง develop/test แต่ไม่เหมาะกับการโหลดข้อมูลหลักร้อยหลักพันแถว RDBMS ส่วนใหญ่จึงมี load utility ที่โหลดข้อมูลจำนวนมากได้เร็ว มีประสิทธิภาพ และ scalable ข้อมูลต้นทางอาจมาจากไฟล์ delimited text, S3 object storage (Amazon) หรือ IBM Cloud Object Storage

---

## Loading a CSV File in Db2 Web Console

ใน Db2 Web Console การโหลดข้อมูลจากไฟล์ CSV มี 4 ขั้นตอน:

```mermaid
flowchart LR
    A["1. Source
    ระบุประเภท/ตำแหน่งข้อมูล
    + authentication"] --> B["2. Target
    เลือก schema/ตาราง
    append หรือ overwrite"]
    B --> C["3. Define
    encoding, delimiter,
    column heading, date format"]
    C --> D["4. Finalize
    ตรวจสอบก่อน load
    ดูสถานะ/error หลังเสร็จ"]
```

1. **Source** — ระบุประเภทและตำแหน่งของข้อมูลต้นทาง พร้อมข้อมูล authentication ที่จำเป็น (เช่น COS endpoint, access key, secret key) หรือแค่เลือกไฟล์ที่จะอัปโหลดถ้าเป็นไฟล์ local
2. **Target** — เลือก schema และตารางปลายทาง เลือกได้ว่าจะ append ข้อมูลใหม่ต่อท้ายหรือ overwrite ข้อมูลเดิม (ถ้าเลือก overwrite แล้ว load ล้มเหลว ข้อมูลเดิมจะหายไปด้วย) หรือสร้างตารางใหม่จากรูปแบบของข้อมูลที่โหลด
3. **Define** — กำหนด character encoding, delimiter, ว่ามี column heading ในแถวแรกหรือไม่ และรูปแบบวันที่/เวลา
4. **Finalize** — ตรวจสอบการตั้งค่าทั้งหมดก่อนเริ่ม load เมื่อโหลดเสร็จ console จะแสดงสถานะและ error/warning ที่เกิดขึ้น

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| S3 Object Storage | บริการเก็บไฟล์แบบ object storage ของ Amazon ที่ใช้เป็นแหล่งข้อมูลต้นทางได้ |
| IBM Cloud Object Storage (COS) | บริการเก็บไฟล์แบบ object storage ของ IBM ที่ใช้เป็นแหล่งข้อมูลต้นทางได้ |
| Append | การเพิ่มข้อมูลใหม่ต่อท้ายข้อมูลเดิมในตาราง (ตรงข้ามกับ overwrite) |
| Overwrite | การเขียนทับข้อมูลเดิมทั้งหมดด้วยข้อมูลใหม่ที่โหลดเข้ามา |

---

## ❓ My Questions & Gaps

- [ ] การ overwrite ข้อมูลระหว่าง load แล้วเกิด failure จะกู้คืนข้อมูลเดิมได้อย่างไรถ้าไม่มี backup ล่วงหน้า

---

## 🔗 Resources

- Db2 Web Console — Load Data utility สำหรับโหลดข้อมูลจาก CSV, S3, Cloud Object Storage
