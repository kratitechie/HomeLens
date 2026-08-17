from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str
    n_results: int = 3


class PropertySearchResult(BaseModel):
    property_id: str
    property_name: str | None
    location: str
    bhk: int | None
    size_sqft: float | None
    price_total_inr: float | None


class AskResponse(BaseModel):
    query: str
    answer: str
    properties: list[PropertySearchResult]


class SearchResponse(BaseModel):
    query: str
    results: list[PropertySearchResult]