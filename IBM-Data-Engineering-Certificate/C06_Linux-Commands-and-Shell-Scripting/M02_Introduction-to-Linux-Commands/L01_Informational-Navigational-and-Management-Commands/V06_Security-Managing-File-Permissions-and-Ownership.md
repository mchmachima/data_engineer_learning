# Security - Managing File Permissions and Ownership

`Tags: Linux, Shell, security, permissions, ownership`

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
- [Why File Ownership and Permissions Matter](#why-file-ownership-and-permissions-matter)
- [File Ownership and Permission Levels](#file-ownership-and-permission-levels)
- [Viewing File Permissions](#viewing-file-permissions)
- [Directory Permissions](#directory-permissions)
- [Making a File Private](#making-a-file-private)
- [Executable Files and Shebangs](#executable-files-and-shebangs)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

Reading นี้อธิบายแนวคิดเรื่อง file ownership และ permission ใน Linux ซึ่งเป็นระบบ multi-user ที่ default แล้วผู้ใช้คนอื่นสามารถเห็นไฟล์ของเราได้ เนื้อหาครอบคลุมระดับการเป็นเจ้าของไฟล์ วิธีดู permission ของไฟล์และ directory และวิธีทำให้ไฟล์เป็นส่วนตัวด้วย `chmod`

---

## Why File Ownership and Permissions Matter

Linux เป็นระบบปฏิบัติการแบบ multi-user หมายความว่า user คนอื่นในระบบสามารถเห็นไฟล์ที่เราเก็บไว้ได้โดย default แต่บางไฟล์ เช่น เอกสารภาษีส่วนตัวหรือเอกสารทรัพย์สินทางปัญญาของบริษัท เป็นข้อมูลที่ private หรือ confidential จึงต้องมีกลไก permission และ ownership เพื่อป้องกันไม่ให้คนอื่นดูหรือแก้ไขได้โดยไม่ได้รับอนุญาต

---

## File Ownership and Permission Levels

Linux แบ่งระดับการเป็นเจ้าของไฟล์เป็น 3 ระดับ:

| ระดับ | ความหมาย |
| --- | --- |
| User | เจ้าของไฟล์ โดย default คือคนที่สร้างไฟล์นั้น |
| Group | กลุ่ม user ที่สามารถใช้สิทธิ์ร่วมกันในไฟล์ได้ |
| Other | ใครก็ตามที่มีสิทธิ์เข้าถึงเครื่อง Linux นั้น (ควรระวังเป็นพิเศษเมื่อกำหนดสิทธิ์ระดับนี้) |

เฉพาะ owner ตัวจริงของไฟล์เท่านั้นที่มีสิทธิ์เปลี่ยน permission ของไฟล์ได้ กล่าวคือมีแต่ owner ที่ตัดสินใจได้ว่าใครอ่าน (read), เขียน (write), หรือรัน (execute) ไฟล์นั้นได้บ้าง

---

## Viewing File Permissions

```bash
# สร้างไฟล์ใหม่โดย echo string ลงไป
echo "Who can read this file?" > my_new_file

# แสดงเนื้อหาไฟล์
more my_new_file

# ตรวจสอบ permission ของไฟล์
ls -l my_new_file
```

output ของ `ls -l` เช่น `-rw-r--r--` แบ่งออกเป็น 3 กลุ่ม กลุ่มละ 3 ตัวอักษร: กลุ่มแรก (`rw-`) คือ permission ของ user (เจ้าของ), กลุ่มที่สอง (`r--`) คือ permission ของ group, และกลุ่มสุดท้าย (`r--`) คือ permission ของ other

จากตัวอย่าง `rw-r--r--` หมายความว่า user เจ้าของมี read และ write permission (แต่ไม่มี execute), ส่วน group และ other มีแค่ read permission เท่านั้น อักขระ `-` ตัวแรกสุดของบรรทัด บ่งบอกว่า permission นี้เป็นของไฟล์ (file) หากเป็น directory จะแสดงเป็น `d` แทน

---

## Directory Permissions

Permission ของ directory ใช้ format `rwx` เหมือนกับไฟล์ แต่มีความหมายต่างออกไป:

| Directory Permission | Permissible Action(s) |
| --- | --- |
| r | list เนื้อหาของ directory ด้วยคำสั่ง `ls` |
| w | เพิ่มหรือลบไฟล์/directory ภายใน |
| x | เข้าไปใน directory ด้วยคำสั่ง `cd` |

การตั้งค่า permission ของ directory ให้เหมาะสมเป็น best practice ทั้งในแง่ security และ stability ของระบบ

---

## Making a File Private

สามารถถอด read permission ของ group และ other ออกได้ด้วย `chmod` เพื่อทำให้ไฟล์เป็น private เฉพาะ owner เท่านั้นที่อ่านได้

```bash
# ถอด read permission ออกจาก group (g) และ other (o)
chmod go-r my_new_file

# ตรวจสอบผลลัพธ์ (เหลือแค่ rw------- คือ owner อ่าน/เขียนได้คนเดียว)
ls -l my_new_file
```

`chmod` ใช้ได้ทั้งกับไฟล์และ directory

---

## Executable Files and Shebangs

ไฟล์ Linux จะเป็น executable ได้เมื่อมี instruction ที่ operating system สามารถตีความและรันได้โดยตรง เรียกอีกอย่างว่า binary หรือ executable โดยเฉพาะ script ซึ่งเป็นโปรแกรมที่เขียนด้วย scripting language เช่น Bash script (เขียนด้วยภาษา Bash หรือ "Bourne Again Shell") ที่เป็น plain text file ที่ shell สามารถตีความได้

การจะให้ text file ถือเป็น executable shell script สำหรับ user คนใดคนหนึ่งได้ ต้องมี 2 อย่างครบ:

1. ตั้งค่า execute permission ให้ user นั้น
2. มี directive ที่เรียกว่า "shebang" อยู่บรรทัดแรกของไฟล์ เพื่อประกาศตัวเองว่าเป็น binary ต่อ operating system

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Multi-user operating system | ระบบปฏิบัติการที่รองรับหลาย user ใช้งานเครื่องเดียวกัน โดย default ไฟล์ของ user หนึ่งจะเห็นได้จาก user อื่น |
| File ownership | การกำหนดว่าใครเป็นเจ้าของไฟล์ แบ่งเป็น 3 ระดับ: user, group, other |
| User (ownership level) | ระดับเจ้าของไฟล์ตัวจริง โดย default คือคนที่สร้างไฟล์นั้น |
| Group (ownership level) | ระดับการเป็นเจ้าของไฟล์ร่วมกันของกลุ่ม user |
| Other (ownership level) | ระดับที่ครอบคลุมทุกคนที่มีสิทธิ์เข้าถึงเครื่อง Linux นั้น |
| more | คำสั่งแสดงเนื้อหาไฟล์ทีละหน้า |
| Binary / Executable | ไฟล์ที่มี instruction ซึ่ง operating system รันได้โดยตรง เรียกอีกอย่างว่า ready-to-run program |
| Script | โปรแกรมที่เขียนด้วย scripting language เช่น Bash script |
| Shebang | directive ที่วางอยู่บรรทัดแรกของไฟล์ ใช้ประกาศตัวเองว่าเป็น binary ต่อ operating system |

---

## ❓ My Questions & Gaps

- [x] รูปแบบของ shebang line เขียนอย่างไร (เช่น `#!/bin/bash`) และมีผลต่างกันอย่างไรถ้าใช้ shell คนละตัว
  - **คำตอบ:** shebang ต้องอยู่บรรทัดแรกสุดของไฟล์ ขึ้นต้นด้วย `#!` ตามด้วย path เต็มไปยัง interpreter ที่จะใช้รัน script เช่น `#!/bin/bash` (ใช้ Bash shell), `#!/bin/sh` (ใช้ POSIX shell), หรือ `#!/usr/bin/env python3` (ใช้ Python 3) เมื่อรัน script ด้วย execute permission แล้ว OS จะอ่าน shebang line เพื่อรู้ว่าต้องส่งไฟล์ที่เหลือให้ interpreter ตัวไหนตีความ ถ้าเปลี่ยน shell ที่ระบุใน shebang ก็อาจทำให้ syntax บางอย่างที่ shell นั้นไม่รองรับ error ได้ (เช่น syntax เฉพาะของ Bash เช่น array หรือ `[[ ]]` จะไม่ทำงานถ้ารันผ่าน `#!/bin/sh` บนระบบที่ sh ไม่ใช่ Bash)
- [x] การตั้งค่า ownership ของไฟล์ (เปลี่ยน user/group เจ้าของ) ทำได้ด้วยคำสั่งอะไร แตกต่างจาก permission อย่างไร
  - **คำตอบ:** ใช้คำสั่ง `chown` เพื่อเปลี่ยน owner (และ/หรือ group) ของไฟล์ เช่น `chown newuser file` (เปลี่ยนเฉพาะ user), `chown newuser:newgroup file` (เปลี่ยนทั้ง user และ group), หรือ `chgrp newgroup file` (เปลี่ยนเฉพาะ group) โดยทั่วไปต้องมีสิทธิ์ระดับ superuser (`sudo`) จึงจะเปลี่ยน ownership ให้ผู้อื่นได้ ความแตกต่างจาก permission คือ ownership กำหนดว่า "ใคร" คือ user/group ที่ผูกกับไฟล์นั้น ส่วน permission (ที่ตั้งด้วย `chmod`) กำหนดว่า user/group/other แต่ละกลุ่ม "ทำอะไรได้บ้าง" (read/write/execute) กับไฟล์นั้น กล่าวคือ ownership ตอบคำถามว่าไฟล์เป็นของใคร ส่วน permission ตอบคำถามว่าคนแต่ละกลุ่มมีสิทธิ์อะไร

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมใน reading นี้
