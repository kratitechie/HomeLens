# 🏡 HomeLens

HomeLens is an AI-powered Real Estate Search Assistant built from scratch using modern backend and AI engineering practices.

The project is being developed incrementally, starting with structured property ingestion and database persistence, and progressing toward semantic retrieval, RAG, and an eventually multimodal real-estate assistant.

---

## Current Features

- CSV Property Ingestion
- Data Cleaning with Pandas
- Data Validation with Pydantic
- PostgreSQL Database
- SQLAlchemy 2.0 ORM
- Repository Pattern
- Mapper Pattern
- Layered Architecture
- Local Text Embeddings
- ChromaDB Vector Storage
- Semantic Similarity Search
- PostgreSQL + ChromaDB Retrieval

---

## Tech Stack

- Python 3.11+
- PostgreSQL
- SQLAlchemy 2.0
- Pydantic
- Pandas
- python-dotenv
- Sentence Transformers
- ChromaDB

---

## Current Architecture

CSV
→ CSV Loader
→ Pydantic Schema
→ Property Mapper
→ Repository
→ PostgreSQL
→ Embedding Service
→ ChromaDB
→ Semantic Retrieval
→ PostgreSQL

PostgreSQL remains the source of truth for property data, while ChromaDB acts as the semantic retrieval index.

---

## Project Status

✅ Sprint 1 - Project Setup

✅ Sprint 2 - CSV Processing & Validation

✅ Sprint 3 - PostgreSQL + SQLAlchemy ORM

✅ Sprint 4 - Repository Layer & Layered Architecture

✅ Sprint 5 - Embeddings & Semantic Retrieval

⬜ Sprint 6 - Retrieval API with FastAPI

⬜ Sprint 7 - RAG Pipeline

⬜ Sprint 8 - Docker & Deployment

⬜ Future - Multimodal Real Estate Search

---

# Sprint 4 - Repository Pattern

### Completed

- Implemented Repository Pattern for database operations.
- Added `PropertyRepository` to encapsulate database access.
- Introduced Mapper Pattern to convert Pydantic schemas into SQLAlchemy models.
- Refactored ingestion pipeline into a layered architecture.
- Removed direct database logic from the ingestion layer.
- Successfully ingested 14 real estate listings into PostgreSQL.

### Architecture

CSV
→ CSV Loader
→ Pydantic Schema
→ Property Mapper
→ Repository
→ PostgreSQL

---

# Sprint 5 - Semantic Retrieval

### Completed

- Added local embedding generation using Sentence Transformers.
- Used `all-MiniLM-L6-v2` to generate 384-dimensional embeddings.
- Added persistent ChromaDB vector storage.
- Implemented vector indexing for property data.
- Added metadata alongside embeddings.
- Implemented semantic similarity search.
- Made vector indexing idempotent using ChromaDB `upsert`.
- Connected ChromaDB retrieval results back to PostgreSQL.
- Implemented retrieval through the Property Repository.
- Successfully tested end-to-end semantic property retrieval.

### Semantic Search Architecture

User Query
→ Embedding Model
→ ChromaDB
→ Relevant Property IDs
→ PostgreSQL
→ Complete Property Records

### Vector Architecture

PostgreSQL
→ Property Search Text
→ Sentence Transformer
→ Embeddings
→ ChromaDB

### Key Design Decision

PostgreSQL is the source of truth.

ChromaDB is used as a semantic retrieval index rather than the primary property database.

---

## Upcoming

### Sprint 6
- FastAPI retrieval endpoint
- Search service
- API response schemas
- Connect semantic retrieval to HTTP requests

### Sprint 7
- RAG pipeline
- LLM integration
- Context construction
- Prompt engineering
- Natural-language property recommendations

### Sprint 8
- Dockerization
- Deployment
- Production configuration

### Future
- Multimodal property search
- Image understanding
- Image + text retrieval
- Production rollout