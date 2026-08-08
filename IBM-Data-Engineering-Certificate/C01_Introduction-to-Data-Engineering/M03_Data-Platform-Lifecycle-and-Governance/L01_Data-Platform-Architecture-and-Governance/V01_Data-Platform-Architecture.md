# Data Platform Architecture

Tags: data platform, architecture, data pipeline

| Field             | Value                                                       |
| ----------------- | --------------------------------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate                    |
| **Course**        | C01 Introduction to Data Engineering                             |
| **Module**        | M03 Data Platform, Lifecycle, and Governance                     |
| **Lesson**        | L01 Data Platform Architecture and Governance                    |
| **Date studied**  | 2026-06-13                                                       |

---

## Table of Contents

- [Overview](#overview)
- [Layers of a Data Platform](#layers-of-a-data-platform)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายสถาปัตยกรรมของ data platform เป็นชั้นๆ ตั้งแต่การ ingest ข้อมูลไปจนถึง pipeline ที่คอยดูแลการไหลของข้อมูลตลอดทุกชั้น

---

## Layers of a Data Platform

Data platform ประกอบด้วยชั้นต่างๆ ดังนี้:

| Layer                    | Responsibility                                                       | Example Tools                                              |
| ------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 1. Data Ingestion        | เชื่อมต่อกับแหล่งข้อมูล; ส่งข้อมูลแบบ batch หรือ stream; ติดตาม metadata           | Kafka, AWS Kinesis, IBM Streams, Google DataFlow                    |
| 2. Storage & Integration | จัดเก็บข้อมูล; รวมข้อมูลจากหลายแหล่ง; รองรับทั้ง batch และ stream                  | IBM DB2, MySQL, MongoDB, Cassandra, Talend, Dell Boomi               |
| 3. Data Processing       | ตรวจสอบ แปลง ทำความสะอาด เตรียมข้อมูลสำหรับการวิเคราะห์                          | Python, R, OpenRefine, Watson Studio Refinery, Trifacta              |
| 4. Analysis & UI         | ส่งมอบให้ BI analyst, data scientist, และแอปพลิเคชัน                            | Tableau, Power BI, Jupyter, IBM Cognos, APIs                         |
| 5. Data Pipeline         | ชั้นที่ครอบทุกชั้น คอยรักษาให้ข้อมูลไหลต่อเนื่อง                                    | Apache Airflow, Google DataFlow                                      |

> ในฐานข้อมูลเชิงสัมพันธ์ storage และ processing อาจอยู่ในชั้นเดียวกันได้ แต่ในระบบ big data ข้อมูลจะถูกเก็บใน HDFS ก่อน แล้วค่อยประมวลผลใน Spark ทีหลัง

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย)                                    |
| ------------- | ---------------------------------------------------------- |
| Data Platform | ชุดของ layer ที่ทำงานร่วมกันตั้งแต่ ingestion จนถึง delivery ข้อมูล |

---

## ❓ My Questions & Gaps

- [ ] ในระบบจริง ชั้น Data Pipeline ถูกดูแลโดยทีมเดียวกับที่ดูแล storage หรือแยกทีมกัน?

---

## 🔗 Resources

- [IBM Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-engineer)
