from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Property(Base):
    __tablename__ = "properties"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    property_id: Mapped[str] = mapped_column(unique=True, nullable=False)

    property_type_raw: Mapped[str]

    location: Mapped[str]

    details: Mapped[str | None]

    property_name: Mapped[str | None]

    bhk_raw: Mapped[str | None]

    bhk: Mapped[int | None]

    size_raw: Mapped[str | None]

    size_sqft: Mapped[float | None]

    price_raw: Mapped[str | None]

    price_per_sqft_inr: Mapped[float | None]

    price_total_inr: Mapped[float | None]

    price_total_source: Mapped[str | None]

    currency: Mapped[str | None]

    furnishing_raw: Mapped[str | None]

    furnishing: Mapped[str | None]

    miscellaneous_details: Mapped[str | None]

    on_website: Mapped[bool | None]

    search_text: Mapped[str]