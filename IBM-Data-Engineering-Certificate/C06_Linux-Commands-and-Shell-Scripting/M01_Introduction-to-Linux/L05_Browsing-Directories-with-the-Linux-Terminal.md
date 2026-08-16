# Browsing Directories with the Linux Terminal

`Tags: Linux, Terminal, pwd, ls, navigation`

| Field            | Value                                                     |
| ---------------- | ---------------------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate             |
| **Course**       | C06 Linux Commands and Shell Scripting                    |
| **Module**       | M01 Introduction to Linux                                 |
| **Lesson**       | L05 Browsing Directories with the Linux Terminal           |
| **Date studied** | 2026-08-16                                                 |

---

## Table of Contents

- [Overview](#overview)
- [The Linux Terminal](#the-linux-terminal)
- [The pwd Command](#the-pwd-command)
- [The ls Command](#the-ls-command)
- [The Root Directory and File System Tree](#the-root-directory-and-file-system-tree)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

Reading นี้พาไปรู้จักการใช้ Linux terminal เพื่อสำรวจ (browse) directory ในระบบไฟล์ โดยเน้นที่คำสั่งพื้นฐานสองตัวคือ `pwd` สำหรับดูตำแหน่งปัจจุบัน และ `ls` สำหรับแสดงเนื้อหาภายใน directory พร้อมยกตัวอย่างการใช้งานจริงประกอบ

---

## The Linux Terminal

ผู้ใช้โต้ตอบกับ Linux shell ได้โดยป้อนคำสั่งใน Linux terminal ซึ่งเรียกอีกชื่อว่า command line หรือ command prompt ตัวอย่างเช่น `/home/project` คือ present working directory ที่แสดงเป็นตัวอักษรสีน้ำเงิน ตามด้วยเครื่องหมาย `$` ซึ่งเรียกว่า command prompt

Terminal คือ user interface ง่าย ๆ ที่ให้ผู้ใช้พิมพ์คำสั่งแล้วกด Enter เพื่อรัน คำสั่งส่วนใหญ่จะคืนค่า output กลับมาเป็นข้อความใน terminal window

---

## The pwd Command

คำสั่ง `pwd` (print working directory) ใช้แสดง path ของ present working directory

```bash
# แสดง path ของ present working directory ปัจจุบัน
pwd
# ตัวอย่างผลลัพธ์: /home/project
```

หลังรันคำสั่งเสร็จ command prompt จะปรากฏขึ้นอีกครั้งในบรรทัดถัดไป เพื่อรอรับคำสั่งต่อไป

---

## The ls Command

คำสั่ง `ls` ใช้แสดงรายการเนื้อหา (list contents) ของ directory ที่กำลังทำงานอยู่

```bash
# แสดงเนื้อหาของ present working directory
# ถ้า directory ว่างเปล่า ls จะไม่พิมพ์อะไรออกมาเลย (ไม่มีแม้แต่บรรทัดว่าง)
ls

# แสดงเนื้อหาของ directory อื่นได้โดยระบุชื่อ directory ต่อท้าย
ls /home
# ตัวอย่างผลลัพธ์: project  theia

# แสดงเนื้อหาของ root directory
ls /
```

จากตัวอย่าง `ls /home` แสดงให้เห็นว่า `/home` มี subdirectory อยู่สองตัวคือ `project` และ `theia` การตั้งชื่อ path แบบ `/home/project` หมายความว่า `project` เป็น subdirectory ของ `/home` เช่นเดียวกับ `/home/theia`

---

## The Root Directory and File System Tree

ระบบไฟล์ของ Linux มีโครงสร้างคล้ายต้นไม้ (tree) โดยมี **root directory** (`/` อ่านว่า "slash") เป็นจุดเริ่มต้นที่ทุก directory แตกแขนงออกมา หนึ่งใน subdirectory สำคัญของ root คือ `home` ซึ่งตรวจสอบได้ด้วยคำสั่ง `ls /`

> **Tip:** มองว่า directory เป็นเหมือน folder ที่บรรจุไฟล์และ subdirectory ไว้ข้างใน subdirectory เองก็สามารถมีไฟล์และ subdirectory ซ้อนอยู่ข้างในต่อไปได้อีก

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Terminal | user interface สำหรับป้อนคำสั่งไปยัง Linux shell และรับ output กลับมา |
| Command prompt | เครื่องหมาย (เช่น `$`) ที่บ่งบอกว่า terminal พร้อมรับคำสั่งถัดไป |
| pwd | คำสั่งที่แสดง path ของ present working directory (print working directory) |
| ls | คำสั่งที่แสดงรายการไฟล์และ directory ภายใน directory ที่ระบุ |
| Present working directory | directory ที่ผู้ใช้กำลังทำงานอยู่ในปัจจุบัน |
| Root directory | directory บนสุดของระบบไฟล์ Linux แทนด้วยเครื่องหมาย `/` |
| Subdirectory | directory ที่อยู่ภายใน directory อื่น |

---

## ❓ My Questions & Gaps

- [ ] `ls` มี flag หรือ option อะไรบ้าง (เช่น `-l`, `-a`) ที่ทำให้แสดงผลลัพธ์แบบละเอียดขึ้นหรือรวมไฟล์ที่ซ่อนอยู่ — น่าจะเจอในบทถัดไป

---

## 🔗 Resources

- (ไม่มีลิงก์ระบุใน reading)
