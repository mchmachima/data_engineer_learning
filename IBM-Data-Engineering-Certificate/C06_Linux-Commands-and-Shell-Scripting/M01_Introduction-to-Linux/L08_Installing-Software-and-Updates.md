# Installing Software and Updates

`Tags: Linux, package-manager, apt, yum, deb, rpm`

| Field            | Value                                         |
| ---------------- | --------------------------------------------- |
| **Certificate**  | IBM Data Engineering Professional Certificate |
| **Course**       | C06 Linux Commands and Shell Scripting        |
| **Module**       | M01 Introduction to Linux                     |
| **Lesson**       | L08 Installing Software and Updates           |
| **Date studied** | 2026-08-16                                    |

---

## Table of Contents

- [Overview](#overview)
- [Packages and Package Managers](#packages-and-package-managers)
- [deb vs RPM Packages](#deb-vs-rpm-packages)
- [GUI-Based Package Managers](#gui-based-package-managers)
- [Command-Line Package Managers](#command-line-package-managers)
- [Package Managers for Other Ecosystems](#package-managers-for-other-ecosystems)
- [Key Terms & Glossary](#-key-terms--glossary)
- [My Questions & Gaps](#-my-questions--gaps)
- [Resources](#-resources)

---

## Overview

วิดีโอนี้อธิบายว่า package และ package manager คืออะไรในระบบ Linux แยกความแตกต่างระหว่างไฟล์ประเภท `.deb` และ `.rpm` ที่ใช้กับ distro คนละตระกูล พร้อมแนะนำ package manager ทั้งแบบ GUI (Update Manager, PackageKit) และแบบ command-line (apt, yum) รวมถึงตัวอย่างการใช้ package manager ของ Python อย่าง pip

---

## Packages and Package Managers

**Package** คือไฟล์ archive ที่บรรจุองค์ประกอบที่จำเป็นสำหรับติดตั้งซอฟต์แวร์ใหม่หรืออัปเดตซอฟต์แวร์ที่มีอยู่แล้ว ทั้ง software update และ software installation file ของ Linux ถูกแจกจ่ายในรูปแบบ package

**Package manager** คือเครื่องมือที่ใช้จัดการการดาวน์โหลดและติดตั้ง package แต่ละ Linux distro มี package manager ของตัวเอง บางตัวเป็นแบบ GUI บางตัวเป็นแบบ command-line

ประโยชน์ของ package manager:

- แก้ปัญหา dependency ระหว่าง package ให้อัตโนมัติ
- แจ้งเตือนเมื่อมี update ใหม่
- (สำหรับ GUI-based) ตรวจสอบ security และ software update ให้อัตโนมัติเป็นประจำ
- ติดตั้ง update ให้อัตโนมัติ หรือให้ผู้ใช้เลือกติดตั้งเฉพาะที่ต้องการ

---

## deb vs RPM Packages

| | `.deb` | `.rpm` |
| --- | --- | --- |
| ชื่อเต็ม | Debian | RPM Package Manager (เดิมคือ Red Hat Package Manager) |
| ใช้กับ distro | Debian, Ubuntu, Mint | CentOS/RHEL, Fedora, openSUSE |

รูปแบบ deb และ RPM เทียบเท่ากันในเชิงเนื้อหา ดังนั้นเนื้อหาข้างในไฟล์สามารถนำไปใช้ข้าม OS ได้ ถ้า package ที่ต้องการมีให้แค่อีกรูปแบบหนึ่ง สามารถแปลงไฟล์ด้วยเครื่องมือ **alien** ได้

```bash
# แปลงไฟล์จาก RPM เป็น deb
alien package_name.rpm

# แปลงไฟล์จาก deb เป็น RPM (ใช้ -r switch)
alien -r package_name.deb
```

---

## GUI-Based Package Managers

**Update Manager** — GUI tool สำหรับอัปเดตระบบที่ใช้ deb-based โดย default จะตรวจสอบ software update ทุกวัน และดาวน์โหลด/ติดตั้ง security update อัตโนมัติทุกวัน ส่วน update ประเภทอื่นจะแสดงผลเป็นรายสัปดาห์ และสามารถตรวจสอบ update ด้วยตัวเองได้ตลอดเวลา

**PackageKit** — GUI tool สำหรับอัปเดตระบบที่ใช้ RPM-based เมื่อมี update จะแสดงไอคอนรูปดาวในพื้นที่ notification ตรวจสอบ update อัตโนมัติตามช่วงเวลาที่ตั้งค่าได้ และสามารถตรวจสอบด้วยตัวเองได้เช่นกัน

ขั้นตอนการติดตั้ง update ผ่านทั้งสองเครื่องมือคล้ายกัน: เลือก update ที่ต้องการ → กด Install Updates → ป้อนรหัสผ่านผู้ใช้ (ถ้าถูกร้องขอ) → กด OK → เครื่องมือจะติดตั้ง update ในพื้นหลังระหว่างที่ยังใช้งานเครื่องต่อได้

---

## Command-Line Package Managers

**apt** — command-line tool สำหรับระบบที่ใช้ deb-based

```bash
# ค้นหา package ที่มีให้อัปเดตสำหรับ distro (แสดงรายการ package, dependency tree, จำนวนที่อัปเกรดได้)
sudo apt update

# อัปเกรด package ที่ติดตั้งอยู่ทั้งหมดในระบบ
sudo apt upgrade

# ติดตั้ง package เฉพาะเจาะจงตามชื่อ
sudo apt install package_name
```

**yum** (Yellowdog Updater, Modified) — command-line tool สำหรับระบบที่ใช้ RPM-based

```bash
# อัปเดต package ทั้งหมดในระบบ
sudo yum update
```

เมื่อรันคำสั่ง `sudo yum update` ระบบจะขอรหัสผ่าน จากนั้น yum จะดึงรายการ update ที่มีทั้งหมด แสดงสรุปและถามยืนยันก่อนดาวน์โหลด เมื่อยืนยันแล้ว yum จะดาวน์โหลดและอัปเดต package ในระบบ และแสดงข้อความ `Complete!` เมื่อเสร็จสิ้น

```bash
# ติดตั้ง software ใหม่บนระบบ deb-based
apt install package_name

# ติดตั้ง software ใหม่บนระบบ RPM-based
yum install package_name
```

---

## Package Managers for Other Ecosystems

นอกจาก package manager ระดับ OS แล้ว หลายแอปพลิเคชันก็มี package manager ของตัวเอง เช่น **pip** และ **conda** สำหรับจัดการ Python environment

```bash
# ติดตั้ง library pandas ผ่าน pip
# pip จะค้นหา package ล่าสุด ดาวน์โหลด ตรวจสอบ/อัปเดต dependency แล้วติดตั้งให้
pip install pandas
```

เมื่อติดตั้งเสร็จ package manager จะแสดงเวอร์ชันของซอฟต์แวร์ที่ติดตั้งใหม่

---

## 📖 Key Terms & Glossary

| Term (ศัพท์) | คำอธิบาย (ภาษาไทย) |
| ------------- | -------------------- |
| Package | ไฟล์ archive ที่บรรจุองค์ประกอบสำหรับติดตั้งซอฟต์แวร์ใหม่หรืออัปเดตซอฟต์แวร์เดิม |
| Package manager | เครื่องมือที่ใช้จัดการการดาวน์โหลดและติดตั้ง package |
| .deb | รูปแบบไฟล์ package ที่ใช้กับ Debian-based distro เช่น Debian, Ubuntu, Mint |
| .rpm | รูปแบบไฟล์ package ที่ใช้กับ Red Hat-based distro เช่น CentOS/RHEL, Fedora, openSUSE |
| alien | เครื่องมือสำหรับแปลง package ระหว่างรูปแบบ deb กับ RPM |
| Dependency | package หรือซอฟต์แวร์อื่นที่ package หนึ่งต้องใช้ร่วมด้วยจึงจะทำงานได้ |
| Update Manager | GUI package manager สำหรับระบบที่ใช้ deb-based |
| PackageKit | GUI package manager สำหรับระบบที่ใช้ RPM-based |
| apt | command-line package manager สำหรับระบบที่ใช้ deb-based |
| yum (Yellowdog Updater, Modified) | command-line package manager สำหรับระบบที่ใช้ RPM-based |
| sudo | คำสั่งที่ใช้รันคำสั่งอื่นด้วยสิทธิ์ผู้ดูแลระบบ (superuser) |
| pip | package manager สำหรับจัดการ library/package ของ Python |
| conda | package manager อีกตัวหนึ่งสำหรับจัดการ Python environment และ package |

---

## ❓ My Questions & Gaps

- [x] ความแตกต่างระหว่าง pip กับ conda ในทางปฏิบัติควรเลือกใช้ตัวไหนเมื่อไหร่
  - **คำตอบ** pip ติดตั้งเฉพาะ Python package จาก PyPI ส่วน conda ติดตั้งได้กว้างกว่านั้น รวมถึงซอฟต์แวร์ที่เขียนด้วยภาษาอื่น เช่น C/C++ library หรือ R package ด้วย pip มักดึง source code มา compile ตอนติดตั้ง ทำให้ช้ากว่าและมีโอกาสพังมากกว่าโดยเฉพาะบน Windows ในขณะที่ conda ติดตั้งจาก binary package ที่ compile ไว้ล่วงหน้า จึงเร็วและเสถียรกว่าโดยเฉพาะ package ที่มี dependency ซับซ้อน นอกจากนี้ conda ยังมีความสามารถสร้าง isolated environment (คนละ Python version และ package กันได้) ในตัวเลย ในขณะที่ pip ต้องพึ่ง tool เสริมอย่าง virtualenv และ dependency resolver ของ conda ก็จัดการ dependency graph ที่ซับซ้อนได้ดีกว่า pip
  - แนวทางเลือกใช้: งาน Python ทั่วไปใช้ pip กับ PyPI ก็เพียงพอและ tooling รอบข้างมักดีกว่า ส่วนงานสาย data science/scientific computing ที่ต้องพึ่ง library ซับซ้อนข้ามภาษา conda (โดยเฉพาะผ่าน conda-forge) มักติดตั้งง่ายกว่า และสามารถใช้ทั้งสองร่วมกันได้ เช่น ใช้ conda จัดการ environment และ system-level library ส่วน pip ติดตั้ง package เฉพาะทาง Python ที่หาไม่ได้ใน conda
- [x] `sudo apt upgrade` กับ `sudo apt full-upgrade`/`dist-upgrade` ต่างกันอย่างไร (ไม่ได้กล่าวถึงในวิดีโอ)
  - **คำตอบ** `apt upgrade` เป็นแนวทางระมัดระวัง จะไม่ติดตั้ง package ใหม่หรือลบ package ที่ติดตั้งอยู่ออกจากระบบ และจะข้าม package ที่ต้องมีการลบ package อื่นเนื่องจากการเปลี่ยนแปลงของ dependency ส่วน `apt full-upgrade` (เทียบเท่ากับ `apt dist-upgrade` ในคำสั่งรุ่นเก่า) มีความสามารถมากกว่า คือติดตั้ง package ใหม่หรือลบ package ที่ขัดแย้งกันได้หากจำเป็นเพื่อให้อัปเกรดสำเร็จ เหมาะกับกรณีที่การอัปเกรด package ต้องพึ่ง dependency ใหม่หรือต้องเอา package ที่ขัดแย้งออก โดยทั่วไป `apt upgrade` เหมาะกับระบบที่เน้นความเสถียรและคาดเดาผลได้ เช่น server สำคัญที่ไม่อยากให้ระบบตัดสินใจลบ package เอง ส่วน `full-upgrade`/`dist-upgrade` เหมาะกับผู้ใช้ desktop ที่ต้องการอัปเดตแบบครอบคลุมกว่า

---

## 🔗 Resources

- [Pip vs Conda — GeeksforGeeks](https://www.geeksforgeeks.org/python/what-is-the-difference-between-pip-and-conda/)
- [Apt Upgrade vs Apt Dist-upgrade — TecAdmin](https://tecadmin.net/difference-between-apt-upgrade-vs-apt-dist-upgrade/)
