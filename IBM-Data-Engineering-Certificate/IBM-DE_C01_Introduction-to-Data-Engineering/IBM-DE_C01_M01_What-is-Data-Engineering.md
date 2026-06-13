# IBM Data Engineering Professional Certificate — C01: Introduction to Data Engineering
## M01: What is Data Engineering
**Lesson:** Modern Data Ecosystem, Roles, and Responsibilities
**Date studied:** 2026-06-13
**File:** IBM-DE_C01_M01_What-is-Data-Engineering.md

---

## 📌 Key Concepts
- A modern data ecosystem is a network of interconnected entities: data sources, tools, stakeholders, and infrastructure.
- The 3 stages of working with data are: acquiring, organizing/preparing, and delivering to end-users.
- Data Engineer's core job: make **analytics-ready data** available — accurate, compliant, and accessible.
- Data roles form a chain: Engineer → Analyst → Scientist → Business/BI Analyst.
- Beyond DE, there are specialized roles: Data Warehouse Engineer, Data Architect, Data Manager, DBA.
- DE scope covers 4 areas: collecting source data, processing, storing, and making data available.
- No single person masters all DE skills — specialization + broad awareness is the goal.
- Key technical skills: OS/infra, databases (SQL + NoSQL), pipelines, ETL tools, Python/R/Java, Big Data tools.
- Soft skills matter: communication, collaboration, translating business needs into technical specs.

---

## Modern Data Ecosystem

A data ecosystem includes:
- Data from disparate sources (text, IoT, social media, legacy DBs, real-time streams)
- Tools and infrastructure to store, process, and disseminate data
- Active stakeholders who act on insights

**3 Stages:**
1. **Acquiring** — pull data from sources; challenge: reliability, security, integrity
2. **Organizing & Preparing** — clean, conform, comply; challenge: data management and repository governance
3. **Delivering** — APIs, dashboards, raw data for analysts; challenge: right interface for the right user

**Emerging forces shaping the ecosystem:** Cloud computing, Machine Learning, Big Data

---

## Key Roles in the Data Ecosystem

| Role | Core Function |
|------|---------------|
| Data Engineer | Converts raw data into usable data (pipelines, repositories) |
| Data Analyst | Uses data to generate insights (correlations, patterns, visualizations) |
| Data Scientist | Uses past data to predict the future (ML/DL models) |
| Business Analyst | Translates insights into business recommendations |
| BI Analyst | Focuses on market forces; builds BI solutions and dashboards |

> Roles are not siloed — professionals often transition between them over their career.

---

## Specializations in Data Engineering

| Role | Focus |
|------|-------|
| Data Warehouse Engineer | ETL pipelines, data warehouses, data lakes for BI |
| Data Architect | Overall data architecture, integration strategy, governance |
| Data Manager | Data governance, compliance, access policies, data literacy |
| Database Administrator (DBA) | DB operations, backups, performance, security |

---

## Scope of Data Engineering

1. **Collecting Source Data** — tools and workflows to acquire from multiple sources; design scalable storage
2. **Processing Data** — ETL pipelines, distributed systems, data quality, validation, compliance
3. **Storing Data** — scalable architecture; privacy, security, backup, and recovery
4. **Making Data Available** — APIs, dashboards, access controls for end-users

---

## Responsibilities and Skillsets

**Core responsibility:** Provide analytics-ready data — accurate, compliant, accessible.

**Technical Skills:**
- OS: UNIX, Linux, Windows, cloud services (AWS, GCP, IBM, Azure)
- RDBMS: IBM DB2, MySQL, Oracle, PostgreSQL
- NoSQL: Redis, MongoDB, Cassandra, Neo4J
- Data Warehouses: Amazon RedShift, IBM Db2 Warehouse, Netezza
- Pipelines: Apache Beam, Airflow, DataFlow
- ETL: IBM InfoSphere, AWS Glue, Improvado
- Languages: SQL, Python, R, Java, Shell, PowerShell
- Big Data: Hadoop, Hive, Spark

**Functional Skills:** SDLC, converting business requirements to tech specs, understanding data risk.

**Soft Skills:** Communication, interpersonal, teamwork across specializations.

---

## Real-World Example: Social Media Sentiment Analysis

| Step | What the DE did |
|------|-----------------|
| Collect | Pulled tweets via APIs and scraped eCommerce reviews |
| Process | Built a Python program to clean and transform data into DB format |
| Pipeline | Automated the ETL process so the dashboard updates in real-time |

---

## 📖 Key Terms & Glossary
| Term | Definition |
|------|------------|
| Data Ecosystem | The full network of data sources, tools, stakeholders, and infrastructure |
| Analytics-Ready Data | Data that is accurate, compliant, and accessible for consumers |
| ETL | Extract, Transform, Load — the standard process for moving and preparing data |
| Data Pipeline | End-to-end flow of data from source to destination systems |
| OLTP | Online Transaction Processing — systems optimized for high-speed daily operations |
| OLAP | Online Analytical Processing — systems optimized for complex analytical queries |
| Data Architect | Designs the overall data management architecture |
| DBA | Database Administrator — manages DB operations, performance, and security |

---

## ❓ My Questions & Gaps
- [ ] What is the exact boundary between a Data Engineer and a Data Architect in practice?
- [ ] When do organizations choose to hire a DBA vs. rely on the DE for database work?
- [ ] How does Airflow differ from Apache Beam at a conceptual level?

---

## 🔗 Resources
- [IBM Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-engineer)
- [Apache Airflow Docs](https://airflow.apache.org/docs/)
- [Dice Tech Job Report 2020](https://techhub.dice.com/Dice-2020-Tech-Job-Report.html)
