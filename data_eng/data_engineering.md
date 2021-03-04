# Data Engineering
Enables data driven decision making by collecting, profiling, storing, transforming, and visualizing data.
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


Standardizing inconsistencies. E.g.,

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

 # Ingestion
 -

 ## Data Categories:
 - Structured: fixed schema - relational dataset
- Semi-structured: Flexible schema: XML, JSON
- Unstructured: No schema -  video, audio

From Nanodegree

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

common activities:
- ingest dataset
- build and maintain warehouse
- create a data pipeline, create an analytics
debug data quality issues, optimize queries, design databases
they do some amount of analytics and thus occasionally perform aggregations, but
airflow: status of pipelines
look at metrics
build in pipeline, presto or spark
most of the day is spent writing
try not to get too lost in tools.
focus on a couple of big names. airflow, redshift, spark, presto
tooling isnt standardized. better to be deep in a couple of important tools rather than broad across many tools

Databases: A database is a structured repository or collection of data that is stored and retrieved electronically for use in applications. Data can be stored, updated, or deleted from a database.

Database Management System (DBMS): The software used to access the database by the user and application is the database management system. Check out these few links describing a DBMS in more detail.

Data model - an abstraction that organizes elements of data and how they will relate to each other.
data modeling can easily translate to databae modeling, as this is the essential end state. To be sure it is persisted and easily used.
Difference between business and user applications

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
- Easier to change business queries
- Flexibility for queries
- Modeling the data not modeling not the queries
- Secondary indexes available
- ACID transactions: strong data integrity. the proprerties of database transactions intended to guarantee validity even in the event of errors or power failures, etc.
  - Atomicity: the whole transaction is processed, or nothing is processed
  - Consistency: only transactions that abide by constraints and rules is written to the db, otherise dab keeps previous state
  - Isolation: transaction sare processed independently and securely, order does not matter. rows will lock until transaction is complete
  - Durability: completed transactions are saved even in case of system failure.  Once it has been *committed*, it will remain comitted. Effects are recorded in memory.






Data engineering focuses on creating the physical data model in relational and nonrelational databases
