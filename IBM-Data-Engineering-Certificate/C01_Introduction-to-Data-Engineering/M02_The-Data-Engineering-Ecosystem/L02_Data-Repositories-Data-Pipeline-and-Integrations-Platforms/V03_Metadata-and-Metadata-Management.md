# Metadata and Metadata Management

Tags: metadata, data governance, data lineage

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
- [Types of Metadata](#types-of-metadata)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบาย metadata 3 ประเภท และเหตุผลที่ metadata สำคัญต่อการค้นหาข้อมูล data lineage governance และ compliance

---

## Types of Metadata

| Type      | What It Tracks                                                                                 |
| --------- | ---------------------------------------------------------------------------------------------- |
| Technical | โครงสร้างของข้อมูล (ชื่อตาราง, จำนวนคอลัมน์, data type) — เก็บไว้ใน System Catalog             |
| Process   | กิจกรรมของ pipeline (เวลาเริ่ม/จบ, การใช้ disk, การเคลื่อนย้ายข้อมูล) — สำหรับ troubleshooting |
| Business  | ความหมายของข้อมูลในมุมมองผู้ใช้ทางธุรกิจ, วิธีได้มาของข้อมูล, ความเชื่อมโยงระหว่าง dataset     |

**ทำไมถึงสำคัญ:** ช่วยให้ค้นหาข้อมูลได้ (data discovery), ตรวจสอบ data lineage (ย้อนรอยต้นทางและการเปลี่ยนแปลง), รองรับ governance และ compliance

เครื่องมือยอดนิยม: IBM Watson Knowledge Catalog, Alation, Informatica Enterprise Data Catalog, Microsoft Azure Data Catalog

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย)                                                      |
| ------------ | ----------------------------------------------------------------------- |
| Metadata     | ข้อมูลเกี่ยวกับข้อมูล — อธิบายโครงสร้าง กระบวนการ หรือความหมายทางธุรกิจ |
| Data Lineage | ความสามารถในการย้อนรอยข้อมูลตั้งแต่ต้นทางผ่านทุกการเปลี่ยนแปลง          |

---

## ❓ My Questions & Gaps

- [ ] What does "data lineage" look like in a real tool like IBM Watson Knowledge Catalog?

---

## 🔗 Resources

- [IBM Watson Knowledge Catalog](https://www.ibm.com/products/watson-knowledge-catalog)
