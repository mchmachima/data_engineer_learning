# Getting Started with MySQL

`Tags: RDBMS, MySQL, MariaDB, database administration tools`

| Field            | Value                                            |
| ---------------- | ------------------------------------------------ |
| **Certificate**  | IBM Data Engineering Professional Certificate    |
| **Course**       | C04 Introduction to Relational Databases (RDBMS) |
| **Module**       | M03 MySQL and PostgreSQL                         |
| **Lesson**       | L01 MySQL                                        |
| **Date studied** | 2026-08-09                                       |

---

## Table of Contents

- [Overview](#overview)
- [What Is MySQL and Deployment Options](#what-is-mysql-and-deployment-options)
- [Applications of MySQL](#applications-of-mysql)
- [MySQL Administration Tools](#mysql-administration-tools)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

วิดีโอนี้แนะนำ MySQL ในภาพรวม ตั้งแต่นิยามของ MySQL ในฐานะ open-source RDBMS และรูปแบบการ deploy ที่หลากหลาย ไปจนถึงตัวอย่าง application จริงที่ใช้ MySQL ในหลายระดับตั้งแต่เว็บไซต์ขนาดใหญ่จนถึงธุรกิจขนาดเล็ก และปิดท้ายด้วยเครื่องมือสำหรับบริหารจัดการ MySQL 4 ตัว พร้อมเปรียบเทียบ MySQL Workbench กับ phpMyAdmin ซึ่งเป็นสองเครื่องมือที่ใช้งานบ่อยที่สุด

---

## What Is MySQL and Deployment Options

MySQL เป็น open-source relational database management system (RDBMS) ที่ใช้สร้าง จัดการ และโต้ตอบกับฐานข้อมูล **MariaDB** เป็น fork ของ MySQL ที่พัฒนาโดยผู้พัฒนา MySQL รุ่นดั้งเดิมบางส่วน

MySQL มีให้เลือกใช้งานหลายรูปแบบ:

- **Community edition** — ดาวน์โหลดและติดตั้งได้ฟรีภายใต้สัญญาอนุญาต GNU General Public License (GPL) นำไป embed ในแอปพลิเคชันได้
- **Commercial editions** — เวอร์ชัน standard, enterprise, และ cluster ที่มีฟีเจอร์เพิ่มเติมสำหรับซื้อใช้งาน
- **Cloud deployment** — self-managed บน virtual machine หรือ container หรือใช้ managed service เช่น IBM Cloud, Amazon RDS, Azure Database, และ Google Cloud SQL เพื่อความสะดวกในการ deploy

---

## Applications of MySQL

- **เว็บไซต์ขนาดใหญ่** เช่น Facebook, YouTube, Twitter เลือกใช้ MySQL เพราะ scalability, performance, และ reliability
- **แพลตฟอร์ม e-commerce** เช่น Shopify, Magento, WooCommerce ใช้จัดการข้อมูลสินค้า ข้อมูลลูกค้า และธุรกรรมจำนวนมาก
- **ธุรกิจขนาดเล็กถึงกลาง** ใช้ MySQL เพราะราคาย่อมเยา ใช้งานง่าย และมีฟีเจอร์หลากหลาย รองรับ internal database, ระบบ customer relationship management (CRM), และซอฟต์แวร์บัญชี

---

## MySQL Administration Tools

มีเครื่องมือหลักสำหรับบริหารจัดการ MySQL ดังนี้:

- **MySQL CLI** — command line interface สำหรับโต้ตอบกับ MySQL server และข้อมูลผ่านคำสั่ง ทำได้ทั้งแบบ interactive และรันจากไฟล์ text (batch mode) เช่นคำสั่ง `show databases` เพื่อแสดงรายชื่อฐานข้อมูล database administrator ใช้เพื่อจัดการ server โดยตรง จัดการสิทธิ์ และ monitor ฐานข้อมูล ส่วน developer ใช้สำหรับสร้าง แก้ไข และเขียน script ฐานข้อมูล และ system administrator ใช้สำหรับตั้งค่า server ปรับ performance และแก้ปัญหาระบบ
- **mysqladmin** — command line program สำหรับงานบริหารจัดการ RDBMS พร้อม MySQL utilities เฉพาะทางอื่น ๆ สำหรับงานเฉพาะด้าน
- **MySQL Workbench** — desktop application (รองรับ Windows, Linux, macOS) ที่รวม SQL development, administration, และ database design ไว้ในที่เดียว หน้า administration ให้ข้อมูลการเชื่อมต่อ, server feature, import-export ข้อมูล, server log และ performance report ส่วนหน้า schemas ใช้จัดการ database object และเข้าถึงเอกสารช่วยเหลือ เหมาะกับ database developer/designer, database administrator, data analyst/scientist และบริษัทพัฒนาซอฟต์แวร์
- **phpMyAdmin** — third-party web-based GUI สำหรับจัดการ MySQL ผ่านเบราว์เซอร์ เมื่อเชื่อมต่อ server แล้วจะเห็นข้อมูล server และฐานข้อมูลระบบ สร้างฐานข้อมูลได้ผ่าน tab ต่าง ๆ นิยมในกลุ่ม web hosting provider, เจ้าของเว็บไซต์ที่มีความรู้ด้านเทคนิคจำกัด และถูกฝังเป็นเครื่องมือใน CMS อย่าง WordPress และ Drupal

### MySQL Workbench vs. phpMyAdmin

| แง่มุม | MySQL Workbench | phpMyAdmin |
| --- | --- | --- |
| รูปแบบ | Desktop application | Web-based tool |
| License | มีทั้ง commercial และ open-source | Free และ open-source |
| ขอบเขตเครื่องมือ | Toolkit ครบวงจรสำหรับ design, develop, deploy ฐานข้อมูล | เครื่องมือเรียบง่าย เน้นจัดการฐานข้อมูล |
| กลุ่มผู้ใช้หลัก | บริษัทพัฒนาซอฟต์แวร์, database administrator, data analyst | บริษัท web hosting, ธุรกิจขนาดเล็ก, ผู้ใช้ทั่วไป |

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| MySQL | Open-source relational database management system (RDBMS) สำหรับสร้าง จัดการ และโต้ตอบกับฐานข้อมูล |
| MariaDB | Fork ของ MySQL ที่พัฒนาโดยผู้พัฒนา MySQL รุ่นดั้งเดิมบางส่วน |
| RDBMS | Relational Database Management System ระบบจัดการฐานข้อมูลเชิงสัมพันธ์ |
| GNU GPL | General Public License สัญญาอนุญาต open source ที่ MySQL community edition ใช้ |
| Managed service | บริการฐานข้อมูลบน cloud ที่ผู้ให้บริการดูแลโครงสร้างพื้นฐานให้ เช่น Amazon RDS, Azure Database |
| MySQL CLI | Command line interface สำหรับโต้ตอบกับ MySQL server ผ่านคำสั่ง |
| mysqladmin | Command line program สำหรับงานบริหารจัดการ RDBMS |
| MySQL Workbench | Desktop application รวม SQL development, administration, และ database design |
| phpMyAdmin | Web-based GUI สำหรับจัดการฐานข้อมูล MySQL ผ่านเบราว์เซอร์ |

---

## ❓ My Questions & Gaps

- [ ] ในงาน data engineering จริง ควรเลือกใช้ MySQL CLI, MySQL Workbench, หรือ phpMyAdmin ในสถานการณ์ไหนบ้าง

---

## 🔗 Resources

- ไม่มีลิงก์อ้างอิงภายนอกในวิดีโอนี้
