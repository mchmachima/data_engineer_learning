# Querying Data

Tags: SQL, querying, aggregation

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
- [Common Query Patterns](#common-query-patterns)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้แสดงตัวอย่าง SQL query พื้นฐานที่ใช้บ่อยในงาน data engineering ตั้งแต่การนับ record ไปจนถึงการ group และ aggregate ข้อมูล

---

## Common Query Patterns

```sql
-- นับจำนวน record
SELECT COUNT(*) FROM orders;
SELECT COUNT(DISTINCT customer_id) FROM orders;

-- การ aggregate
SELECT SUM(amount), AVG(amount), STDDEV(amount) FROM orders;

-- ค่าสูงสุด/ต่ำสุด
SELECT MAX(amount), MIN(amount) FROM orders;

-- เรียงลำดับผลลัพธ์
SELECT * FROM orders ORDER BY amount DESC;

-- กรองข้อมูลตามรูปแบบ (partial match)
SELECT * FROM customers WHERE postcode LIKE '100%';

-- จัดกลุ่มและ aggregate
SELECT region, SUM(amount) FROM orders GROUP BY region;
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย)                                        |
| ------------ | --------------------------------------------------------- |
| Aggregation  | การรวมค่าจากหลาย record ให้เป็นค่าสรุปเดียว เช่น SUM, AVG |

---

## ❓ My Questions & Gaps

- [ ] GROUP BY กับ subquery ต่างกันในแง่ performance อย่างไรเมื่อข้อมูลมีขนาดใหญ่มาก?

---

## 🔗 Resources

- [IBM Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-engineer)
