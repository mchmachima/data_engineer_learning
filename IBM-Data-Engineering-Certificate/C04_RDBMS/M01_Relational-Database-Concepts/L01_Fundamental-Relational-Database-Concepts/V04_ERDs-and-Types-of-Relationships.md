# ERDs and Types of Relationships

`Tags: RDBMS, ERD, entity relationship diagram, crow's foot notation`

| Field             | Value                                            |
| ----------------- | ------------------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate    |
| **Course**        | C04 Introduction to Relational Databases (RDBMS) |
| **Module**        | M01 Relational Database Concepts                 |
| **Lesson**        | L01 Fundamental Relational Database Concepts     |
| **Date studied**  | 2026-07-12                                       |

---

## Table of Contents

- [Overview](#overview)
- [What is an ERD?](#what-is-an-erd)
- [Fundamental Components of an ERD](#fundamental-components-of-an-erd)
- [Types of Relationships](#types-of-relationships)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบาย ERD (Entity Relationship Diagram) ซึ่งใช้แสดงความสัมพันธ์ระหว่าง entity ในฐานข้อมูลก่อนแปลงเป็นตารางจริง ครอบคลุมองค์ประกอบพื้นฐานสามอย่างของ ERD และประเภทความสัมพันธ์สามแบบ (one-to-one, one-to-many, many-to-many) พร้อมสัญลักษณ์ crow's foot notation ที่ใช้บอกลักษณะความสัมพันธ์นั้น

---

## What is an ERD?

ERD (Entity Relationship Diagram) คือการนำเสนอเชิงภาพที่แสดงความสัมพันธ์และปฏิสัมพันธ์ระหว่าง entity ในฐานข้อมูล แสดงโครงสร้างเชิงตรรกะของระบบฐานข้อมูล โดยแสดง entity และความสัมพันธ์ระหว่างกันเป็นเส้นเชื่อมระหว่างกล่อง

---

## Fundamental Components of an ERD

ERD ประกอบด้วยองค์ประกอบพื้นฐาน 3 อย่าง:

- **Entities** — แทนบุคคล, วัตถุ หรือแนวคิดที่จัดเก็บข้อมูลในฐานข้อมูล เป็นส่วนประกอบพื้นฐาน แสดงเป็นสี่เหลี่ยม และมี attribute (คุณสมบัติ) ที่อธิบายคุณลักษณะเฉพาะ (เช่น entity `Book` มี attribute อย่าง title, edition, year, price; entity `Author` มี attribute อย่าง last name, first name, email, city, country, author ID) แต่ละ attribute เชื่อมกับ entity เพียงตัวเดียวเท่านั้น entity เป็นพื้นฐานสำหรับความสัมพันธ์ในโมเดลฐานข้อมูล
- **Relationship sets** — แสดงว่า entity เชื่อมโยงหรือสัมพันธ์กันอย่างไร แสดงว่า instance ของ entity หนึ่งสัมพันธ์กับ instance ของอีก entity อย่างไร แทนด้วยรูปสี่เหลี่ยมข้าวหลามตัด (diamond) พร้อมเส้นเชื่อมไปยัง entity ที่เกี่ยวข้อง diagram ที่แสดงประเภทความสัมพันธ์มักมีแค่ entity เท่านั้น (ไม่มี attribute) เพื่อไม่ให้ดูรก
- **Crow's foot notation** — สัญลักษณ์เชิงภาพที่บ่งบอกลักษณะและปริมาณของความสัมพันธ์ระหว่าง entity: สี่เหลี่ยมสำหรับ entity set, สี่เหลี่ยมข้าวหลามตัดสำหรับ relationship set และสัญลักษณ์อย่าง `>`, `<` และเส้นแนวตั้ง เพื่อบ่งบอกว่าความสัมพันธ์เป็นแบบ one-to-one, one-to-many หรือ many-to-many

---

## Types of Relationships

ใช้ตัวอย่าง Book/Author: หนังสือหนึ่งเล่มต้องมีผู้แต่งอย่างน้อยหนึ่งคน (และอาจมีมากกว่านั้น) และผู้แต่งหนึ่งคนสามารถเขียนหนังสือได้หนึ่งเล่มหรือมากกว่า ลักษณะของความเชื่อมโยงนี้เป็นตัวกำหนดประเภทความสัมพันธ์

| Relationship Type | นิยาม | สัญลักษณ์ Crow's Foot | ตัวอย่าง Book/Author |
| --- | --- | --- | --- |
| One-to-one | Entity แต่ละตัวใน set มีความสัมพันธ์เพียงหนึ่งเดียว | เส้นหนา/เรียบ ไม่มี crow's foot | หนังสือแต่ละเล่มเขียนโดยผู้แต่งคนเดียว ("Authored by") |
| One-to-many (หรือ many-to-one) | Entity หนึ่งตัวมีส่วนร่วมในความสัมพันธ์หลายรายการภายใน set | สัญลักษณ์ less-than (`<`) ด้านหนึ่ง | หนังสือหนึ่งเล่มมีผู้แต่งหลายคน; มองอีกมุมคือผู้แต่งหลายคนร่วมเขียนหนังสือเล่มเดียว |
| Many-to-many | Instance หลายตัวของ entity หนึ่งสัมพันธ์กับ instance หลายตัวของอีก entity | สัญลักษณ์ greater-than และ less-than (`>` ... `<`) ทั้งสองด้าน | ผู้แต่งหลายคนเขียนหนังสือหลายเล่ม |

แผนภาพอย่างง่ายของแต่ละประเภท (Book–Author):

```
One-to-One:      [ Book ] ──────── [ Author ]
                  (หนังสือแต่ละเล่มมีผู้แต่งเพียงคนเดียว)

One-to-Many:      [ Book ] ───────≺ [ Author ]
                  (หนังสือหนึ่งเล่ม มีผู้แต่งหลายคน)

Many-to-Many:     [ Book ] ≻─────≺ [ Author ]
                  (หนังสือหลายเล่ม ผู้แต่งหลายคน)
```

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| ERD | Entity Relationship Diagram — การนำเสนอเชิงภาพ/graphical ของ entity และความสัมพันธ์ในฐานข้อมูล |
| Entity | วัตถุ แนวคิด หรือสิ่งของในโลกจริงที่จัดเก็บและจัดการข้อมูล แสดงเป็นสี่เหลี่ยมใน ERD |
| Attribute | คุณลักษณะ (property) ของ entity แสดงเป็นวงรี เชื่อมกับ entity เพียงตัวเดียว |
| Relationship set | องค์ประกอบรูปสี่เหลี่ยมข้าวหลามตัดที่แสดงว่า entity สองตัวเชื่อมโยงกันอย่างไร |
| Crow's foot notation | Notation ที่ใช้สัญลักษณ์ (>, <, เส้นแนวตั้ง) เพื่อบ่งบอกชนิดและปริมาณของความสัมพันธ์ |
| Relationship | ความเชื่อมโยงที่แสดงว่า entity สัมพันธ์กันอย่างไร แสดงเป็นเส้นระหว่างสี่เหลี่ยมของ entity |
| One-to-one relationship | Instance ของ entity หนึ่งเชื่อมกับ instance เพียงหนึ่งเดียวของอีก entity |
| One-to-many relationship | Instance ของ entity หนึ่งเชื่อมกับ instance หลายตัวของอีก entity |
| Many-to-many relationship | Instance หลายตัวของ entity หนึ่งเชื่อมกับ instance หลายตัวของอีก entity |
| Cardinality (ในความหมาย ERD) | ลักษณะเชิงตัวเลขของความสัมพันธ์ (one vs many) ระหว่าง entity ที่เชื่อมกัน |
| Foreign key | Field ที่เชื่อมโยงตารางหนึ่งไปยัง primary key ของอีกตาราง แทนความสัมพันธ์ |

---

## ❓ My Questions & Gaps

- [ ] Crow's foot notation แยกความแตกต่างระหว่าง optional participation (zero-or-many) กับ mandatory participation (one-or-many) ได้อย่างไร
- [ ] ความสัมพันธ์แบบ many-to-many ถูก implement จริงในระดับ schema อย่างไร (เช่นผ่าน junction/associative table) — วิดีโอนี้ยังไม่ครอบคลุม
- [ ] เหตุใด attribute มักถูกละไว้ใน diagram ที่แสดงประเภทความสัมพันธ์ และควรใส่กลับเมื่อไร
- [ ] ความสัมพันธ์ (เช่น one-to-many ระหว่าง `Author` กับ `Book`) ถูก implement ในระดับตารางอย่างไร — ผ่าน foreign key — เนื่องจากวิดีโอนี้ยังไม่ได้ลงรายละเอียดว่า foreign key เชื่อมกับ relationship ที่วาดใน ERD อย่างไร

---

## 🔗 Resources

- https://www.geeksforgeeks.org/dbms/introduction-of-er-model/
