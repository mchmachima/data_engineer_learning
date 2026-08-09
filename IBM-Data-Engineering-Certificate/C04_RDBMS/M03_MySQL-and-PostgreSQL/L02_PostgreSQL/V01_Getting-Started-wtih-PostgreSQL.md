# Getting Started with PostgreSQL

`Tags: RDBMS, PostgreSQL, psql, pgAdmin`

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
- [What Is PostgreSQL and Deployment Options](#what-is-postgresql-and-deployment-options)
- [Tools for Connecting to PostgreSQL](#tools-for-connecting-to-postgresql)
- [psql Command-Line Interface](#psql-command-line-interface)
- [pgAdmin](#pgadmin)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้แนะนำ PostgreSQL ในภาพรวม ตั้งแต่นิยามและรูปแบบการ deploy ไปจนถึงเครื่องมือที่ใช้เชื่อมต่อกับฐานข้อมูล โดยเจาะลึกสองเครื่องมือหลักคือ **psql** (command-line) และ **pgAdmin** (graphical interface) ซึ่งเป็นเครื่องมือที่ใช้บ่อยที่สุดในการบริหารจัดการ PostgreSQL

---

## What Is PostgreSQL and Deployment Options

PostgreSQL (Postgres) เป็น open-source object-relational database management system ที่ขึ้นชื่อเรื่อง reliability, flexibility และรองรับทั้งข้อมูลแบบ relational และ non-relational เป็นตัวเลือกยอดนิยมสำหรับงาน OLTP, data analytics, และ geographic information systems (GIS)

PostgreSQL มีรูปแบบการ deploy ที่หลากหลาย:

- **ติดตั้งแบบ local** — ดาวน์โหลดและติดตั้งบน macOS, UNIX, หรือ Windows server
- **Virtualization/containerization** — self-manage ผ่าน virtual machine image หรือ container เพื่อประสิทธิภาพการใช้ทรัพยากรและ scalability
- **Cloud-based** — ใช้ managed service เช่น Amazon RDS, Google Cloud SQL, Microsoft Azure, IBM Cloud Databases, และ EnterpriseDB Cloud

---

## Tools for Connecting to PostgreSQL

| เครื่องมือ | ประเภท | ลักษณะเด่น |
| --- | --- | --- |
| **psql** | Command-line interface | เหมาะกับผู้ใช้ที่ถนัดการโต้ตอบแบบ text-based |
| **pgAdmin** | Open-source graphical interface | ใช้ได้ทั้ง desktop และ web application ทำให้จัดการฐานข้อมูลง่ายขึ้นด้วย GUI |
| **Navicat, DBeaver** | Commercial graphical interface | รองรับ PostgreSQL และฐานข้อมูลอื่น ๆ |
| **Managed service console** (เช่น Amazon RDS for PostgreSQL) | Web-based console/API | ช่วยจัดการฐานข้อมูลบน cloud environment ได้สะดวกขึ้น |

---

## psql Command-Line Interface

psql เป็น command-line interface มาตรฐานสำหรับโต้ตอบกับ PostgreSQL server เชื่อมต่อได้ผ่านคำสั่งเดียวโดยระบุ parameter เช่น username, database, host, และ port เมื่อเชื่อมต่อสำเร็จ psql จะเปลี่ยน terminal ให้เป็น interactive shell ที่รัน SQL command ได้แบบ real-time ตั้งแต่สร้างฐานข้อมูล/ตาราง ไปจนถึง query ข้อมูลที่ซับซ้อน มีฟีเจอร์ช่วยใช้งานอย่าง autocompletion และ syntax highlighting

เมื่อเชื่อมต่อเข้าไป จะเห็นฐานข้อมูล `postgres` (default user database) และฐานข้อมูลภายในอย่าง `template0` และ `template1` ซึ่ง Postgres ใช้เป็น template ตอนสร้างฐานข้อมูลใหม่

---

## pgAdmin

pgAdmin เป็น platform ที่ครบวงจรสำหรับโต้ตอบกับ PostgreSQL และช่วยงานทั้งด้าน development และ administration เมื่อเชื่อมต่อครั้งแรก pgAdmin จะพาไปที่ฐานข้อมูล default (`postgres`) และสามารถสลับไปฐานข้อมูลอื่นได้เมื่อสร้างเพิ่ม รองรับฟังก์ชันหลากหลาย เช่น สร้างฐานข้อมูล/ตาราง, load ข้อมูล, query, พัฒนา stored procedure และ function, จัดการ database object, security, และ monitoring

### Query Tool

หน้าต่างด้านบนใช้พิมพ์หรือวาง SQL query ส่วนผลลัพธ์แสดงด้านล่าง (แก้ไข dataset ได้ถ้าผลลัพธ์นั้น editable) มี 3 tab สำคัญในบานล่าง:

| Tab | หน้าที่ | ตัวอย่าง |
| --- | --- | --- |
| **Explain** | แสดง execution plan ของ query ช่วยทำ performance tuning หาจุดที่ไม่มีประสิทธิภาพ | `explain select * from employees where department = 'sales'` → อาจแสดงว่าเป็น sequential scan ที่สแกนทุกแถวเพื่อหา department ที่ตรงกับ sales |
| **Messages** | แสดงข้อความจาก query ล่าสุด ทั้ง success และ error | `select * from non_existing_table` → `error: relation non_existing_table does not exist` |
| **Notifications** | แสดง asynchronous notification จากคำสั่ง `LISTEN`/`NOTIFY` ของ PostgreSQL | function/trigger สั่ง `notify mychannel, 'sample payload'` และ session กำลัง listen บน `mychannel` → tab แสดง channel name, payload, และเวลาที่ notify |

### Entity Relationship Diagram (ERD) Tool

pgAdmin มีเครื่องมือสร้าง ERD สำหรับฐานข้อมูลที่มีอยู่ หรือ generate SQL statement จาก database object ที่มี โดย right-click แล้วเลือก "Generate ERD" เครื่องมือจะตรวจสอบโครงสร้างฐานข้อมูลอัตโนมัติแล้วสร้าง diagram แสดงตารางและความสัมพันธ์ ใช้จัดเรียงตารางใหม่ แก้ไขความสัมพันธ์ เพิ่ม note และ generate SQL statement ได้ในเครื่องมือเดียว

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| PostgreSQL (Postgres) | Open-source object-relational database management system รองรับทั้งข้อมูล relational และ non-relational |
| OLTP | Online Transaction Processing งานประมวลผลธุรกรรมแบบ real-time |
| psql | Command-line interface มาตรฐานสำหรับเชื่อมต่อและโต้ตอบกับ PostgreSQL |
| pgAdmin | Open-source graphical interface (desktop/web) สำหรับจัดการฐานข้อมูล PostgreSQL |
| template0 / template1 | ฐานข้อมูลภายในที่ PostgreSQL ใช้เป็นต้นแบบตอนสร้างฐานข้อมูลใหม่ |
| Explain tab | Tab ใน pgAdmin query tool ที่แสดง execution plan ของ query |
| LISTEN/NOTIFY | คำสั่งของ PostgreSQL สำหรับส่ง asynchronous notification ระหว่าง session |
| ERD (Entity Relationship Diagram) | แผนภาพแสดงตารางและความสัมพันธ์ระหว่างตารางในฐานข้อมูล |

---

## ❓ My Questions & Gaps

- [ ] pgAdmin's Explain tab กับคำสั่ง `EXPLAIN ANALYZE` ต่างกันอย่างไร และควรใช้ตอนไหนในการ tuning จริง
- [x] **VM (Virtual Machine) คืออะไร?** — โปรแกรมจำลองคอมพิวเตอร์ทั้งเครื่องขึ้นมาบน hardware จริง โดยมี hypervisor (เช่น VMware, VirtualBox, Hyper-V) เป็นตัวจัดสรรทรัพยากร (CPU, RAM, disk) ให้แต่ละ VM แต่ละ VM มี guest OS ของตัวเอง (เช่น ติดตั้ง Windows หรือ Linux แยกกันได้) จึงแยก isolate จากเครื่อง host และ VM อื่นอย่างสมบูรณ์ ข้อเสียคือกินทรัพยากรเยอะและเปิดใช้งานช้ากว่า container เพราะต้องบูต OS ทั้งระบบ ในบริบทของ PostgreSQL การ deploy บน VM หมายถึงการติดตั้ง PostgreSQL ลงใน guest OS ของ VM image นั้น เหมือนติดตั้งบนเครื่อง physical server ทั่วไป
- [x] **Container คืออะไร?** — แพ็กเกจที่รวม application พร้อม dependency ที่จำเป็นทั้งหมด (library, config) ไว้ในหน่วยเดียว แต่ **ใช้ OS kernel ร่วมกับเครื่อง host** (ผ่าน container engine เช่น Docker) จึงไม่ต้องมี guest OS แยกของตัวเองแบบ VM ทำให้เบากว่า เปิดได้เร็วกว่า และ scale ได้ง่ายกว่ามาก แลกกับ isolation ที่หลวมกว่า VM เล็กน้อยเพราะ share kernel เดียวกัน ในบริบทของ PostgreSQL การ deploy ผ่าน container หมายถึงการรัน PostgreSQL image (เช่น official `postgres` Docker image) เป็น container แยกต่างหาก ซึ่งเป็นวิธีที่นิยมมากในการทดสอบหรือ deploy แบบ portable

---

## 🔗 Resources

- [PostgreSQL Official Documentation](https://www.postgresql.org/docs/)
- [psql — PostgreSQL command-line client docs](https://www.postgresql.org/docs/current/app-psql.html)
- [pgAdmin Official Documentation](https://www.pgadmin.org/docs/)
