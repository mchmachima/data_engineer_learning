# Data Wrangling

Tags: data wrangling, data cleaning, ETL

| Field            | Value                                         |
| ---------------- | --------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate |
| **Course**       | C01 Introduction to Data Engineering          |
| **Module**       | M03 Data Platform, Lifecycle, and Governance  |
| **Lesson**       | L02 Data Collection and Data Wrangling        |
| **Date studied** | 2026-06-13                                    |

---

## Table of Contents

- [Overview](#overview)
- [Transformation Tasks](#transformation-tasks)
- [Data Cleaning](#data-cleaning)
- [Wrangling Tools](#wrangling-tools)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบาย data wrangling (หรือ data munging) ซึ่งเป็นกระบวนการวนซ้ำระหว่าง explore → transform → validate → prepare พร้อมงาน transform หลัก วิธีทำความสะอาดข้อมูล และเครื่องมือที่ใช้กันทั่วไป

---

## Transformation Tasks

**Structuring:**

- **Joins** — รวม _คอลัมน์_ จากสองตารางเข้าเป็นแถวเดียว
- **Unions** — รวม _แถว_ จากสองตารางเข้าเป็นตารางเดียว

**Normalization** — ลดความซ้ำซ้อนของข้อมูล; เหมาะกับระบบ OLTP

**Denormalization** — รวมตารางเข้าด้วยกันเพื่อให้ query เร็วขึ้น; ใช้ก่อนรัน analytical report

---

## Data Cleaning

**ขั้นที่ 1 — ตรวจหาปัญหา:**

- Data profiling (ตรวจสอบโครงสร้าง เนื้อหา และความผิดปกติ)
- Data visualization (หาค่าผิดปกติผ่านกราฟทางสถิติ)

**ขั้นที่ 2 — แก้ไขปัญหา:**

| Issue                   | Fix                                                                   |
| ----------------------- | --------------------------------------------------------------------- |
| ค่าที่หายไป             | กรองออก, หาแหล่งข้อมูลภายนอก, หรือทำ imputation (คำนวณจากค่าทางสถิติ) |
| ข้อมูลซ้ำ               | ลบ record ที่ซ้ำกันออก                                                |
| ข้อมูลที่ไม่เกี่ยวข้อง  | กรอง field ที่ไม่เกี่ยวกับ use case ออก                               |
| ข้อผิดพลาดของ data type | แปลงให้เป็น type ที่ถูกต้อง (ตัวเลข, วันที่)                          |
| รูปแบบไม่สอดคล้องกัน    | ปรับให้เป็นมาตรฐานเดียวกัน (ตัวพิมพ์, วันที่, หน่วยวัด)               |
| ข้อผิดพลาดด้าน syntax   | แก้ช่องว่างเกิน, การพิมพ์ผิด, คำย่อ                                   |
| ค่าผิดปกติ (outlier)    | ตรวจสอบเพิ่มเติม — อาจเป็นข้อผิดพลาดหรือค่าจริงที่สุดโต่ง             |

---

## Wrangling Tools

| Tool                   | Key Strength                                                   |
| ---------------------- | -------------------------------------------------------------- |
| Excel / Google Sheets  | สูตรคำนวณที่รวดเร็ว; Power Query สำหรับ import และ transform   |
| OpenRefine             | open-source, ใช้เมนู, ไม่ต้องเขียนโค้ด                         |
| Google DataPrep        | ตรวจจับ schema และความผิดปกติอัตโนมัติ, fully managed          |
| Watson Studio Refinery | เครื่องมือของ IBM ตรวจจับ type อัตโนมัติ, บังคับใช้ governance |
| Python (Pandas, NumPy) | ยืดหยุ่น, ทำ transformation แบบ programmatic ในขนาดใหญ่ได้     |
| R (dplyr, data.table)  | wrangling เชิงสถิติ, รวมข้อมูลชุดใหญ่ได้ดี                     |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์)    | คำอธิบาย (ภาษาไทย)                                                       |
| --------------- | ------------------------------------------------------------------------ |
| Data Wrangling  | กระบวนการวนซ้ำในการแปลงและทำความสะอาดข้อมูลดิบให้พร้อมสำหรับการวิเคราะห์ |
| Data Profiling  | การตรวจสอบข้อมูลต้นทางเพื่อเข้าใจโครงสร้าง เนื้อหา และความผิดปกติ        |
| Normalization   | การจัดข้อมูลเพื่อลดความซ้ำซ้อน — เหมาะกับ OLTP                           |
| Denormalization | การรวมตารางเพื่อความเร็วในการ query — เหมาะกับ OLAP และการทำรายงาน       |
| Imputation      | การเติมค่าที่หายไปด้วยวิธีทางสถิติ                                       |

---

## ❓ My Questions & Gaps

- [ ] Normalization กับ Denormalization ควรใช้ร่วมกันในระบบเดียวได้หรือไม่ และในสถานการณ์ใด?

---

## 🔗 Resources

- [OpenRefine](https://openrefine.org/)
