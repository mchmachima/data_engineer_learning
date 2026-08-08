# Big Data Tools

Tags: big data, Hadoop, Spark

| Field            | Value                                         |
| ---------------- | --------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate |
| **Course**       | C01 Introduction to Data Engineering          |
| **Module**       | M02 The Data Engineering Ecosystem            |
| **Lesson**       | L03 Big Data Platforms                        |
| **Date studied** | 2026-06-13                                    |

---

## Table of Contents

- [Overview](#overview)
- [Core Tools](#core-tools)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้แนะนำเครื่องมือหลักในระบบนิเวศ Big Data ได้แก่ Apache Hadoop, HDFS, Apache Hive และ Apache Spark พร้อมจุดเด่นของแต่ละตัว

---

## Core Tools

| Tool          | Type                             | Best For                                                                   |
| ------------- | -------------------------------- | -------------------------------------------------------------------------- |
| Apache Hadoop | distributed storage + processing | จัดเก็บและประมวลผล dataset ขนาดใหญ่บน cluster                              |
| HDFS          | ระบบไฟล์ของ Hadoop               | จัดเก็บแบบ fault-tolerant ด้วยการแบ่งไฟล์และทำ replication                 |
| Apache Hive   | SQL บน Hadoop (OLAP)             | งาน ETL และ analytics บน data warehouse; latency สูง ไม่เหมาะกับ real-time |
| Apache Spark  | in-memory processing engine      | real-time analytics, ML, streaming; เร็วกว่า Hadoop มาก                    |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย)                                                  |
| ------------ | ------------------------------------------------------------------- |
| HDFS         | Hadoop Distributed File System — แบ่งและ replicate ไฟล์ข้าม cluster |

---

## ❓ My Questions & Gaps

- [ ] What makes Spark faster than Hadoop MapReduce exactly — is it purely in-memory?
- [ ] How does HDFS replication work if a node fails mid-write?

---

## 🔗 Resources

- [Apache Hadoop Docs](https://hadoop.apache.org/docs/)
- [Apache Spark Docs](https://spark.apache.org/docs/latest/)
