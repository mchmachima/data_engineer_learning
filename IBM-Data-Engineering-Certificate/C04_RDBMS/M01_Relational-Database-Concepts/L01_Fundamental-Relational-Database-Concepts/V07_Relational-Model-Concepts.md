# Relational Model Concepts

`Tags: RDBMS, set theory, relation, tuple, degree, cardinality`

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
- [Sets and Set Operations](#sets-and-set-operations)
- [Relations and Their Properties](#relations-and-their-properties)
- [Relation Schema vs. Relation Instance](#relation-schema-vs-relation-instance)
- [Degree and Cardinality](#degree-and-cardinality)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้ปิดท้าย lesson ด้วยรากฐานทางคณิตศาสตร์ของ relational model ตั้งแต่แนวคิดเรื่อง set และ operation พื้นฐาน ไปจนถึง relation และคุณสมบัติของมัน (reflexivity, symmetry, transitivity, anti-symmetry) รวมถึงความแตกต่างระหว่าง relation schema กับ relation instance และปิดท้ายด้วยคำว่า degree กับ cardinality ที่ใช้บอกขนาดของ relation

---

## Sets and Set Operations

Set คือกลุ่มของ element ที่ไม่ซ้ำกันและไม่มีลำดับ ประกอบด้วยรายการที่เป็นชนิดเดียวกัน มักเขียนแทนด้วยวงเล็บปีกกา (ระบุ element ไว้ข้างใน) หรือ set-builder notation (เงื่อนไขที่อธิบายการเป็นสมาชิก) Set เป็นรากฐานของคณิตศาสตร์สมัยใหม่หลายแขนง รวมถึง algebra, geometry และ probability

แนวคิดและ operation พื้นฐานของ set:

| Concept | Notation | ความหมาย |
| --- | --- | --- |
| Membership | `a ∈ A` | `a` เป็นสมาชิกของ set `A` |
| Subset | `A ⊆ B` | ทุก element ของ `A` เป็น element ของ `B` ด้วย |
| Union | `A ∪ B` | Element ที่อยู่ใน `A`, ใน `B`, หรือทั้งคู่ |
| Intersection | `A ∩ B` | Element ที่อยู่ทั้งใน `A` และ `B` |
| Difference | `A − B` (หรือ `A / B`) | Element ที่อยู่ใน `A` แต่ไม่อยู่ใน `B` |
| Empty set | `{}` หรือ `∅` | Set ที่ไม่มี element ใด ๆ เป็น subset ของทุก set |
| Power set | `P(A)` | Set ของ subset ที่เป็นไปได้ทั้งหมดของ `A` รวมถึง `∅` และ `A` เอง |
| Universal set | `U` | Set ที่รวมทุก object ที่พิจารณา; set อื่นทั้งหมดเป็น subset ของมัน |
| Disjoint sets | — | สอง set ที่ไม่มี element ร่วมกันเลย |

Venn diagram เป็นการนำเสนอเชิงภาพที่ใช้แสดงความสัมพันธ์เชิงตรรกะระหว่าง set

---

## Relations and Their Properties

Relation คือแนวคิดทางคณิตศาสตร์ที่สร้างบนแนวคิดของ set — อธิบายความเชื่อมโยงระหว่าง element ของ set และเป็นแนวคิดสำคัญของ set theory และ logic ประเภทที่พบบ่อยได้แก่:

- **Binary relation** — ความเชื่อมโยงระหว่าง element สองตัว (เช่น relation "less than" อย่าง 3 < 5)
- **Ordered pairs** — subset ของ Cartesian product `A × B` แทน binary relation บน set `A` และ `B` เขียนแทนด้วย `(a, b)`

Relation อาจมีคุณสมบัติดังนี้:

| Property | นิยาม | ตัวอย่าง |
| --- | --- | --- |
| Reflexivity | Element แต่ละตัวสัมพันธ์กับตัวมันเอง | Equality — `A = A` สำหรับทุก element `A` |
| Symmetry | ถ้า `A` สัมพันธ์กับ `B` แล้ว `B` ก็สัมพันธ์กับ `A` ด้วย | "Is a sibling of" |
| Transitivity | ถ้า `A` สัมพันธ์กับ `B` และ `B` สัมพันธ์กับ `C` แล้ว `A` สัมพันธ์กับ `C` | "Less than" — ถ้า `A < B` และ `B < C` แล้ว `A < C` |
| Anti-symmetry | ถ้า `A` สัมพันธ์กับ `B` และ `B` สัมพันธ์กับ `A` แล้ว `A` ต้องเท่ากับ `B` | "Less than or equal to" |

---

## Relation Schema vs. Relation Instance

Relation ประกอบด้วยองค์ประกอบสำคัญ 2 อย่าง:

- **Relation schema** — ระบุโครงสร้าง: ชื่อของ relation และชื่อ/data type ของแต่ละคอลัมน์ (attribute) เช่น สำหรับ relation `Author`: `Author_ID` (CHAR — string ความยาวคงที่), `last_name`, `first_name`, `email` (VARCHAR — string ความยาวไม่คงที่) และ `country` (CHAR)
- **Relation instance** — ข้อมูลจริงในโลกจริงที่จัดเก็บในตาราง ประกอบด้วยแถวและคอลัมน์ คอลัมน์สอดคล้องกับ attribute ที่กำหนดใน schema และแถวแทน tuple (record แต่ละรายการ)

---

## Degree and Cardinality

- **Degree** — จำนวน attribute (คอลัมน์) ใน relation
- **Cardinality** — จำนวน tuple (แถว) ใน relation

ในตัวอย่าง `Author` ของบทเรียน: degree เท่ากับ 6 (หกคอลัมน์: `Author_ID`, `last_name`, `first_name`, `email`, `city`, `country`) และ cardinality เท่ากับ 5 (ห้าแถวของข้อมูล)

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Set | กลุ่มของ element ที่ไม่ซ้ำกันและไม่มีลำดับ |
| Relation | แนวคิดทางคณิตศาสตร์ที่สร้างบนแนวคิดของ set อธิบายความเชื่อมโยงระหว่าง element |
| Binary relation | Relation ที่สร้างความเชื่อมโยงระหว่าง element สองตัว |
| Ordered pair | Subset ของ Cartesian product ของสอง set แทน binary relation |
| Reflexivity | คุณสมบัติของ relation ที่ element แต่ละตัวสัมพันธ์กับตัวมันเอง |
| Symmetry | คุณสมบัติของ relation ที่ A สัมพันธ์กับ B แล้วนัยว่า B สัมพันธ์กับ A |
| Transitivity | คุณสมบัติของ relation ที่ A สัมพันธ์กับ B และ B สัมพันธ์กับ C แล้วนัยว่า A สัมพันธ์กับ C |
| Anti-symmetry | คุณสมบัติของ relation ที่ A สัมพันธ์กับ B และ B สัมพันธ์กับ A แล้วนัยว่า A เท่ากับ B |
| Relation schema | โครงสร้างของ relation — ชื่อและชื่อ/type ของแต่ละ attribute |
| Relation instance | ข้อมูลจริง (แถวและคอลัมน์) ที่จัดเก็บสำหรับ relation |
| Tuple | แถวหนึ่งใน relation instance |
| Degree | จำนวน attribute (คอลัมน์) ใน relation |
| Cardinality (ในความหมาย relational model) | จำนวน tuple (แถว) ใน relation |

---

## ❓ My Questions & Gaps

- [ ] คุณสมบัติของ relation (reflexivity, symmetry, transitivity, anti-symmetry) เชื่อมโยงกับการตัดสินใจออกแบบฐานข้อมูลจริงอย่างไร หรือเป็นเพียงรากฐานเชิงทฤษฎี
- [ ] แนวคิด "relation" ของ relational model ต่างจาก SQL "table" ในทางปฏิบัติอย่างไร มี edge case ที่ต่างกันหรือไม่ (เช่น แถวที่ซ้ำกัน)
- [ ] Cardinality ในความหมายของ relational model (จำนวนแถว) สับสนกับ cardinality ในความสัมพันธ์แบบ ER diagram (one-to-many ฯลฯ) หรือไม่ ควรแยกสองความหมายนี้อย่างไร

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่กล่าวถึงในวิดีโอนี้
