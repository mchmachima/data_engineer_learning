# **Modern Data Ecosystem and role of Data Engineering**

## Welcome to Introduction to Data Engineering

### Course Overview

Welcome to this introductory course on Data Engineering, the first in a series of courses designed to prepare you for a career as a Junior Data Engineer. Data is growing at an unprecedented rate. And so are the ways in which data is being tapped by businesses, industries, institutions, and governments, all over the world, for making decisions that guide their future and the future of the people they serve.

How much value we can derive from data really depends on just two things – the accuracy of data and the efficiency with which we're able to access the data we need, when we need it. And that, in a nutshell, is the job of a Data Engineer. And the opportunity is huge. Dice Tech Job Report of 2020 lists data engineering as the fastest-growing tech occupation with year-over-year growth of 50%.

### Who Is This Course For?

This course is for you if you want to become a data engineer. You may have a background in engineering or computer science, you may be a graduate from a non-related stream, or you may be a non-graduate who loves coding – you can start your journey on this path by taking this course. You may even be a data professional who is excited about engineering, or a working professional with a technical role, in whichever capacity – this course will help you upskill and gain an opportunity in this field.

### What You Will Learn

This course introduces you to the core concepts, ecosystem, and life cycle of data engineering. You will learn about:

- Data, data repositories, data pipelines, data integration platforms, and big data
- The architecture of a data platform
- Design considerations for a data store
- How to extract, transform, and clean data to make it ready for analytics
- The principles of data security, privacy, and compliance regulations

You will hear from a panel of subject matter experts and practitioners sharing their knowledge and advising you on possible pathways that can help you become a data engineer.

### Meet Your Instructors

**Rav Ahuja** — A computer engineer by education, a data engineer by training, currently leading the content and strategy team for IBM Skills Network.

**Amber Crooks** — A data professional for about 20 years. Started her career with databases straight out of college with IBM as a DB2 database administrator. Currently a lead database engineer for an organization that does a lot of work with DevOps.

**Ramesh Sannareddy** — CEO of Mongo Factory, a company that provides data engineering consulting.

**Xiao Yang** — Data engineer at Coursera.

**Ragu Cherukuru** — Lead database administrator for a large retailer in the Midwest.

---

We are very excited to bring this course to you. Congratulations on choosing to be on this journey and good luck!

---

## The Modern Data Ecosystem

> "The constant increase in data processing speeds and bandwidth, the nonstop invention of new tools for creating, sharing, and consuming data, and the steady addition of new data creators and consumers around the world, ensure that data growth continues unabated. Data begets more data in a constant virtuous cycle." — Forbes, 2020

A modern data ecosystem includes a whole network of interconnected, independent, and continually evolving entities. It includes:

- Data that has to be integrated from disparate sources
- Different types of analysis and skills to generate insights
- Active stakeholders to collaborate and act on insights generated
- Tools, applications, and infrastructure to store, process, and disseminate data as required

### Data Sources

Data is available in a variety of structured and unstructured datasets, residing in:

- Text, images, and videos
- Clickstreams and user conversations
- Social media platforms
- Internet of Things (IoT) devices
- Real-time streaming events
- Legacy databases
- Data sourced from professional data providers and agencies

The sources have never before been so diverse and dynamic.

### Stage 1: Acquiring Data

When working with many different sources of data, the first step is to pull a copy of the data from the original sources into a data repository. At this stage, the focus is on acquiring the needed data — working with data formats, sources, and interfaces through which data can be pulled in.

**Key challenges:** Reliability, security, and integrity of the data being acquired.

### Stage 2: Organizing and Preparing Data

Once the raw data is in a common place, it needs to get organized, cleaned up, and optimized for access by end-users. The data must also conform to compliances and standards enforced in the organization, such as:

- Guidelines that regulate the storage and use of personal data (e.g., health, biometrics, or household data from IoT devices)
- Adherence to master data tables to ensure standardization across all applications and systems

**Key challenges:** Data management and working with repositories that provide high availability, flexibility, accessibility, and security.

### Stage 3: Delivering Data to End-Users

Business stakeholders, applications, programmers, analysts, and data science use cases all pull data from the enterprise data repository. Their needs vary:

- **Data Analysts** may need raw data to work with
- **Business stakeholders** may need reports and dashboards
- **Applications** may need custom APIs to pull this data

**Key challenges:** Building the right interfaces, APIs, and applications to deliver data to end-users in line with their specific needs.

### Emerging Technologies Shaping the Ecosystem

Several new and emerging technologies are transforming today's data ecosystem:

- **Cloud Computing** — Gives every enterprise access to limitless storage, high-performance computing, open source technologies, machine learning tools, and the latest libraries.
- **Machine Learning** — Data Scientists are creating predictive models by training machine learning algorithms on past data.
- **Big Data** — Today's datasets are so massive and varied that traditional tools and analysis methods are no longer adequate, paving the way for new tools, techniques, and insights.

We'll learn more about Big Data and its influence in shaping business decisions further along in this course.

---

## Key Roles in the Data Ecosystem

Organizations that use data to uncover opportunities and apply that knowledge to differentiate themselves are the ones leading into the future. Whether detecting fraud in financial transactions, using recommendation engines to drive conversion, mining social media for customer voice, or personalizing offers based on behavior analysis — business leaders recognize that data holds the key to competitive advantage.

To get value from data, you need a vast number of skillsets and people playing different roles.

### Data Engineer

Data Engineers develop and maintain data architectures and make data available for business operations and analysis. They work within the data ecosystem to:

- Extract, integrate, and organize data from disparate sources
- Clean, transform, and prepare data
- Design, store, and manage data in data repositories

They enable data to be accessible in formats and systems that business applications, Data Analysts, and Data Scientists can utilize.

**Required skills:** Programming, systems and technology architectures, relational databases, and non-relational datastores.

### Data Analyst

A Data Analyst translates data and numbers into plain language so organizations can make decisions. They:

- Inspect and clean data for deriving insights
- Identify correlations, find patterns, and apply statistical methods to analyze and mine data
- Visualize data to interpret and present findings

Analysts answer questions like: _"Are users' search experiences generally good or bad?"_, _"What is the popular perception of our rebranding initiatives?"_, or _"Is there a correlation between sales of one product and another?"_

**Required skills:** Spreadsheets, query writing, statistical tools for charts and dashboards, some programming, and strong analytical and storytelling skills.

### Data Scientist

Data Scientists analyze data for actionable insights and build Machine Learning or Deep Learning models that train on past data to create predictive models. They answer questions like: _"How many new social media followers am I likely to get next month?"_, _"What percentage of my customers am I likely to lose to competition?"_, or _"Is this financial transaction unusual for this customer?"_

**Required skills:** Mathematics, Statistics, programming languages, databases, data modeling, and domain knowledge.

### Business Analyst & BI Analyst

**Business Analysts** leverage the work of Data Analysts and Data Scientists to look at possible implications for their business and recommend actions.

**BI Analysts** do the same, but focus specifically on market forces and external influences that shape the business. They provide business intelligence solutions by organizing and monitoring data on different business functions and extracting insights to improve business performance.

### Summary: How the Roles Connect

| Role                          | Core Function                                             |
| ----------------------------- | --------------------------------------------------------- |
| Data Engineer                 | Converts raw data into usable data                        |
| Data Analyst                  | Uses data to generate insights                            |
| Data Scientist                | Uses past data to predict the future                      |
| Business Analyst / BI Analyst | Uses insights and predictions to drive business decisions |

> It's not uncommon for data professionals to start their career in one data role and transition to another by supplementing their skills.

---

## Specializations in the Data Engineering Ecosystem

The modern data landscape is expansive and complex, driven by a diverse range of skilled professionals. Although they share a common objective of ensuring efficient and dependable data management, each role carries unique responsibilities.

### Data Warehouse Engineer

Data Warehouse Engineers design, build, and maintain data warehouses to store and analyze large datasets for business intelligence and reporting purposes. Their responsibilities include:

- Developing ETL (Extract, Transform, Load) processes to ensure efficient data integration and management
- Implementing data lakes for unstructured data as architectures evolve to include big data systems
- Enabling organizations to store and process diverse data types for advanced analytics and machine learning

### Data Architect

Data Architects design the overall architecture for an organization's data management system, encompassing data warehousing, big data, and analytics platforms. They:

- Define strategies for data integration, governance, and security
- Establish schemas, indexing methods, and partitioning strategies to optimize data retrieval
- Model data relationships and design solutions for high availability and disaster recovery
- Plan for future growth and technological advancements to keep systems adaptable

### Data Manager

Data Managers oversee the governance and strategy of an organization's data, ensuring that quality, compliance, and accessibility meet both business and regulatory standards. Key tasks include:

- Developing data governance frameworks and enforcing adherence to established standards
- Defining access control policies
- Promoting cross-departmental collaboration and aligning data usage with organizational objectives
- Cultivating a culture of data literacy

### Database Administrator (DBA)

Database Administrators ensure the smooth operation of databases, with a focus on security, availability, and optimal performance. Their duties include:

- Conducting routine backups, optimizing performance, and managing patches
- Monitoring database activity to identify and resolve issues such as slow queries or unauthorized access
- Implementing encryption protocols and maintaining audit logs for compliance

### Role Comparison

| Aspect                | Data Warehouse Engineer                                    | Data Architect                             | Data Manager                               | Database Administrator                  |
| --------------------- | ---------------------------------------------------------- | ------------------------------------------ | ------------------------------------------ | --------------------------------------- |
| **Focus**             | Designing & maintaining data warehouses and pipelines      | Overall data architecture and scalability  | Strategy, governance, and compliance       | Operational reliability and security    |
| **Key Deliverables**  | ETL pipelines, data transformations, warehouse deployments | Scalable data management solutions         | Policies, standards, compliance frameworks | Secure and reliable database operations |
| **Tools**             | Apache Kafka, Spark, cloud data warehousing                | ERD tools, MySQL, MongoDB, cloud platforms | Data governance platforms                  | SQL, database monitoring tools          |
| **Collaborates With** | Architects, DBAs, BI analysts                              | Engineers, DBAs, business leaders          | Business and technical teams               | Engineers and architects                |

### Real-World Example: Hospital Network

| Role                        | Responsibilities                                                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Data Warehouse Engineer** | Designs ETL processes to transform and load patient data from EHR and lab systems into structured formats for analytics and reporting            |
| **Data Architect**          | Develops a scalable structure for millions of patient records with indexing strategies for fast retrieval of medical histories and prescriptions |
| **Data Manager**            | Ensures adherence to healthcare regulations, establishes access policies, supervises data quality, and aligns IT with clinical objectives        |
| **Database Administrator**  | Ensures uninterrupted EHR operation, conducts regular backups, manages user access, and implements disaster recovery protocols                   |

### How These Roles Collaborate

- **Data Warehouse Engineers** coordinate with Data Architects on warehouse design and with Data Managers to ensure pipelines meet governance requirements.
- **Data Architects** partner with Engineers for smooth implementation and with DBAs for system design.
- **Database Administrators** draw on Architects' expertise and work with Data Managers to uphold compliance standards.

Together, these roles form an essential framework for managing and leveraging data effectively in any organization. Understanding their distinctions helps you choose a path where you can thrive in the data-driven era.

---

## The Scope of Data Engineering

In the simplest possible terms, Data Engineering concerns itself with the mechanics for the flow and access of data. Its goal is to make quality data available for fact-finding and data-driven decision making.

As data has grown — from a single manageable database to wide-ranging sources, structures, and types — so has the field of data engineering. The scope spans four core areas:

### 1. Collecting Source Data

This involves extracting, integrating, and organizing data from disparate sources. To do this effectively, you need to:

- Develop tools, workflows, and processes to acquire data from multiple sources
- Design, build, and maintain scalable data architecture to store data (databases, data warehouses, data lakes, or other repositories)

### 2. Processing Data

Processing involves cleaning, transforming, and preparing data so that it is usable. This requires you to:

- Implement and maintain distributed systems for large-scale data processing
- Design pipelines for extracting, transforming, and loading (ETL) data into repositories
- Design or implement solutions for validating and safeguarding data quality, privacy, and security
- Optimize tools, systems, and workflows for performance, reliability, and scalability
- Ensure data meets all regulatory and compliance guidelines

### 3. Storing Data

Reliable and easy availability of data depends on sound storage practices. This involves:

- Architecting or implementing data stores for processed data
- Ensuring systems are scalable, keeping in mind the evolving nature of data and business needs
- Ensuring tools and systems handle data privacy, security, compliance, monitoring, backup, and recovery

### 4. Making Data Available to Users

The final step is delivering data securely to end-users through:

- APIs, services, and programs that retrieve data on defined parameters
- Interfaces and dashboards that allow users to derive insights
- Rights-based access controls and checks to keep data secure

### Data Engineering Is a Team Sport

No single person is expected to have all the knowledge, skills, and specializations required for the wide-ranging tasks in data engineering. For example:

- **Architecting** data management systems requires the skills of a data architect
- **Ensuring data stores** are available and optimized requires database expertise
- **Proficiency** in database tools, programming languages, and distributed systems each require different skill sets

Additionally, not all teams need to build an end-to-end data engineering practice from scratch. There are tools, applications, and solutions available — both on-premise and cloud-based — that can be evaluated for individual organizational needs.

> Data engineering is about the tools and technologies involved in data manipulation — but it is also about understanding the complexities of data and how it is ultimately leveraged for fact-finding and decision-making.

---

# **Responsibilities and Skillsets of a Data Engineer**

## Core Responsibility

The overarching responsibility of a Data Engineer is to provide **analytics-ready data** to data consumers. Data is considered analytics-ready when it is:

- **Accurate** and reliable
- **Compliant** with the regulations it is governed by
- **Accessible** to consumers when they need it

---

## Key Responsibilities

At a broad level, Data Engineers:

- Extract, organize, and integrate data from disparate sources
- Prepare data for analysis and reporting by transforming and cleansing it
- Design and manage data pipelines that encompass the journey of data from source to destination systems
- Set up and manage the infrastructure required for the ingestion, processing, and storage of data — including data platforms, distributed systems, and data repositories

---

## Technical Skills

### Operating Systems & Infrastructure

- Working with **operating systems** such as UNIX, Linux, and Windows, including administrative tools, system utilities, and commands
- Knowledge of **infrastructure components** such as virtual machines, networking, load balancing, and application performance monitoring
- **Cloud-based services** from providers such as Amazon, Google, IBM, and Microsoft

### Databases & Data Warehouses

- **Relational databases (RDBMS):** IBM DB2, MySQL, Oracle Database, PostgreSQL
- **NoSQL databases:** Redis, MongoDB, Cassandra, Neo4J
- **Data warehouses:** Oracle Exadata, IBM Db2 Warehouse on Cloud, IBM Netezza Performance Server, Amazon RedShift

### Data Pipelines & ETL Tools

- **Data pipeline solutions:** Apache Beam, AirFlow, DataFlow
- **ETL tools:** IBM Infosphere Information Server, AWS Glue, Improvado

### Languages

- **Query languages:** SQL for relational databases; SQL-like languages for NoSQL databases
- **Programming languages:** Python, R, Java
- **Shell and scripting languages:** Unix/Linux Shell, PowerShell

### Big Data

- Familiarity with big data processing tools such as **Hadoop**, **Hive**, and **Spark**

> Having a working knowledge of comparable technologies helps you evaluate trade-offs between different tools and make appropriate recommendations.

---

## Functional Skills

Data Engineering sits at the intersection of software engineering and data science. Beyond tools and technologies, Data Engineers need to understand how data scientists, analysts, and business users leverage analysis-ready data. Key functional skills include:

- Converting business requirements into technical specifications
- Working across the complete **software development lifecycle** — ideation, architecture, design, prototyping, testing, deployment, and monitoring
- Understanding data's potential application in business
- Understanding the risks of poor data management — covering data quality, privacy, security, and compliance

---

## Soft Skills

Data Engineering is a team sport. Multiple data engineers often collaborate on a project, closely interacting with analysts, data scientists, business users, and other technical teams. Essential soft skills include:

- **Interpersonal skills** and the ability to work collaboratively
- **Communication** — conveying complex concepts clearly to both technical and non-technical stakeholders
- **Teamwork** — coordinating across specializations and departments

---

## Summary

Data Engineering requires a broad set of skillsets. No single data engineer is expected to master all of them — the key is to:

1. Select one or more **specialization areas**
2. Maintain a **solid understanding across all areas** to make informed decisions
3. Continuously **upskill** through experience and focused learning over time

---

# Real-World Example: Social Media Sentiment Analysis

_Told by Sarah Flinch, Data Engineer at a multinational hair care company._

## Background

Sarah's company was preparing to launch a new shampoo and needed to monitor customer sentiment across social media from day one. The business team wanted real-time visibility into what online communities — Twitter, Facebook, Instagram, eCommerce platforms, and bloggers — were saying about their product: positive feedback, negative comments, suggestions, and comparisons with competitors.

The Data Science team had already built a prototype dashboard using a sentiment analysis algorithm and dummy data, displaying customer sentiment scores across social media sources and demographics. Once approved, the Data Engineering team was brought in to make it a reality.

## Step 1: Collecting the Data

Sarah's first task was pulling data from all identified social media and online sources into the organization's environment:

- Used **APIs** to pull tweets and posts containing the product's hashtag into temporary storage
- Used **web scraping** to collect product-specific data from eCommerce portals and product review blogs

The result was a diverse mix of formats and structures — tweets, posts, comments, articles, and memes.

## Step 2: Processing the Data

Once all data was collected, Sarah inspected it to assess what transformations were needed before it could be loaded into the database:

- Built a **Python program** to process and load the data
- Cleaned the data and transformed it into a format compatible with the database
- The database then served as the source for the dashboard's reports

The results matched exactly what the Data Scientists had hoped to see — a successful first delivery.

## Step 3: Building a Data Pipeline

A one-time data pull would require the business team to submit a new request every time they needed updated statistics — an inefficient solution. The next step was to automate the process:

- Build a **data pipeline** that continuously extracts, transforms, and loads data on an ongoing basis
- Once in place, business teams would be able to see **real-time sentiment projections** every time they log into the dashboard

## Key Takeaway

This example illustrates the end-to-end role of a Data Engineer in a real business scenario — from data collection and transformation to pipeline automation — ultimately enabling data-driven decisions at scale.
