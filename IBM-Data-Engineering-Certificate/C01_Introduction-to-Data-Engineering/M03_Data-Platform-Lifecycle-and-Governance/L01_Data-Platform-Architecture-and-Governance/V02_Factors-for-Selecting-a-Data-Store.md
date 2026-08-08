# Factors for Selecting a Data Store

Tags: data store, RDBMS, NoSQL

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
- [Selection Factors](#selection-factors)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้สรุปปัจจัยที่ต้องพิจารณาเมื่อเลือก data store สำหรับระบบใดระบบหนึ่ง ตั้งแต่ประเภทข้อมูลไปจนถึงข้อกำหนดด้าน compliance

---

## Selection Factors

| Factor                   | Considerations                                                             |
| ------------------------ | -------------------------------------------------------------------------------- |
| **ประเภทข้อมูล**            | structured → RDBMS; semi/unstructured → NoSQL                                    |
| **ปริมาณ**                 | ข้อมูลดิบปริมาณสูง → Data Lake; ต้องประมวลผลแบบ distributed → Big Data repository     |
| **การใช้งาน**              | OLTP (อ่าน/เขียน/อัปเดตเร็ว) เทียบกับ OLAP (query ประวัติที่ซับซ้อน)                   |
| **Performance**           | throughput (อัตราการอ่าน/เขียน), latency (เวลาในการเข้าถึง)                          |
| **Availability**          | ต้องการ zero downtime หรือไม่                                                      |
| **Integrity**             | ปลอดภัยจากการเสียหาย สูญหาย หรือการเข้าถึงโดยไม่ได้รับอนุญาต                          |
| **Recoverability**        | ความสามารถในการกู้คืนจากความล้มเหลว                                                 |
| **Privacy & Compliance**  | GDPR, CCPA, HIPAA — ต้องออกแบบไว้ตั้งแต่ต้น ไม่ใช่มาเติมทีหลัง                          |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย)                                              |
| ------------- | -------------------------------------------------------------------- |
| Throughput    | อัตราการอ่าน/เขียนข้อมูลของระบบ                                          |
| Latency       | ระยะเวลาที่ใช้ในการเข้าถึงข้อมูล                                          |

---

## ❓ My Questions & Gaps

- [ ] ในทางปฏิบัติ ปัจจัยใดมักถูกให้น้ำหนักมากที่สุดเมื่อทีมต้องตัดสินใจเลือก data store อย่างรวดเร็ว?

---

## 🔗 Resources

- [GDPR Official Text](https://gdpr.eu/)
