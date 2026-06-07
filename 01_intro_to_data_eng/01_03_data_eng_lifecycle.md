# **Data Platforms, Data Stores, and Security**

## Architecting the Data Platform

A data platform is organized into distinct **layers**, each performing a specific set of tasks. These layers work together to move data from its raw sources to the hands of decision-makers.

### Layer 1: Data Ingestion / Collection

The Data Collection Layer connects to source systems and brings data into the data platform. Key tasks include:

- Connecting to data sources
- Transferring data in **streaming**, **batch**, or both modes
- Maintaining metadata about ingested data (volume, source, timestamps, etc.)

**Tools:** Google Cloud DataFlow, IBM Streams, IBM Streaming Analytics on Cloud, Amazon Kinesis, Apache Kafka

### Layer 2: Data Storage and Integration

Once ingested, data needs to be stored and integrated. This layer must:

- Store data for processing and long-term use
- Transform and merge extracted data (logically or physically)
- Make data available for both streaming and batch processing

The storage layer must be **reliable, scalable, high-performing, and cost-efficient**.

**Relational databases:** IBM DB2, Microsoft SQL Server, MySQL, Oracle Database, PostgreSQL

**Cloud-based (Database-as-a-Service):** IBM DB2 on Cloud, Amazon RDS, Google Cloud SQL, SQL Azure

**NoSQL (cloud):** IBM Cloudant, Redis, MongoDB, Cassandra, Neo4J

**Integration tools:** IBM Cloud Pak for Data, Talend Data Fabric, Dell Boomi, SnapLogic

**iPaaS (Integration Platform as a Service):** Adeptia Integration Suite, Google Cloud Cooperation 534, IBM Application Integration Suite, Informatica Integration Cloud

### Layer 3: Data Processing

Raw, integrated data must be validated, transformed, and prepared for use. This layer must:

- Read data in batch or streaming modes and apply transformations
- Support popular querying tools and programming languages
- Scale to meet growing dataset demands
- Provide an environment for analysts and data scientists to work with data

**Key transformation tasks:**

| Task                | Description                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| **Structuring**     | Changes the form and schema of data (e.g., changing field order, combining fields with joins/unions) |
| **Normalization**   | Cleans unused data and reduces redundancy and inconsistency                                          |
| **Denormalization** | Combines multiple tables into one for faster reporting and analysis queries                          |
| **Data Cleaning**   | Fixes irregularities to produce credible data for downstream use                                     |

**Tools:** Spreadsheets, OpenRefine, Google DataPrep, Watson Studio Refinery, Trifacta Wrangler, Python, R

> Note: Storage and processing do not always occur in separate layers. In relational databases they may share the same layer, while in big data systems data is often stored in HDFS first and processed later in Spark.

### Layer 4: Analysis and User Interface

This layer delivers processed data to data consumers, including:

- BI Analysts and business stakeholders — via dashboards and reports
- Data Scientists and Data Analysts — for further processing and specific use cases
- Other applications and services — via APIs

**Supported tools and interfaces:**

- SQL and SQL-like query languages (e.g., CQL for Cassandra)
- Programming languages: Python, R, Java
- APIs for both online and offline reporting
- Dashboarding and BI applications: IBM Cognos Analytics, Tableau, Jupyter Notebooks, Microsoft Power BI
-

### The Data Pipeline Layer

Overlaying the ingestion, storage, and processing layers is the **Data Pipeline** — responsible for implementing and maintaining a continuously flowing data flow using ETL (Extract, Transform, Load) tools.

**Popular solutions:** Apache Airflow, Google DataFlow

---

## Factors for Selecting and Designing Data Stores

A **data store** (or data repository) is a general term for data that has been collected, organized, and isolated for business operations or analysis. It can be a database, data warehouse, data mart, big data store, or data lake.

### Type of Data

- **Relational databases (RDBMS)** — best for structured data with a well-defined schema (tabular format)
- **Non-relational databases (NoSQL)** — best for semi-structured and unstructured, schema-less data; available in four types:
  - Key-value
  - Document
  - Column
  - Graph-based

> Choose carefully: document-based databases are not ideal for complex search and multi-operation transactions; graph-based databases are not optimized for high-volume analytics queries.

### Volume of Data

- **Data Lake** — ideal when storing large volumes of raw data in its native format; supports both relational and non-relational data without defining structure or schema upfront
- **Big Data Repository** — suited for high-volume, high-velocity, diverse data requiring distributed processing and fast analytics; splits large files across multiple computers for parallel access

### Intended Use

| Use Case                         | Design Focus                                                                 |
| -------------------------------- | ---------------------------------------------------------------------------- |
| **Transactional systems (OLTP)** | High-speed read, write, and update operations                                |
| **Analytical systems (OLAP)**    | Complex queries on large historical data; faster response to complex queries |

Schema design, indexing, and partitioning strategies all play a major role in performance based on how data is used.

**Scalability** — the data store's capability to handle growth in data volume, workloads, and users — is also driven by intended use.

**Normalization** is important for transactional systems but can lead to performance issues in analytical systems.

### Storage Considerations

| Property           | Description                                                           |
| ------------------ | --------------------------------------------------------------------- |
| **Performance**    | Throughput (read/write rate) and latency (access time)                |
| **Availability**   | Data must be accessible at all times with no downtime                 |
| **Integrity**      | Data must be safe from corruption, loss, and outside attack           |
| **Recoverability** | The system must enable recovery in the event of failures or disasters |

### Privacy, Security, and Governance

A secure data strategy is a **layered approach** involving:

- Access control
- Multizone encryption
- Data management
- Monitoring systems

Relevant regulations include **GDPR**, **CCPA**, and **HIPAA**, which restrict ownership, use, and management of personal and sensitive data.

> Security and compliance strategies must be built into data store design from the start — retrofitting them later results in patchwork solutions.

---

## Security

Enterprise-level data platforms must tackle security at multiple levels. The overarching framework is the **CIA Triad**:

| Letter | Principle       | Meaning                                                  |
| ------ | --------------- | -------------------------------------------------------- |
| **C**  | Confidentiality | Control unauthorized access                              |
| **I**  | Integrity       | Validate that resources are trustworthy and untampered   |
| **A**  | Availability    | Ensure authorized users can access resources when needed |

The CIA Triad applies across all facets of security: infrastructure, network, application, and data.

### 1. Physical Infrastructure Security

The physical security of facilities housing IT systems is foundational — and extends to cloud service providers' infrastructure. Measures include:

- Perimeter access based on authentication with round-the-clock surveillance
- Multiple independent power feeds with dedicated generators and UPS battery backup
- Temperature and humidity management systems
- Facilities located away from flood plains; earthquake-resistant structures where necessary
- Multi-level lightning protection and earthing systems

### 2. Network Security

Network security keeps interconnected systems and data safe. Solutions include:

- **Firewalls** — prevent unauthorized access to private networks connected to the internet
- **Network Access Control** — ensures only authorized devices connect to the network (e.g., devices with outdated service packs may be blocked)
- **Network Segmentation** — creates virtual local area networks (VLANs) to segregate assets based on required security levels
- **Security Protocols** — prevent attackers from intercepting data in transit
- **Intrusion Detection and Prevention Systems (IDS/IPS)** — inspect incoming traffic for intrusion attempts and vulnerabilities

### 3. Application Security

Application security protects customer data and ensures applications remain fast and reliable. Security must be built into the foundation of an application through:

- **Threat modeling** — identifies weaknesses and attack patterns
- **Secure design** — mitigates risks at the architectural level
- **Secure coding guides and practices** — prevents vulnerabilities in implementation
- **Security testing** — validates that the application is free from known issues before and after deployment

### 4. Data Security

Data exists in two states — **at rest** and **in transit** — and must be protected in both.

**Access control** is the primary mechanism:

- **Authentication** — verifies user identity via passwords, tokens, biometrics, or a combination
- **Authorization** — ensures users access data based on their roles and assigned privileges

**Data at rest** (databases, data warehouses, tapes, backups, mobile devices):

- Protected using **encryption** — even if data is lost or intercepted, it cannot be disclosed

**Data in transit** (moving over networks or the internet):

- Protected using encryption methods such as **HTTPS**, **SSL**, and **TLS**

---

## Security Monitoring

It is vital to proactively monitor, track, and react to security violations in time. This requires:

- End-to-end visibility and integration of security processes and tools across the enterprise
- **Security monitoring and intelligence systems** that create complete audit histories for triage and compliance
- Reports and alerts that enable rapid response to security violations

> Every enterprise needs a corporate-level security policy that ensures business, IT, and all stakeholders contribute to achieving security goals through people, policy, processes, systems, and tools.

---

## Summary and Highlights

In this lesson, you have learned:

The architecture of a data platform can be seen as a set of layers, or functional components, each one performing a set of specific tasks. These layers include:

- Data Ingestion or Data Collection Layer, responsible for bringing data from source systems into the data platform.
- Data Storage and Integration Layer, responsible for storing and merging extracted data.
- Data Processing Layer, responsible for validating, transforming, and applying business rules to data.
- Analysis and User Interface Layer, responsible for delivering processed data to data consumers.
- Data Pipeline Layer, responsible for implementing and maintaining a continuously flowing data pipeline.

A well-designed data repository is essential for building a system that is scalable and capable of performing during high workloads. The choice or design of a data store is influenced by the type and volume of data that needs to be stored, the intended use of data, and storage considerations. The privacy, security, and governance needs of your organization also influence this choice. The CIA, or Confidentiality, Integrity, and Availability triad are three key components of an effective strategy for information security. The CIA triad is applicable to all facets of security, be it infrastructure, network, application, or data security.

---

# **Data Collection and Data Wrangling**

## How to Gather and Import Data

Data can be gathered from a wide variety of sources using the following methods:

**SQL / Query Languages** — SQL extracts information from relational databases using commands to retrieve, filter, group, sort, and limit results. Non-relational databases use SQL-like tools such as CQL for Cassandra and GraphQL for Neo4J.

**APIs (Application Programming Interfaces)** — Invoked from applications to access endpoints containing data, including databases, web services, and data marketplaces. Also used for data validation (e.g., validating postal addresses).

**Web Scraping** — Also known as screen scraping or web harvesting. Downloads specific data from web pages based on defined parameters — text, contact information, images, videos, podcasts, and product items.

**RSS Feeds** — Capture updated data from online forums and news sites where content is refreshed on an ongoing basis.

**Data Streams** — Aggregate constant streams of data from instruments, IoT devices, applications, GPS systems, social media, and interactive platforms.

**Data Exchange Platforms** — Facilitate the exchange of data between providers and consumers using well-defined standards, protocols, and formats. They also ensure security, governance, data licensing workflows, de-identification of personal information, and legal frameworks. Examples: AWS Data Exchange, Crunchbase, Lotame, Snowflake.

**Research and Advisory Firms** — For specific needs such as marketing trends, ad spending, user behavior, or demographic studies. Trusted sources include Forrester, Business Insider, and Gartner.

### Importing Data into Repositories

Once gathered, data is loaded into a data repository before wrangling and analysis. The right repository depends on data type and volume:

```
+---------------------+       +------------------------+       +---------------------------+
|   Data Sources      |       |   Import Process       |       |   Data Repository         |
|---------------------|       |------------------------|       |---------------------------|
| - Relational DBs    |       | - Combine disparate    |       | - Relational DB           |
| - APIs / Web Svcs   | ----> |   sources into unified | ----> |   (structured data)       |
| - Web Scraping      |       |   view                 |       | - NoSQL Clusters          |
| - Data Streams      |       | - ETL tools: Talend,   |       |   (semi-structured)       |
| - RSS / Exchanges   |       |   Informatica          |       | - NoSQL DB / Data Lake    |
|                     |       | - Languages: Python, R |       |   (unstructured data)     |
+---------------------+       +------------------------+       +---------------------------+
```

| Data Type           | Storage Options             |
| ------------------- | --------------------------- |
| **Structured**      | Relational databases, NoSQL |
| **Semi-structured** | NoSQL clusters, XML, JSON   |
| **Unstructured**    | NoSQL databases, Data Lakes |

---

## Data Wrangling

Data wrangling (also called data munging) is an iterative process that includes data exploration, transformation, validation, and preparation to make data analytics-ready.

### Transformation Tasks

**Structuring** — Changes the form and schema of data. Incoming data may come from different sources (e.g., relational databases and web APIs) and must be merged into a consistent format.

- **Joins** — Combine _columns_ from two tables into a single row; each row in the result contains columns from both source tables
- **Unions** — Combine _rows_ from two tables into a single table; each row in the result comes from one source table or the other

**Normalization** — Cleans unused data and reduces redundancy and inconsistency. Transactional systems are typically highly normalized due to frequent insert, update, and delete operations.

**Denormalization** — Combines data from multiple tables into a single table for faster querying. Normalized transactional data is typically denormalized before running reports and analysis queries.

### Data Cleaning

Cleaning fixes irregularities to produce credible and accurate data for analysis.

**Step 1 — Detect Issues** using:

- Scripts and tools that validate data against defined rules and constraints
- **Data profiling** — inspects source data to understand structure, content, and interrelationships; uncovers anomalies such as null values, duplicates, or out-of-range values
- **Data visualization** — statistical methods to spot outliers (e.g., plotting average income to identify anomalous values)

**Step 2 — Fix Issues:**

| Issue                | Description                                        | Fix                                                                                        |
| -------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Missing values**   | Blank or null fields that can cause biased results | Filter out records, source missing data, or use imputation (calculate based on statistics) |
| **Duplicate data**   | Repeated data points in the dataset                | Remove duplicates                                                                          |
| **Irrelevant data**  | Data that doesn't fit the use case                 | Filter out (e.g., contact numbers in a health study)                                       |
| **Data type errors** | Values stored in the wrong type                    | Convert to correct data type (numbers, dates, etc.)                                        |
| **Standardization**  | Inconsistent formats across records                | Standardize case, date formats, units of measurement                                       |
| **Syntax errors**    | Extra spaces, typos, or format inconsistencies     | Correct whitespace, fix abbreviations vs. full forms                                       |
| **Outliers**         | Values vastly different from the rest              | Investigate — may be incorrect (age = 5 in voter data) or valid but extreme (income = $1M) |

### Tools for Data Wrangling

| Tool                       | Key Features                                                                                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Excel / Google Sheets**  | Built-in formulae for cleaning and transformation; Power Query (Excel) and Query function (Google Sheets) for importing and transforming data                   |
| **OpenRefine**             | Open-source; supports TSV, CSV, XLS, XML, JSON; menu-based operations — no syntax needed; extends data with web services                                        |
| **Google DataPrep**        | Intelligent cloud service; auto-detects schemas, data types, and anomalies; fully managed; suggests next steps as you work                                      |
| **Watson Studio Refinery** | IBM tool via Watson Studio / Cloud Pak for Data; auto-detects data types and enforces governance policies; transforms raw data into analytics-ready information |
| **Trifacta Wrangler**      | Cloud-based; known for collaboration features; exports to Excel, Tableau, and R                                                                                 |
| **Python**                 | Jupyter Notebook, NumPy, Pandas (merging, joining, transforming data), BeautifulSoup / Scrapy (web scraping), Matplotlib / Seaborn (visualization)              |
| **R**                      | Dplyr (data wrangling), Data.table (large dataset aggregation), Jsonlite (JSON parsing for web APIs)                                                            |

---

# **Querying Data, Performance Tuning, and Troubleshooting**

## Querying and Analyzing Data

Query languages allow us to access and explore data in databases. The techniques below map to SQL but are applicable to other query languages (e.g., CQL for Cassandra, Cypher for Neo4J) and APIs as well.

### Core Querying Techniques

**Counting and Aggregating**

```sql
COUNT()       -- counts total number of rows/records
COUNT(DISTINCT column)  -- counts unique values
SUM()         -- sum of a numeric column
AVG()         -- average value of a numeric column
STDDEV()      -- measures how spread out values are
```

**Identifying Extreme Values**

```sql
MAX()   -- highest value in a column
MIN()   -- lowest value in a column
```

**Slicing Data** — Retrieve records based on a specific condition or set of conditions (e.g., customers who spent between $1,000 and $2,000 in a specific area).

**Sorting Data**

```sql
ORDER BY column ASC | DESC   -- arrange data in ascending or descending order
```

**Filtering Patterns** — The `LIKE` operator returns records that partially match a data value, using wildcard characters for unknown portions. Unlike `=` (exact match), `LIKE` supports partial matching (e.g., filtering pincodes where only the first 3 digits are known).

**Grouping Data**

```sql
GROUP BY column   -- groups rows with matching values
SUM() + GROUP BY  -- e.g., total amount spent by customers grouped by pincode
```

---

## Performance Tuning and Troubleshooting

One of the key responsibilities of a data engineer is to monitor and optimize systems and data flows for performance and availability.

### Data Pipeline Performance

A data pipeline moves data from source to destination through multiple systems, applications, and processes. Common performance threats include:

- **Scalability** — struggling to handle increasing data sets and workloads
- **Application failures** — unexpected crashes or errors in pipeline tools
- **Scheduling issues** — jobs not starting on time, waiting on dependencies, or running out of sequence
- **Tool incompatibilities** — conflicts between the variety of tools in a pipeline

**Performance Metrics to Monitor:**

| Metric                   | Description                                        |
| ------------------------ | -------------------------------------------------- |
| **Latency**              | Time it takes for a service to fulfill a request   |
| **Failure rate**         | Rate at which a service fails                      |
| **Resource utilization** | CPU, memory, and disk usage patterns               |
| **Traffic**              | Number of user requests received in a given period |

### Troubleshooting Steps

```
1. Collect information about the incident
       |
       v
2. Verify software versions and source code
       |
       v
3. Review recent deployments for changes
       |
       v
4. Check logs and metrics
   (error messages, network load, CPU/memory at time of failure)
       |
       v
5. Reproduce the issue in a test environment (if logs are inconclusive)
       |
       v
6. Validate root cause hypothesis through testing
       |
       v
7. Deploy fix to production per team process
```

### Database Performance Optimization

**Metrics to Monitor:**

- System outages and capacity utilization
- Application slowdown
- Query performance
- Conflicting activities from multiple simultaneous users or batch jobs

**Optimization Best Practices:**

| Technique             | Description                                                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Capacity planning** | Determine optimal hardware and software resources for current and future load                                   |
| **Indexing**          | Quickly locates data without scanning every row; minimizes disk access during queries                           |
| **Partitioning**      | Divides large tables into smaller individual tables; queries run faster on smaller data; improves manageability |
| **Normalization**     | Reduces redundancy and anomalies from update, delete, and insert operations                                     |

### Monitoring and Alerting Systems

| System                                       | Purpose                                                                                 |
| -------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Database monitoring tools**                | Take frequent snapshots of performance indicators; help track when and how issues start |
| **Application performance management (APM)** | Track request response time, error messages, and resource utilization per process       |
| **Query performance monitoring**             | Gather statistics on query throughput, execution time, and resource usage               |
| **Job-level runtime monitoring**             | Break jobs into logical steps and monitor each for completion time                      |
| **Data volume monitoring**                   | Assess if workload size is slowing down a system                                        |

### Maintenance Schedules

- **Time-based** — Planned at pre-fixed time intervals (e.g., weekly, monthly)
- **Condition-based** — Triggered when a specific issue or performance decrease is flagged

---

# **Governance and Compliance**

## Governance and Compliance

Data Governance is a collection of principles, practices, and processes to maintain the security, privacy, and integrity of data through its lifecycle. A governance framework encompasses technologies, databases, and data models across the entire organization.

### What Data Is Protected?

Regulations primarily protect **personal and sensitive data** — data that can be traced back to an individual, used to identify them, or cause them harm (e.g., race, sexual orientation, genetic information).

### Key Regulations

| Regulation  | Scope            | Focus                                                                                      |
| ----------- | ---------------- | ------------------------------------------------------------------------------------------ |
| **GDPR**    | European Union   | Protects personal data and privacy of EU citizens for transactions within EU member states |
| **CCPA**    | California, USA  | Protects customer data for California residents                                            |
| **HIPAA**   | Healthcare (USA) | Governs collection and disclosure of protected health information                          |
| **PCI DSS** | Retail           | Governs credit card data standards                                                         |
| **SOX**     | Finance (USA)    | Governs handling and reporting of financial information                                    |

**Consequences of non-compliance:** financial penalties, damage to public perception, and loss of trust from clients and partners.

### Data Lifecycle and Governance Considerations

```
+------------------+------------------+------------------+------------------+------------------+
|  Data            |  Data            |  Data            |  Data            |  Data Retention  |
|  Acquisition     |  Processing      |  Storage         |  Sharing         |  & Disposal      |
|------------------|------------------|------------------|------------------|------------------|
| - What data to   | - How personal   | - Where data     | - Which 3rd-     | - Retention      |
|   collect        |   data will be   |   will be stored |   party vendors  |   policies for   |
| - Legal basis    |   processed      | - Security       |   have access    |   personal data  |
|   (contract /    | - Legal basis    |   breach         | - Contractual    | - Deletion from  |
|   consent)       |   for processing |   prevention     |   accountability |   all locations  |
| - Intended use / |                  |   measures       |   for compliance |   including 3rd  |
|   privacy policy |                  |                  |                  |   party systems  |
+------------------+------------------+------------------+------------------+------------------+
                        Auditable trail required at every stage
```

### Compliance Tools and Technologies

**Authentication and Access Control**

- Layered authentication: passwords + tokens + biometrics
- Role-based access control ensures users only access data relevant to their role
- Databases use roles and privileges to restrict access to specific tables, rows, or columns

**Encryption and Data Masking**

- **Encryption** — converts data to an encoded format; decryptable only via a secure key; applies to both data at rest and data in transit
- **Anonymization** — abstracts the presentation layer without changing underlying data (e.g., replacing characters with symbols on screen)
- **Pseudonymization** — replaces personally identifiable information with artificial identifiers so data cannot be traced back to an individual

**Hosting Options** — On-premise and cloud systems that comply with requirements and restrictions for international data transfers.

**Monitoring and Alerting**

- Proactively monitors, tracks, and reacts to security violations across infrastructure, applications, and platforms
- Provides detailed audit reports tracking data access and operations
- Alerts flag security breaches based on pre-defined severity and urgency levels

**Data Erasure** — A software-based method of permanently overwriting data from a system — different from simple deletion, which leaves data retrievable.
