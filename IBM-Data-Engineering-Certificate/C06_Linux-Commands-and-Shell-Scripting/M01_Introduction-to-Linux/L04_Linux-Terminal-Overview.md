# Linux Terminal Overview

`Tags: Linux, Shell, Terminal, cd, navigation, file-system`

| Field            | Value                                         |
| ---------------- | --------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate |
| **Course**       | C06 Linux Commands and Shell Scripting        |
| **Module**       | M01 Introduction to Linux                     |
| **Lesson**       | L04 Linux Terminal Overview                   |
| **Date studied** | 2026-08-16                                    |

---

## Table of Contents

- [Overview](#overview)
- [The Linux Shell](#the-linux-shell)
- [The Linux Terminal](#the-linux-terminal)
- [How a Command Travels from Terminal to Hardware](#how-a-command-travels-from-terminal-to-hardware)
- [Command Line and Command Prompt](#command-line-and-command-prompt)
- [Paths and Special Paths](#paths-and-special-paths)
- [Navigating with cd](#navigating-with-cd)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้แนะนำว่า Linux Shell และ Linux Terminal คืออะไร และทำงานร่วมกันอย่างไรเมื่อผู้ใช้ป้อนคำสั่ง พร้อมอธิบายแนวคิดเรื่อง current working directory, path และ special path ต่าง ๆ ปิดท้ายด้วยการใช้คำสั่ง `cd` เพื่อนำทางไปมาระหว่าง directory ใน Linux file system

---

## The Linux Shell

Linux Shell คือ OS-level application ที่ทำหน้าที่ตีความ (interpret) คำสั่งที่ผู้ใช้ป้อนเข้ามา ในยุคแรกของ Unix และ Linux, Shell เป็นวิธีเดียวที่ใช้โต้ตอบกับ operating system ได้ ปัจจุบันแม้จะมี graphical user interface (GUI) ให้ใช้แล้ว แต่ Shell ก็ยังคงเป็นตัวเลือกที่ยืดหยุ่นและเป็นวิธีที่ง่ายในการรัน script file

Shell commands ใช้ทำงานได้หลายอย่าง เช่น:

- ย้ายและคัดลอกไฟล์ (moving and copying files)
- เขียนและอ่านไฟล์ (writing to and reading from files)
- ดึงและกรองข้อมูล (extracting and filtering data)
- ค้นหาข้อมูล (searching for data)

Shell มีหลายเวอร์ชัน แต่ base functionality ของแต่ละตัวใกล้เคียงกัน ตัวอย่างที่นิยม ได้แก่ **bash** และ **zsh**

---

## The Linux Terminal

ผู้ใช้โต้ตอบกับ Linux Shell ผ่าน **Linux Terminal** ซึ่งเป็น application หรือ user interface ที่ใช้ป้อนคำสั่งที่ต้องการรัน และรับผลลัพธ์ (output) จากคำสั่งนั้น

ตัวอย่างเช่น การเปิดโปรแกรม Python เพื่อรันไฟล์ `myprogram.py` ทำได้โดยพิมพ์ `python myprogram.py` แล้วกด Enter, Shell จะรันคำสั่งนี้และโปรแกรมจะพิมพ์ข้อความ `Hello World` ออกมาที่ Terminal

---

## How a Command Travels from Terminal to Hardware

```mermaid
flowchart LR
    A[User พิมพ์คำสั่งใน Terminal] --> B[Terminal ส่งคำสั่งไปยัง Shell]
    B --> C[OS core components และ Kernel แปลคำสั่งให้ Hardware]
    C --> D[Hardware ทำงานตามคำสั่ง]
    D --> E[Kernel อ่านผลลัพธ์/การเปลี่ยนแปลง]
    E --> F[ส่งผลลัพธ์กลับผ่าน Shell ไปยัง Terminal]
```

ลำดับการทำงาน: ผู้ใช้ป้อนคำสั่งใน Terminal → Terminal ส่งต่อคำสั่งไปยัง Shell → core component ของ OS และ Kernel แปลคำสั่งให้ hardware ทำงานตาม → เมื่อ hardware ทำงานเสร็จ Kernel จะอ่านผลลัพธ์หรือการเปลี่ยนแปลง แล้วส่งกลับผ่าน Shell ไปแสดงที่ Terminal ให้ผู้ใช้เห็น

---

## Command Line and Command Prompt

Terminal ส่วนใหญ่มี user interface ที่คล้ายกันสำหรับป้อนคำสั่ง:

- **Command line** — พื้นที่ที่ใช้พิมพ์คำสั่ง
- **Command prompt** — เส้นแนวตั้ง (cursor) ที่บ่งบอกตำแหน่งที่ข้อความจะปรากฏเมื่อพิมพ์

Terminal บางตัวจะแสดง current working directory แบบเต็ม path (เช่น `/home/me/documents`) แต่บางตัวก็แสดงแค่ชื่อ directory ปัจจุบัน (เช่น `documents`) เท่านั้น

**Current working directory** คือตำแหน่งที่ Shell จะค้นหาคำสั่งหรือไฟล์ที่ผู้ใช้ระบุในการรันคำสั่ง (เช่น โปรแกรม Python ในตัวอย่างก่อนหน้า)

---

## Paths and Special Paths

**Path** คือตำแหน่งของไฟล์หรือ directory ในรูปแบบที่มนุษย์อ่านเข้าใจได้ (human-readable location) ในระบบไฟล์ของ Linux โครงสร้าง `A/B` หมายถึงไฟล์หรือ directory ชื่อ `B` อยู่ภายใน directory ชื่อ `A`

| สัญลักษณ์ | ความหมาย |
| --- | --- |
| `~` (tilde) | home directory ของผู้ใช้ |
| `/` (slash ที่ต้นบรรทัด) | root directory |
| `..` (สองจุด) | parent ของ current directory |
| `.` (จุดเดียว) | current directory |

---

## Navigating with cd

ใช้คำสั่ง `cd` (change directory) เพื่อเปลี่ยน current working directory

```bash
# ไปที่ root directory
cd /

# ย้ายเข้าไปที่ bin directory (อยู่ภายใต้ root, มีโปรแกรมที่ระบบต้องใช้ เช่น ls)
cd bin

# รันโปรแกรม ls ที่อยู่ใน current working directory โดยตรง
./ls

# กลับไปที่ home directory ของผู้ใช้
cd ~

# แม้ current working directory จะไม่มีโปรแกรม ls อยู่ แต่ก็ยังรันได้
# เพราะคำสั่งใน bin หลายตัวถูกผูกไว้ใน shell ให้เรียกใช้ได้จากทุกที่
ls

# จาก /home ย้ายไปที่ parent directory (คือ / หรือ root)
cd ..

# ย้ายไปยัง USB drive ชื่อ my_usb_drive ที่อยู่ใน /media
cd /media/my_usb_drive

# นำทางขึ้นสองระดับในคำสั่งเดียว (จาก media ขึ้นไปที่ root)
cd ../..

# นำทางลงไปที่ documents directory แบบระบุ absolute path
cd /home/me/documents

# เริ่มโปรแกรม Python และรันไฟล์ myprogram.py ที่อยู่ใน /home/me
python myprogram.py
```

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Shell | OS-level application ที่ตีความและรันคำสั่งที่ผู้ใช้ป้อนเข้ามา |
| Terminal | application หรือ user interface ที่ใช้ป้อนคำสั่งและรับผลลัพธ์จาก Shell |
| bash | ตัวอย่าง Shell ที่นิยมใช้กันแพร่หลาย |
| zsh | ตัวอย่าง Shell ที่นิยมใช้อีกตัวหนึ่ง |
| Command line | พื้นที่ใน Terminal ที่ใช้พิมพ์คำสั่ง |
| Command prompt | เส้น cursor ที่บ่งบอกตำแหน่งที่ข้อความจะปรากฏใน Terminal |
| Current working directory | directory ปัจจุบันที่ Shell ใช้เป็นจุดอ้างอิงในการค้นหาไฟล์หรือคำสั่ง |
| Path | ตำแหน่งของไฟล์หรือ directory ที่มนุษย์อ่านเข้าใจได้ในระบบไฟล์ |
| Root directory | directory บนสุดของระบบไฟล์ Linux แทนด้วยเครื่องหมาย `/` |
| Home directory | directory ส่วนตัวของผู้ใช้ แทนด้วยเครื่องหมาย `~` |
| cd | คำสั่งสำหรับเปลี่ยน current working directory (ย่อจาก change directory) |
| bin directory | directory ที่เก็บโปรแกรม (executable file) ที่ระบบต้องใช้งาน |
| ls | โปรแกรมสำหรับแสดงชื่อไฟล์และ directory ทั้งหมดใน directory ปัจจุบัน |

---

## ❓ My Questions & Gaps

- [x] ทำไมคำสั่งบางตัวใน `/bin` (เช่น `ls`) ถึงเรียกใช้ได้จากทุก directory โดยไม่ต้องระบุ path เต็ม ในขณะที่บางโปรแกรมต้องใช้ `./` นำหน้าเสมอ — เกี่ยวข้องกับ `PATH` environment variable หรือไม่
  - **คำตอบ:** ใช่ เกี่ยวข้องโดยตรงกับ **`PATH` environment variable** ซึ่งเป็นตัวแปรที่เก็บรายการ directory (คั่นด้วย `:`) ที่ shell จะค้นหาโปรแกรมให้อัตโนมัติเมื่อพิมพ์ชื่อคำสั่งเฉย ๆ โดยปกติ `/bin`, `/usr/bin` และ directory สำคัญอื่น ๆ จะถูกใส่ไว้ใน `PATH` อยู่แล้ว ทำให้พิมพ์ `ls` จากที่ไหนก็รันได้ทันที แต่ถ้าโปรแกรมนั้นอยู่ใน directory ปัจจุบันที่ **ไม่ได้อยู่ใน `PATH`** (เช่น โฟลเดอร์ project ของผู้ใช้เอง) shell จะหาไม่เจอถ้าพิมพ์ชื่อโปรแกรมเฉย ๆ จึงต้องระบุ `./` นำหน้าเพื่อบอกว่า "รันโปรแกรมนี้จาก current working directory โดยตรง" แทนที่จะให้ shell ไปค้นหาใน `PATH`
- [x] ความแตกต่างระหว่าง absolute path กับ relative path ในทางปฏิบัติควรเลือกใช้แบบไหนเมื่อไหร่
  - **คำตอบ:** **Absolute path** คือ path ที่เริ่มต้นจาก root directory (`/`) เสมอ เช่น `/home/me/documents` ระบุตำแหน่งที่แน่นอนไม่ว่าจะรันคำสั่งจาก directory ไหนก็ได้ผลลัพธ์เดียวกัน เหมาะกับการใช้ใน script หรือ config ที่ต้องการความแน่นอนและ portability ข้าม environment ส่วน **Relative path** คือ path ที่อ้างอิงจาก current working directory เช่น `../documents` หรือ `./ls` สั้นและสะดวกกว่าเวลาพิมพ์คำสั่งแบบ interactive ใน terminal แต่ผลลัพธ์จะเปลี่ยนไปตาม directory ที่รันคำสั่งอยู่ ในทางปฏิบัติ: ใช้ relative path เวลาทำงานแบบ interactive หรือทำงานภายใน project เดียวกัน และใช้ absolute path เมื่อเขียน script, cron job หรืออ้างอิง resource ข้าม location ที่ต้องการความแน่นอน

---

## 🔗 Resources

- (ไม่มีลิงก์ระบุในวิดีโอ)
