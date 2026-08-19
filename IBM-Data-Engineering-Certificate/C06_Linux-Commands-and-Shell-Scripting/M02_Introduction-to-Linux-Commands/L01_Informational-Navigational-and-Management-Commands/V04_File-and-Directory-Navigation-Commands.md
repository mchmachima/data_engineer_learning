# File and Directory Navigation Commands

`Tags: Linux, Shell, navigation, file-system`

| Field             | Value                                    |
| ----------------- | ----------------------------------------- |
| **Certificate**   | IBM Data Engineering Professional Certificate |
| **Course**        | C06 Hands-on Introduction to Linux Commands and Shell Scripting |
| **Module**        | M02 Introduction to Linux Commands        |
| **Lesson**        | L01 Informational, Navigational, & Management Commands |
| **Date studied**  | 2026-08-16                                |

---

## Table of Contents

- [Overview](#overview)
- [Listing Contents with ls](#listing-contents-with-ls)
- [Checking Your Location with pwd](#checking-your-location-with-pwd)
- [Changing Directory with cd](#changing-directory-with-cd)
- [Relative vs. Absolute Paths](#relative-vs-absolute-paths)
- [Finding Files with find](#finding-files-with-find)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้สอนคำสั่งพื้นฐานสำหรับสำรวจ (navigate) โครงสร้างไฟล์และ directory ใน Linux ได้แก่ `ls`, `pwd`, `cd` และ `find` พร้อมอธิบายความแตกต่างระหว่าง relative path กับ absolute path ซึ่งเป็นพื้นฐานสำคัญก่อนจะไปเรียนคำสั่งจัดการไฟล์ในวิดีโอถัดไป

---

## Listing Contents with ls

`ls` ("list") แสดงไฟล์และ directory ที่อยู่ภายใน directory ที่ระบุ หากไม่ระบุ argument จะแสดงเนื้อหาของ current directory

```bash
# แสดงไฟล์/directory ใน current directory
ls

# แสดงเนื้อหาของ directory ที่ระบุ
ls Downloads

# แสดงแบบละเอียด (long format) พร้อม permission, วันที่แก้ไขล่าสุด, และเจ้าของไฟล์
ls -l
```

---

## Checking Your Location with pwd

`pwd` ("print working directory") แสดง path เต็มของ directory ที่กำลังทำงานอยู่ในปัจจุบัน มีประโยชน์เมื่อต้องการยืนยันว่าตอนนี้อยู่ที่ไหนในโครงสร้างไฟล์

```bash
# แสดง current working directory
pwd
```

---

## Changing Directory with cd

`cd` ("change directory") ใช้เปลี่ยน current working directory สามารถระบุได้ทั้งแบบ relative path และ absolute path

```bash
# เข้าไปยัง subdirectory ชื่อ Documents (relative path)
cd Documents

# กลับไปยัง parent directory (relative path)
cd ..

# กลับไปยัง home directory (absolute path แบบย่อ)
cd ~

# ระบุ absolute path เต็ม
cd /Users/me/Documents/Math/Notes
```

---

## Relative vs. Absolute Paths

Path ในระบบไฟล์แบ่งเป็นสองแบบ:

| ประเภท Path | ความหมาย | ตัวอย่าง |
| --- | --- | --- |
| Relative path | อ้างอิงตำแหน่งเทียบกับ current working directory | `..` (parent directory), `Documents` |
| Absolute path | อ้างอิงตำแหน่งแบบสมบูรณ์ ไม่ขึ้นกับตำแหน่งปัจจุบัน | `~` (home), `/Users/me/Documents/Math/Notes` |

`..` หมายถึง parent directory ของตำแหน่งปัจจุบัน ส่วนเครื่องหมาย tilde (`~`) แทน absolute path ไปยัง home directory ของ user

---

## Finding Files with find

`find` เป็นคำสั่งที่คืน path ของทุกไฟล์ที่ตรงกับเงื่อนไข (criterion) ที่กำหนด

```bash
# ค้นหาไฟล์ชื่อ a.txt ภายใน current working directory และ subdirectory ทั้งหมด
find . -name 'a.txt'

# ค้นหาแบบ case-insensitive (จะเจอทั้ง a.txt และ A.txt)
find . -iname 'a.txt'
```

argument `.` หมายถึง "ค้นหาเริ่มจากตรงนี้" คือค้นเฉพาะภายใน current working directory และ subdirectory ของมัน

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| ls | คำสั่งแสดงไฟล์และ directory ที่อยู่ภายใน directory ที่ระบุ (list) |
| pwd | คำสั่งแสดง path เต็มของ current working directory (print working directory) |
| cd | คำสั่งเปลี่ยน current working directory (change directory) |
| find | คำสั่งค้นหา path ของไฟล์ที่ตรงกับเงื่อนไขที่ระบุภายใน directory tree |
| Relative path | path ที่อ้างอิงตำแหน่งเทียบกับ current working directory เช่น `..` |
| Absolute path | path ที่อ้างอิงตำแหน่งแบบสมบูรณ์ ไม่ขึ้นกับตำแหน่งปัจจุบัน |
| Tilde (~) | สัญลักษณ์แทน absolute path ไปยัง home directory ของ user |
| Long format (-l option) | รูปแบบ output ของ `ls` ที่แสดงรายละเอียดเพิ่ม เช่น permission, วันที่แก้ไข, เจ้าของไฟล์ |

---

## ❓ My Questions & Gaps

- [ ] option อื่น ๆ ของ `find` นอกเหนือจาก `-name`/`-iname` เช่นการค้นหาตาม file type หรือวันที่แก้ไข
- [ ] ความแตกต่างของพฤติกรรม `cd -` (กลับไป directory ก่อนหน้า) เทียบกับ `cd ..`

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมในวิดีโอนี้
