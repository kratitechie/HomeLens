from typing import Optional

from pydantic import BaseModel


class Property(BaseModel):
    property_id: str

    property_type_raw: str

    location: str

    details: Optional[str] = None

    property_name: Optional[str] = None

    bhk_raw: Optional[str] = None

    bhk: Optional[int] = None

    size_raw: Optional[str] = None

    size_sqft: Optional[float] = None

    price_raw: Optional[str] = None

    price_per_sqft_inr: Optional[float] = None

    price_total_inr: Optional[float] = None

    price_total_source: Optional[str] = None

    currency: Optional[str] = None

    furnishing_raw: Optional[str] = None

    furnishing: Optional[str] = None

    miscellaneous_details: Optional[str] = None

    on_website: Optional[bool] = None

    search_text: str