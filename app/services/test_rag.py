from app.database.session import get_session
from app.repositories.property_repository import PropertyRepository
from app.services.llm_service import LLMService
from app.services.property_retriever import PropertyRetriever
from app.services.rag_service import RAGService


def main():

    session = get_session()

    try:

        repository = PropertyRepository(session)

        retriever = PropertyRetriever(repository)

        llm = LLMService()

        rag = RAGService(
            retriever=retriever,
            llm=llm
        )

        query = "luxury villa with jacuzzi and home theatre"

        answer = rag.answer(
            query=query,
            n_results=5
        )

        print("\nHomeLens Answer:\n")
        print(answer)

    finally:
        session.close()


if __name__ == "__main__":
    main()