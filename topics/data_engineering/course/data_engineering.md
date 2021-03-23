# Data Engineering
## Overview
Enables data driven decision-making by collecting, profiling, storing, transforming, and visualizing data.

Data Engineering comprises all engineering and operational tasks required to make data available for the end-user, whether for the purposes of analytics, model building, app development, etc.
Take raw data, do work to it, and deliver a clean dataset to whoever needs it.

DS Hierarchy of needs:
1. Collect,
2. Move/store,
3. explore/transform,
4. aggregate/label,
5. learn/optimize


 Move Store: reliable data flow, infrastrucure, pipelines, etl, storage,
Explore/Transform: cleaning anomaly detection, and prep.
in some ways, a blend of a data scientist and a software engineer.
core role: data warehouses, data lakes, and data pipelines

Activities include but not limited to:
- Data Acquisition
- Data Profiling
  - How many rows?
  - How are entites related?
  - Distribution of values?
- Data Cleansing
- Data Transformation
- Data Loading
- Metadata Management (data about data)
  - Technical
    - Where is coming from?
    - Who is updating it?
    - How frequently is updated?
  - Business
    - Is it sensitive?

#### Common activities:
- ingest dataset
- build and maintain warehouse
- create a data pipeline, create an analytics
- debug data quality issues, optimize queries, design databases
- they do some amount of analytics and thus occasionally perform aggregations, but not their main focus
- airflow: status of pipelines
- look at metrics
- build  pipeline, presto or spark
- most of the day is spent writing code
- try not to get too lost in tools.
- focus on a couple of big names. airflow, redshift, spark, presto
- tooling isn't standardized. better to be deep in a couple of important tools rather than broad across many tools

Databases: A database is a structured repository or collection of data that is stored and retrieved electronically for use in applications. Data can be stored, updated, or deleted from a database.

Database Management System (DBMS): The software used to access the database by the user and application is the database management system. Check out these few links describing a DBMS in more detail.

Data model - an abstraction that organizes elements of data and how they will relate to each other.
data modeling can easily translate to databae modeling, as this is the essential end state. To be sure it is persisted and easily used.
Difference between business and user applications


### Standardizing inconsistencies. E.g.,

Plan, design, implement, test, and operationalize.
It's a process or a methodology.
How to handle NULL values?
Not just ETL (Extract, Transform, Load)

## Responsibilities
- Accuracy, security, availablility
- Compliance (Country, industry)
- Hybrid Locations (On-Prem, Cloud)
- Localization, Provenance

## Scope
- Data is ubiquitous and the world's most valuable resource
- Variety
  - Text, Stream, A/V
  - Meta, Big Relational
  - Schema (SQL, NoSQL)
  - Object Storage


### Factors
 - Volume: Total size of dataset
 - Velocity: Rate at which data is received for processing (Batch vs. Real-time streams)
 - Variety: Structured, Unstructured, and Semi-Structured
 - Data Access Patterns: Frequency of reads and writes
 - Security: Is access restricted to complete or partial file

Ingestion

 ### Process
 -  mainly about aggregation, standardization and Cleansing
 - remove/replace values that do not belong to the columns
 - migrate data from OLTP to OLAP

 ## Storage
 Three broad considerations:
 - Data access Patterns
 - Data access Control
 - Lifecycle (don't want to keep it indefintely, may want to archive it.)

 ### Analyze

 ## Explore
 - Reports
 - Dashboards
 - Data storytelling

 <!-- # Ingestion
 - -->

 ## Data Categories:
- Structured: fixed schema - relational dataset
- Semi-structured: Flexible schema: XML, JSON
- Unstructured: No schema -  video, audio

***

### Data Modeling
process to support business and user applications
1. gather requirements
2. conceptual data Modeling (create an ERD)
3. logical data modeling (mapping conceptual data model to physical data model)
4. physical data Modeling (Write DDL)

### Why data Modeling
- organization is important
- organized data determines later use
- begin prior to building out application, business logic, and analytics processes
- Iterative process
- Important for everyone who deals with data

Data engineering focuses on creating the physical data model in relational and nonrelational databases

## Relational Model
- Organizes data into one or more tables (or "relations") of columns and rows with a unique key identying each row.
- Generally each table represents one "entity" type such as *customer* or *product*
- Develoed at IBM by Edgar Codd in 1970
- a software system used to maintain relational databases is a realtional database management system (RDBMS)
- SQL is the language used across almost all relational database systems
Common type (roughly in order of enterprise management):
 - Oracle: banking, etc
 - Teradata
 - MySql: used for dev or for extremely simple tasks

### Advantages of Relational Database
- Ease of use: SQL
- Ability to do JOINS
- Ability to do aggregations and analytics
- Smaller data volumes
- Easy to change business requirements on data
- Flexibility for queries
- Modeling the data not modeling not the queries
- Secondary indexes available
- ACID transactions: strong data integrity. the proprerties of database transactions intended to guarantee validity even in the event of errors or power failures, etc.
  - Atomicity: the whole transaction is processed, or nothing is processed
  - Consistency: only transactions that abide by constraints and rules is written to the db, otherise dab keeps previous state
  - Isolation: transaction sare processed independently and securely, order does not matter. rows will lock until transaction is complete
  - Durability: completed transactions are saved even in case of system failure.  Once it has been *committed*, it will remain comitted. Effects are recorded in memory.

### When Not to Use a realational DB
- Have large amounts of data. they are not distributed. can only scale vertically
need to be able to store diferent types of data formats
need high thoughput -- fast reads and fast writes
need flexible schemas - nov every column has to be used by every row, can save disk space
need high availability. HA means very little or no donwtime.  when an RDB fails, it needs to fail over to a backup system, which can take time.
need horizontal scalability. ability to add more servers to the system. Many traditional relational databases cannot do otherise

### What is postgreSQL
- Open source object-relational database system
- Has its own syntax (all RDBs have their own syntax and operations)

***

## NoSQL databases

### What is a NoSQL Database?
- simpler design
- simpler horizontal scaling
- finer control of availabbility
- data structures are different
- some operations are faster


### Common Types of NoSQL Databases
- Apache Cassandra (Partition Row store)
- MongoDB (Document store)
- DynamoDB (Key-value store)
- Apache HBase (Wide Column Store)
- Neo4J (Graph database -- nodes and edges)

### The Basics of Apache Cassandra
- Keyspace: collection of tables
- Partition:
  - funametnal unit of access
  - collection of rows
  - how data are distributed
- Primary Key
  - made up of a partition key and clustering columns
- Columns
  - Cluster and Data
  - Labeled element

### Good Use Cases:
- Transaction logging (retail, health care)
- Internet of Things (IoT)
- Time series data
- Any workload that is heavy on writes to the database (since Apache Cassandra is optimized for writes).
- Large amounts of data
- Need for horizontal scaling
- Need high throughput fast reads and writes
- Need a flexible schema
- Need high availability
- Need to be able to store different data type formats
- Users are distributed geographically -- low latency

### When not to use
- Need ACID transactions.
  - caveat: MongoDB has added multi-document ACID transactions within a single replica set and in a sharded/partitioned deployment.
- Need ability to do joins. NoSQL does not allow the ability to do JOINS. This will result in full table scans, which is highly frowned on.
- Ability to do aggregations and analytics (possible with Spark, etc.)
- Queries are not available in advance and need to have flexibility.  Ad-hoc queries are possible but difficult as the data model was done to fix particular queries
- Have small dataset


Relational is great for joins and aggregations, but NoSQL is better when you have large amounts of data for which you need high availability or if you need to scale out quickly.
