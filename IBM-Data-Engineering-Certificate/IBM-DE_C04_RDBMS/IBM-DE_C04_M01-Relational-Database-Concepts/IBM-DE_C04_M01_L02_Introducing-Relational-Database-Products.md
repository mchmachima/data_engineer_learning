# L02 Introducing Relational Database Products

`Tags: RDBMS, database, Db2, MySQL, PostgreSQL, normalization`

| Field            | Value                                            |
| ---------------- | ------------------------------------------------ |
| **Certificate**  | IBM Data Engineering Professional Certificate    |
| **Course**       | C04 Introduction to Relational Databases (RDBMS) |
| **Module**       | M01 Relational Database Concepts                 |
| **Date studied** | 2026-07-30                                       |

---

## Table of Contents

- [Overview](#overview)
- [Database Architecture](#database-architecture)
- [Distributed Architecture and Clustered Databases](#distributed-architecture-and-clustered-databases)
- [Database Usage Patterns](#database-usage-patterns)
- [Introduction to Relational Database Offerings](#introduction-to-relational-database-offerings)
- [Db2](#db2)
- [MySQL](#mysql)
- [PostgreSQL](#postgresql)
- [Database normalization](#database-normalization)
- [📖 Key Terms & Glossary](#-key-terms--glossary)
- [❓ My Questions & Gaps](#-my-questions--gaps)
- [🔗 Resources](#-resources)

---

## Overview

บทเรียนนี้พาไปสำรวจภาพรวมของผลิตภัณฑ์ฐานข้อมูลเชิงสัมพันธ์ (relational database) ตั้งแต่รูปแบบสถาปัตยกรรมการติดตั้งใช้งาน (deployment topology) แบบ single-tier, two-tier และ three-tier ไปจนถึงสถาปัตยกรรมแบบกระจาย (distributed architecture) ที่ช่วยเพิ่ม scalability และ fault tolerance ให้กับ workload ขนาดใหญ่ นอกจากนี้ยังครอบคลุมว่าผู้ใช้งานแต่ละกลุ่ม เช่น data engineer, DBA, data scientist และ application developer ใช้เครื่องมืออะไรในการเข้าถึงฐานข้อมูล พร้อมทั้งเจาะลึกผลิตภัณฑ์ RDBMS ยอดนิยมสามตัวคือ Db2, MySQL และ PostgreSQL รวมถึงแนวคิดขั้นสูงของโมเดลเชิงสัมพันธ์อย่าง functional dependency, multi-valued dependency และ candidate key ซึ่งเป็นพื้นฐานสำคัญของการทำ normalization

---

## Database Architecture

Deployment topology คือรูปแบบการจัดวางองค์ประกอบของ hardware, software และ network ในการติดตั้งระบบ ซึ่งเลือกใช้ตามปัจจัยด้าน scalability, performance, reliability และลักษณะของแอปพลิเคชัน มีรูปแบบหลักดังนี้

- **Single-tier architecture**: ทุกองค์ประกอบ (UI, application logic, data storage) อยู่บนเครื่องเดียวกัน
- **Two-tier (client-server) architecture**: แบ่งเป็น client layer (UI) และ server layer (application logic + data storage) โดย client เชื่อมต่อกับ database server ผ่าน database interface เช่น API หรือ framework ฝั่ง server จะมี data access layer (รองรับ JDBC, ODBC, CLP และ interface เฉพาะของแต่ละ vendor), database engine layer (คอมไพล์ query, ดึงและประมวลผลข้อมูล) และ database storage layer
- **Three-tier architecture**: เพิ่ม middle tier หรือ application server layer คั่นระหว่าง client กับ database server นิยมใช้ใน production เพราะช่วยเรื่อง security (จำกัดการเข้าถึง database server เฉพาะ admin), performance optimization และ maintainability เช่น ระบบ internet banking ที่ mobile app เชื่อมต่อกับ application server ก่อนจะไปคุยกับ database server อีกที
- **Cloud-based deployment**: database อยู่บน cloud environment ไม่ต้องติดตั้งหรือดูแล infrastructure เอง เข้าถึงได้ทุกที่ที่มีอินเทอร์เน็ต เหมาะกับทั้งงาน development, testing และ production

---

## Distributed Architecture and Clustered Databases

สำหรับ workload ขนาดใหญ่หรือที่ต้องการ high availability RDBMS จะใช้สถาปัตยกรรมแบบกระจาย (distributed architecture) ซึ่งเป็นกลุ่มของเครื่อง (cluster) ที่เชื่อมต่อกันผ่านเครือข่าย ช่วยเพิ่ม scalability, fault tolerance และ performance

ประเภทสถาปัตยกรรมหลัก:

- **Shared Disk**: หลาย database server ใช้ storage ทางกายภาพเดียวกันร่วมกัน (common disk) และประสานงานกันผ่าน high-speed interconnection กระจายภาระงานได้ดี และหาก server ตัวใดล่มก็สามารถ reroute client ไปยัง server อื่นได้
- **Shared Nothing**: แต่ละ node มี CPU, memory และ storage เป็นของตัวเอง ไม่มีการใช้ disk ร่วมกัน ใช้เทคนิค replication หรือ partitioning ในการกระจายข้อมูล ทำให้ fault tolerance ดีเพราะ reroute client ไปยัง node อื่นได้เมื่อเกิดปัญหา
- **Combination/Specialized architecture**: ผสมผสานทั้ง shared disk, shared nothing, replication หรือ partitioning ร่วมกับ hardware เฉพาะทาง

เทคนิคจัดการข้อมูลและเพิ่มประสิทธิภาพ:

- **Database replication**: คัดลอกการเปลี่ยนแปลงจาก database server หลักไปยัง replica หนึ่งตัวหรือมากกว่า ช่วยกระจาย workload หาก replica อยู่ที่เดียวกันเรียกว่า **HA (high availability) replica** ใช้สำหรับ failover เมื่อ server หลักล่ม ส่วน replica ที่อยู่ต่างพื้นที่ทางภูมิศาสตร์เรียกว่า **disaster recovery replica** ป้องกันกรณี data center ทั้งหมดล่ม (ไฟดับ, ไฟไหม้, แผ่นดินไหว, น้ำท่วม)
- **Partitioning และ Sharding**: แบ่งตารางขนาดใหญ่ออกเป็นส่วนย่อยเชิงตรรกะ (เช่น ข้อมูลยอดขายแยกตามไตรมาส) แล้วนำแต่ละ partition ไปวางบน node แยกกันใน cluster (เรียกว่า sharding) แต่ละ shard มี compute resource ของตัวเอง เมื่อ client query จะถูกประมวลผลแบบขนาน (parallel) ในหลาย node แล้วนำผลลัพธ์มารวมกัน เพิ่ม node/shard ได้ตามปริมาณข้อมูลที่โตขึ้น นิยมใช้ในงาน data warehousing และ BI

---

## Database Usage Patterns

ผู้ใช้งานฐานข้อมูลแบ่งได้เป็น 3 กลุ่มหลัก แต่ละกลุ่มใช้เครื่องมือต่างกัน

1. **Data Engineers และ Database Administrators (DBAs)**: ทำงานด้าน admin เช่น สร้าง/ดูแล database object, กำหนด access control, monitor และปรับปรุง performance เครื่องมือที่ใช้ได้แก่
   - GUI/web-based management tools (เช่น Oracle SQL Developer)
   - Command-line interfaces เช่นคำสั่งตรง (`db2 create database sample`, `mysqldump sakila > sakila.sql`) หรือ interactive shell (`sqlplus`, `db2 clp`)
   - APIs สำหรับงาน automation หรือ programmatic access
2. **Data Scientists และ Business Analysts**: เน้นอ่านข้อมูลเพื่อวิเคราะห์และคาดการณ์ บางครั้งสร้าง object ใน sandbox ของตัวเอง เครื่องมือที่ใช้บ่อยได้แก่ Jupyter, R Studio, Zeppelin, SAS, SPSS (ฝั่ง data science/ML) และ Excel, Power BI, Tableau, MicroStrategy (ฝั่ง reporting/BI) ซึ่งส่วนใหญ่เชื่อมกับฐานข้อมูลผ่าน SQL interface/API โดยซ่อนรายละเอียด SQL ไว้เบื้องหลัง
3. **Application Developers**: มักไม่เข้าถึงฐานข้อมูลโดยตรง แต่เขียนแอปพลิเคชันด้วยภาษาต่าง ๆ (C++, C#, Java, JavaScript, .NET, PHP, Perl, Python, Ruby) ที่สื่อสารกับฐานข้อมูลผ่าน SQL interface/API เช่น ODBC, JDBC หรือ REST API ปัจจุบันนิยมใช้ **ORM (Object Relational Mapping) framework** เช่น ActiveRecord (Ruby), Django (Python), Entity Framework (.NET), Hibernate (Java), Sequelize (JavaScript) เพื่อซ่อนความซับซ้อนของ SQL และฐานข้อมูลเชิงสัมพันธ์

---

## Introduction to Relational Database Offerings

ประวัติของฐานข้อมูลเชิงสัมพันธ์:

- **1960s**: IBM และ American Airlines สร้าง IBM Sabre ระบบจองที่นั่งซึ่งถือเป็นต้นแบบฐานข้อมูลเชิงสัมพันธ์ยุคแรก
- **ต้นปี 1970s**: Edgar F. Codd เสนอกฎ 12 ข้อสำหรับนิยามฐานข้อมูลเชิงสัมพันธ์
- **1976**: Peter P. Chen เสนอโมเดล Entity-Relationship (ER)
- **ปลาย 1970s**: Ingres (UC Berkeley) และ System R (IBM San Jose) เริ่มใช้งาน
- **1980s**: RDBMS เชิงพาณิชย์ประสบความสำเร็จ DB2 กลายเป็นสินค้าเรือธงของ IBM และ SQL กลายเป็นภาษามาตรฐาน
- **ต้นปี 1990s**: เครื่องมือฝั่ง client ใหม่ ๆ เช่น Oracle Developer, PowerBuilder, VB และเครื่องมือส่วนบุคคลอย่าง ODBC, Excel, Access เริ่มเป็นที่นิยม
- **ปลาย 1990s**: อุตสาหกรรมฐานข้อมูลเติบโตแบบก้าวกระโดด ผู้เล่นรายใหญ่ ได้แก่ Oracle, Microsoft SQL Server, IBM DB2 ขณะที่ฐานข้อมูล open source อย่าง MySQL, PostgreSQL เริ่มได้รับความนิยม
- **2010s**: ฐานข้อมูลบน cloud ได้รับความนิยมสูงขึ้นมาก ผู้เล่นหลักคือ Amazon RDS, IBM Db2 on Cloud, Microsoft SQL Azure, Oracle Cloud

**Commercial vs Open-source licensing**: RDBMS เชิงพาณิชย์ (Oracle, Microsoft SQL Server, IBM Db2) ยังคงได้รับความนิยมด้านความน่าเชื่อถือและ feature ที่ครบครัน ส่วน open-source licensing (เช่น MySQL, PostgreSQL, SQLite) อนุญาตให้ผู้ใช้ดู แก้ไข และแจกจ่าย source code ได้ฟรี ซึ่งได้รับความนิยมเพิ่มขึ้นต่อเนื่อง จากข้อมูลของ DB-Engines (ผู้จัดอันดับความนิยมของฐานข้อมูลจากหลายปัจจัย เช่น การกล่าวถึงบน Google/Bing, Google Trends, Stack Overflow, ตำแหน่งงานบน Indeed/LinkedIn) พบว่าในปี 2023 ระบบ open source มีสัดส่วนคะแนนความนิยมถึง 55.3% เพิ่มขึ้นจาก 35.5% ในปี 2013

ฐานข้อมูลเชิงสัมพันธ์ยอดนิยม 10 อันดับ (ข้อมูล ณ กุมภาพันธ์ 2021): Oracle, MySQL, Microsoft SQL Server, PostgreSQL, MongoDB, Redis, Elasticsearch, IBM Db2, SQLite, Microsoft Access

**Cloud database**: บริการฐานข้อมูลที่สร้างและเข้าถึงผ่าน cloud platform ได้รับความนิยมเพิ่มขึ้นกว่าเท่าตัวในช่วงสิบปีที่ผ่านมา คาดการณ์ว่าภายในปี 2025 ฐานข้อมูลกว่า 80% จะอยู่บนหรือย้ายไปยัง cloud แรงขับเคลื่อนหลักคือโมเดล SaaS ที่ช่วยเรื่อง scalability, การประมวลผลข้อมูลปริมาณมากสำหรับ analytics และระบบ backup/disaster recovery ในตัว ตัวอย่าง cloud database ชั้นนำ ได้แก่ Amazon DynamoDB, Microsoft Azure Cosmos DB, Microsoft Azure SQL DB, Google BigQuery, Amazon Redshift

---

## Db2

Db2 (Database 2) เปิดตัวโดย IBM ครั้งแรกในปี 1983 บน mainframe และต่อมาพัฒนาให้รองรับหลายแพลตฟอร์ม (OS/2, Unix, Linux, Windows) โดยใช้ codebase เดียวกันทำให้ย้าย application ข้ามระบบปฏิบัติการได้ง่าย ปัจจุบัน Db2 เป็นตระกูลผลิตภัณฑ์ที่ประกอบด้วย Db2 database, Db2 Warehouse, Db2 on Cloud, Db2 Warehouse on Cloud, Db2 Big SQL และ Db2 for z/OS

**คุณสมบัติเด่น**:

- ใช้ AI/machine learning ช่วยเพิ่มประสิทธิภาพ query
- **Column store** เพิ่มประสิทธิภาพงาน analytic โดย query เฉพาะคอลัมน์ที่ต้องการ
- **Data skipping** ข้ามการประมวลผลข้อมูลที่ไม่จำเป็นต่อ query
- ใช้ SQL engine เดียวกันทั่วทั้งตระกูลผลิตภัณฑ์ ทำให้ query เดียวใช้ได้กับหลายผลิตภัณฑ์
- รองรับข้อมูลทุกประเภท (relational, structured, unstructured)
- มีฟีเจอร์ replication สำหรับ high availability และ disaster recovery

**การ scale**: สามารถขยาย storage/power ไปยัง cloud ชั่วคราวเพื่อรองรับ peak, ปรับ power/storage แยกกันได้ใน managed cloud deployment หรือใช้ **database partitioning** ใน Db2 Warehouse เพื่อกระจายข้อมูลข้าม partition/server รองรับ massively parallel processing (MPP)

**ผลิตภัณฑ์หลักในตระกูล**:

- **Db2 database**: RDBMS แบบ on-premises เหมาะกับ OLTP รองรับ Linux, Unix, Windows
- **Db2 Warehouse**: data warehouse on-premises รองรับ analytics ขั้นสูง, MPP, machine learning
- **Db2 on Cloud**: fully managed cloud SQL database คุณสมบัติใกล้เคียง Db2 database
- **Db2 Warehouse on Cloud**: data warehouse บน cloud แบบ elastic
- **Db2 Big SQL**: SQL-on-Hadoop engine รองรับ MPP และ query ข้อมูลจากหลายแหล่ง (HDFS, RDBMS, NoSQL)
- **Db2 for z/OS**: enterprise data server สำหรับ IBM Z รองรับงาน mission-critical

**Db2 on Cloud** มี 3 แผน: Lite (ฟรี ไม่จำกัดเวลา แต่จำกัดข้อมูล 200MB และ 15 connection พร้อมกัน), Standard (scale ได้ยืดหยุ่น พร้อม HA clustering 3-node) และ Enterprise (dedicated instance พร้อม HA clustering เช่นกัน) เข้าถึงผ่าน CLPPlus, GUI console หรือ API มาตรฐาน (ODBC, JDBC, REST)

**HADR (High Availability, Disaster Recovery)**: replicate การเปลี่ยนแปลงจาก primary database ไปยัง standby server หลายตัว หาก primary ล่ม ระบบจะ promote standby ตัวหนึ่งขึ้นเป็น primary และ redirect client โดยอัตโนมัติ

---

## MySQL

MySQL เป็น object-relational database management system ที่มีบทบาทสำคัญในงาน web development พัฒนาโดยบริษัท MySQL AB จากสวีเดน (ตั้งชื่อตามลูกสาวของผู้ร่วมก่อตั้ง Monty Widenius) ต่อมาถูก Sun Microsystems ซื้อกิจการ แล้ว Oracle Corporation ซื้อ Sun Microsystems อีกทอดหนึ่ง โลโก้เป็นรูปโลมาชื่อ Sakila ได้รับความนิยมมากในช่วงปลายปี 1990s-ต้น 2000s จากบทบาทใน **LAMP stack** (Linux, Apache, MySQL, PHP)

**License**: ใช้ dual licensing คือ open source GNU GPL และ commercial license สำหรับ application ที่ต้องการ embed MySQL การเป็น open source ทำให้เกิด fork เช่น MariaDB

**คุณสมบัติ**: รองรับ Unix, Windows, Linux เขียน client application ได้หลายภาษา ใช้ SQL มาตรฐานพร้อม extension เพิ่มเติม (เช่นคำสั่ง `LOAD DATA` สำหรับ import ข้อมูลจากไฟล์ text) รองรับทั้งข้อมูลเชิงสัมพันธ์และ JSON

**Storage engines**:

- **InnoDB** (ค่า default): รองรับ transaction, row-level locking, clustered index บน primary key, foreign key constraint ให้ performance และ reliability ที่สมดุล
- **MyISAM**: เหมาะกับ workload ที่อ่านมากกว่าเขียน (เช่น data warehouse, web application) ใช้ table-level locking ซึ่งลดประสิทธิภาพในสภาพแวดล้อมที่ read-write พร้อมกันมาก
- **NDB**: รองรับการรัน MySQL server หลาย instance เป็น cluster เหมาะกับงานที่ต้องการ availability และ redundancy สูง

**Clustering options**:

1. **InnoDB + Group Replication**: มี primary server เดียวสำหรับ read-write และ secondary server หลายตัว ใช้ MySQL Router ทำ load balancing และ reconnect client อัตโนมัติเมื่อ server ล่ม
2. **MySQL Cluster Edition + NDB storage engine**: หลาย MySQL server node เข้าถึงชุด data node ที่มักเก็บใน memory เพิ่ม redundancy (หลาย data node) และ scalability (หลาย server node)

---

## PostgreSQL

PostgreSQL มีต้นกำเนิดจากโปรเจกต์ POSTGRES ที่ University of California เมื่อกว่า 30 ปีก่อน ในปี 1994 มีการเปิดตัว Postgres95 แบบ open source พร้อม SQL interpreter ซึ่งภายหลังเปลี่ยนชื่อเป็น PostgreSQL (มักเรียกสั้น ๆ ว่า Postgres) ใช้เป็นส่วนหนึ่งของ **LAPP stack** (Linux, Apache, PostgreSQL, PHP) และรองรับ extension เพิ่มเติม เช่น PostGIS สำหรับข้อมูลภูมิสารสนเทศ

เป็น free open-source **object-relational** DBMS หมายถึงรองรับแนวคิดแบบ object-oriented เช่น inheritance และ overloading ทำงานได้บนระบบปฏิบัติการส่วนใหญ่ ดูแลรักษาง่าย รองรับหลายภาษาโปรแกรมมิ่งและมาตรฐาน ANSI-SQL

รองรับโครงสร้างมาตรฐานของ relational database (keys, transactions, views, functions, stored procedures) รวมถึงฟีเจอร์แบบ NoSQL เช่น JSON (ข้อมูลมีโครงสร้าง) และ HSTORE (ข้อมูลไม่มีลำดับชั้น)

**Replication**:

- **Two-node synchronous replication**: เก็บสำเนาข้อมูลไว้ที่ node ที่สอง ทุกการเปลี่ยนแปลงที่ node 1 จะถูก apply ที่ node 2 ด้วย แชร์ read load ได้ และหาก node 1 ล่ม node 2 จะรับ traffic แทนได้ทันที
- **Multi-node asynchronous replication**: master node กระจายการเปลี่ยนแปลงไปยัง read-only replica หลายตัวเพื่อ scalability หาก node หลักล่มก็แทนที่ด้วย replica ตัวใดตัวหนึ่งได้
- **Commercial extension** เช่น EDB PostgreSQL Replication Server รองรับ multi-master read/write replication ให้หลาย database เขียน/replicate ข้อมูลระหว่างกันได้

รองรับ **partitioning** (แบ่งตารางใหญ่เป็นส่วนย่อยเพื่อเพิ่มประสิทธิภาพ query) และ **sharding** (กระจาย horizontal partition ไปยัง remote server หลายตัว) เพื่อรองรับ scalability และข้อมูลขนาดใหญ่

---

## Database normalization

การ Normalize ฐานข้อมูล คือกระบวนการจัดโครงสร้างข้อมูลให้อยู่ในรูปแบบที่เหมาะสม โดยใช้หลักการของความสัมพันธ์ระหว่างข้อมูล (Dependencies) และการกำหนดคีย์ (Keys) เพื่อจัดระเบียบตารางให้มีประสิทธิภาพสูงสุด

**ความสำคัญของการทำ Normalization มีดังนี้:**

1. **ลดความซ้ำซ้อนของข้อมูล (Reduce Redundancy):** ช่วยป้องกันการเก็บข้อมูลเดิมซ้ำ ๆ หลายครั้งในที่ต่าง ๆ ซึ่งเป็นจุดประสงค์หลักของการใช้ Functional Dependencies (FDs) เข้ามาช่วยออกแบบ
2. **รักษาความถูกต้องของข้อมูล (Data Integrity):** ช่วยให้มั่นใจว่าข้อมูลในระบบมีความถูกต้องและสอดคล้องกัน หากเราละเลยความสัมพันธ์บางอย่าง เช่น Multi-Valued Dependencies (MVDs) อาจนำไปสู่การบันทึกข้อมูลที่ผิดพลาดได้
3. **เพิ่มประสิทธิภาพในการสืบค้น (Query Performance):** การกำหนด Candidate Keys ที่ดีจะช่วยในการทำ Indexing ซึ่งส่งผลให้การค้นหาข้อมูลทำได้รวดเร็วขึ้น
4. **ป้องกันข้อมูลซ้ำซ้อนและระบุตัวตนของข้อมูลได้ชัดเจน:** การใช้ Candidate Key ที่มีความเป็นเอกลักษณ์ (Uniqueness) และมีขนาดเล็กที่สุด (Minimality) จะช่วยบังคับให้แต่ละแถวในตารางไม่ซ้ำกัน และระบุแต่ละรายการได้อย่างเฉพาะเจาะจง
5. **จัดระเบียบโครงสร้างให้ยืดหยุ่น:** ช่วยในการสร้างความสัมพันธ์ระหว่างตารางอย่างเป็นระบบ ทำให้ง่ายต่อการบำรุงรักษาและขยายระบบในอนาคต

**สรุปง่าย ๆ คือ:** การ Normalize เป็นเหมือนการ "จัดบ้าน" ให้ข้อมูล โดยการแยกสิ่งของที่กระจัดกระจายไปไว้ในที่ที่ถูกต้องตามความสัมพันธ์ของมัน เพื่อให้หาของง่าย (เร็ว) ไม่เก็บของซ้ำซ้อน (ประหยัดพื้นที่) และมั่นใจว่าของไม่หายหรือผิดเพี้ยน (ถูกต้อง)

### Functional Dependencies (FDs) — "รู้ A แล้วจะรู้ B แน่นอน"

เป็นความสัมพันธ์ที่ค่าของข้อมูลชุดหนึ่ง (ตัวกำหนด หรือ Determinant) สามารถระบุค่าของอีกชุดหนึ่ง (ตัวที่ถูกกำหนด หรือ Dependent) ได้อย่างเฉพาะเจาะจง

- **สัญลักษณ์:** `X→Y`
- **ตัวอย่าง:** ถ้าเรามีรหัสพนักงาน (`EmployeeID`) เราจะสามารถรู้ชื่อพนักงาน (EmployeeName) ของคนนั้นได้ทันทีและแน่นอน เช่น `EmployeeID` 1 คือ Alice เสมอ
- **ทำไมต้องมี:** เพื่อช่วยรักษาความถูกต้องของข้อมูลและลดความซ้ำซ้อน

### Multi-Valued Dependencies (MVDs) — "รู้ A แล้วจะรู้เซตของค่า B"

แนวคิดนี้จะซับซ้อนกว่า FD เล็กน้อย คือการที่ข้อมูลตัวหนึ่งกำหนด "กลุ่มของค่า" ที่เป็นไปได้หลายค่า
มักพบในความสัมพันธ์แบบ Many-to-Many

- สัญลักษณ์: `X↠{Y1,Y2,...}`
- ตัวอย่าง: รหัสพนักงานคนหนึ่งอาจจะทำงานหลายโปรเจกต์ ดังนั้น `EmployeeID` จึงกำหนดชุดของ ProjectID ได้หลายชุด เช่น `EmployeeID` 1 (Alice) ทำงานทั้ง Project 101 และ 102
- ทำไมต้องมี: เพื่อจัดการความสัมพันธ์ที่ซับซ้อนและป้องกันไม่ให้ข้อมูลผิดพลาดจากการละเลยความสัมพันธ์แบบกลุ่มนี้

### Candidate Keys — "บัตรประชาชนของแถวข้อมูล"

Candidate key คือชุด attribute ขั้นต่ำ (minimal) ที่ระบุแต่ละแถวในตารางได้อย่างไม่ซ้ำกัน คุณสมบัติสำคัญ:

- **Uniqueness**: ค่าที่ประกอบกันต้องระบุแถวได้เฉพาะเจาะจง ไม่ซ้ำ
- **Minimality**: ไม่มี subset ย่อยของ candidate key ที่ระบุแถวได้เพียงพอแล้ว (ต้องเป็นชุดที่เล็กที่สุด)
- ตารางหนึ่งอาจมี candidate key ได้มากกว่าหนึ่งชุด
- Candidate key ที่ดีช่วยเพิ่มประสิทธิภาพ query ผ่าน indexing และป้องกันข้อมูลซ้ำซ้อน

### ตัวอย่างเชิงปฏิบัติ

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

### สรุปเปรียบเทียบ

| ประเด็น    | Functional Dependencies                     | Multi-Valued Dependencies (MVDs)                    | Candidate Keys                                 |
| ---------- | ------------------------------------------- | --------------------------------------------------- | ---------------------------------------------- |
| นิยาม      | ความสัมพันธ์ระหว่าง attribute               | ขยายแนวคิดไปสู่กลุ่มของ attribute                   | ชุด attribute ที่ระบุแถวได้ไม่ซ้ำกัน           |
| แก่นสาระ   | ค่าบาง attribute ถูกกำหนดโดย attribute อื่น | ความสัมพันธ์ระหว่างชุดของ attribute                 | ระบุแต่ละแถวในตารางได้อย่างเฉพาะเจาะจง         |
| ตัวอย่าง   | รู้ attribute หนึ่งแล้วหาอีก attribute ได้  | อธิบายว่าชุด attribute หนึ่งกำหนดอีกชุดอย่างไร      | การรวมกันของ attribute ที่ระบุแต่ละ record ได้ |
| จุดประสงค์ | รักษาความถูกต้องของข้อมูล ลดความซ้ำซ้อน     | จัดระเบียบข้อมูลอย่างมีประสิทธิภาพ ป้องกันความสับสน | บังคับใช้ entity integrity constraint          |
| การใช้งาน  | สำคัญต่อการทำ normalization                 | สำคัญต่อการรักษา data integrity                     | ใช้สร้างความสัมพันธ์ระหว่างตาราง               |

---

## 📖 Key Terms & Glossary

| Term                                       | Definition                                                                                                               |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Deployment Topology                        | รูปแบบการจัดวาง hardware, software และ network component ในการติดตั้งระบบ (single-tier, two-tier, three-tier, cloud)     |
| Single-tier Architecture                   | สถาปัตยกรรมที่ UI, application logic และ data storage อยู่บนเครื่องเดียวกันทั้งหมด                                       |
| Two-tier (Client-Server) Architecture      | แบ่งเป็น client layer (UI) และ server layer (application logic + data storage)                                           |
| Three-tier Architecture                    | เพิ่ม application server layer คั่นระหว่าง client กับ database server เพื่อความปลอดภัยและ maintainability                |
| Cloud Deployment                           | การติดตั้งฐานข้อมูลบน cloud environment โดยไม่ต้องดูแล infrastructure เอง                                                |
| Shared Disk Architecture                   | หลาย database server ใช้ storage ทางกายภาพร่วมกัน ประสานงานผ่าน high-speed interconnection                               |
| Shared Nothing Architecture                | แต่ละ node มี CPU, memory, storage เป็นของตัวเอง กระจายข้อมูลด้วย replication หรือ partitioning                          |
| Replication                                | การคัดลอกการเปลี่ยนแปลงของข้อมูลจาก database server หลักไปยัง replica อื่น                                               |
| HA (High Availability) Replica             | replica ที่อยู่ตำแหน่งเดียวกับ primary ใช้สำหรับ failover เมื่อ primary ล่ม                                              |
| Disaster Recovery Replica                  | replica ที่อยู่ต่างพื้นที่ทางภูมิศาสตร์ ป้องกันกรณี data center ทั้งหมดล่ม                                               |
| Partitioning                               | การแบ่งตารางขนาดใหญ่ออกเป็นส่วนย่อยเชิงตรรกะ                                                                             |
| Sharding                                   | การนำ partition ไปวางบน node แยกกันใน cluster เพื่อรองรับ parallel processing                                            |
| ORM (Object Relational Mapping)            | framework ที่ช่วยให้ภาษาโปรแกรมมิ่งเชิงวัตถุทำงานกับ relational database ได้ง่ายขึ้นโดยซ่อน SQL ไว้เบื้องหลัง            |
| Storage Engine                             | ส่วนประกอบของ MySQL ที่จัดการ SQL operation บนตารางและกำหนดฟีเจอร์ที่ตารางนั้นใช้ได้                                     |
| InnoDB                                     | storage engine ค่า default ของ MySQL รองรับ transaction, row-level locking, foreign key                                  |
| MyISAM                                     | storage engine ของ MySQL เหมาะกับ workload ที่อ่านมากกว่าเขียน ใช้ table-level locking                                   |
| NDB                                        | storage engine ของ MySQL สำหรับรองรับการรันเป็น cluster                                                                  |
| HADR (High Availability Disaster Recovery) | ฟีเจอร์ของ Db2 ที่ replicate ข้อมูลจาก primary ไปยัง standby server และ promote อัตโนมัติเมื่อ primary ล่ม               |
| DB-Engines Ranking                         | การจัดอันดับความนิยมของฐานข้อมูลโดยพิจารณาหลายปัจจัย เช่น การกล่าวถึงออนไลน์และตำแหน่งงาน                                |
| Open-source Licensing                      | รูปแบบ license ที่อนุญาตให้ดู แก้ไข และแจกจ่าย source code ได้อย่างเสรี                                                  |
| Cloud Database                             | บริการฐานข้อมูลที่สร้างและเข้าถึงผ่าน cloud platform                                                                     |
| Functional Dependency (FD)                 | ความสัมพันธ์ที่ attribute หนึ่ง (determinant) กำหนดค่า attribute อีกตัว (dependent) ได้อย่างเฉพาะเจาะจง เขียนเป็น X -> Y |
| Multi-Valued Dependency (MVD)              | ความสัมพันธ์ที่ attribute หนึ่งกำหนด "ชุด" ของค่าที่เป็นไปได้ของอีก attribute เขียนเป็น X ->> {Y1, Y2, ...}              |
| Candidate Key                              | ชุด attribute ขั้นต่ำที่ระบุแต่ละแถวในตารางได้อย่างไม่ซ้ำกัน                                                             |
| Normalization                              | กระบวนการจัดโครงสร้างฐานข้อมูลเพื่อลดความซ้ำซ้อนและรักษาความถูกต้องของข้อมูล โดยอาศัย FD และ MVD เป็นพื้นฐาน             |

---

## ❓ My Questions & Gaps

- [ ] ในทางปฏิบัติควรเลือกใช้ shared disk หรือ shared nothing architecture ในสถานการณ์แบบไหน ปัจจัยอะไรที่ใช้ตัดสินใจ
- [ ] ความแตกต่างระหว่าง HA replica กับ disaster recovery replica ในแง่ของ RTO/RPO (เวลาที่ยอมรับได้ในการกู้คืนระบบ) เป็นอย่างไร
- [ ] MVD ต่างจาก FD อย่างชัดเจนในกรณีใช้งานจริงอย่างไร และการมี MVD ที่ไม่ได้ normalize อาจก่อให้เกิดปัญหาอะไรกับตาราง
- [ ] เมื่อไรควรเลือกใช้ partitioning เทียบกับ sharding ในการออกแบบระบบจริง
- [ ] Storage engine ของ MySQL แต่ละตัว (InnoDB, MyISAM, NDB) เหมาะกับ use case แบบไหนมากที่สุดในงาน data engineering
- [x] LAMP stack vs. LAPP stack
  - The primary difference between LAMP and LAPP stacks is the database system they use: LAMP uses MySQL, while LAPP uses PostgreSQL.
  - Both share Linux for the operating system, Apache for the web server, and PHP (along with Python or Perl) for scripting.
  - Database Comparison
    - MySQL (LAMP):
      - Faster and simpler setup for basic, standard web projects.
      - Highly popular with content management systems like WordPres
      - Great for standard relational data storage.
    - PostgreSQL (LAPP):
      - Advanced features for complex data queries, data integrity, and heavy workloads.
      - Better support for enterprise-level applications, custom data types, and high concurrency.
  - Use Cases
    - Choose LAMP when: Building standard blogs, e-commerce sites, or simple dynamic applications that rely on traditional MySQL databases
    - Choose LAPP when: Developing large-scale enterprise software that requires advanced database functions, strict data rules, or complex analytical processing.

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงภายนอกที่ระบุไว้ในเนื้อหาบทเรียนนี้ นอกจากชื่อผลิตภัณฑ์ที่กล่าวถึง (Db2, MySQL, PostgreSQL, DB-Engines)
