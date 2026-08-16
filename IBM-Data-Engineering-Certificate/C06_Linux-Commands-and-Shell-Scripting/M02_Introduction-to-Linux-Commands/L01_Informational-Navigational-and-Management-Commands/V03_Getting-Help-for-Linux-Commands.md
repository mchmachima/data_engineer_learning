# Getting Help for Linux Commands

`Tags: Linux, Shell, documentation, man`

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
- [Sources for Getting Help](#sources-for-getting-help)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

Reading นี้รวบรวมแหล่งข้อมูลที่ใช้ค้นหาความช่วยเหลือเกี่ยวกับคำสั่ง Linux เมื่อการลองผิดลองถูก (experimenting) ไม่พอที่จะตอบคำถามได้ทั้งหมด เนื้อหาครอบคลุมทั้งเครื่องมือที่มากับระบบและแหล่งข้อมูลภายนอกที่ควรรู้จักไว้

---

## Sources for Getting Help

| แหล่งข้อมูล | ลักษณะการใช้งาน |
| --- | --- |
| `man` command | เข้าถึง manual page ของคำสั่งบนเครื่องโดยตรง มีมาตั้งแต่ปี 1971 |
| `tldr` command | เครื่องมือ command-line ที่แสดงตัวอย่างการใช้งานแบบกระชับ คล้าย cheatsheet ต้องติดตั้งผ่าน `npm install -g tldr` |
| Stack Overflow | community Q&A สำหรับโปรแกรมเมอร์ ค้นหาด้วยชื่อคำสั่งและ tag เช่น `linux`, `command-line` |
| Stack Exchange | เครือข่าย Q&A ที่กว้างกว่า Stack Overflow มี community เฉพาะทางเช่น Unix & Linux, Ask Ubuntu, Server Fault |
| Google search | ค้นหาทั่วไป ควรกรองผลลัพธ์ด้วยคำเช่น "Wikipedia" หรือ "Stack Overflow" และตรวจสอบความน่าเชื่อถือของแหล่งข้อมูลเอง |
| Course cheat sheets | เอกสารสรุปย่อที่คอร์สเตรียมไว้ให้ ใช้ทบทวนและช่วยทำ assignment |
| Wikipedia: List of Unix commands | หน้ารวมคำสั่ง Unix พร้อมคำอธิบายสั้น ๆ สำหรับอ้างอิงเร็ว ๆ |

```bash
# แสดงรายการคำสั่งทั้งหมดบนระบบที่มี manual page พร้อมคำอธิบายสั้น
man -k .

# เปิด manual page ของคำสั่งใดคำสั่งหนึ่ง
man command_name

# ติดตั้งเครื่องมือ tldr ผ่าน npm
npm install -g tldr

# แสดง tldr page ของคำสั่งใดคำสั่งหนึ่ง
tldr command_name
```

manual page ของ `man` แบ่งเป็นหลาย section ได้แก่ NAME (ชื่อคำสั่งและคำอธิบายสั้น), SYNOPSIS (สรุป syntax), DESCRIPTION (คำอธิบายละเอียด), OPTIONS (option ที่ใช้ได้), EXAMPLES (ตัวอย่างการใช้งาน) และ SEE ALSO (คำสั่ง/เอกสารที่เกี่ยวข้อง) นอกจากนี้อาจพบ section อื่น เช่น EXIT STATUS, RETURN VALUE, ENVIRONMENT, BUGS, FILES, AUTHOR, HISTORY และ COPYRIGHT

เมื่อค้นหาผ่าน Stack Overflow หรือ Stack Exchange ควรตรวจสอบวันที่ของคำตอบว่ายังทันสมัยอยู่หรือไม่ และอ่าน comment/discussion ประกอบเพื่อเข้าใจ context หรือข้อจำกัดของคำสั่งนั้น ๆ

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| man page | เอกสาร manual ของคำสั่ง Linux ที่เข้าถึงผ่านคำสั่ง `man` |
| tldr | เครื่องมือ command-line ที่แสดงตัวอย่างการใช้งานคำสั่งแบบสั้นกระชับ คล้าย cheatsheet ย่อมาจาก "Too Long; Didn't Read" |
| Stack Overflow | community Q&A สำหรับโปรแกรมเมอร์และนักพัฒนา |
| Stack Exchange | เครือข่าย community Q&A ครอบคลุมหัวข้อกว้างกว่า Stack Overflow |

---

## ❓ My Questions & Gaps

- [ ] tldr page แตกต่างจาก `man -h` หรือ `command --help` อย่างไรในทางปฏิบัติ ควรใช้ตัวไหนก่อน
- [ ] มี alternative อื่นสำหรับติดตั้ง tldr ที่ไม่ต้องพึ่ง npm หรือไม่

---

## 🔗 Resources

- [Newest Linux questions on Stack Overflow](https://stackoverflow.com/questions/tagged/linux)
- [Unix & Linux Stack Exchange](https://unix.stackexchange.com/)
- [Wikipedia: List of Unix commands](https://en.wikipedia.org/wiki/List_of_Unix_commands)
