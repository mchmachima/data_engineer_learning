# Distributed Architecture and Clustered Databases

`Tags: RDBMS, distributed architecture, replication, partitioning, sharding`

| Field            | Value                                            |
| ---------------- | ------------------------------------------------ |
| **Certificate**  | IBM Data Engineering Professional Certificate    |
| **Course**       | C04 Introduction to Relational Databases (RDBMS) |
| **Module**       | M01 Relational Database Concepts                 |
| **Lesson**       | L02 Introducing Relational Database Products     |
| **Date studied** | 2026-07-30                                       |

---

## Table of Contents

- [Overview](#overview)
- [Types of Distributed Architecture](#types-of-distributed-architecture)
- [Data Management and Performance Techniques](#data-management-and-performance-techniques)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายสถาปัตยกรรมแบบกระจาย (distributed architecture) ที่ RDBMS ใช้สำหรับ workload ขนาดใหญ่หรือที่ต้องการ high availability ครอบคลุมสองรูปแบบหลักคือ shared disk กับ shared nothing และเทคนิคจัดการข้อมูลอย่าง replication, partitioning และ sharding ที่ช่วยเพิ่ม scalability และ fault tolerance

---

## Types of Distributed Architecture

สำหรับ workload ขนาดใหญ่หรือที่ต้องการ high availability RDBMS จะใช้สถาปัตยกรรมแบบกระจาย ซึ่งเป็นกลุ่มของเครื่อง (cluster) ที่เชื่อมต่อกันผ่านเครือข่าย ช่วยเพิ่ม scalability, fault tolerance และ performance

| ประเภท | โครงสร้าง | จุดเด่น |
| ------ | --------- | ------- |
| **Shared Disk** | หลาย database server ใช้ storage ทางกายภาพเดียวกันร่วมกัน (common disk) และประสานงานกันผ่าน high-speed interconnection | กระจายภาระงานได้ดี และหาก server ตัวใดล่มก็สามารถ reroute client ไปยัง server อื่นได้ |
| **Shared Nothing** | แต่ละ node มี CPU, memory และ storage เป็นของตัวเอง ไม่มีการใช้ disk ร่วมกัน ใช้เทคนิค replication หรือ partitioning ในการกระจายข้อมูล | fault tolerance ดีเพราะ reroute client ไปยัง node อื่นได้เมื่อเกิดปัญหา |
| **Combination/Specialized** | ผสมผสานทั้ง shared disk, shared nothing, replication หรือ partitioning ร่วมกับ hardware เฉพาะทาง | ปรับแต่งให้ตรงกับ workload เฉพาะทาง |

---

## Data Management and Performance Techniques

- **Database replication** — คัดลอกการเปลี่ยนแปลงจาก database server หลักไปยัง replica หนึ่งตัวหรือมากกว่า ช่วยกระจาย workload หาก replica อยู่ที่เดียวกันเรียกว่า **HA (high availability) replica** ใช้สำหรับ failover เมื่อ server หลักล่ม ส่วน replica ที่อยู่ต่างพื้นที่ทางภูมิศาสตร์เรียกว่า **disaster recovery replica** ป้องกันกรณี data center ทั้งหมดล่ม (ไฟดับ, ไฟไหม้, แผ่นดินไหว, น้ำท่วม)
- **Partitioning และ Sharding** — แบ่งตารางขนาดใหญ่ออกเป็นส่วนย่อยเชิงตรรกะ (เช่น ข้อมูลยอดขายแยกตามไตรมาส) แล้วนำแต่ละ partition ไปวางบน node แยกกันใน cluster (เรียกว่า sharding) แต่ละ shard มี compute resource ของตัวเอง เมื่อ client query จะถูกประมวลผลแบบขนาน (parallel) ในหลาย node แล้วนำผลลัพธ์มารวมกัน เพิ่ม node/shard ได้ตามปริมาณข้อมูลที่โตขึ้น นิยมใช้ในงาน data warehousing และ BI

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Shared Disk Architecture | หลาย database server ใช้ storage ทางกายภาพร่วมกัน ประสานงานผ่าน high-speed interconnection |
| Shared Nothing Architecture | แต่ละ node มี CPU, memory, storage เป็นของตัวเอง กระจายข้อมูลด้วย replication หรือ partitioning |
| Replication | การคัดลอกการเปลี่ยนแปลงของข้อมูลจาก database server หลักไปยัง replica อื่น |
| HA (High Availability) Replica | replica ที่อยู่ตำแหน่งเดียวกับ primary ใช้สำหรับ failover เมื่อ primary ล่ม |
| Disaster Recovery Replica | replica ที่อยู่ต่างพื้นที่ทางภูมิศาสตร์ ป้องกันกรณี data center ทั้งหมดล่ม |
| Partitioning | การแบ่งตารางขนาดใหญ่ออกเป็นส่วนย่อยเชิงตรรกะ |
| Sharding | การนำ partition ไปวางบน node แยกกันใน cluster เพื่อรองรับ parallel processing |

---

## ❓ My Questions & Gaps

- [ ] ในทางปฏิบัติควรเลือกใช้ shared disk หรือ shared nothing architecture ในสถานการณ์แบบไหน ปัจจัยอะไรที่ใช้ตัดสินใจ
- [ ] ความแตกต่างระหว่าง HA replica กับ disaster recovery replica ในแง่ของ RTO/RPO (เวลาที่ยอมรับได้ในการกู้คืนระบบ) เป็นอย่างไร
- [ ] เมื่อไรควรเลือกใช้ partitioning เทียบกับ sharding ในการออกแบบระบบจริง

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
