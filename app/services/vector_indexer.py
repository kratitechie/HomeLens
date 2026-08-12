from app.services.embedding_service import EmbeddingService
from app.vectorstore.chroma_store import ChromaStore


class VectorIndexer:

    def __init__(self):
        self.embedding_service = EmbeddingService(
            "all-MiniLM-L6-v2"
        )

        self.vector_store = ChromaStore()

    def index_properties(self, properties):

        texts = [property.search_text for property in properties]

        embeddings = self.embedding_service.embed_documents(texts)

        ids = [property.property_id for property in properties]

        metadatas = [
            {
                "property_id": property.property_id,
                "location": property.location,
                "bhk": property.bhk or 0,
            }
            for property in properties
        ]

        self.vector_store.add_properties(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        return len(properties)