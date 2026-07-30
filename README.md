# 🏡 HomeLens

HomeLens is an AI-powered Real Estate Search Assistant built from scratch using modern backend engineering practices.

---

## Current Features

- CSV Property Ingestion
- Data Cleaning with Pandas
- Validation using Pydantic
- PostgreSQL Database
- SQLAlchemy ORM
- Clean Project Structure

---

## Tech Stack

- Python 3.11+
- PostgreSQL
- SQLAlchemy 2.0
- Pydantic
- Pandas
- python-dotenv

---

### Current Architecture

CSV
→ CSV Loader
→ Pydantic Schema
→ Property Mapper
→ Repository
→ PostgreSQL

## Upcoming

- Repository Pattern
- Service Layer
- Embeddings
- ChromaDB
- Semantic Search
- RAG Pipeline
- FastAPI
- Docker Deployment

---

## Project Status

✅ Sprint 1 - Project Setup

✅ Sprint 2 - CSV Processing

✅ Sprint 3 - PostgreSQL + SQLAlchemy ORM

✅ Sprint 4 - Repository Layer

⬜ Sprint 5 - Embeddings

⬜ Sprint 6 - RAG

## Sprint 4 - Repository Pattern

### Completed
- Implemented Repository Pattern for database operations.
- Added PropertyRepository to encapsulate CRUD operations.
- Introduced Mapper Pattern to convert Pydantic schemas into SQLAlchemy models.
- Refactored ingestion pipeline to follow a layered architecture.
- Removed direct database logic from the ingestion layer.
- Successfully ingested 14 real estate listings into PostgreSQL.

