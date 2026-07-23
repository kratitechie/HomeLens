# HomeLens 🏡

An AI-powered Real Estate Search Assistant built to learn production-grade AI engineering concepts from scratch.

---

## Project Goal

HomeLens is a portfolio project focused on learning and implementing:

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Vector Databases
- Retrieval-Augmented Generation (RAG)
- LLM Integration
- Production-ready Backend Architecture

The long-term goal is to allow users to search properties using natural language queries powered by AI.

Example:

> "Show me a furnished 3 BHK under ₹80 lakhs near Vijay Nagar."

---

## Tech Stack

### Backend

- Python
- FastAPI *(Upcoming)*
- SQLAlchemy
- PostgreSQL

### AI

- Sentence Transformers *(Upcoming)*
- ChromaDB *(Upcoming)*
- Ollama / Llama 3 *(Upcoming)*

### Data

- Pandas
- Pydantic

---

## Project Structure

```
HomeLens/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── embeddings/
│   ├── ingestion/
│   ├── models/
│   ├── rag/
│   ├── services/
│   └── utils/
│
├── data/
├── tests/
├── .env
├── .gitignore
└── README.md
```

---

## Progress

### Sprint 1 ✅

- Project setup
- Folder structure
- Git repository initialized

### Sprint 2 ✅

- CSV ingestion
- Data cleaning
- Pandas DataFrame loading
- Property validation using Pydantic

### Sprint 3 (In Progress)

Completed:

- PostgreSQL 17 installation
- Database creation (`homelens`)
- Virtual environment setup
- SQLAlchemy installation
- psycopg2 installation
- python-dotenv configuration
- Environment variable management
- SQLAlchemy Engine configuration
- Python ↔ PostgreSQL connection established

Upcoming:

- SQLAlchemy ORM models
- Table creation
- Insert property records
- Query data
- CSV → PostgreSQL synchronization

---

## Learning Objectives

This project is being built from scratch to understand:

- Backend Architecture
- Database Design
- ORM Concepts
- AI Search Systems
- Retrieval-Augmented Generation
- Production Deployment

The focus is on understanding engineering concepts instead of simply using libraries.

---

## Status

🚧 Sprint 3 in Progress