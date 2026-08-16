# Linux Distributions

`Tags: Linux, distro, Debian, Ubuntu, Red-Hat, open-source`

| Field            | Value                                         |
| ---------------- | --------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate |
| **Course**       | C06 Linux Commands and Shell Scripting        |
| **Module**       | M01 Introduction to Linux                     |
| **Lesson**       | L02 Linux Distributions                       |
| **Date studied** | 2026-08-16                                    |

---

## Table of Contents

- [Overview](#overview)
- [What is a Linux Distribution](#what-is-a-linux-distribution)
- [What Differentiates Distros](#what-differentiates-distros)
- [Popular Linux Distributions](#popular-linux-distributions)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายว่า Linux distribution (หรือ distro) คืออะไร และอะไรที่ทำให้แต่ละ distro แตกต่างกัน ไม่ว่าจะเป็น default utilities, GUI, shell commands ที่รองรับ หรือรูปแบบการ support จากนั้นจะพาไปรู้จัก distro ยอดนิยม เช่น Debian, Ubuntu, Red Hat, Fedora, SUSE Linux Enterprise และ Arch Linux พร้อมจุดเด่นและกลุ่มผู้ใช้เป้าหมายของแต่ละตัว

---

## What is a Linux Distribution

Linux distribution คือ flavor เฉพาะตัวหนึ่งของ Linux operating system หรือเรียกสั้น ๆ ว่า distro ทุก distro ต้องใช้ Linux kernel ซึ่งเป็น core component ที่ทำให้ระบบใช้งาน hardware ของเครื่องได้อย่างถูกต้อง ปัจจุบันมี Linux distro อยู่หลายร้อยตัว แต่ละตัวถูกออกแบบมาเพื่อกลุ่มผู้ใช้หรืองานเฉพาะทาง

---

## What Differentiates Distros

แต่ละ distro มีจุดต่างกันในหลายมิติ:

- **Default utilities** — ชุด commands และแอปพลิเคชันที่มาพร้อมกับ distro
- **GUI (Graphical User Interface)** — หน้าตาที่ใช้โต้ตอบกับระบบ
- **Shell commands** — ชุด commands ที่รองรับใน shell ซึ่งเป็นหน้าต่างสำหรับป้อนคำสั่งและรับผลลัพธ์
- **Support model** — พัฒนาโดย community หรือ commercial enterprise และเป็น long-term support (LTS) หรือ rolling release ที่อัปเดต package แบบต่อเนื่อง

---

## Popular Linux Distributions

| Distro                      | ปีเริ่มต้น                      | ลักษณะเด่น                                                                                                                                          | เหมาะกับ                                              |
| --------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Debian                      | 1993 (v0.01), stable แรกปี 1996 | Stable, reliable, fully open source, รองรับหลาย architecture, community-run distro ที่ใหญ่ที่สุด                                                    | Server                                                |
| Ubuntu                      | 2004                            | Debian-based, พัฒนาโดย Canonical, มี 3 edition: Desktop / Server / Core (IoT)                                                                       | Desktop, server, IoT                                  |
| Red Hat Linux               | —                               | Core distro (ไม่ได้ derive จากตัวอื่น), stable, reliable, open source, บริหารโดย Red Hat (IBM subsidiary), ปัจจุบันคือ RHEL                         | Enterprise customer                                   |
| Fedora                      | —                               | Stable, secure, มี firewall/security feature เฉพาะตัว, community ใหญ่และ active, sponsored โดย Red Hat (RHEL ใช้ code base ต่อจาก Fedora หลัง test) | ผู้ใช้ที่ต้องการฟีเจอร์ใหม่ที่ผ่านการพัฒนาต่อเนื่อง   |
| SUSE Linux Enterprise (SLE) | —                               | มี 2 edition: Server (SLES) และ Desktop (SLED), รองรับหลาย architecture เช่น ARM (Raspberry Pi), มี SUSE Package Hub, ดูแลโดยบริษัทเยอรมัน SUSE     | องค์กรที่ต้องการความยืดหยุ่นด้าน architecture         |
| Arch Linux                  | —                               | แนวทาง do-it-yourself, ปรับแต่งได้ทุกส่วน, เข้าถึงซอฟต์แวร์ใหม่ล่าสุดได้ไว แต่ไม่เน้น stability เท่า distro อื่น                                    | ผู้ใช้ที่มีความเข้าใจ Linux และ system tools ระดับสูง |

---

## 📖 Key Terms & Glossary

| Term (ศัพท์)                    | คำอธิบาย (ภาษาไทย)                                                                                   |
| ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Linux distribution (distro)     | flavor เฉพาะตัวหนึ่งของ Linux operating system                                                       |
| Shell                           | แอปพลิเคชัน (มักเป็นส่วนหนึ่งของ OS) ที่เป็นหน้าต่างสำหรับป้อนคำสั่งและรับผลลัพธ์                    |
| Long-term support (LTS)         | รูปแบบการ support ของ distro ที่เน้นความเสถียรระยะยาว                                                |
| Rolling release                 | รูปแบบการอัปเดต package แบบต่อเนื่องเป็นระยะ ๆ แทนการออก version ใหญ่ทีเดียว                         |
| RHEL (Red Hat Enterprise Linux) | edition ของ Red Hat Linux ที่เน้นกลุ่ม enterprise customer โดยเฉพาะ                                  |
| SUSE Package Hub                | แหล่ง package เสริมที่ให้ผู้ใช้ SLE ติดตั้ง package ที่ไม่ได้เป็นส่วนหนึ่งของ SLE อย่างเป็นทางการได้ |

---

## ❓ My Questions & Gaps

- [x] ในบริบทงาน data engineering ปกติจะเจอ distro ไหนบ่อยที่สุดบน production server (Ubuntu Server, Debian, หรือ RHEL/CentOS)
  - **คำตอบ:** ที่พบบ่อยที่สุดคือ **Ubuntu Server** และ **RHEL/CentOS-based distro** (เช่น Rocky Linux, AlmaLinux ที่มาแทน CentOS) ทั้งสองตัวเป็นตัวเลือกหลักในสภาพแวดล้อม enterprise และ cloud (AWS, Azure, GCP มักมี base image ให้ทั้งคู่) Ubuntu ได้รับความนิยมสูงในฝั่ง cloud-native/DevOps เพราะ package ใหม่และ community ใหญ่ ส่วน RHEL นิยมในองค์กรที่ต้องการ enterprise support และ compliance ระยะยาว **Debian** ก็พบได้บ่อยเช่นกันในระบบที่เน้นความเสถียรสูงสุด เพราะ Ubuntu เองก็ build ต่อจาก Debian
- [x] rolling release เหมาะกับ use case แบบใดมากกว่า LTS ในงานจริง
  - **คำตอบ:** **Rolling release** (เช่น Arch Linux) เหมาะกับงานที่ต้องการ software/library เวอร์ชันล่าสุดตลอดเวลา เช่น เครื่อง dev/workstation ของนักพัฒนาที่อยากทดสอบฟีเจอร์ใหม่ หรือ environment สำหรับทดลอง (research, bleeding-edge tooling) แต่แลกมาด้วยความเสี่ยงเรื่อง stability และ breaking change ที่บ่อยกว่า ส่วน **LTS** (เช่น Ubuntu LTS, RHEL) เหมาะกับ production server และงาน data engineering ที่ต้องการความเสถียร, security patch ระยะยาว และการเปลี่ยนแปลงที่คาดเดาได้ ซึ่งสำคัญกว่าการได้ฟีเจอร์ใหม่ล่าสุด

---

## 🔗 Resources

- [Kernel in Operating System](https://www.geeksforgeeks.org/operating-systems/kernel-in-operating-system/)
- [Difference between Operating System and Kernel](https://www.geeksforgeeks.org/operating-systems/difference-between-operating-system-and-kernel/)
