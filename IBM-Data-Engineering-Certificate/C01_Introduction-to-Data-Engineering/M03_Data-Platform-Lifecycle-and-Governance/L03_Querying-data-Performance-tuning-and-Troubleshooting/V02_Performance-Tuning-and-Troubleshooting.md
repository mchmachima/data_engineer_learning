# Performance Tuning and Troubleshooting

Tags: performance tuning, troubleshooting, indexing

| Field            | Value                                                      |
| ---------------- | ---------------------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate              |
| **Course**       | C01 Introduction to Data Engineering                       |
| **Module**       | M03 Data Platform, Lifecycle, and Governance               |
| **Lesson**       | L03 Querying Data, Performance Tuning, and Troubleshooting |
| **Date studied** | 2026-06-13                                                 |

---

## Table of Contents

- [Overview](#overview)
- [Pipeline Performance Metrics to Monitor](#pipeline-performance-metrics-to-monitor)
- [Troubleshooting Steps](#troubleshooting-steps)
- [Database Optimization Techniques](#database-optimization-techniques)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้ครอบคลุมงาน operational ของ Data Engineer ด้าน performance ได้แก่ metric ที่ต้องติดตาม ขั้นตอนการ troubleshoot เมื่อเกิดปัญหา และเทคนิคการ optimize ฐานข้อมูล

---

## Pipeline Performance Metrics to Monitor

| Metric               | What it measures                     |
| -------------------- | ------------------------------------ |
| Latency              | เวลาที่บริการใช้ในการตอบสนอง request |
| Failure rate         | อัตราที่บริการล้มเหลว                |
| Resource utilization | การใช้งาน CPU, memory, disk          |
| Traffic              | จำนวน request ต่อช่วงเวลา            |

---

## Troubleshooting Steps

1. รวบรวมข้อมูลเกี่ยวกับ incident
2. ตรวจสอบเวอร์ชันซอฟต์แวร์และ source code
3. ทบทวนการ deploy ล่าสุด
4. ตรวจสอบ log และ metric (error, การใช้ CPU/memory ณ เวลาที่เกิดปัญหา)
5. จำลองปัญหาซ้ำในสภาพแวดล้อมทดสอบ
6. ยืนยันสมมติฐานสาเหตุที่แท้จริง
7. deploy การแก้ไขตามขั้นตอนของทีม

---

## Database Optimization Techniques

| Technique         | Purpose                                                       |
| ----------------- | ------------------------------------------------------------- |
| Indexing          | ค้นหาข้อมูลได้เร็วโดยไม่ต้อง scan ทั้งตาราง                   |
| Partitioning      | แบ่งตารางขนาดใหญ่ออกเป็นตารางย่อยเพื่อให้ query เร็วขึ้น      |
| Normalization     | ลดความซ้ำซ้อนและป้องกันความผิดปกติจากการอัปเดต                |
| Capacity planning | จัดขนาดฮาร์ดแวร์และซอฟต์แวร์ให้เหมาะกับ load ปัจจุบันและอนาคต |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย)                                           |
| ------------ | ------------------------------------------------------------ |
| Indexing     | เทคนิคช่วยให้ค้นหาข้อมูลได้เร็วโดยไม่ต้อง scan ทั้งตาราง     |
| Partitioning | การแบ่งตารางขนาดใหญ่เป็นตารางย่อยเพื่อเพิ่มความเร็วของ query |

---

## ❓ My Questions & Gaps

- [ ] How does partitioning interact with indexing in practice — do you always need both?
- [ ] In a streaming pipeline, how do you monitor latency in real-time (what tools are used)?

---

## 🔗 Resources

- [Apache Airflow Docs](https://airflow.apache.org/docs/)
