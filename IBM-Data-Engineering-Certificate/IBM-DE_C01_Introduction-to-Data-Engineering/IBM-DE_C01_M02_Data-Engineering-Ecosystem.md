# IBM Data Engineering Professional Certificate — C01: Introduction to Data Engineering
## M02: The Data Engineering Ecosystem
**Lesson:** Data Types, File Formats, Sources, Repositories, Languages, Metadata, and Big Data
**Date studied:** 2026-06-13
**File:** IBM-DE_C01_M02_Data-Engineering-Ecosystem.md

---

## 📌 Key Concepts
- Data is categorized into 3 types: structured, semi-structured, and unstructured.
- Common file formats: CSV, TSV, XLSX, XML, PDF, JSON — each suited to different use cases.
- Data sources include: relational DBs, flat files, APIs, web scraping, data streams, RSS feeds.
- Repositories split into OLTP (transactional) and OLAP (analytical) systems.
- RDBMS excels at structured data with ACID compliance; NoSQL handles flexible, schema-less data.
- Data Warehouse = single source of truth for analysis; Data Lake = raw dump for future use; Lakehouse = both.
- ETL: transform before loading; ELT: load first, transform in the target using its compute power.
- Big Data is defined by 5 V's: Velocity, Volume, Variety, Veracity, Value.
- Hadoop (distributed storage), Hive (SQL on Hadoop), and Spark (fast in-memory processing) are the Big Data trio.
- Metadata has 3 types: Technical, Process, Business — all important for governance and data lineage.

---

## Types of Data

| Type | Description | Storage |
|------|-------------|---------|
| Structured | Fixed schema, rows & columns | RDBMS, SQL databases |
| Semi-structured | Some structure, no rigid schema | XML, JSON, NoSQL |
| Unstructured | No predefined format | Files, NoSQL, Data Lakes |

---

## File Formats

| Format | Best For |
|--------|----------|
| CSV / TSV | Simple tabular data; CSV for general use, TSV when values contain commas |
| XLSX | Excel workbooks with multiple sheets and formulas |
| XML | Hierarchical, platform-independent data sharing |
| JSON | Web APIs and data transmission; supports any data size and type |
| PDF | Documents needing consistent presentation across systems |

---

## Sources of Data

- **Relational Databases** — internal systems (SQL Server, Oracle, MySQL, DB2)
- **Flat Files / XML** — external releases from governments and data vendors
- **APIs & Web Services** — Twitter, stock market, data validation services
- **Web Scraping** — price comparison, lead generation, ML training data; tools: BeautifulSoup, Scrapy, Selenium
- **Data Streams** — IoT, GPS, real-time events; tools: Apache Kafka, Spark Streaming, Storm
- **RSS Feeds** — updated content from news and forums

---

## Data Repositories

### RDBMS
- Organizes data into tables with rows and columns; tables linked by common keys
- Supports ACID transactions: **A**tomicity, **C**onsistency, **I**solation, **D**urability
- Best for: OLTP, data warehousing, IoT solutions
- Limitations: poor with unstructured data; strict field length limits; difficult cross-RDBMS migration
- Popular: IBM DB2, SQL Server, MySQL, Oracle, PostgreSQL; Cloud: Amazon RDS, Google Cloud SQL, SQL Azure

### NoSQL

| Type | Description | Best For | Examples |
|------|-------------|----------|---------|
| Key-value | Unique key maps to a value | Session data, caching, recommendations | Redis, DynamoDB |
| Document | Full record stored in one document | eCommerce, CRM, analytics | MongoDB, CouchDB |
| Column | Data grouped by column families | Time-series, IoT, heavy writes | Cassandra, HBase |
| Graph | Nodes + relationships | Social networks, fraud detection | Neo4J, CosmosDB |

**NoSQL advantages:** handles large volumes of all data types; scales horizontally on commodity hardware; flexible schema.

**RDBMS vs NoSQL:**
- RDBMS: rigid schema, ACID compliant, mature, expensive at scale
- NoSQL: schema-agnostic, not always ACID, lower cost, better for big data

### Data Warehouses, Marts, and Lakes

| Repository | Description |
|------------|-------------|
| Data Warehouse | Central, analysis-ready, single source of truth; 3-tier: DB layer → OLAP → client |
| Data Mart | Subset of DW for a specific business unit (sales, finance) |
| Data Lake | Raw data in native format; schema-on-read; risk of becoming a Data Swamp |
| Data Lakehouse | Combines DL flexibility + DW performance and governance |

---

## ETL vs ELT

| Aspect | ETL | ELT |
|--------|-----|-----|
| Transform step | Before loading (in staging) | After loading (in target) |
| Best for | Structured targets, legacy systems | Data lakes, cloud-native DW |
| Flexibility | Less flexible — schema required upfront | More flexible — raw data preserved |
| Tools (ETL) | IBM InfoSphere, AWS Glue, Informatica | — |

**ETL Transform steps:** standardization, deduplication, filtering, data enrichment, relationship mapping, business rules.

**ELT advantages:** handles big/unstructured data; shorter delivery cycles; multi-use downstream transformations.

**Data Pipelines** are broader than ETL/ELT — they cover the full journey from source to destination and can be batch, streaming, or hybrid.

Pipeline tools: Apache Beam, Apache Airflow, Google Cloud Dataflow

---

## Languages for Data Professionals

| Category | Language | Key Use |
|----------|----------|---------|
| Query | SQL | Standard for relational DBs |
| Programming | Python | Data cleaning, ML, scripting; libraries: Pandas, NumPy, Matplotlib, BeautifulSoup |
| Programming | R | Statistical analysis, visualization; libraries: ggplot2, dplyr |
| Programming | Java | Big data frameworks (Hadoop, Spark written in Java); speed-critical tasks |
| Scripting | Unix/Linux Shell | File ops, batch jobs, system admin |
| Scripting | PowerShell | Structured data (JSON, CSV, XML), automation, cloud admin |

---

## Metadata and Metadata Management

| Type | What It Tracks |
|------|---------------|
| Technical | Structure of data (table names, column counts, data types) — stored in System Catalog |
| Process | Pipeline activity (start/end times, disk usage, data movement) — for troubleshooting |
| Business | What data means to business users, how it's acquired, connections between datasets |

**Why it matters:** enables data discovery, data lineage (trace origin and transformations), governance, and compliance.

Popular tools: IBM Watson Knowledge Catalog, Alation, Informatica Enterprise Data Catalog, Microsoft Azure Data Catalog

---

## Big Data: The 5 V's

| V | Definition |
|---|------------|
| Velocity | Speed of data generation (e.g., YouTube uploads every 60 seconds) |
| Volume | Scale — ~2.5 quintillion bytes generated daily |
| Variety | Diversity of types and sources (structured, social media, IoT, video) |
| Veracity | Quality and accuracy; 80% of data is unstructured and needs validation |
| Value | Turning data into meaningful outcomes (business, medical, social) |

---

## Big Data Tools

| Tool | Type | Best For |
|------|------|----------|
| Apache Hadoop | Distributed storage + processing | Storing and processing massive datasets across clusters |
| HDFS | Hadoop's file system | Fault-tolerant storage via file splitting and replication |
| Apache Hive | SQL on Hadoop (OLAP) | ETL and data warehouse analytics; high latency, not for real-time |
| Apache Spark | In-memory processing engine | Real-time analytics, ML, streaming; much faster than Hadoop |

---

## 📖 Key Terms & Glossary
| Term | Definition |
|------|------------|
| Structured Data | Data in a fixed schema — rows and columns in a relational DB |
| Semi-structured | Data with partial organization (XML, JSON) but no fixed schema |
| Unstructured | Data with no predefined format (images, videos, social media posts) |
| ACID | Atomicity, Consistency, Isolation, Durability — guarantees for DB transactions |
| OLTP | Optimized for high-speed transactional read/write operations |
| OLAP | Optimized for complex analytical queries on large historical data |
| Data Swamp | A data lake that becomes unusable due to lack of governance |
| Data Lakehouse | Architecture combining data lake flexibility with DW structure and governance |
| ETL | Extract, Transform, Load — transforms data before loading into target |
| ELT | Extract, Load, Transform — loads raw data first, transforms in the target system |
| HDFS | Hadoop Distributed File System — splits and replicates files across a cluster |
| Data Lineage | Ability to trace data from its origin through all transformations |
| Metadata | Data about data — describes structure, processes, or business meaning |

---

## ❓ My Questions & Gaps
- [ ] When should you choose ELT over ETL in a real project — what's the tipping point?
- [ ] How does a Data Lakehouse (e.g., Databricks Delta Lake) enforce ACID compliance on a data lake?
- [ ] What makes Spark faster than Hadoop MapReduce exactly — is it purely in-memory?
- [ ] How does HDFS replication work if a node fails mid-write?

---

## 🔗 Resources
- [Apache Hadoop Docs](https://hadoop.apache.org/docs/)
- [Apache Spark Docs](https://spark.apache.org/docs/latest/)
- [Apache Kafka Docs](https://kafka.apache.org/documentation/)
- [MongoDB University](https://university.mongodb.com/)
