# Sprint 03 - PostgreSQL + SQLAlchemy ORM

## Goal

Store validated property data inside PostgreSQL instead of keeping it only in Python memory.

---

# Before Sprint 3

```
CSV
 ↓
Pandas
 ↓
Pydantic
 ↓
Python Memory
```

Problem:

Everything disappears when Python exits.

---

# After Sprint 3

```
CSV
 ↓
Pandas
 ↓
Cleaning
 ↓
Pydantic
 ↓
SQLAlchemy ORM
 ↓
PostgreSQL
```

Now data is permanently stored.

---

# Files Created

## app/database/database.py

Purpose

- Database connection
- Engine
- Base
- Session Factory

---

## app/database/session.py

Purpose

Creates database sessions.

---

## app/database/init_db.py

Purpose

Creates tables inside PostgreSQL.

---

## app/models/property.py

Purpose

Database model.

Maps Python objects to database rows.

---

## app/schemas/property.py

Purpose

Validation.

Checks incoming data before inserting.

---

## app/ingestion/db_loader.py

Purpose

Stores validated properties inside PostgreSQL.

---

# New Concepts Learned

- PostgreSQL
- SQLAlchemy
- ORM
- Engine
- Session
- Base
- DeclarativeBase
- Mapped
- mapped_column
- Primary Key
- Unique Constraint

---

# Biggest Lesson

Pydantic validates.

SQLAlchemy stores.

These are two completely different responsibilities.

---

# Interview Questions

### What is ORM?

Object Relational Mapping.

Maps Python Objects to Database Tables.

---

### Difference between Pydantic and SQLAlchemy?

Pydantic validates data.

SQLAlchemy interacts with the database.

---

### Why use PostgreSQL?

Reliable relational database used in production.

---

### Why use an integer primary key?

Small

Fast

Stable

Efficient joins

---

# Architecture

```
CSV

↓

Pandas

↓

Cleaning

↓

Pydantic

↓

SQLAlchemy

↓

PostgreSQL
```

---

# Git Commit

```
feat: implement PostgreSQL persistence with SQLAlchemy ORM
```

---

# Next Sprint

Repository Pattern

Service Layer

Database Queries

# PostgreSQL

## Beginner

A database stores information permanently.

Instead of

```
properties = []
```

which disappears,

PostgreSQL saves data even after the program closes.

---

## Intermediate

PostgreSQL is a Relational Database Management System (RDBMS).

It stores data in tables.

Example

| id | property |
|----|----------|
|1|Sky Heights|

---

## Advanced

Supports

- Transactions
- ACID
- Indexes
- Foreign Keys
- Views
- Stored Procedures
- Extensions

---

## Used By

Instagram

Discord

Reddit

OpenAI

---

## Commands

```sql
SELECT * FROM properties;

INSERT INTO properties ...

UPDATE properties ...

DELETE FROM properties ...
```

---

## Interview

Why PostgreSQL over SQLite?

SQLite

Single file

Good for local apps.

PostgreSQL

Production

Concurrent users

Networking

Indexes

Security

# SQLAlchemy

## Beginner

SQLAlchemy lets Python talk to PostgreSQL.

Instead of writing SQL,

you write Python.

---

## Example

Instead of

```sql
INSERT INTO properties ...
```

you write

```python
Property(...)
```

---

## Internal Flow

Python Object

↓

SQLAlchemy

↓

SQL Query

↓

PostgreSQL

---

## Components

Engine

↓

Session

↓

ORM Model

↓

Database

---

## Common Classes

Engine

Session

DeclarativeBase

Mapped

mapped_column

---

## Interview

Why use SQLAlchemy?

Cleaner code

Reusable

Database independent

Less SQL

Supports ORM


# SQLAlchemy Cheat Sheet

## Create Table

```python
Base.metadata.create_all(engine)
```

---

## Create Session

```python
session = SessionLocal()
```

---

## Insert

```python
session.add(obj)
session.commit()
```

---

## Query

```python
session.query(Property).all()
```

(SQLAlchemy 1.x)

---

```python
from sqlalchemy import select

stmt = select(Property)

session.execute(stmt).scalars().all()
```

(SQLAlchemy 2.0)

---

## Rollback

```python
session.rollback()
```

---

## Close

```python
session.close()
```