# L01 Fundamental Relational Database Concepts

- **Certificate:** IBM Data Engineering Professional Certificate
- **Course:** C04 Introduction to Relational Databases (RDBMS)
- **Module:** M01 Relational Database Concepts
- **Date studied:** 2026-07-12

---

## 📌 Key Concepts

**Data and Data Repositories**

- Data is unorganized information (facts, observations, numbers, symbols, images, or a mix) that becomes meaningful once processed.
- Data falls into three structural categories: structured, unstructured, and semi-structured.
- Structured data follows a rigid, predefined schema (rows/columns) — e.g., spreadsheets, SQL databases, online forms.
- Unstructured data has no predefined format — e.g., text files, media files, web pages, social media content.
- Semi-structured data has partial organization via tags/hierarchy rather than strict tables — e.g., JSON, XML, emails.
- Common file formats for storing/transferring data: delimited text files (CSV, TSV), spreadsheets, and language files (XML, JSON).
- Data repositories centrally store, manage, and organize data; the two major categories are relational and non-relational databases.
- Relational databases (RDBMS) store structured data in linked tables, minimizing duplication, and mainly support OLTP (day-to-day transactional work).
- OLAP systems (which can include relational/non-relational stores, data warehouses, and data lakes) focus on querying and analyzing large datasets for insights.
- Non-relational databases (e.g., MongoDB, Cassandra, Redis) offer flexibility for unstructured or semi-structured data.

**Information Models and Data Models**

- Information models and data models are the two key concepts in data organization, operating at different levels of abstraction.
- An information model is an abstract, conceptual framework representing entities, properties, relationships, and functions — a high-level, technology-agnostic view for business stakeholders.
- A data model is a tangible blueprint that translates the information model into a technical database structure, defining schema, tables, columns, data types, indexes, and relationships (e.g., foreign keys) — often via normalization.
- Business analysts/stakeholders use information models to agree on concepts; database designers/developers use data models to build the system.
- The hierarchical model is an early physical implementation of an information system, structuring data in a tree-like format; it has lower abstraction and struggles with many-to-many relationships, causing redundancy.
- The two most common data model types are the relational model and the entity-relationship (ER) model.
- The relational model is the most widely used, storing data in tables and providing logical, physical, and storage independence, with the advantages of simplicity, flexibility, and ease of use.
- The ER model conceptualizes a database as entities (rectangles) with attributes (ovals) and their relationships; it's used for conceptual design and is then mapped into relational tables.
- Three independence concepts — logical, physical, and physical storage — let parts of a database change without breaking other parts of the system.

**ERDs and Types of Relationships**

- An ERD (Entity Relationship Diagram) is a visual representation illustrating the relationships and interactions between entities in a database.
- An ERD shows the logical structure of a database — entities as boxes, with lines connecting them to show relationships.
- The three fundamental components of an ERD are entities, relationship sets, and crow's foot notation.
- Entities are people, objects, or concepts that store data, represented as rectangles; their attributes (properties) are shown as ovals, each attribute connecting to exactly one entity.
- Relationship sets illustrate how entities are interconnected, represented as diamonds with lines connecting the associated entities.
- Crow's foot notation uses symbols (greater-than, less-than, vertical lines) to show the nature and quantity of a relationship between entities.
- There are three relationship types: one-to-one, one-to-many (or many-to-one), and many-to-many — illustrated in the lesson using a Book/Author example.

**Mapping Entities to Tables**

- An ERD is a graphical representation of the entities and relationships in a database, used as a modeling technique in database design.
- The primary ERD components are entities (rectangles), attributes (ovals inside the entity), and relationships (lines connecting entities).
- A relational database organizes data into tables, with relationships between tables based on common fields.
- Designing a relational database starts with an ERD, which is then mapped to tables.
- Mapping an ERD to tables is a three-step process: create a table for each entity, translate attributes into columns, then add data values into the columns.
- Best practices for relational database design include primary key designation, data validation, default values, use of views, and concurrency control.

**Data Types**

- A data type defines what kind of data a column can hold and controls what can be validly entered into it (text, date, number, etc.).
- Varchar (variable character) stores strings up to a specified maximum length but only uses the space actually needed — more space-efficient than fixed-length types.
- Char is a fixed-length character type that always uses the specified number of characters, padding with spaces if the value is shorter.
- Date/time types include DATE (year, month, day), TIME, and combined DATETIME or TIMESTAMP types; exact behavior varies by database system (e.g., MySQL).
- Float stores approximate floating-point numbers (fine when exact precision isn't required); Decimal stores exact numbers and is preferred for financial calculations.
- Integer types (INT, SMALLINT, etc.) store whole numbers, each with a different supported range.
- Binary types like BLOB (Binary Large Object) store non-textual data such as images or files as raw bytes.
- Choosing the correct data type prevents invalid data entry, enables accurate sorting and range selection, and allows correct numeric calculations.

**Relational Model Concepts**

- The relational model (introduced in 1970) is built on two core mathematical concepts: sets and relations.
- A set is a collection of unique, unordered elements of a similar type, typically written with curly braces or set-builder notation.
- Key set operations include membership, subset, union, intersection, difference, empty set, power set, universal set, and disjoint sets.
- A relation describes a connection between elements of sets; common types include binary relations and ordered pairs (from the Cartesian product).
- Relations can exhibit properties: reflexivity, symmetry, transitivity, and anti-symmetry.
- A relation has two components: the relation schema (structure — relation name plus attribute names/types) and the relation instance (the actual data — rows and columns).
- Degree is the number of attributes (columns) in a relation; cardinality is the number of tuples (rows).

---

## Data and Data Repositories

### Data and Data Structures

Data refers to unorganized information — facts, observations, perceptions, numbers, characters, symbols, images, or a combination — that becomes meaningful once processed. How data is structured determines how efficiently it can be stored, managed, and analyzed. There are three main structural categories:

- **Structured data** — highly organized, follows a strict predefined schema, typically arranged in rows/columns. Examples: Excel spreadsheets, SQL databases, online forms with designated fields (name, address, credit card number).
- **Unstructured data** — lacks a specific format or organization, doesn't follow predefined rules, harder to process with traditional methods. Examples: text files, media files (images/audio/video), web pages, social media content.
- **Semi-structured data** — has some organizational properties (hierarchical structure or tags) without a strict tabular format, balancing flexibility and structure. Examples: JSON files (arrays/objects with keys), XML documents (tags, attributes, schema), emails (structured fields like to/from/subject, but unstructured message body).

---

### Common File Formats for Data Transfer

Businesses pull data from many sources — traditional databases, flat files, XML data sets, web scraping, data streams/feeds, social media, IoT sensors — and need standard formats to hold or transfer it between systems:

- **Delimited text files** — data in rows, with each variable separated by a specific character (comma or tab). Includes CSV (comma-separated values) and TSV (tab-separated values).
- **Spreadsheets** — data arranged in rows and columns like a table, making access and manipulation easy; can be used to create CSV files.
- **Language files** — formats like XML and JSON that have set rules and structures for encoding data to send over the internet.

---

### Data Repositories: Relational vs Non-Relational Databases

Data repositories actively store, manage, and organize data centrally, providing a structured framework for efficient retrieval and administration. The two major categories:

- **Relational databases** — structured data stored in related tables; links between tables minimize data duplication while preserving relationships. Collectively known as Relational Database Management Systems (RDBMS). Prominent examples: IBM DB2, Microsoft SQL Server, Oracle, MySQL.
- **Non-relational databases** — offer flexibility for handling diverse and unstructured/semi-structured data. Examples: MongoDB (document-oriented), Cassandra, Redis.

---

### OLTP vs OLAP

- **OLTP (Online Transaction Processing)** — relational databases are primarily OLTP systems, supporting day-to-day business activities like customer transactions, HR activities, and workflows. Their normalized structure ensures transactional integrity and supports concurrent access for routine operations.
- **OLAP (Online Analytical Processing)** — includes various storage solutions (relational and non-relational databases, data warehouses, data lakes, big data stores) focused on querying and analyzing large datasets to extract insights. Example: using CRM-sourced data for analytics like sales projections.

---

## Information Models and Data Models

### Information Models vs Data Models

An information model is a conceptual framework representing entities, properties, relationships, and functions abstractly — giving stakeholders a high-level view of data without implementation detail. A data model operates at a tangible level, translating that conceptual view into a technical blueprint: schema, tables, columns, data types, indexes, and relationships (often refined through normalization).

| Aspect | Information Model | Data Model |
| --- | --- | --- |
| Level of abstraction | High — conceptual, technology-agnostic | Low — concrete, technical |
| Focus | Broad business concepts and relationships | Storage, schema, and technical manipulation methods |
| Detail | Fewer details | Detailed (tables, columns, data types, constraints) |
| Tied to a specific DBMS? | No | Often, yes |
| Used by | Business analysts and stakeholders | Database designers and developers |
| Purpose | Agree on business concepts without technicalities | Construct and implement the actual database system |

In system development, the information model captures the essential business information types first; that is then translated into a data model as the technical blueprint for the database system.

---

### The Hierarchical Model

The hierarchical model is a physical implementation of an information system, storing relationships in a tree-like structure — unlike an information model, which conceptualizes relationships without specifying storage.

| Aspect | Information Model | Hierarchical Model |
| --- | --- | --- |
| Abstraction | High — conceptualizes without specifying storage | Lower — physically structures data in a tree format |
| Relationship handling | Represents entity relationships clearly for real-world scenarios | Struggles with many-to-many relationships |
| Consequence | N/A (conceptual only) | Structural limitations can lead to data redundancy |
| Historical role | N/A | Rooted in early database systems; linked to the initial phases of information models |

---

### Types of Data Models: Relational and Entity-Relationship (ER)

The two most common data model types are the **relational model** and the **entity-relationship (ER) model**.

- **Relational model** — the most widely used data model for databases. Stores data in tables and provides logical, physical, and storage independence. Advantages include simplicity, flexibility, and ease of use.
- **ER model** — an alternative that conceptualizes a database as a collection of independently existing entities and objects. Entities are represented as rectangles, attributes as ovals (e.g., in a library database, `Author` is an entity with attributes like last name, first name, email). An ER diagram (ERD) is used for conceptual design and is then converted into tables — each entity becomes a table, with its attributes becoming columns.

| Aspect | Relational Model | Entity-Relationship (ER) Model |
| --- | --- | --- |
| Representation | Data stored directly in tables | Entities (rectangles) and attributes (ovals) in a diagram |
| Typical use | Actual database storage/implementation | Conceptual design stage, before implementation |
| Independence | Provides logical, physical, and storage independence | N/A — a design/modeling tool |
| Relationship to each other | End implementation target | Maps into relational tables (entity → table, attribute → column) |
| Example | Tables like `Books`, `Authors`, `Borrowers` | ERD showing `Book`, `Author`, `Borrower` entities and their relationships |

---

### Data Independence Concepts

Three concepts support adaptability and efficiency in database management, each isolating one layer of the system from changes in another:

| Independence Type | What it allows to change | What stays unaffected |
| --- | --- | --- |
| Logical data independence | Database structure (e.g., altering data types, adding fields) | User data access |
| Physical data independence | Internal database organization (e.g., storage type, indexing strategy) | User views or applications |
| Physical storage independence | Location/organization of data on physical storage devices | Application programs processing the data |

---

## ERDs and Types of Relationships

### What is an ERD?

An ERD (Entity Relationship Diagram) is a visual representation that illustrates the relationships and interactions between entities in a database. It showcases the logical structure of a database system, displaying entities and the relationships between them as lines connecting boxes.

---

### Fundamental Components of an ERD

An ERD is built from three fundamental components:

- **Entities** — represent people, objects, or concepts that store data in a database. They are the fundamental building blocks, depicted as rectangles, and contain attributes describing specific properties (e.g., the `Book` entity has attributes like title, edition, year, price; the `Author` entity has attributes like last name, first name, email, city, country, author ID). Each attribute connects to exactly one entity. Entities form the basis for relationships within the database model.
- **Relationship sets** — illustrate how entities are interconnected or associated with each other, showing how instances of one entity type relate to instances of another. Represented as a diamond, with lines connecting the associated entities. Diagrams showing relationship types typically feature only entities (no attributes), to avoid clutter.
- **Crow's foot notation** — a visual notation using symbols to signify the nature and quantity of relationships between entities: a rectangle for entity sets, a diamond for relationship sets, and symbols like `>`, `<`, and vertical lines to indicate whether a relationship is one-to-one, one-to-many, or many-to-many.

---

### Types of Relationships

Using the Book/Author example: a book requires at least one author (and can have more than one), and an author can write one or more books. The nature of this connection defines the relationship type.

| Relationship Type | Definition | Crow's Foot Symbol | Book/Author Example |
| --- | --- | --- | --- |
| One-to-one | Each entity in the set is engaged in exactly one relationship | Thick/plain line, no crow's foot | Each book is written by a single author ("Authored by") |
| One-to-many (or many-to-one) | One entity participates in multiple relationships within the set | Less-than symbol (`<`) on one side | One book has multiple authors; viewed the other way, multiple authors contribute to one book |
| Many-to-many | Multiple instances of one entity relate to multiple instances of another | Greater-than and less-than symbols (`>` ... `<`) on both sides | Many authors write many books |

Simple diagram of each type (Book–Author):

```
One-to-One:      [ Book ] ──────── [ Author ]
                  (each book has exactly one author)

One-to-Many:      [ Book ] ───────≺ [ Author ]
                  (one book, multiple authors)

Many-to-Many:     [ Book ] ≻─────≺ [ Author ]
                  (many books, many authors)
```

---

## Mapping Entities to Tables

### From ERD to Relational Database

An ERD is a graphical representation of the entities and relationships between them in a database — a modeling technique used to visually represent a database system's structure. Its primary components are:

- **Entities** — real-world objects, concepts, or things that store and manage data, depicted as rectangles (e.g., `Book`).
- **Attributes** — characteristics associated with an entity, depicted as ovals inside the entity rectangle (e.g., ISBN, title, author, published year for `Book`).
- **Relationships** — illustrate how entities interrelate, shown as a line connecting entity rectangles (e.g., an `Author` "writes" a `Book`).

A relational database provides a well-defined framework for managing and manipulating structured data, organizing data elements into tables where relationships between tables depend on common fields.

---

### Steps for Mapping Entities to Tables

To design a relational database, begin with an ERD, then map it to tables:

1. **Entity → Table** — the entity becomes a table with the same name (e.g., `Book` entity becomes the `Book` table). This step only provides the structure for rows and columns; the table is still empty.
2. **Attributes → Columns** — the attributes of the entity become columns in the table (e.g., ISBN, title, and author become columns in the `Book` table).
3. **Add data values** — relevant data is entered into the table's columns, completing the transformation from a conceptual entity into a tangible table with real data.

The same three steps are repeated for every other entity in the ERD (e.g., transforming the `Author` entity into an `Author` table).

---

### Best Practices for Relational Database Design

- **Primary key designation** — assign a primary key (e.g., `Book ID`) to uniquely identify each entry in a table.
- **Data validation** — implement checks for data types, ranges, and formats to ensure accuracy and consistency (e.g., ensuring `published year` only accepts numerical values within a specified range).
- **Default values** — assign default values to certain columns to streamline data entry (e.g., defaulting the `author` column to "Unknown" when the author is not available).
- **Use of views** — utilize views to present a customized, simplified perspective of the data, especially for complex queries or reporting (e.g., a view combining `Book` and `Author` tables into a single list without exposing the underlying complexity).
- **Concurrency control** — implement mechanisms to manage multiple users accessing and modifying the database concurrently, preventing data inconsistency and conflicts (e.g., a "Last modified" timestamp column in the `Book` table).

---

## Data Types

### What Is a Data Type

A database table represents a single entity, where each column represents an attribute of that entity (e.g., a `Book` table with `title`, `publish date`, and `pages` columns). Every value in a column should be the same kind of data — the data type assigned to a column controls what it can store. A text column holds alphanumeric data, a date column only accepts valid dates, and a numeric column only accepts numbers.

---

### Varchar

Varchar is a data type for storing character strings of varying length, up to a specified maximum. For example, `VARCHAR(100)` allocates space for up to 100 characters, but a 50-character string only uses the space needed for those 50 characters — not the full 100.

Key considerations:

- **Efficiency** — Varchar only allocates the space actually used, making it more space-efficient than fixed-length types like Char.
- **Flexibility** — ideal for strings whose length varies significantly, such as names, addresses, or descriptions.

---

### Common Data Types

Different database systems handle these common types with some variation:

| Category | Type(s) | Description | Example |
| --- | --- | --- | --- |
| Date / Time | DATE, TIME, DATETIME, TIMESTAMP | DATE stores year, month, day; TIME stores the time of day; DATETIME/TIMESTAMP combine both | In MySQL, DATE uses year-month-day format while TIMESTAMP includes both date and time |
| Float | FLOAT | Approximate floating-point number, used when exact precision isn't necessary | `FLOAT(24)` in SQL Server |
| Decimal | DECIMAL | Exact numeric type for precise arithmetic; more suitable for financial calculations | `DECIMAL(5,2)` stores 5 total digits, 2 after the decimal point |
| Integer | INT, SMALLINT | Whole numbers, each type with a different supported range | INT typically ranges from -2,147,483,648 to 2,147,483,647 |
| Binary | BLOB | Binary Large Object; stores data as a sequence of bytes, ideal for non-textual data | Images, files |
| Char | CHAR | Fixed-length character type; always uses the specified number of characters, padding with spaces if necessary | `CHAR(10)` always stores 10 characters |

---

### Advantages of Using Appropriate Data Types

- Prevents incorrect data from being inserted into a column, since the data type restricts what counts as valid input.
- Allows date, time, and numeric data to be sorted accurately.
- Allows accurate selection of data ranges (e.g., filtering dates or numbers within a range).
- Enables numeric calculations on correctly typed data, such as calculating an order's total cost.

---

## Relational Model Concepts

### Sets and Set Operations

A set is a collection of unique elements without a specified order, comprising items of a similar type. Sets are usually denoted with curly braces (elements listed inside) or set-builder notation (a condition describing membership). Sets underpin much of modern mathematics, including algebra, geometry, and probability.

Basic set operations and concepts:

| Concept | Notation | Meaning |
| --- | --- | --- |
| Membership | `a ∈ A` | `a` is an element of set `A` |
| Subset | `A ⊆ B` | Every element of `A` is also an element of `B` |
| Union | `A ∪ B` | Elements that are in `A`, in `B`, or both |
| Intersection | `A ∩ B` | Elements that are in both `A` and `B` |
| Difference | `A − B` (or `A / B`) | Elements that are in `A` but not in `B` |
| Empty set | `{}` or `∅` | A unique set with no elements; a subset of every set |
| Power set | `P(A)` | The set of all possible subsets of `A`, including `∅` and `A` itself |
| Universal set | `U` | The set containing all objects under consideration; all other sets are subsets of it |
| Disjoint sets | — | Two sets that share no common element |

Venn diagrams are visual representations used to illustrate logical relations between sets.

---

### Relations and Their Properties

A relation is a mathematical concept built on the idea of sets — it describes connections between elements of sets and is essential to set theory and logic. Common types include:

- **Binary relation** — a connection between two elements (e.g., the "less than" relation, as in 3 < 5).
- **Ordered pairs** — a subset of the Cartesian product `A × B`, representing a binary relation on sets `A` and `B`, denoted `(a, b)`.

Relations can exhibit the following properties:

| Property | Definition | Example |
| --- | --- | --- |
| Reflexivity | Each element relates to itself | Equality — `A = A` for any element `A` |
| Symmetry | If `A` relates to `B`, then `B` also relates to `A` | "Is a sibling of" |
| Transitivity | If `A` relates to `B` and `B` relates to `C`, then `A` relates to `C` | "Less than" — if `A < B` and `B < C`, then `A < C` |
| Anti-symmetry | If `A` relates to `B` and `B` relates to `A`, then `A` must equal `B` | "Less than or equal to" |

---

### Relation Schema vs. Relation Instance

A relation consists of two essential components:

- **Relation schema** — specifies the structure: the name of the relation, and the name and data type of each column (attribute). For example, for an `Author` relation: `Author_ID` (CHAR — a fixed-length character string), `last_name`, `first_name`, `email` (VARCHAR — a variable-length character string), and `country` (CHAR).
- **Relation instance** — the actual real-world data stored in the table, made up of rows and columns. The columns correspond to the attributes defined in the schema, and the rows represent tuples (individual records).

---

### Degree and Cardinality

- **Degree** — the number of attributes (columns) in a relation.
- **Cardinality** — the number of tuples (rows) in a relation.

In the lesson's `Author` example: degree is 6 (six columns: `Author_ID`, `last_name`, `first_name`, `email`, `city`, `country`) and cardinality is 5 (five rows of data).

---

## 📖 Key Terms & Glossary

| Term | Definition |
| --- | --- |
| Structured data | Highly organized data following a predefined schema, typically in rows and columns |
| Unstructured data | Data with no specific format or predefined organization |
| Semi-structured data | Data with some organizational properties (tags/hierarchy) but no strict tabular structure |
| CSV | Comma-separated values — a delimited text file format |
| TSV | Tab-separated values — a delimited text file format |
| XML | Extensible Markup Language — encodes data using tags, attributes, and schema |
| JSON | JavaScript Object Notation — encodes data using arrays and objects with keys |
| Data repository | A centralized system that stores, manages, and organizes data |
| RDBMS | Relational Database Management System — software managing relational databases |
| OLTP | Online Transaction Processing — systems supporting day-to-day operational transactions |
| OLAP | Online Analytical Processing — systems for querying/analyzing large datasets for insights |
| MongoDB | A document-oriented, non-relational database suited to semi-structured/unstructured data |
| Information model | An abstract, conceptual representation of entities, properties, relationships, and functions |
| Data model | A technical blueprint translating an information model into a database structure |
| Hierarchical model | An early database model that physically structures data in a tree-like format |
| Relational model | The most widely used data model; stores data in tables with logical/physical/storage independence |
| Entity-Relationship (ER) model | A conceptual model representing a database as entities and their relationships |
| Entity | A real-world object, concept, or thing that stores and manages data, represented as a rectangle in an ERD |
| Attribute | A characteristic (property) of an entity, represented as an oval, connected to exactly one entity |
| ERD | Entity Relationship Diagram — a visual/graphical representation of entities and their relationships in a database |
| Normalization | The process of organizing data to reduce redundancy and ensure integrity |
| Foreign key | A field linking one table to the primary key of another, representing a relationship |
| Logical data independence | Ability to change database structure without affecting user data access |
| Physical data independence | Ability to change internal storage/indexing without affecting user views/applications |
| Physical storage independence | Ability to move/reorganize data on storage devices without affecting applications |
| Relationship set | A diamond-shaped element illustrating how two entities are interconnected |
| Crow's foot notation | A notation using symbols (>, <, vertical lines) to indicate the type and quantity of a relationship |
| One-to-one relationship | Each entity instance is linked to exactly one instance of another entity |
| One-to-many relationship | One entity instance is linked to multiple instances of another entity |
| Many-to-many relationship | Multiple instances of one entity are linked to multiple instances of another entity |
| Cardinality (ERD sense) | The numeric nature of a relationship (one vs. many) between connected entities |
| Relational database | A database model that organizes data into tables, with relationships between tables based on common fields |
| Relationship | A connection illustrating how entities interrelate, shown as a line between entity rectangles |
| Primary key | An exclusive identifier assigned to each entry in a table to uniquely identify it |
| Data validation | Mechanisms that check data types, ranges, and formats to ensure accuracy and consistency of entered data |
| Default value | A pre-set value assigned to a column to streamline data entry when no value is provided |
| View | A customized, simplified perspective of data, often combining multiple tables, used to simplify complex queries or reporting |
| Concurrency control | Mechanisms that manage multiple users' simultaneous access to and modification of a database to prevent inconsistency and conflicts |
| Data type | A property assigned to a column that defines what kind of data it can store and validates data entered into it |
| Varchar | Variable character — a data type that stores character strings of varying length up to a specified maximum |
| Char | A fixed-length character data type that pads values with spaces to always use the specified number of characters |
| DATE | A data type storing a calendar date (year, month, day) |
| TIME | A data type storing a time of day |
| DATETIME / TIMESTAMP | A data type storing a combined date and time value |
| Float | An approximate, floating-point numeric data type used when exact precision isn't required |
| Decimal | An exact numeric data type used for precise arithmetic, such as financial calculations |
| Integer (INT, SMALLINT) | Data types that store whole numbers, each with its own supported range |
| Binary / BLOB | Binary Large Object — a data type that stores non-textual data (e.g., images, files) as a sequence of bytes |
| Set | A collection of unique elements without a specified order |
| Relation | A mathematical concept, based on sets, describing connections between elements |
| Binary relation | A relation establishing a connection between two elements |
| Ordered pair | A subset of the Cartesian product of two sets, representing a binary relation |
| Reflexivity | A relation property where each element relates to itself |
| Symmetry | A relation property where A relating to B implies B relates to A |
| Transitivity | A relation property where A relating to B and B relating to C implies A relates to C |
| Anti-symmetry | A relation property where A relating to B and B relating to A implies A equals B |
| Relation schema | The structure of a relation — its name and the name/type of each attribute |
| Relation instance | The actual data (rows and columns) stored for a relation |
| Tuple | A row in a relation instance |
| Degree | The number of attributes (columns) in a relation |
| Cardinality (relational-model sense) | The number of tuples (rows) in a relation |
| CHAR | A data type storing a fixed-length character string |
| VARCHAR | A data type storing a variable-length character string |

---

## ❓ My Questions & Gaps

- [ ] What specifically distinguishes a data warehouse from a data lake within OLAP systems?
- [ ] How does normalization in RDBMS concretely reduce data duplication (need a worked example)?
- [ ] In practice, what criteria decide when to use a non-relational database (e.g., MongoDB) over a relational one?
- [ ] What are the concrete steps to convert an ER diagram into relational tables (beyond entity → table, attribute → column)?
- [ ] What specific structural limitation causes many-to-many relationship problems in the hierarchical model?
- [ ] In practice, how do the three independence types differ when a real schema change is made (e.g., adding an index vs. adding a column)?
- [ ] How does crow's foot notation visually distinguish optional participation (zero-or-many) from mandatory participation (one-or-many)?
- [ ] How is a many-to-many relationship actually implemented in a relational schema (e.g., via a junction/associative table) — not covered in this lesson?
- [ ] Why are attributes typically omitted from relationship-type diagrams, and when would you need to include them?
- [ ] How exactly are relationships (e.g., one-to-many between `Author` and `Book`) implemented at the table level — via foreign keys — since this lesson only covered mapping entities and attributes, not relationships?
- [ ] What is the difference between a primary key and other unique identifiers, and when would a table need a composite primary key?
- [ ] How do views interact with concurrency control — do they reflect live data changes, or a snapshot at query time?
- [ ] What are the practical differences between DATETIME and TIMESTAMP across database systems (e.g., time zone handling, range limits)?
- [ ] Does choosing a large VARCHAR max length (e.g., VARCHAR(255) vs VARCHAR(50)) have any real performance or indexing cost even though storage is only used as needed?
- [ ] In practice, when would Float be an acceptable choice over Decimal beyond financial calculations — are there performance tradeoffs?
- [ ] Are there size limits or best practices for storing large files in a BLOB column versus storing a file path/reference instead?
- [ ] How do relation properties (reflexivity, symmetry, transitivity, anti-symmetry) map onto practical database design decisions, or are they purely theoretical foundations?
- [ ] How does the relational model's concept of a "relation" differ in practice from a SQL "table" — are there edge cases where they diverge (e.g., duplicate rows)?
- [ ] Does cardinality in the relational-model sense (row count) ever get confused with cardinality in ER-diagram relationships (one-to-many, etc.)? How should the two uses of the term be distinguished?

---

## 🔗 Resources

- https://www.geeksforgeeks.org/dbms/what-is-data-independence-in-dbms/
- https://www.geeksforgeeks.org/dbms/introduction-of-er-model/
