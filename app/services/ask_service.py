from app.database.session import get_session
from app.repositories.property_repository import PropertyRepository
from app.services.llm_service import LLMService
from app.services.property_retriever import PropertyRetriever
from app.services.rag_service import RAGService


class AskService:

    def answer(self, query: str, n_results: int = 5):

        session = get_session()

        try:
            repository = PropertyRepository(session)

            retriever = PropertyRetriever(repository)

            llm = LLMService()

            rag_service = RAGService(
                retriever=retriever,
                llm=llm
            )

            return rag_service.answer(
                query=query,
                n_results=n_results
            )

        finally:
            session.close()