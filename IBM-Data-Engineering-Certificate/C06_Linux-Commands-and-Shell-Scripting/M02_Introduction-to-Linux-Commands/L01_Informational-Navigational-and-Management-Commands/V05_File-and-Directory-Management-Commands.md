# File and Directory Management Commands

`Tags: Linux, Shell, file-management, permissions`

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
- [Creating and Removing Directories](#creating-and-removing-directories)
- [Creating and Updating Files with touch](#creating-and-updating-files-with-touch)
- [Copying Files and Directories](#copying-files-and-directories)
- [Moving Files and Directories](#moving-files-and-directories)
- [Managing Executable Permissions with chmod](#managing-executable-permissions-with-chmod)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้สอนคำสั่งจัดการไฟล์และ directory ได้แก่การสร้าง/ลบด้วย `mkdir`, `rm`, `rmdir`, `touch`, การคัดลอก/ย้ายด้วย `cp`/`mv` และการปรับ permission ให้ไฟล์รันเป็น executable ได้ด้วย `chmod` ต่อยอดจากคำสั่ง navigation ในวิดีโอก่อนหน้า

---

## Creating and Removing Directories

`mkdir` ("make directory") สร้าง directory ใหม่ ส่วน `rm` ("remove") ใช้ลบไฟล์หรือ directory โดยการลบ directory ต้องใช้ option `-r` (recursive) เพื่อลบไฟล์ลูกทั้งหมดไปด้วย

```bash
# สร้าง directory ชื่อ test
mkdir test

# ลบไฟล์
rm file1

# ลบ directory พร้อมไฟล์ลูกทั้งหมด (recursive)
rm -r folder1
```

การใช้ `rm -r` ควรระมัดระวังเป็นพิเศษ เพราะสามารถลบข้อมูลสำคัญโดยไม่ตั้งใจได้ง่าย สำหรับกรณีที่ต้องการลบเฉพาะ directory ที่ว่างเปล่า ควรใช้ `rmdir` แทน เพราะ `rmdir` จะลบได้ก็ต่อเมื่อ directory นั้นว่างเปล่าเท่านั้น จึงการันตีว่าจะไม่ลบไฟล์สำคัญโดยไม่ตั้งใจ

```bash
# สร้าง directory ว่างเปล่าแล้วลบด้วย rmdir (ปลอดภัยกว่า rm -r)
mkdir empty_folder
rmdir empty_folder
```

---

## Creating and Updating Files with touch

`touch` สร้างไฟล์เปล่า หากใช้กับไฟล์ที่มีอยู่แล้ว จะอัปเดต last-modified timestamp ของไฟล์นั้นแทนการสร้างใหม่

```bash
# สร้างไฟล์เปล่าหลายไฟล์พร้อมกัน
touch a.txt b.txt c.txt d.txt

# ตรวจสอบวันที่แก้ไขล่าสุดของไฟล์
date -r notes.txt

# อัปเดต last-modified timestamp ของไฟล์ที่มีอยู่แล้ว
touch notes.txt
```

---

## Copying Files and Directories

`cp` ("copy") คัดลอกไฟล์หรือ directory หากไม่ระบุชื่อไฟล์ปลายทาง จะใช้ชื่อเดิม การคัดลอกทั้ง directory ต้องใช้ option `-r` เพื่อคัดลอกไฟล์และ subdirectory ทั้งหมดแบบ recursive

```bash
# คัดลอกไฟล์ notes.txt เข้าไปในโฟลเดอร์ Documents (ใช้ current directory เป็น source โดย default)
cp notes.txt Documents

# คัดลอกทั้ง directory แบบ recursive
cp -r Documents Docs_copy
```

---

## Moving Files and Directories

`mv` ("move") ใช้ย้ายไฟล์หรือ directory (และสามารถใช้เปลี่ยนชื่อไฟล์ได้ในตัวด้วย) โดยระบุ path ต้นทางตามด้วย path ปลายทาง

```bash
# ย้ายไฟล์ my_script.sh ไปยังโฟลเดอร์ Scripts
mv my_script.sh Scripts

# ย้ายหลาย directory ไปรวมไว้ในโฟลเดอร์ Documents
mv Notes Scripts Documents
```

---

## Managing Executable Permissions with chmod

`chmod` ("change mode") ใช้เปลี่ยน read, write, execute permission ของไฟล์ โดย default ไฟล์ script มักมีแค่ read/write permission ทำให้รันไฟล์โดยตรงไม่ได้ (permission denied)

```bash
# ตรวจสอบ permission ปัจจุบันของไฟล์ (rw- หมายถึงมีแค่ read/write)
ls -l my_script.sh

# เพิ่ม execute permission ให้ไฟล์
chmod +x my_script.sh

# ตรวจสอบอีกครั้งว่ามี execute permission แล้ว (x ปรากฏใน output)
ls -l my_script.sh

# รัน script ที่เพิ่ง set permission เป็น executable
./my_script.sh
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| mkdir | คำสั่งสร้าง directory ใหม่ (make directory) |
| rm | คำสั่งลบไฟล์หรือ directory ต้องใช้ option `-r` เพื่อลบ directory แบบ recursive |
| rmdir | คำสั่งลบเฉพาะ directory ที่ว่างเปล่าเท่านั้น ปลอดภัยกว่า `rm -r` |
| touch | คำสั่งสร้างไฟล์เปล่า หรืออัปเดต last-modified timestamp ของไฟล์ที่มีอยู่แล้ว |
| cp | คำสั่งคัดลอกไฟล์หรือ directory (copy) ต้องใช้ `-r` เพื่อคัดลอก directory แบบ recursive |
| mv | คำสั่งย้ายหรือเปลี่ยนชื่อไฟล์/directory (move) |
| chmod | คำสั่งเปลี่ยน read, write, execute permission ของไฟล์ (change mode) |
| Executable permission | สิทธิ์ที่อนุญาตให้รันไฟล์เป็นโปรแกรมได้ แสดงเป็นตัวอักษร `x` ใน output ของ `ls -l` |

---

## ❓ My Questions & Gaps

- [ ] `chmod` รองรับการตั้งค่า permission แบบตัวเลข (เช่น `chmod 755`) ต่างจากแบบ symbolic (`+x`) อย่างไร
- [ ] เหตุใด `rm -rf` ถึงถูกแนะนำให้หลีกเลี่ยงเมื่อเทียบกับ `rmdir` สำหรับ directory ที่ว่างเปล่า

---

## 🔗 Resources

- ไม่มีลิงก์หรือเอกสารอ้างอิงเพิ่มเติมในวิดีโอนี้
