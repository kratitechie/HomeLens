from app.services.embedding_service import EmbeddingService
from app.vectorstore.chroma_store import ChromaStore


def main():

    embedding_service = EmbeddingService("all-MiniLM-L6-v2")
    vector_store = ChromaStore()

    query = "luxury villa with jacuzzi and home theatre"

    query_embedding = embedding_service.embed_text(query)

    results = vector_store.search(
        query_embedding,
        n_results=3
    )

    print("\nSemantic Search Results:\n")

    for i in range(len(results["ids"][0])):
        print(f"Result {i + 1}")
        print(f"Property ID: {results['ids'][0][i]}")
        print(f"Property: {results['documents'][0][i]}")
        print(f"Distance: {results['distances'][0][i]}")
        print()


if __name__ == "__main__":
    main()