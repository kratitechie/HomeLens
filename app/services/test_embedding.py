from app.services.embedding_service import EmbeddingService


def main():

    embedding_service = EmbeddingService("all-MiniLM-L6-v2")

    text = "3 BHK furnished apartment in South Tukoganj"

    vector = embedding_service.embed_text(text)

    print("Embedding generated!")
    print("Vector dimensions:", len(vector))
    print("First 5 values:", vector[:5])


if __name__ == "__main__":
    main()