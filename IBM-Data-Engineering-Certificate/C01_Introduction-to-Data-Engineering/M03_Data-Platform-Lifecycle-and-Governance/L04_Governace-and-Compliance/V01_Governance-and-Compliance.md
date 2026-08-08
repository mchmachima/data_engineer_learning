# Governance and Compliance

Tags: data governance, compliance, GDPR

| Field            | Value                                         |
| ---------------- | --------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate |
| **Course**       | C01 Introduction to Data Engineering          |
| **Module**       | M03 Data Platform, Lifecycle, and Governance  |
| **Lesson**       | L04 Governance and Compliance                 |
| **Date studied** | 2026-06-13                                    |

---

## Table of Contents

- [Overview](#overview)
- [Key Regulations](#key-regulations)
- [Data Lifecycle Governance Areas](#data-lifecycle-governance-areas)
- [Compliance Tools](#compliance-tools)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบาย data governance ว่าคือหลักการ แนวปฏิบัติ และกระบวนการที่รักษาความปลอดภัย ความเป็นส่วนตัว และความถูกต้องของข้อมูลตลอดวงจรชีวิตของมัน พร้อมกฎระเบียบสำคัญและเครื่องมือที่ใช้รองรับ compliance

---

## Key Regulations

| Regulation | Scope               | Focus                                          |
| ---------- | ------------------- | ---------------------------------------------- |
| GDPR       | สหภาพยุโรป          | ข้อมูลส่วนบุคคลและความเป็นส่วนตัวของพลเมือง EU |
| CCPA       | แคลิฟอร์เนีย สหรัฐฯ | ข้อมูลลูกค้าของผู้อยู่อาศัยในแคลิฟอร์เนีย      |
| HIPAA      | ธุรกิจสุขภาพ สหรัฐฯ | ข้อมูลสุขภาพที่ได้รับการคุ้มครอง               |
| PCI DSS    | ธุรกิจค้าปลีก       | มาตรฐานข้อมูลบัตรเครดิต                        |
| SOX        | การเงิน สหรัฐฯ      | การจัดการและรายงานข้อมูลทางการเงิน             |

---

## Data Lifecycle Governance Areas

```
Acquisition → Processing → Storage → Sharing → Retention & Disposal
    ↓               ↓           ↓         ↓              ↓
Legal basis,   How PII is   Where &    3rd-party     Retention
consent,       processed,   how data   access &      policies,
intended use   legal basis  is stored  accountability  deletion
```

_ต้องมี audit trail ที่ตรวจสอบย้อนกลับได้ในทุกขั้นตอน_

---

## Compliance Tools

| Tool                            | Purpose                                                                       |
| ------------------------------- | ----------------------------------------------------------------------------- |
| Authentication + Access Control | รหัสผ่าน, token, biometrics; สิทธิ์ตาม role                                   |
| Encryption                      | เข้ารหัสข้อมูลที่พักและระหว่างส่ง; ถอดรหัสได้เฉพาะด้วย key ที่ปลอดภัยเท่านั้น |
| Anonymization                   | ปิดบังข้อมูลในชั้นการแสดงผลโดยไม่เปลี่ยนข้อมูลต้นฉบับ                         |
| Pseudonymization                | แทนที่ PII ด้วยตัวระบุตัวตนสมมติ                                              |
| Monitoring & Alerting           | audit trail, แจ้งเตือนแบบ real-time เมื่อพบการละเมิดความปลอดภัย               |
| Data Erasure                    | เขียนทับข้อมูลถาวร (ต่างจากการลบทั่วไปที่ข้อมูลยังกู้คืนได้)                  |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์)     | คำอธิบาย (ภาษาไทย)                                                            |
| ---------------- | ----------------------------------------------------------------------------- |
| Data Governance  | นโยบายและกระบวนการที่รักษาความปลอดภัย ความเป็นส่วนตัว และความถูกต้องของข้อมูล |
| GDPR             | กฎระเบียบของ EU ที่กำกับดูแลความเป็นส่วนตัวและการคุ้มครองข้อมูลส่วนบุคคล      |
| HIPAA            | กฎระเบียบของสหรัฐฯ ที่กำกับดูแลข้อมูลสุขภาพที่ได้รับการคุ้มครอง               |
| Pseudonymization | การแทนที่ PII ด้วยตัวระบุตัวตนสมมติเพื่อไม่ให้ย้อนกลับไปหาบุคคลได้            |
| Data Erasure     | การเขียนทับข้อมูลด้วยซอฟต์แวร์อย่างถาวร (แข็งแรงกว่าการลบทั่วไป)              |

---

## ❓ My Questions & Gaps

- [ ] What is the difference between anonymization and pseudonymization in a GDPR context — when is each required?

---

## 🔗 Resources

- [GDPR Official Text](https://gdpr.eu/)
- [IBM Watson Knowledge Catalog](https://www.ibm.com/products/watson-knowledge-catalog)
