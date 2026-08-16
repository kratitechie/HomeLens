# 🏡 HomeLens

HomeLens is an AI-powered Real Estate Search Assistant built from scratch using modern backend and AI engineering practices.

The project is being developed incrementally, starting with structured property ingestion and database persistence, and progressing toward semantic retrieval, Retrieval-Augmented Generation (RAG), and a React-based user interface.

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
- Sentence Transformers
- ChromaDB Vector Storage
- Semantic Similarity Search
- PostgreSQL + ChromaDB Retrieval
- FastAPI REST API
- Search Service Layer
- RAG Pipeline
- Gemini LLM Integration
- Context Construction
- Grounded Natural-Language Property Recommendations

---

## Tech Stack

### Backend

- Python 3.11+
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0
- Pydantic
- Pandas
- python-dotenv

### AI / Retrieval

- Sentence Transformers
- `all-MiniLM-L6-v2`
- ChromaDB
- Gemini API
- Retrieval-Augmented Generation (RAG)

### Frontend

- React *(planned)*

---

## Current Architecture

### Data Ingestion

CSV
→ CSV Loader
→ Pydantic Schema
→ Property Mapper
→ Repository
→ PostgreSQL

### Semantic Retrieval

User Query
→ Embedding Service
→ ChromaDB
→ Relevant Property IDs
→ PostgreSQL
→ Complete Property Records

### RAG Pipeline

User Query
→ FastAPI
→ Search / RAG Service
→ Semantic Retrieval
→ ChromaDB
→ PostgreSQL
→ Context Builder
→ Gemini
→ Natural-Language Response

PostgreSQL remains the source of truth for property data, while ChromaDB acts as the semantic retrieval index.

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

# Sprint 6 - FastAPI Retrieval API

### Completed

- Added FastAPI application.
- Added `/health` endpoint.
- Added `POST /search` endpoint.
- Added Pydantic request and response schemas.
- Added `SearchService` to orchestrate semantic search.
- Connected semantic retrieval to HTTP requests.
- Maintained separation between API, service, repository, and retrieval layers.
- Tested configurable result counts using `n_results`.
- Successfully exposed PostgreSQL + ChromaDB retrieval through a REST API.

### API Architecture

Client
→ FastAPI
→ SearchService
→ PropertyRetriever
→ ChromaDB
→ PostgreSQL
→ JSON Response

---

# Sprint 7 - Retrieval-Augmented Generation

### Completed

- Added Gemini LLM integration using the Google GenAI SDK.
- Created dedicated `LLMService`.
- Added `ContextBuilder` for converting retrieved property records into LLM-readable context.
- Implemented `RAGService`.
- Combined semantic retrieval with LLM generation.
- Added grounded prompting to prevent unsupported property claims.
- Added `AskService` to orchestrate the RAG workflow.
- Added `POST /ask` endpoint.
- Added `AskResponse` schema.
- Successfully tested end-to-end RAG through FastAPI.

### RAG Architecture

User Query
→ FastAPI
→ AskService
→ RAGService
→ PropertyRetriever
→ ChromaDB
→ PostgreSQL
→ ContextBuilder
→ Gemini
→ Natural-Language Answer

### RAG Mental Model

Retrieval finds candidate properties.

The LLM receives those retrieved properties as context and generates a grounded response based on the available information.

### Example

Query:

> "luxury villa with jacuzzi and home theatre"

HomeLens retrieves candidate properties and uses the available property context to identify the strongest match.

The system correctly identifies the CAT Road / Treasure Fantasy property (`HL-011`) because its listing explicitly contains both a jacuzzi and home theatre.

---

# Project Status

✅ Sprint 1 - Project Setup

✅ Sprint 2 - CSV Processing & Validation

✅ Sprint 3 - PostgreSQL + SQLAlchemy ORM

✅ Sprint 4 - Repository Layer & Layered Architecture

✅ Sprint 5 - Embeddings & Semantic Retrieval

✅ Sprint 6 - FastAPI Retrieval API

✅ Sprint 7 - RAG Pipeline

⬜ Sprint 8 - React Frontend

⬜ Sprint 9 - Docker & Deployment

⬜ Future - Multimodal Real Estate Search

---

# Upcoming

## Sprint 8 - React Frontend

- React application
- Real estate search interface
- Connect React to FastAPI
- Natural-language search
- Display property recommendations
- Loading and error states
- API integration

## Sprint 9 - Docker & Deployment

- Dockerize backend
- Containerize frontend
- Production configuration
- Deployment
- Environment management

## Future - Multimodal Search

- Property image understanding
- Image + text search
- Multimodal embeddings
- Visual property discovery
- Production rollout