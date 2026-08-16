# Informational Commands

`Tags: Linux, Shell, command-line, system-information`

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
- [User and OS Information](#user-and-os-information)
- [Disk Usage](#disk-usage)
- [Process Monitoring](#process-monitoring)
- [Printing Strings, Variables, and Dates](#printing-strings-variables-and-dates)
- [Getting Help with man](#getting-help-with-man)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้เจาะลึกกลุ่มคำสั่ง informational command ที่ใช้ดูข้อมูล user, ระบบปฏิบัติการ, การใช้งาน disk, process ที่กำลังทำงาน รวมถึงการพิมพ์ string/variable/date และการเปิดดู manual ของคำสั่งต่าง ๆ เป็นชุดคำสั่งพื้นฐานที่ใช้ตรวจสอบสถานะระบบก่อนเริ่มงานอื่น

---

## User and OS Information

`whoami` แสดง username ของ user ปัจจุบัน ไม่รับ argument หรือ option ใด ๆ ส่วน `id` คืนค่า user ID หรือ group ID ซึ่งเป็นตัวเลขที่ระบบกำหนดให้แต่ละ user/group

```bash
# แสดง username ของ user ปัจจุบัน
whoami
# ผลลัพธ์ (ตัวอย่างจากวิดีโอ user "John Doe"): johndoe

# แสดง numerical user ID
id -u
# ผลลัพธ์: ตัวเลข user ID เช่น 501

# แสดงชื่อ (name) แทนตัวเลข user ID
id -un
# ผลลัพธ์: ชื่อ user เช่น johndoe
```

`uname` ("Unix name") คืนข้อมูล OS เช่น kernel name และ version สามารถใช้ระบุชนิดระบบหรือช่วย diagnose ปัญหาที่เกี่ยวกับระบบได้

```bash
# แสดงชื่อ operating system
uname
# ผลลัพธ์ (ตัวอย่างจากวิดีโอ): Darwin

# แสดงทั้งชื่อ OS และ version
uname -s -r
# ผลลัพธ์: ชื่อ OS ตามด้วยเลข version เช่น Darwin 22.1.0

# แสดงข้อมูล version แบบละเอียด
uname -v
# ผลลัพธ์: build/version string แบบละเอียดของ kernel
```

---

## Disk Usage

`df` ("disk free") แสดงข้อมูลการใช้งาน disk ของ filesystem ที่ mount อยู่ ใช้ตรวจสอบพื้นที่ว่างหรือ monitor การใช้ disk

```bash
# แสดง disk usage เฉพาะ home directory (~) แบบอ่านง่าย (human readable)
df -h ~
# ผลลัพธ์: ตาราง disk ที่ mount อยู่บน home directory พร้อม size, used, avail, capacity (%)

# แสดง disk usage ของทุก filesystem
df -h
# ผลลัพธ์: ตาราง disk usage ของทุก filesystem ในระบบ พร้อมหน่วยแบบ human readable (GB/TB)
```

option `-h` ทำให้ output อยู่ในหน่วยที่ "human readable" เช่น GB, TB แทนการแสดงเป็น byte ตรง ๆ ผลลัพธ์จะรวมขนาด (size), พื้นที่ใช้ไป (capacity used) และพื้นที่ว่าง (available space) ของแต่ละ filesystem

---

## Process Monitoring

`ps` ("process status") แสดงรายการ process ที่กำลังรันอยู่ พร้อมชื่อ process, process ID (PID) และเวลาที่ process รันมาแล้ว

```bash
# แสดงทุก process ในระบบ ไม่ว่าใครเป็นคนเริ่ม
ps -e
# ผลลัพธ์: ตารางรายชื่อ process, PID, และเวลาที่รันมาแล้ว (เช่น TIME) ของทุก process
```

`top` ("table of processes") ทำหน้าที่คล้าย task manager แสดงตารางของ process ที่กำลังรันพร้อม resource usage (CPU, memory, I/O) โดย default จะเรียงตาม CPU usage

```bash
# แสดง 3 task ที่ใช้ CPU สูงสุด
top -n 3
# ผลลัพธ์ (ตัวอย่างจากวิดีโอ): Chrome, top, Spotify (เรียงตาม CPU usage มากไปน้อย)
```

---

## Printing Strings, Variables, and Dates

`echo` ใช้พิมพ์ text หรือค่า variable ออกทาง terminal หรือใน shell script แม้ไม่จำเป็นต้องใส่ quote รอบ string ที่มี space แต่เป็น best practice ที่ควรทำ

```bash
# พิมพ์บรรทัดว่างเปล่า
echo
# ผลลัพธ์: บรรทัดว่างเปล่า (newline)

# พิมพ์คำเดียว
echo hello
# ผลลัพธ์: hello

# พิมพ์ string ที่มี quote (best practice)
echo "Learning Linux is fun!"
# ผลลัพธ์: Learning Linux is fun!

# แสดงค่าของตัวแปร PATH
echo $PATH
# ผลลัพธ์: รายการ path คั่นด้วย colon (:) เช่น /usr/local/bin:/usr/bin:/bin
```

`date` แสดงวันที่และเวลาปัจจุบันของระบบ สามารถ format output ได้ด้วย control character ที่ขึ้นต้นด้วย `%` ภายใน quoted string ที่นำหน้าด้วยเครื่องหมาย `+`

```bash
# แสดง default date format
date
# ผลลัพธ์: วันในสัปดาห์, วันที่, เดือน, ปี, เวลา, และ time zone เช่น Tue Apr 7 10:32:15 EDT 2023

# แสดงวันของปี (day of year) และปี ในรูปแบบ custom
date +"%j day of %Y"
# ผลลัพธ์ (ตัวอย่างจากวิดีโอ): 097 day of 2023

# ตัวอย่าง combine format control กับข้อความอื่น
date +"%A %j %Y"
# ผลลัพธ์: ชื่อวันแบบเต็ม วันของปี และปี เช่น Friday 097 2023
```

`%j` คือ numerical day of the year, `%Y` คือปี ค.ศ. เต็ม และ `%A` คือชื่อวันแบบเต็ม (เช่น Monday)

---

## Getting Help with man

`man` ("manual") ใช้เปิด reference manual ของคำสั่ง Linux เกือบทุกคำสั่งมี manual page ให้เรียกดูได้

```bash
# แสดง manual ของคำสั่ง id
man id
# ผลลัพธ์: manual page ของ id เช่น NAME "id — return user identity", ตามด้วย SYNOPSIS, DESCRIPTION, OPTIONS (เช่น -a)
```

manual page จะให้สรุปสั้น ๆ ว่าคำสั่งนั้นทำอะไร (เช่น "return user identity") พร้อมรายการ option ที่ใช้ได้ (เช่น `-a`) วงเล็บเหลี่ยม `[ ]` หมายถึง parameter ที่เป็น optional และมีคำอธิบายแบบละเอียดกว่าด้วย แม้แต่คำสั่ง `man` เองก็มี manual page ของตัวเอง

---

## 📖 Key Terms & Glossary

| Term (ศัพท์)               | คำอธิบาย (ภาษาไทย)                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------- |
| whoami                     | คำสั่งแสดง username ของ user ปัจจุบัน ไม่รับ argument หรือ option                                       |
| id                         | คำสั่งแสดง user ID หรือ group ID ของ user ปัจจุบัน                                                      |
| uname                      | คำสั่งแสดงข้อมูล operating system เช่น kernel name และ version                                          |
| df                         | คำสั่งแสดงข้อมูลการใช้งาน disk ของ filesystem ที่ mount อยู่ (disk free)                                |
| ps                         | คำสั่งแสดงรายการ process ที่กำลังทำงานอยู่พร้อม process ID (process status)                             |
| top                        | คำสั่งที่ทำหน้าที่คล้าย task manager แสดง process และ resource usage แบบ real-time (table of processes) |
| echo                       | คำสั่งพิมพ์ text หรือค่าตัวแปรออกทาง terminal                                                           |
| date                       | คำสั่งแสดงวันที่และเวลาปัจจุบันของระบบ รองรับการ format output ด้วย control character                   |
| man                        | คำสั่งเปิด reference manual ของคำสั่งอื่น (manual)                                                      |
| Human readable (-h option) | option ที่ทำให้ output แสดงหน่วยที่อ่านง่าย เช่น GB, TB แทนการแสดงเป็น byte                             |
| Mount                      | การทำให้ file system ของ disk หนึ่งเข้าถึงได้ผ่าน directory หนึ่งในระบบ                                 |

---

## ❓ My Questions & Gaps

- [x] ความแตกต่างระหว่าง PID ที่ได้จาก `ps` กับข้อมูลที่ได้จาก `top` ในแง่ความละเอียดและการอัปเดตแบบ real-time
  - **คำตอบ:** `ps` เป็น snapshot ครั้งเดียว ณ เวลาที่รันคำสั่ง แสดง process, PID, และเวลาที่รันมาแล้ว แต่ไม่รีเฟรชเอง ส่วน `top` แสดงข้อมูลแบบ real-time รีเฟรชตารางเป็นระยะ (default ทุกไม่กี่วินาที) และมีข้อมูล resource usage เพิ่มเติม เช่น % CPU, memory ทำให้เหมาะกับการเฝ้าดู process ที่กินทรัพยากรมากขณะระบบทำงานอยู่ ในขณะที่ `ps` เหมาะกับการเช็คสถานะ ณ จุดใดจุดหนึ่งหรือใช้ใน script

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมในวิดีโอนี้
