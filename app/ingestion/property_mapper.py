from app.models.property import Property

def map_to_model(schema_property):

    return Property(
        property_id=schema_property.property_id,
        property_type_raw=schema_property.property_type_raw,
        location=schema_property.location,
        details=schema_property.details,
        property_name=schema_property.property_name,
        bhk_raw=schema_property.bhk_raw,
        bhk=schema_property.bhk,
        size_raw=schema_property.size_raw,
        size_sqft=schema_property.size_sqft,
        price_raw=schema_property.price_raw,
        price_per_sqft_inr=schema_property.price_per_sqft_inr,
        price_total_inr=schema_property.price_total_inr,
        price_total_source=schema_property.price_total_source,
        currency=schema_property.currency,
        furnishing_raw=schema_property.furnishing_raw,
        furnishing=schema_property.furnishing,
        miscellaneous_details=schema_property.miscellaneous_details,
        on_website=schema_property.on_website,
        search_text=schema_property.search_text,
    )