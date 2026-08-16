# Overview of Common Linux Shell Commands

`Tags: Linux, Shell, Bash, command-line`

| Field            | Value                                                           |
| ---------------- | --------------------------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate                   |
| **Course**       | C06 Hands-on Introduction to Linux Commands and Shell Scripting |
| **Module**       | M02 Introduction to Linux Commands                              |
| **Lesson**       | L01 Informational, Navigational, & Management Commands          |
| **Date studied** | 2026-08-16                                                      |

---

## Table of Contents

- [Overview](#overview)
- [What a Shell Is](#what-a-shell-is)
- [Applications of Shell Commands](#applications-of-shell-commands)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้แนะนำภาพรวมของ shell ใน Unix-like operating system ว่าคืออะไร ใช้ทำอะไรได้บ้าง และมีคำสั่งพื้นฐานอะไรบ้างที่ใช้บ่อยในแต่ละหมวดงาน เนื้อหานี้เป็นการปูพื้นก่อนจะเจาะลึกแต่ละคำสั่งในวิดีโอถัดไปของโมดูลนี้

---

## What a Shell Is

Shell เป็น user interface ที่ทรงพลังสำหรับระบบปฏิบัติการแบบ Unix-like สามารถตีความ (interpret) คำสั่งและรันโปรแกรมอื่นได้ นอกจากจะเป็นช่องทางเข้าถึงไฟล์ ยูทิลิตี้ และแอปพลิเคชันแล้ว shell ยังเป็นทั้ง interactive language และ scripting language ที่ใช้เขียน script เพื่อ automate งานได้ด้วย

shell เริ่มต้น (default) บนระบบ Linux ส่วนใหญ่คือ Bash ("Bourne Again SHell") ส่วน shell อื่น ๆ ที่พบได้ เช่น Bourne shell (SH), Korn shell (KSH), TC shell, Z shell และ fish คอร์สนี้จะใช้ Bash shell เป็นหลัก

```bash
# ตรวจสอบว่า default shell ของระบบคืออะไร
printenv SHELL

# สลับไปใช้ bash shell
bash
```

Convention ของคอร์สนี้ใช้เครื่องหมาย `$` แทน command prompt ส่วนที่อื่นอาจใช้เครื่องหมาย `>` แทนความหมายเดียวกัน

---

## Applications of Shell Commands

คำสั่ง shell ถูกใช้งานได้หลายด้าน แบ่งเป็นหมวดหมู่ตามลักษณะงาน:

| หมวดงาน                                     | ตัวอย่างการใช้งาน                     |
| ------------------------------------------- | ------------------------------------- |
| Getting information                         | ตรวจสอบ user, OS, process, disk usage |
| Navigating & working with files/directories | เข้าถึงและจัดการไฟล์-โฟลเดอร์         |
| Printing file and string contents           | แสดงเนื้อหาไฟล์หรือ string            |
| File compression and archiving              | บีบอัดและรวมไฟล์                      |
| Performing network operations               | ทำงานด้านเครือข่าย                    |
| Monitoring performance and status           | ติดตามสถานะระบบและ resource           |
| Running batch jobs                          | เช่นงาน ETL                           |

รายการคำสั่งที่พบบ่อยในแต่ละหมวด:

| หมวด                   | คำสั่ง                                                    | ความหมายโดยย่อ                                                                                             |
| ---------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| ข้อมูลระบบ             | `whoami`, `id`, `uname`, `ps`, `top`, `df`, `man`, `date` | ดู username, user/group ID, ชื่อ OS, process ที่รันอยู่, resource usage, disk usage, manual, วันที่        |
| ไฟล์                   | `cp`, `mv`, `rm`, `touch`, `chmod`, `wc`, `grep`          | คัดลอก, ย้าย/เปลี่ยนชื่อ, ลบ, สร้างไฟล์เปล่า, เปลี่ยน permission, นับ line/word/character, ค้นหา pattern   |
| directory              | `ls`, `find`, `pwd`, `mkdir`, `cd`, `rmdir`               | list ไฟล์, ค้นหาไฟล์, แสดง current directory, สร้าง directory, เปลี่ยน directory, ลบ directory             |
| แสดงเนื้อหาไฟล์/string | `cat`, `more`, `head`, `tail`, `echo`                     | แสดงเนื้อหาไฟล์ทั้งหมด, แสดงทีละหน้า, แสดง N บรรทัดแรก/สุดท้าย, พิมพ์ string หรือค่าตัวแปร                 |
| compression/archiving  | `tar`, `zip`, `unzip`                                     | archive ไฟล์, บีบอัดไฟล์, แตกไฟล์ zip                                                                      |
| networking             | `hostname`, `ping`, `ifconfig`, `curl`, `wget`            | แสดงชื่อ host, ทดสอบการเชื่อมต่อ, ตั้งค่า/แสดง network interface, แสดงเนื้อหาจาก URL, ดาวน์โหลดไฟล์จาก URL |

หากใช้เครื่อง Windows แต่ต้องการรัน Linux สามารถทำได้หลายวิธี เช่น ติดตั้งบน drive partition แยก (ต้อง reboot เพื่อสลับ OS), ใช้ virtual machine, ใช้ Linux emulator เช่น CygWin หรือใช้ Windows Subsystem for Linux (WSL) ซึ่งเป็น compatibility layer ที่รัน Linux binary executable บน Windows ได้โดยตรง

---

## 📖 Key Terms & Glossary

| Term (ศัพท์)                      | คำอธิบาย (ภาษาไทย)                                                                                                     |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Shell                             | user interface สำหรับตีความคำสั่งและรันโปรแกรมบนระบบ Unix-like เป็นได้ทั้ง interactive language และ scripting language |
| Bash                              | shell เริ่มต้น (default) ของระบบ Linux ส่วนใหญ่ ย่อมาจาก "Bourne Again SHell"                                          |
| Command prompt                    | สัญลักษณ์ที่บ่งบอกว่า shell พร้อมรับคำสั่งถัดไป คอร์สนี้ใช้ `$`                                                        |
| WSL (Windows Subsystem for Linux) | compatibility layer ที่ทำให้รัน Linux binary executable ได้โดยตรงบน Windows                                            |
| Emulator                          | โปรแกรมที่จำลองสภาพแวดล้อมของระบบอื่นให้ทำงานบนระบบปัจจุบันได้ เช่น CygWin จำลอง Linux บน Windows                      |

---

## ❓ My Questions & Gaps

- [x] ความแตกต่างระหว่างการติดตั้ง Linux ผ่าน dual-boot partition, virtual machine, และ WSL ในแง่ performance และ use case ที่เหมาะสม

  | วิธีการ                       | Performance                                                                                  | Use case ที่เหมาะสม                                                                                            |
  | ------------------------------ | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
  | **Dual-boot (separate partition)** | ดีที่สุด — รัน Linux บน hardware โดยตรง (native) ไม่มี overhead จากการ virtualize             | ต้องการ performance เต็มที่ (เช่นงาน compute หนัก, gaming), ยอมรับการต้อง reboot สลับ OS ได้                    |
  | **Virtual Machine (VM)**       | ช้ากว่า native เพราะมี hypervisor คั่นกลางและแบ่ง resource (CPU/RAM) จาก host OS               | ต้องการรัน Linux เต็มรูปแบบพร้อมกับ Windows แบบ real-time (ไม่ต้อง reboot), ทดสอบหลาย distro, isolate environment ชัดเจน |
  | **WSL**                        | เร็วกว่า VM ทั่วไป เพราะ WSL2 ใช้ lightweight VM ที่ผูก integrate กับ Windows kernel/file system โดยตรง | งาน dev/data engineering ทั่วไปที่ใช้ command line, script, หรือ tool ของ Linux ควบคู่กับ Windows โดยไม่ต้องสลับ OS หรือใช้ resource มาก (เหมาะกับคอร์สนี้) |
  | **Emulator (เช่น CygWin)**     | มักช้าที่สุดในบางงาน เพราะ translate คำสั่ง Linux ให้ทำงานบน Windows kernel โดยตรง ไม่ใช่ Linux kernel จริง | ต้องการแค่ชุดคำสั่ง Unix-like พื้นฐานบน Windows แบบเบา ๆ ไม่ต้องการ Linux kernel เต็มรูปแบบ                     |

  โดยสรุป สำหรับการเรียนคอร์สนี้ WSL เป็นตัวเลือกที่สมดุลที่สุดระหว่าง performance และความสะดวก เพราะไม่ต้อง reboot และใช้ resource น้อยกว่า VM

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมในวิดีโอนี้
