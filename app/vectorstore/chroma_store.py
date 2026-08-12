import chromadb


class ChromaStore:

    def __init__(self, collection_name: str = "properties"):
        self.client = chromadb.PersistentClient(
            path="./data/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_properties(
        self,
        ids: list[str],
        documents: list[str],
        embeddings,
        metadatas: list[dict]
    ):
        self.collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(self, query_embedding, n_results: int = 3):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )