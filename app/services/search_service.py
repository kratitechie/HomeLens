from app.database.session import get_session
from app.repositories.property_repository import PropertyRepository
from app.services.property_retriever import PropertyRetriever


class SearchService:

    def search(self, query: str, n_results: int = 3):

        session = get_session()

        try:
            repository = PropertyRepository(session)

            retriever = PropertyRetriever(repository)

            return retriever.search(
                query=query,
                n_results=n_results
            )

        finally:
            session.close()