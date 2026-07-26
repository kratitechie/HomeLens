from app.database.session import get_session
from app.models.property import Property


def save_properties(properties):
    session = get_session()

    try:
        for item in properties:

            db_property = Property(
                property_id=item.property_id,
                property_type_raw=item.property_type_raw,
                location=item.location,
                details=item.details,
                property_name=item.property_name,
                bhk_raw=item.bhk_raw,
                bhk=item.bhk,
                size_raw=item.size_raw,
                size_sqft=item.size_sqft,
                price_raw=item.price_raw,
                price_per_sqft_inr=item.price_per_sqft_inr,
                price_total_inr=item.price_total_inr,
                price_total_source=item.price_total_source,
                currency=item.currency,
                furnishing_raw=item.furnishing_raw,
                furnishing=item.furnishing,
                miscellaneous_details=item.miscellaneous_details,
                on_website=item.on_website,
                search_text=item.search_text,
            )

            session.add(db_property)

        session.commit()
        
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()