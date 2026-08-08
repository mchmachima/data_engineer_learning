# ETL vs ELT

Tags: ETL, ELT, data pipeline

| Field            | Value                                                                 |
| ---------------- | --------------------------------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate                         |
| **Course**       | C01 Introduction to Data Engineering                                  |
| **Module**       | M02 The Data Engineering Ecosystem                                    |
| **Lesson**       | L02 Data Repositories, Data Pipelines, and Data Integration Platforms |
| **Date studied** | 2026-06-13                                                            |

---

## Table of Contents

- [Overview](#overview)
- [ETL vs ELT Comparison](#etl-vs-elt-comparison)
- [Data Pipelines](#data-pipelines)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้เปรียบเทียบ ETL กับ ELT ว่าต่างกันตรงจุดไหน และอธิบายว่า data pipeline เป็นแนวคิดที่กว้างกว่า ETL/ELT อย่างไร

---

## ETL vs ELT Comparison

| Aspect            | ETL                                          | ELT                                   |
| ----------------- | -------------------------------------------- | ------------------------------------- |
| ขั้นตอน transform | ก่อนโหลดข้อมูล (ใน staging)                  | หลังโหลดข้อมูล (ใน target)            |
| เหมาะกับ          | ระบบปลายทางที่มี schema ตายตัว, ระบบเก่า     | data lake, data warehouse บน cloud    |
| ความยืดหยุ่น      | ยืดหยุ่นน้อยกว่า — ต้องกำหนด schema ล่วงหน้า | ยืดหยุ่นมากกว่า — เก็บข้อมูลดิบไว้ได้ |
| เครื่องมือ (ETL)  | IBM InfoSphere, AWS Glue, Informatica        | —                                     |

**ขั้นตอน Transform ของ ETL:** การทำ standardization, deduplication, filtering, data enrichment, การ map ความสัมพันธ์, กฎทางธุรกิจ

**ข้อดีของ ELT:** รองรับข้อมูลขนาดใหญ่/unstructured ได้ดี; ส่งมอบงานได้เร็วกว่า; นำข้อมูลดิบไป transform ต่อได้หลายรูปแบบ

---

## Data Pipelines

**Data Pipeline** เป็นแนวคิดที่กว้างกว่า ETL/ELT — ครอบคลุมเส้นทางทั้งหมดตั้งแต่ต้นทางถึงปลายทาง และอาจเป็นแบบ batch, streaming หรือแบบผสมก็ได้

เครื่องมือสำหรับ pipeline: Apache Beam, Apache Airflow, Google Cloud Dataflow

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย)                                                            |
| ------------ | ----------------------------------------------------------------------------- |
| ETL          | Extract, Transform, Load — แปลงข้อมูลก่อนโหลดเข้าระบบปลายทาง                  |
| ELT          | Extract, Load, Transform — โหลดข้อมูลดิบก่อน แล้วค่อย transform ในระบบปลายทาง |

---

## ❓ My Questions & Gaps

- [ ] When should you choose ELT over ETL in a real project — what's the tipping point?

---

## 🔗 Resources

- [Apache Kafka Docs](https://kafka.apache.org/documentation/)
