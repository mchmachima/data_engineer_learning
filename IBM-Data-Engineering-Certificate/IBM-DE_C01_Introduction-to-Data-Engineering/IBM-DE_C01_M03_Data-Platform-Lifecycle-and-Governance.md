# IBM Data Engineering Professional Certificate — C01: Introduction to Data Engineering
## M03: Data Platform, Lifecycle, and Governance
**Lesson:** Data Platform Architecture, Data Wrangling, Querying, Performance Tuning, Security, and Governance
**Date studied:** 2026-06-13
**File:** IBM-DE_C01_M03_Data-Platform-Lifecycle-and-Governance.md

---

## 📌 Key Concepts
- A data platform has 5 layers: Ingestion → Storage & Integration → Processing → Analysis/UI → Pipeline (overlays all).
- Data store design is driven by: data type, volume, intended use (OLTP vs OLAP), and security requirements.
- Data wrangling = iterative process of exploring, transforming, cleaning, and validating data to make it analytics-ready.
- Key wrangling operations: structuring (joins/unions), normalization, denormalization, and data cleaning.
- SQL aggregation functions (COUNT, SUM, AVG, MAX, MIN) plus GROUP BY and LIKE are core querying tools.
- Performance tuning focuses on: indexing, partitioning, normalization, capacity planning, and monitoring.
- Security is structured around the CIA Triad: Confidentiality, Integrity, Availability.
- Governance ensures data lifecycle compliance under regulations: GDPR, CCPA, HIPAA, PCI DSS, SOX.
- Compliance tools: authentication/access control, encryption, anonymization, pseudonymization, monitoring, data erasure.

---

## Data Platform Architecture

A data platform is a set of layered components:

| Layer | Responsibility | Example Tools |
|-------|---------------|---------------|
| 1. Data Ingestion | Connect to sources; transfer in batch or stream; track metadata | Kafka, AWS Kinesis, IBM Streams, Google DataFlow |
| 2. Storage & Integration | Store data; merge from disparate sources; serve batch + stream | IBM DB2, MySQL, MongoDB, Cassandra, Talend, Dell Boomi |
| 3. Data Processing | Validate, transform, clean, prepare for analysis | Python, R, OpenRefine, Watson Studio Refinery, Trifacta |
| 4. Analysis & UI | Deliver to BI analysts, data scientists, applications | Tableau, Power BI, Jupyter, IBM Cognos, APIs |
| 5. Data Pipeline | Overlay that keeps data flowing across all layers continuously | Apache Airflow, Google DataFlow |

> In relational DBs, storage and processing can share a layer. In big data systems, data is stored in HDFS first, processed later in Spark.

---

## Factors for Selecting a Data Store

| Factor | Considerations |
|--------|---------------|
| **Type of data** | Structured → RDBMS; semi/unstructured → NoSQL |
| **Volume** | High volume raw data → Data Lake; distributed processing → Big Data repository |
| **Intended use** | OLTP (fast read/write/update) vs OLAP (complex historical queries) |
| **Performance** | Throughput (read/write rate), latency (access time) |
| **Availability** | Zero downtime requirements |
| **Integrity** | Safe from corruption, loss, unauthorized access |
| **Recoverability** | Ability to recover from failures |
| **Privacy & Compliance** | GDPR, CCPA, HIPAA — must be built in from the start, not retrofitted |

---

## Data Collection Methods

| Method | Description |
|--------|-------------|
| SQL / Query Languages | Extract from relational DBs; NoSQL equivalents: CQL (Cassandra), GraphQL (Neo4J) |
| APIs | Access endpoints for data from databases, web services, and marketplaces |
| Web Scraping | Download specific data from web pages by defined parameters |
| RSS Feeds | Capture ongoing updates from news sites and forums |
| Data Streams | Aggregate real-time data from IoT, GPS, social media |
| Data Exchange Platforms | Governed exchange of data between providers and consumers (AWS Data Exchange, Snowflake) |

---

## Data Wrangling

Data wrangling = data munging. An iterative loop of: explore → transform → validate → prepare.

### Transformation Tasks

**Structuring:**
- **Joins** — combine *columns* from two tables into one row
- **Unions** — combine *rows* from two tables into one table

**Normalization** — removes redundancy; ideal for OLTP systems.

**Denormalization** — combines tables for faster queries; used before running analytical reports.

### Data Cleaning

**Step 1 — Detect Issues:**
- Data profiling (inspect structure, content, anomalies)
- Data visualization (spot outliers via statistical plots)

**Step 2 — Fix Issues:**

| Issue | Fix |
|-------|-----|
| Missing values | Filter out, source externally, or impute (calculate from statistics) |
| Duplicates | Remove duplicate records |
| Irrelevant data | Filter out fields that don't apply to the use case |
| Data type errors | Convert to correct type (numbers, dates) |
| Inconsistent formats | Standardize case, dates, units of measurement |
| Syntax errors | Fix extra spaces, typos, abbreviations |
| Outliers | Investigate — may be error or legitimate extreme value |

### Wrangling Tools

| Tool | Key Strength |
|------|-------------|
| Excel / Google Sheets | Quick formulae; Power Query for import and transform |
| OpenRefine | Open-source, menu-based, no coding required |
| Google DataPrep | Auto-detects schema and anomalies, fully managed |
| Watson Studio Refinery | IBM tool, auto-detects types, enforces governance |
| Python (Pandas, NumPy) | Flexible, programmatic transformations at scale |
| R (dplyr, data.table) | Statistical wrangling, large dataset aggregation |

---

## Querying Data

```sql
-- Count records
SELECT COUNT(*) FROM orders;
SELECT COUNT(DISTINCT customer_id) FROM orders;

-- Aggregations
SELECT SUM(amount), AVG(amount), STDDEV(amount) FROM orders;

-- Extreme values
SELECT MAX(amount), MIN(amount) FROM orders;

-- Sort results
SELECT * FROM orders ORDER BY amount DESC;

-- Filter by pattern (partial match)
SELECT * FROM customers WHERE postcode LIKE '100%';

-- Group and aggregate
SELECT region, SUM(amount) FROM orders GROUP BY region;
```

---

## Performance Tuning and Troubleshooting

### Pipeline Performance Metrics to Monitor

| Metric | What it measures |
|--------|-----------------|
| Latency | Time for a service to fulfill a request |
| Failure rate | Rate at which a service fails |
| Resource utilization | CPU, memory, disk usage |
| Traffic | Number of requests per time period |

### Troubleshooting Steps
1. Collect information about the incident
2. Verify software versions and source code
3. Review recent deployments
4. Check logs and metrics (errors, CPU/memory at time of failure)
5. Reproduce in a test environment
6. Validate root cause hypothesis
7. Deploy fix per team process

### Database Optimization Techniques

| Technique | Purpose |
|-----------|---------|
| Indexing | Quickly locate data without full table scan |
| Partitioning | Divide large tables into smaller ones for faster queries |
| Normalization | Reduce redundancy and update anomalies |
| Capacity planning | Right-size hardware and software for current and future load |

---

## Security: The CIA Triad

| Letter | Principle | Meaning |
|--------|-----------|---------|
| C | Confidentiality | Prevent unauthorized access |
| I | Integrity | Ensure data is trustworthy and untampered |
| A | Availability | Authorized users can always access resources |

### 4 Layers of Security

1. **Physical** — facility access, surveillance, power backup, temperature control
2. **Network** — firewalls, network access control, VLANs, IDS/IPS, encryption in transit
3. **Application** — threat modeling, secure design, secure coding, security testing
4. **Data** — authentication + authorization; encryption at rest (databases, backups) and in transit (HTTPS, SSL, TLS)

---

## Governance and Compliance

**Data Governance** = principles, practices, and processes to maintain security, privacy, and integrity across the data lifecycle.

### Key Regulations

| Regulation | Scope | Focus |
|------------|-------|-------|
| GDPR | EU | Personal data and privacy for EU citizens |
| CCPA | California, USA | Customer data for California residents |
| HIPAA | Healthcare, USA | Protected health information |
| PCI DSS | Retail | Credit card data standards |
| SOX | Finance, USA | Financial information handling and reporting |

### Data Lifecycle Governance Areas

```
Acquisition → Processing → Storage → Sharing → Retention & Disposal
    ↓               ↓           ↓         ↓              ↓
Legal basis,   How PII is   Where &    3rd-party     Retention
consent,       processed,   how data   access &      policies,
intended use   legal basis  is stored  accountability  deletion
```
*An auditable trail is required at every stage.*

### Compliance Tools

| Tool | Purpose |
|------|---------|
| Authentication + Access Control | Passwords, tokens, biometrics; role-based privileges |
| Encryption | Encodes data at rest and in transit; decryptable only via secure key |
| Anonymization | Masks data presentation layer without changing underlying data |
| Pseudonymization | Replaces PII with artificial identifiers |
| Monitoring & Alerting | Audit trails, real-time alerts on security violations |
| Data Erasure | Permanently overwrites data (vs. simple deletion which leaves data recoverable) |

---

## 📖 Key Terms & Glossary
| Term | Definition |
|------|------------|
| Data Wrangling | Iterative process of transforming and cleaning raw data into analytics-ready form |
| Data Profiling | Inspecting source data to understand structure, content, and anomalies |
| Normalization | Organizing data to reduce redundancy — optimal for OLTP |
| Denormalization | Combining tables for query speed — optimal for OLAP and reporting |
| Imputation | Filling in missing values using statistical methods |
| CIA Triad | Confidentiality, Integrity, Availability — the three pillars of data security |
| GDPR | EU regulation governing personal data privacy and protection |
| HIPAA | US regulation governing protected health information |
| Pseudonymization | Replacing PII with artificial identifiers so data can't be traced back to a person |
| Data Erasure | Software-based permanent overwriting of data (stronger than deletion) |
| IDS/IPS | Intrusion Detection/Prevention Systems — inspect and block malicious network traffic |
| Data Governance | Policies and processes to maintain security, privacy, and integrity of data |

---

## ❓ My Questions & Gaps
- [ ] What is the difference between anonymization and pseudonymization in a GDPR context — when is each required?
- [ ] How does partitioning interact with indexing in practice — do you always need both?
- [ ] In a streaming pipeline, how do you monitor latency in real-time (what tools are used)?
- [ ] What does "data lineage" look like in a real tool like IBM Watson Knowledge Catalog?

---

## 🔗 Resources
- [GDPR Official Text](https://gdpr.eu/)
- [Apache Airflow Docs](https://airflow.apache.org/docs/)
- [OpenRefine](https://openrefine.org/)
- [IBM Watson Knowledge Catalog](https://www.ibm.com/products/watson-knowledge-catalog)
