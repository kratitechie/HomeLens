from pydantic import BaseModel

from app.services.context_builder import ContextBuilder
from app.services.llm_service import LLMService
from app.services.property_retriever import PropertyRetriever


class RAGResult(BaseModel):
    answer: str
    ranked_property_ids: list[str]


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

        available_ids = [
            property.property_id
            for property in properties
        ]

        prompt = f"""
You are HomeLens, an AI real estate search assistant.

You are given a user's property search query and a set of
candidate properties retrieved through semantic search.

Your job is to:

1. Analyze how well each candidate matches the user's query.
2. Rank ALL candidate properties from strongest match to weakest match.
3. Return every property ID exactly once.
4. Write a concise explanation for the user.

IMPORTANT RULES:

- Use ONLY the property information provided in the context.
- Do not invent property features.
- Do not introduce property IDs that are not present in the context.
- A property should rank higher when its actual features directly
  satisfy the user's requirements.
- Explicit feature matches are more important than vague semantic similarity.
- Return ALL candidate property IDs in ranked_property_ids.

User Query:
{query}

Available Property IDs:
{available_ids}

Property Context:
{context}
"""

        result = self.llm.generate_structured(
            prompt=prompt,
            response_model=RAGResult
        )

        property_map = {
            property.property_id: property
            for property in properties
        }

        ranked_properties = []

        for property_id in result.ranked_property_ids:

            property_obj = property_map.get(property_id)

            if property_obj:
                ranked_properties.append(property_obj)

        # Safety fallback:
        # If Gemini somehow omits a property, append it
        # using the original retrieval order.
        ranked_ids = {
            property.property_id
            for property in ranked_properties
        }

        for property in properties:

            if property.property_id not in ranked_ids:
                ranked_properties.append(property)

        return {
            "answer": result.answer,
            "properties": ranked_properties,
        }