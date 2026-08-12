from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str):
        return self.model.encode(text)

    def embed_documents(self, texts: list[str]):
        return self.model.encode(texts)