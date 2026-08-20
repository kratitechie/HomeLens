# 🏡 HomeLens

### **Find the right property.**

> An AI-powered real estate search engine that understands what you're looking for in natural language.

HomeLens is a full-stack AI real estate search engine built from scratch using modern backend, retrieval, RAG, and frontend engineering practices.

Instead of relying only on traditional keyword-based filtering, HomeLens combines **semantic search, vector retrieval, PostgreSQL, and Retrieval-Augmented Generation (RAG)** to understand natural-language property requirements and generate grounded property recommendations.

---

## ✨ HomeLens V1

**Version 1.0 — Complete**

HomeLens V1 represents the first complete end-to-end version of the product.

The system can:

- Ingest structured real estate data
- Validate and persist properties in PostgreSQL
- Generate semantic embeddings
- Store and retrieve vectors using ChromaDB
- Perform semantic property search
- Expose retrieval through FastAPI
- Retrieve contextual property information
- Use Gemini to generate grounded recommendations
- Serve the AI search experience through a React frontend

### V1 Product Flow

```mermaid
flowchart LR

    U[👤 User] --> F[⚛️ React Frontend]

    F --> A[⚡ FastAPI]

    A --> R[🔎 Semantic Retrieval]

    R --> C[(ChromaDB)]

    C --> P[(PostgreSQL)]

    P --> CB[📄 Context Builder]

    CB --> L[✨ Gemini LLM]

    L --> RES[🏡 AI Property Recommendations]

    RES --> F