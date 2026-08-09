# Best Practices of RDBMS Design

`Tags: RDBMS, database-design, normalization, indexing, partitioning`

| Field            | Value                                            |
| ---------------- | ------------------------------------------------ |
| **Certificate**  | IBM Data Engineering Professional Certificate    |
| **Course**       | C04 Introduction to Relational Databases (RDBMS) |
| **Module**       | M04 Database Design                              |
| **Lesson**       | L02 Best Practices of RDBMS Design               |
| **Date studied** | 2026-08-09                                       |

---

## Table of Contents

- [Overview](#overview)
- [Understand Business Requirements](#understand-business-requirements)
- [Normalize Data to Reduce Redundancy](#normalize-data-to-reduce-redundancy)
- [Denormalize for Performance Optimization](#denormalize-for-performance-optimization)
- [Establish Foreign Key Relationships](#establish-foreign-key-relationships)
- [Indexing for Query Performance](#indexing-for-query-performance)
- [Partitioning for Scalability](#partitioning-for-scalability)
- [Optimize Data Types and Constraints](#optimize-data-types-and-constraints)
- [Plan for Data Growth and Maintenance](#plan-for-data-growth-and-maintenance)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

บทความนี้รวบรวม best practice สำหรับการออกแบบ RDBMS schema เพื่อให้ได้ performance, data integrity, และ flexibility ที่ดี โดยยกตัวอย่างระบบ e-commerce ประกอบทุกหัวข้อ ครอบคลุมตั้งแต่การทำความเข้าใจ business requirement ไปจนถึงการวางแผนรองรับการเติบโตของข้อมูลในระยะยาว

---

## Understand Business Requirements

ก่อนเริ่มออกแบบฐานข้อมูล ต้องเข้าใจ business requirement และความต้องการข้อมูลของแอปพลิเคชันก่อน โดยทำงานร่วมกับ stakeholders อย่างใกล้ชิดเพื่อระบุ entities, relationships, และ data constraints ความเข้าใจ business domain ที่ชัดเจนช่วยให้ออกแบบ schema ที่สะท้อนข้อมูลจริงได้อย่างแม่นยำ

**ตัวอย่าง:** แพลตฟอร์ม e-commerce ที่ต้องจัดการข้อมูลลูกค้า, แคตตาล็อกสินค้า, คำสั่งซื้อ, และธุรกรรม

---

## Normalize Data to Reduce Redundancy

Normalization ช่วยลด data redundancy และเพิ่ม data integrity โดยจัดข้อมูลให้แยกเป็นตารางต่าง ๆ และกำจัดข้อมูลซ้ำซ้อน ลดความเสี่ยงของข้อผิดพลาดเวลา update, insert, หรือ delete ข้อมูล การยึดตาม normal form อย่าง 1NF, 2NF, และ 3NF ช่วยให้ schema มีโครงสร้างที่ logic และรักษาความสอดคล้องของข้อมูล

**ตัวอย่าง:** ลูกค้าที่สั่งซื้อหลายครั้ง แทนที่จะเก็บข้อมูลลูกค้า (ชื่อ, ที่อยู่) ซ้ำในทุกคำสั่งซื้อ ให้แยกตาราง Customers และ Orders ออกจากกัน ช่วยลดข้อมูลซ้ำและทำให้การอัปเดตข้อมูลลูกค้าส่งผลไปยังทุกคำสั่งซื้อที่เกี่ยวข้องโดยอัตโนมัติ

---

## Denormalize for Performance Optimization

ในขณะที่ normalization ช่วยปกป้อง data integrity บางครั้ง denormalization ก็ช่วยเรื่อง performance ได้ Denormalization คือการเพิ่มข้อมูลซ้ำซ้อนหรือรวม (aggregate) ข้อมูลจากหลายตารางเพื่อเพิ่มประสิทธิภาพการ query อย่างไรก็ตามต้องใช้อย่างระมัดระวัง เพราะอาจนำไปสู่ data duplication และความไม่สอดคล้องของข้อมูล ต้องหาสมดุลระหว่าง normalization กับ denormalization ตามความต้องการด้าน performance ของแอปพลิเคชัน

**ตัวอย่าง:** dashboard รายงานที่ดึงข้อมูลยอดขายรวมตามภูมิภาคบ่อย ๆ แทนที่จะ join หลายตารางทุกครั้งที่สร้างรายงาน สามารถ denormalize โดย pre-calculate และเก็บตัวเลขยอดขายรวมตามภูมิภาคไว้ล่วงหน้า ช่วยเพิ่มประสิทธิภาพ query เชิงวิเคราะห์ที่ซับซ้อน

---

## Establish Foreign Key Relationships

การสร้างความสัมพันธ์ระหว่างตารางด้วย foreign key ช่วยรักษา data integrity และบังคับใช้ referential integrity constraint Foreign key ทำให้แต่ละ record ใน child table ต้องสอดคล้องกับ record ที่ valid ใน parent table ป้องกัน orphaned หรือ dangling record ควรกำหนด cascading action เช่น `CASCADE DELETE` หรือ `CASCADE UPDATE` เพื่อรักษาความสอดคล้องของข้อมูลระหว่างตารางที่เกี่ยวข้อง

**ตัวอย่าง:** foreign key constraint บนคอลัมน์ `CustomerID` ในตาราง Orders ที่เชื่อมกับตาราง Customers ทำให้แต่ละคำสั่งซื้อต้องมี record ลูกค้าที่ valid เสมอ ป้องกัน orphaned order

```sql
-- Add a foreign key constraint linking Orders to a valid Customer record
ALTER TABLE Orders
ADD CONSTRAINT fk_customer
FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID);
```

---

## Indexing for Query Performance

Index ที่มีประสิทธิภาพช่วยเพิ่มความเร็วในการดึงข้อมูล ควรระบุคอลัมน์ที่ถูก query บ่อย แล้วสร้าง index บนคอลัมน์เหล่านั้นเพื่อเร่งการค้นหา อย่างไรก็ตาม การสร้าง index มากเกินไปทำให้เกิด overhead ด้าน storage และการดูแลรักษา จึงควร monitor และปรับ index ให้สอดคล้องกับรูปแบบ query และ workload อย่างสม่ำเสมอ

**ตัวอย่าง:** ลูกค้าค้นหาสินค้าจากชื่อหรือหมวดหมู่บ่อย การสร้าง index บนคอลัมน์ `ProductName` และ `Category` ในตาราง Products ช่วยให้การค้นหาเร็วขึ้นอย่างมาก เพราะ database engine หาแถวที่เกี่ยวข้องได้เร็วขึ้น ลดเวลาในการ execute query

```sql
-- Speed up searches on ProductName and Category
CREATE INDEX idx_product_name_category ON Products (ProductName, Category);
```

---

## Partitioning for Scalability

Partitioning คือการแบ่งตารางขนาดใหญ่ออกเป็นส่วนย่อยที่จัดการได้ง่ายขึ้น ตามเกณฑ์ที่กำหนด เช่น range, list, หรือ hash การ partition ช่วยเพิ่ม query performance, manageability, และ availability โดยเฉพาะในสภาพแวดล้อมที่มีข้อมูลขนาดใหญ่มาก การกระจายข้อมูลไปยัง storage device หรือ server หลายตัวช่วยให้ scale ได้แบบ horizontal และประมวลผล query แบบ parallel ได้

**ตัวอย่าง:** แพลตฟอร์ม e-commerce ที่เติบโตเร็วจนตาราง Orders มีขนาดใหญ่มาก สามารถ partition ตาราง Orders ตามช่วงวันที่สั่งซื้อ (เช่น แบ่งเป็นรายเดือน) เพื่อกระจายข้อมูลไปยัง storage หรือ server หลายตัว ช่วยเพิ่ม query performance และรองรับการ scale ได้เมื่อข้อมูลเติบโตขึ้น

---

## Optimize Data Types and Constraints

การเลือก data type และ constraint ที่เหมาะสมสำหรับแต่ละคอลัมน์ช่วยให้ใช้ storage อย่างมีประสิทธิภาพและตรวจสอบความถูกต้องของข้อมูลได้ ควรใช้ data type ที่เล็กที่สุดที่รองรับช่วงค่าของคอลัมน์นั้นได้ เพื่อลด storage overhead นอกจากนี้ควรบังคับใช้ constraint อย่าง `NOT NULL`, `UNIQUE`, และ `CHECK` เพื่อรักษา data integrity และป้องกันการป้อนข้อมูลที่ไม่ถูกต้อง

**ตัวอย่าง:** คอลัมน์ `Quantity` ในตาราง OrderDetails ควรใช้ integer data type เพื่อแทนจำนวนเต็ม และควรบังคับ constraint ให้ค่า `Quantity` มากกว่าศูนย์เสมอด้วย `CHECK` constraint

```sql
-- Ensure Quantity is always a positive whole number
ALTER TABLE OrderDetails
ADD CONSTRAINT chk_quantity_positive CHECK (Quantity > 0);
```

---

## Plan for Data Growth and Maintenance

ควรคาดการณ์การเติบโตของข้อมูลในอนาคตและวางแผน schema ให้รองรับการ scale ตั้งแต่ต้น ควรมีกลยุทธ์ backup และ recovery ที่แข็งแรงเพื่อป้องกันข้อมูลสูญหายและรักษาความต่อเนื่องของธุรกิจ ควร monitor database performance, วิเคราะห์ query execution plan, และทำ performance tuning อย่างสม่ำเสมอเพื่อ optimize การใช้ทรัพยากรและรักษาความเร็วในการตอบสนอง

**ตัวอย่าง:** ระบบ e-commerce อาจต้อง archive คำสั่งซื้อเก่าเป็นระยะเพื่อจัดการขนาดฐานข้อมูลและ optimize performance การมีกลยุทธ์ data archiving ช่วยลดผลกระทบของการเติบโตของข้อมูลต่อ query performance และ storage resource งาน maintenance ประจำ เช่น index rebuild และ statistics update ก็จำเป็นต่อการรักษา performance ที่ดี

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Normalization | กระบวนการจัดข้อมูลให้ลด redundancy โดยยึดตาม normal form (1NF, 2NF, 3NF) |
| Denormalization | การเพิ่มข้อมูลซ้ำซ้อนหรือรวมข้อมูลจากหลายตารางโดยตั้งใจ เพื่อเพิ่ม query performance |
| Foreign key | Constraint ที่เชื่อม column ใน child table กับ primary key ใน parent table เพื่อรักษา referential integrity |
| Referential integrity | หลักการที่รับประกันว่าความสัมพันธ์ระหว่างตารางยังคงถูกต้องอยู่เสมอ ไม่มี orphaned record |
| CASCADE DELETE / CASCADE UPDATE | Action ที่กำหนดให้การลบ/แก้ไข record ใน parent table ส่งผลต่อ record ที่เกี่ยวข้องใน child table โดยอัตโนมัติ |
| Index | โครงสร้างข้อมูลที่ช่วยเร่งความเร็วในการค้นหา/ดึงข้อมูลจากตาราง |
| Partitioning | การแบ่งตารางขนาดใหญ่ออกเป็นส่วนย่อยตามเกณฑ์ เช่น range, list, hash เพื่อเพิ่ม performance และ scalability |
| Horizontal scalability | ความสามารถในการรองรับโหลดที่เพิ่มขึ้นโดยกระจายข้อมูล/งานไปยัง server หรือ storage หลายตัว |
| CHECK constraint | Constraint ที่ตรวจสอบว่าค่าที่ป้อนเข้าตรงตามเงื่อนไขที่กำหนด เช่น ต้องมากกว่าศูนย์ |
| Data archiving | การย้ายข้อมูลเก่าที่ไม่ค่อยถูกใช้งานออกจากตารางหลัก เพื่อจัดการขนาดฐานข้อมูลและ performance |

---

## ❓ My Questions & Gaps

- [ ] ในการ partition ตาราง ควรเลือกระหว่าง range, list, หรือ hash partitioning อย่างไรให้เหมาะกับ workload แต่ละแบบ
- [ ] การตั้ง index มากเกินไปส่งผลต่อ write performance (insert/update) อย่างไรบ้าง และมีวิธี monitor ผลกระทบนี้อย่างไร
- [ ] แนวทาง data archiving ที่ดีควรเก็บข้อมูลเก่าไว้ที่ไหน (cold storage, separate table, data warehouse) และเข้าถึงย้อนหลังอย่างไรเมื่อจำเป็น

---

## 🔗 Resources

- [PostgreSQL Documentation — Indexes](https://www.postgresql.org/docs/current/indexes.html)
- [PostgreSQL Documentation — Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)
