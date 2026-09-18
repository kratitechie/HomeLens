# 🏡 HomeLens

### Find the right property.

> An AI-powered real estate search engine that understands what you're looking for in natural language.

HomeLens is a full-stack AI real estate search application built with **FastAPI, PostgreSQL, ChromaDB, Sentence Transformers, Gemini, and React**.

Instead of relying only on keyword matching, HomeLens uses **semantic search + Retrieval-Augmented Generation (RAG)** to retrieve relevant properties and generate grounded recommendations.

---

## 🚀 Live Demo

**Frontend:**  
https://homelens-frontend-884492552799.asia-south1.run.app

**Backend API:**  
https://homelens-backend-884492552799.asia-south1.run.app

**API Documentation:**  
https://homelens-backend-884492552799.asia-south1.run.app/docs

---

# ✨ How It Works

A user can search naturally:

> "Luxury villa with jacuzzi and home theatre"

HomeLens processes the request through:

```text
User Query
    ↓
React Frontend
    ↓
FastAPI
    ↓
Semantic Retrieval
    ↓
ChromaDB
    ↓
Relevant Property IDs
    ↓
PostgreSQL
    ↓
Complete Property Records
    ↓
Context Builder
    ↓
Gemini
    ↓
Grounded AI Recommendation
```

The LLM does not act as the property database. It receives retrieved property information and generates a recommendation based on that context.

---

# 🧠 System Architecture

```text
                    ┌─────────────────────┐
                    │   React + Vite      │
                    │      Frontend       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       FastAPI       │
                    │       Backend       │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
             ┌─────────────┐       ┌─────────────┐
             │  Search /   │       │     RAG     │
             │ Ask Service │       │   Service   │
             └──────┬──────┘       └──────┬──────┘
                    │                     │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │  Property Retriever │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │    ChromaDB     │        │   PostgreSQL    │
        │ Semantic Search │        │  Source of Truth│
        └─────────────────┘        └────────┬────────┘
                                           │
                                           ▼
                                  ┌─────────────────┐
                                  │ Context Builder │
                                  └────────┬────────┘
                                           │
                                           ▼
                                  ┌─────────────────┐
                                  │   Gemini LLM    │
                                  └────────┬────────┘
                                           │
                                           ▼
                                  AI Recommendation
```

---

# 🔎 Semantic Search

HomeLens uses:

```text
all-MiniLM-L6-v2
```

to generate **384-dimensional embeddings**.

```text
Property Search Text
        ↓
Sentence Transformer
        ↓
384-Dimensional Embedding
        ↓
ChromaDB
```

When a user searches:

```text
"large luxury house with entertainment features"
```

the system can retrieve properties containing concepts such as:

```text
4 BHK Villa
Home Theatre
Jacuzzi
Garden
```

even when the exact wording differs.

---

# 🤖 RAG Pipeline

HomeLens combines semantic retrieval with Gemini through a Retrieval-Augmented Generation pipeline.

```text
User Query
    ↓
Query Embedding
    ↓
ChromaDB Similarity Search
    ↓
Relevant Property IDs
    ↓
PostgreSQL Lookup
    ↓
Property Context
    ↓
Gemini
    ↓
Grounded Recommendation
```

### Example

**Query**

```text
Luxury villa with jacuzzi and home theatre
```

**Retrieved Property**

```text
HL-011
CAT Road / Treasure Fantasy

4 BHK Villa
4,800 sqft
₹7 Crore

Features:
- Jacuzzi
- Home theatre
- Garden
```

Gemini can explain why this property matches because the relevant features are present in the retrieved context.

The system is designed to reduce unsupported property claims by grounding generation in retrieved data.

---

# 🏗️ Architecture Principles

### PostgreSQL = Source of Truth

PostgreSQL stores the authoritative property records:

```text
Property ID
Property Name
Location
BHK
Area
Price
Property Type
Furnishing
Property Details
```

### ChromaDB = Semantic Retrieval Index

```text
PostgreSQL
    ↓
Authoritative Property Data

ChromaDB
    ↓
Semantic Retrieval Index
```

The vector database is not treated as the primary property database.

### Retrieval Before Generation

```text
Retrieve
   ↓
Build Context
   ↓
Generate
```

The LLM is one component of the application rather than the application itself.

---

# 📥 Data Ingestion

Property data is ingested from structured CSV data.

```text
CSV
 ↓
CSV Loader
 ↓
Pandas Cleaning
 ↓
Pydantic Validation
 ↓
Property Mapper
 ↓
Repository
 ↓
PostgreSQL
```

The ingestion pipeline includes:

- Data cleaning
- Validation
- Normalization
- Pydantic schemas
- Property mapping
- Repository-based persistence
- PostgreSQL storage

---

# ⚡ API

### Health Check

```http
GET /health
```

### Semantic Search

```http
POST /search
```

Example:

```json
{
  "query": "furnished 3 BHK in South Tukoganj",
  "n_results": 5
}
```

### AI Property Search

```http
POST /ask
```

Example:

```json
{
  "query": "luxury villa with jacuzzi and home theatre",
  "n_results": 5
}
```

Swagger documentation:

https://homelens-backend-884492552799.asia-south1.run.app/docs

---

# ⚛️ Frontend

The HomeLens frontend is built with React and Vite and provides a SaaS-style AI search experience.

It includes:

- Natural-language property search
- Search suggestions
- Loading states
- Error handling
- AI recommendations
- Property result cards
- FastAPI integration
- Responsive UI

```text
User
 ↓
React Search Interface
 ↓
POST /ask
 ↓
FastAPI
 ↓
RAG Pipeline
 ↓
Gemini
 ↓
JSON Response
 ↓
React
 ↓
AI Recommendation + Property Cards
```

---

# ☁️ GCP Deployment

HomeLens is containerized with Docker and deployed on **Google Cloud Platform**.

```text
                         GitHub
                            │
                            ▼
                      Cloud Build
                            │
                            ▼
                   Artifact Registry
                      ┌─────┴─────┐
                      ▼           ▼
               Backend Image   Frontend Image
                      │           │
                      ▼           ▼
                 Cloud Run     Cloud Run
                      │           │
                      ▼           ▼
                  FastAPI       React/Nginx
                      │
                      ▼
                  Cloud SQL
                 PostgreSQL
```

### Production Infrastructure

| Service | Purpose |
|---|---|
| Cloud Run | Backend + Frontend hosting |
| Cloud SQL | Managed PostgreSQL |
| Artifact Registry | Docker image storage |
| Cloud Build | CI/CD builds |
| GitHub | Source control |

The local development environment uses PostgreSQL through Docker Compose, while production uses **Google Cloud SQL for PostgreSQL**.

---

# 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Pandas

### AI / Retrieval

- Sentence Transformers
- `all-MiniLM-L6-v2`
- ChromaDB
- Google Gemini
- Retrieval-Augmented Generation (RAG)

### Frontend

- React
- Vite
- JavaScript
- CSS
- Nginx

### DevOps / Cloud

- Docker
- Docker Compose
- Google Cloud Run
- Google Cloud SQL
- Google Artifact Registry
- Google Cloud Build
- GitHub

---

# 🧩 Engineering Patterns

HomeLens uses a layered architecture to keep responsibilities separated.

```text
API Layer
    ↓
Service Layer
    ↓
Retrieval / Repository Layer
    ↓
Database / Vector Store
```

### Repository Pattern

```text
Service
   ↓
Repository
   ↓
PostgreSQL
```

Database operations are isolated from business logic.

### Mapper Pattern

```text
Pydantic Schema
      ↓
Property Mapper
      ↓
SQLAlchemy Model
```

### Separation of Responsibilities

| Component | Responsibility |
|---|---|
| React | UI and interaction |
| FastAPI | API boundary |
| Services | Application orchestration |
| Property Retriever | Semantic retrieval |
| Repository | Database operations |
| PostgreSQL | Source of truth |
| ChromaDB | Vector retrieval |
| Context Builder | LLM context |
| LLM Service | Gemini communication |

---

# 📂 Project Structure

```text
HomeLens/
│
├── app/
│   ├── api/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── ingestion/
│   └── main.py
│
├── data/
│
├── frontend/
│   └── src/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🏁 V1 Status

## HomeLens V1 — Complete 🚀

```text
Data Ingestion          ✅
PostgreSQL              ✅
SQLAlchemy              ✅
Repository Pattern      ✅
Embeddings              ✅
ChromaDB                ✅
Semantic Search         ✅
FastAPI                 ✅
RAG                     ✅
Gemini                  ✅
React                   ✅
Docker                  ✅
GCP Deployment          ✅
Cloud SQL               ✅
Cloud Run               ✅
Cloud Build             ✅
```

The V1 objective was to build a complete AI application end-to-end:

```text
Structured Data
      ↓
PostgreSQL
      ↓
Embeddings
      ↓
ChromaDB
      ↓
Semantic Retrieval
      ↓
RAG
      ↓
Gemini
      ↓
FastAPI
      ↓
React
      ↓
AI Property Search
```

---

# 💡 What HomeLens Demonstrates

HomeLens was built to understand the engineering surrounding modern AI applications, not simply how to call an LLM API.

```text
Backend Engineering
        +
Data & Database Engineering
        +
Semantic Retrieval
        +
RAG
        +
LLM Integration
        +
Frontend Engineering
        +
Docker & Cloud Deployment
        =
End-to-End AI Application
```

---

# 👩‍💻 Built By

## Krati Bhatia

AI / Backend Engineer building practical AI systems from the ground up.

**GitHub:** https://github.com/kratitechie

**LinkedIn:** https://www.linkedin.com/in/kratibhatia/

---

<p align="center">

# 🏡 HomeLens

### Find the right property.

**Version 1.0 — Complete 🚀**

*Python · FastAPI · PostgreSQL · ChromaDB · Sentence Transformers · Gemini · React · Docker · GCP*

</p>