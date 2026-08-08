# Database Normalization

`Tags: RDBMS, normalization, functional dependency, candidate key`

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
- [Why Normalize](#why-normalize)
- [Functional Dependencies (FDs)](#functional-dependencies-fds)
- [Multi-Valued Dependencies (MVDs)](#multi-valued-dependencies-mvds)
- [Candidate Keys](#candidate-keys)
- [Practical Example](#practical-example)
- [Comparison Summary](#comparison-summary)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้ปูพื้นฐานแนวคิดขั้นสูงของโมเดลเชิงสัมพันธ์ที่เป็นรากฐานของการทำ normalization คือ functional dependency (FD), multi-valued dependency (MVD) และ candidate key พร้อมตัวอย่างเชิงปฏิบัติจากตารางพนักงาน/โปรเจกต์ และตารางเปรียบเทียบทั้งสามแนวคิด

---

## Why Normalize

การ Normalize ฐานข้อมูล คือกระบวนการจัดโครงสร้างข้อมูลให้อยู่ในรูปแบบที่เหมาะสม โดยใช้หลักการของความสัมพันธ์ระหว่างข้อมูล (Dependencies) และการกำหนดคีย์ (Keys) เพื่อจัดระเบียบตารางให้มีประสิทธิภาพสูงสุด

**ความสำคัญของการทำ Normalization มีดังนี้:**

1. **ลดความซ้ำซ้อนของข้อมูล (Reduce Redundancy):** ช่วยป้องกันการเก็บข้อมูลเดิมซ้ำ ๆ หลายครั้งในที่ต่าง ๆ ซึ่งเป็นจุดประสงค์หลักของการใช้ Functional Dependencies (FDs) เข้ามาช่วยออกแบบ
2. **รักษาความถูกต้องของข้อมูล (Data Integrity):** ช่วยให้มั่นใจว่าข้อมูลในระบบมีความถูกต้องและสอดคล้องกัน หากเราละเลยความสัมพันธ์บางอย่าง เช่น Multi-Valued Dependencies (MVDs) อาจนำไปสู่การบันทึกข้อมูลที่ผิดพลาดได้
3. **เพิ่มประสิทธิภาพในการสืบค้น (Query Performance):** การกำหนด Candidate Keys ที่ดีจะช่วยในการทำ Indexing ซึ่งส่งผลให้การค้นหาข้อมูลทำได้รวดเร็วขึ้น
4. **ป้องกันข้อมูลซ้ำซ้อนและระบุตัวตนของข้อมูลได้ชัดเจน:** การใช้ Candidate Key ที่มีความเป็นเอกลักษณ์ (Uniqueness) และมีขนาดเล็กที่สุด (Minimality) จะช่วยบังคับให้แต่ละแถวในตารางไม่ซ้ำกัน และระบุแต่ละรายการได้อย่างเฉพาะเจาะจง
5. **จัดระเบียบโครงสร้างให้ยืดหยุ่น:** ช่วยในการสร้างความสัมพันธ์ระหว่างตารางอย่างเป็นระบบ ทำให้ง่ายต่อการบำรุงรักษาและขยายระบบในอนาคต

**สรุปง่าย ๆ คือ:** การ Normalize เป็นเหมือนการ "จัดบ้าน" ให้ข้อมูล โดยการแยกสิ่งของที่กระจัดกระจายไปไว้ในที่ที่ถูกต้องตามความสัมพันธ์ของมัน เพื่อให้หาของง่าย (เร็ว) ไม่เก็บของซ้ำซ้อน (ประหยัดพื้นที่) และมั่นใจว่าของไม่หายหรือผิดเพี้ยน (ถูกต้อง)

---

## Functional Dependencies (FDs)

"รู้ A แล้วจะรู้ B แน่นอน" — เป็นความสัมพันธ์ที่ค่าของข้อมูลชุดหนึ่ง (ตัวกำหนด หรือ Determinant) สามารถระบุค่าของอีกชุดหนึ่ง (ตัวที่ถูกกำหนด หรือ Dependent) ได้อย่างเฉพาะเจาะจง

- **สัญลักษณ์:** `X→Y`
- **ตัวอย่าง:** ถ้าเรามีรหัสพนักงาน (`EmployeeID`) เราจะสามารถรู้ชื่อพนักงาน (EmployeeName) ของคนนั้นได้ทันทีและแน่นอน เช่น `EmployeeID` 1 คือ Alice เสมอ
- **ทำไมต้องมี:** เพื่อช่วยรักษาความถูกต้องของข้อมูลและลดความซ้ำซ้อน

---

## Multi-Valued Dependencies (MVDs)

"รู้ A แล้วจะรู้เซตของค่า B" — แนวคิดนี้จะซับซ้อนกว่า FD เล็กน้อย คือการที่ข้อมูลตัวหนึ่งกำหนด "กลุ่มของค่า" ที่เป็นไปได้หลายค่า มักพบในความสัมพันธ์แบบ Many-to-Many

- **สัญลักษณ์:** `X↠{Y1,Y2,...}`
- **ตัวอย่าง:** รหัสพนักงานคนหนึ่งอาจจะทำงานหลายโปรเจกต์ ดังนั้น `EmployeeID` จึงกำหนดชุดของ ProjectID ได้หลายชุด เช่น `EmployeeID` 1 (Alice) ทำงานทั้ง Project 101 และ 102
- **ทำไมต้องมี:** เพื่อจัดการความสัมพันธ์ที่ซับซ้อนและป้องกันไม่ให้ข้อมูลผิดพลาดจากการละเลยความสัมพันธ์แบบกลุ่มนี้

---

## Candidate Keys

"บัตรประชาชนของแถวข้อมูล" — Candidate key คือชุด attribute ขั้นต่ำ (minimal) ที่ระบุแต่ละแถวในตารางได้อย่างไม่ซ้ำกัน คุณสมบัติสำคัญ:

- **Uniqueness**: ค่าที่ประกอบกันต้องระบุแถวได้เฉพาะเจาะจง ไม่ซ้ำ
- **Minimality**: ไม่มี subset ย่อยของ candidate key ที่ระบุแถวได้เพียงพอแล้ว (ต้องเป็นชุดที่เล็กที่สุด)
- ตารางหนึ่งอาจมี candidate key ได้มากกว่าหนึ่งชุด
- Candidate key ที่ดีช่วยเพิ่มประสิทธิภาพ query ผ่าน indexing และป้องกันข้อมูลซ้ำซ้อน

---

## Practical Example

พิจารณาตารางติดตามพนักงานกับโปรเจกต์:

| EmployeeID | ProjectID | EmployeeName | ProjectName | Department |
| ---------- | --------- | ------------ | ----------- | ---------- |
| 1          | 101       | Alice        | Project X   | HR         |
| 1          | 102       | Alice        | Project Y   | Finance    |
| 2          | 101       | Bob          | Project X   | HR         |
| 3          | 101       | Charlie      | Project X   | IT         |
| 3          | 102       | Charlie      | Project Y   | Finance    |

- **FD**: `EmployeeID -> EmployeeName` (เช่น EmployeeID 1 -> Alice), `ProjectID -> ProjectName` (ProjectID 101 -> Project X, 102 -> Project Y)
- **MVD**: `{EmployeeID} ->> {ProjectID}` — EmployeeID 1 (Alice) เกี่ยวข้องกับทั้ง ProjectID 101 (แผนก HR) และ 102 (แผนก Finance) สะท้อนความสัมพันธ์แบบ many-to-many ระหว่าง EmployeeID กับ ProjectID
- **Candidate Keys**: มีสองชุดในตัวอย่างนี้คือ (1) `EmployeeID` เพียงตัวเดียว เพราะแต่ละพนักงานมี ID ไม่ซ้ำกัน และ (2) การรวมกันของ `EmployeeID` และ `ProjectID` ซึ่งระบุแถวได้เฉพาะเจาะจง (และยังกำหนด Department ได้ด้วย: `EmployeeID, ProjectID -> Department`)

---

## Comparison Summary

| ประเด็น    | Functional Dependencies                     | Multi-Valued Dependencies (MVDs)                    | Candidate Keys                                 |
| ---------- | -------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------ |
| นิยาม      | ความสัมพันธ์ระหว่าง attribute               | ขยายแนวคิดไปสู่กลุ่มของ attribute                   | ชุด attribute ที่ระบุแถวได้ไม่ซ้ำกัน           |
| แก่นสาระ   | ค่าบาง attribute ถูกกำหนดโดย attribute อื่น | ความสัมพันธ์ระหว่างชุดของ attribute                 | ระบุแต่ละแถวในตารางได้อย่างเฉพาะเจาะจง         |
| ตัวอย่าง   | รู้ attribute หนึ่งแล้วหาอีก attribute ได้  | อธิบายว่าชุด attribute หนึ่งกำหนดอีกชุดอย่างไร      | การรวมกันของ attribute ที่ระบุแต่ละ record ได้ |
| จุดประสงค์ | รักษาความถูกต้องของข้อมูล ลดความซ้ำซ้อน     | จัดระเบียบข้อมูลอย่างมีประสิทธิภาพ ป้องกันความสับสน | บังคับใช้ entity integrity constraint          |
| การใช้งาน  | สำคัญต่อการทำ normalization                 | สำคัญต่อการรักษา data integrity                     | ใช้สร้างความสัมพันธ์ระหว่างตาราง               |

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Functional Dependency (FD) | ความสัมพันธ์ที่ attribute หนึ่ง (determinant) กำหนดค่า attribute อีกตัว (dependent) ได้อย่างเฉพาะเจาะจง เขียนเป็น X -> Y |
| Multi-Valued Dependency (MVD) | ความสัมพันธ์ที่ attribute หนึ่งกำหนด "ชุด" ของค่าที่เป็นไปได้ของอีก attribute เขียนเป็น X ->> {Y1, Y2, ...} |
| Candidate Key | ชุด attribute ขั้นต่ำที่ระบุแต่ละแถวในตารางได้อย่างไม่ซ้ำกัน |
| Normalization | กระบวนการจัดโครงสร้างฐานข้อมูลเพื่อลดความซ้ำซ้อนและรักษาความถูกต้องของข้อมูล โดยอาศัย FD และ MVD เป็นพื้นฐาน |

---

## ❓ My Questions & Gaps

- [ ] MVD ต่างจาก FD อย่างชัดเจนในกรณีใช้งานจริงอย่างไร และการมี MVD ที่ไม่ได้ normalize อาจก่อให้เกิดปัญหาอะไรกับตาราง

---

## 🔗 Resources

- ไม่มีลิงก์อ้างอิงภายนอกในวิดีโอนี้
