# Database Architecture

`Tags: RDBMS, deployment topology, database architecture`

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
- [Deployment Topologies](#deployment-topologies)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายรูปแบบสถาปัตยกรรมการติดตั้งใช้งานฐานข้อมูล (deployment topology) สี่แบบหลัก ตั้งแต่ single-tier ที่ทุกอย่างอยู่บนเครื่องเดียว ไปจนถึง three-tier ที่นิยมใช้ใน production และ cloud-based deployment ที่ไม่ต้องดูแล infrastructure เอง เป็นพื้นฐานก่อนเข้าใจสถาปัตยกรรมแบบกระจายในวิดีโอถัดไป

---

## Deployment Topologies

Deployment topology คือรูปแบบการจัดวางองค์ประกอบของ hardware, software และ network ในการติดตั้งระบบ ซึ่งเลือกใช้ตามปัจจัยด้าน scalability, performance, reliability และลักษณะของแอปพลิเคชัน

| Topology | โครงสร้าง | จุดเด่น |
| -------- | --------- | ------- |
| **Single-tier** | ทุกองค์ประกอบ (UI, application logic, data storage) อยู่บนเครื่องเดียวกัน | เรียบง่าย เหมาะกับงานเล็ก |
| **Two-tier (client-server)** | แบ่งเป็น client layer (UI) และ server layer (application logic + data storage) โดย client เชื่อมต่อผ่าน database interface เช่น API หรือ framework — ฝั่ง server มี data access layer (รองรับ JDBC, ODBC, CLP), database engine layer (คอมไพล์ query, ดึง/ประมวลผลข้อมูล) และ database storage layer | แยก client กับ server ชัดเจน |
| **Three-tier** | เพิ่ม middle tier หรือ application server layer คั่นระหว่าง client กับ database server | นิยมใน production เพราะช่วยเรื่อง security (จำกัดการเข้าถึง database server เฉพาะ admin), performance optimization และ maintainability เช่น ระบบ internet banking ที่ mobile app คุยกับ application server ก่อนไปคุยกับ database server |
| **Cloud-based deployment** | database อยู่บน cloud environment ไม่ต้องติดตั้งหรือดูแล infrastructure เอง | เข้าถึงได้ทุกที่ที่มีอินเทอร์เน็ต เหมาะกับทั้งงาน development, testing และ production |

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Deployment Topology | รูปแบบการจัดวาง hardware, software และ network component ในการติดตั้งระบบ (single-tier, two-tier, three-tier, cloud) |
| Single-tier Architecture | สถาปัตยกรรมที่ UI, application logic และ data storage อยู่บนเครื่องเดียวกันทั้งหมด |
| Two-tier (Client-Server) Architecture | แบ่งเป็น client layer (UI) และ server layer (application logic + data storage) |
| Three-tier Architecture | เพิ่ม application server layer คั่นระหว่าง client กับ database server เพื่อความปลอดภัยและ maintainability |
| Cloud Deployment | การติดตั้งฐานข้อมูลบน cloud environment โดยไม่ต้องดูแล infrastructure เอง |

---

## ❓ My Questions & Gaps

- [ ] ในทางปฏิบัติ three-tier architecture เพิ่ม latency เมื่อเทียบกับ two-tier มากน้อยแค่ไหน คุ้มกับ security ที่ได้เพิ่มหรือไม่

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
