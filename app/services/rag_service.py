from app.services.context_builder import ContextBuilder
from app.services.llm_service import LLMService
from app.services.property_retriever import PropertyRetriever


class RAGService:

    def __init__(
        self,
        retriever: PropertyRetriever,
        llm: LLMService,
    ):

        self.retriever = retriever
        self.llm = llm
        self.context_builder = ContextBuilder()

    def answer(self, query: str, n_results: int = 5):

        properties = self.retriever.search(
            query=query,
            n_results=n_results
        )

        context = self.context_builder.build(properties)

        prompt = f"""
You are HomeLens, an AI real estate search assistant.

Answer the user's question using ONLY the property information
provided in the context below.

Do not invent property details.
If the available properties do not contain enough information
to answer something, say so.

User Query:
{query}

Property Context:
{context}

Rank the provided properties based on how well they match the user's request.

Identify the strongest match first and briefly explain why it is the best match.
You may mention other relevant properties if useful.

Do not claim that a property has a feature unless that feature appears in the provided context.

Provide a concise and useful answer.
"""

        return self.llm.generate(prompt)