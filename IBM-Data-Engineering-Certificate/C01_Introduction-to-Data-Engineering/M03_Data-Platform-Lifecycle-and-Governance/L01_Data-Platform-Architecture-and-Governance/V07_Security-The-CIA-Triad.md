# Security: The CIA Triad

Tags: security, CIA triad, encryption

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
- [The CIA Triad](#the-cia-triad)
- [4 Layers of Security](#4-layers-of-security)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายหลักความปลอดภัยข้อมูล CIA Triad และ 4 ชั้นความปลอดภัยที่องค์กรต้องดูแลตั้งแต่ระดับกายภาพจนถึงระดับข้อมูล

---

## The CIA Triad

| Letter | Principle       | Meaning                                    |
| ------ | ---------------- | ---------------------------------------------- |
| C      | Confidentiality  | ป้องกันการเข้าถึงโดยไม่ได้รับอนุญาต               |
| I      | Integrity        | รับประกันว่าข้อมูลน่าเชื่อถือและไม่ถูกแก้ไข          |
| A      | Availability     | ผู้ใช้ที่ได้รับอนุญาตเข้าถึงทรัพยากรได้เสมอ          |

---

## 4 Layers of Security

1. **Physical** — การเข้าถึงสถานที่, กล้องวงจรปิด, ระบบไฟสำรอง, การควบคุมอุณหภูมิ
2. **Network** — firewall, การควบคุมการเข้าถึงเครือข่าย, VLAN, IDS/IPS, การเข้ารหัสระหว่างส่งข้อมูล
3. **Application** — threat modeling, การออกแบบที่ปลอดภัย, secure coding, การทดสอบความปลอดภัย
4. **Data** — authentication + authorization; การเข้ารหัสข้อมูลที่พัก (ฐานข้อมูล, backup) และระหว่างส่ง (HTTPS, SSL, TLS)

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย)                                                          |
| ------------- | ---------------------------------------------------------------------------------- |
| CIA Triad     | Confidentiality, Integrity, Availability — สามเสาหลักของความปลอดภัยข้อมูล            |
| IDS/IPS       | Intrusion Detection/Prevention Systems — ระบบตรวจจับและป้องกัน traffic ที่เป็นอันตราย   |

---

## ❓ My Questions & Gaps

- [ ] ในทางปฏิบัติ ทีม Data Engineering รับผิดชอบ layer ไหนของ security โดยตรง และ layer ไหนที่เป็นหน้าที่ของทีม infra/security?

---

## 🔗 Resources

- [IBM Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-engineer)
