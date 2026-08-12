from app.services.embedding_service import EmbeddingService
from app.vectorstore.chroma_store import ChromaStore
from app.repositories.property_repository import PropertyRepository


class PropertyRetriever:

    def __init__(self, repository: PropertyRepository):

        self.repository = repository

        self.embedding_service = EmbeddingService(
            "all-MiniLM-L6-v2"
        )

        self.vector_store = ChromaStore()

    def search(self, query: str, n_results: int = 3):

        query_embedding = self.embedding_service.embed_text(query)

        results = self.vector_store.search(
            query_embedding,
            n_results=n_results
        )

        property_ids = results["ids"][0]

        properties = self.repository.get_by_property_ids(
            property_ids
        )

        return properties