from fastapi import FastAPI

from app.schemas.search import (
    SearchRequest,
    SearchResponse,
    PropertySearchResult,
    AskResponse,
)
from app.services.ask_service import AskService
from app.services.search_service import SearchService


app = FastAPI(
    title="HomeLens API",
    description="AI-powered semantic real estate search API",
    version="1.0.0",
)


search_service = SearchService()
ask_service = AskService()


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "HomeLens API"
    }


@app.post(
    "/search",
    response_model=SearchResponse
)
def search_properties(request: SearchRequest):

    properties = search_service.search(
        query=request.query,
        n_results=request.n_results
    )

    return SearchResponse(
        query=request.query,
        results=[
            PropertySearchResult(
                property_id=property.property_id,
                property_name=property.property_name,
                location=property.location,
                bhk=property.bhk,
                size_sqft=property.size_sqft,
                price_total_inr=property.price_total_inr,
            )
            for property in properties
        ]
    )


@app.post(
    "/ask",
    response_model=AskResponse
)
def ask_home_lens(request: SearchRequest):

    answer = ask_service.answer(
        query=request.query,
        n_results=request.n_results
    )

    return AskResponse(
        query=request.query,
        answer=answer
    )