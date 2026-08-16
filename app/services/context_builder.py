class ContextBuilder:

    def build(self, properties):

        context_parts = []

        for property in properties:

            property_text = f"""
Property ID: {property.property_id}
Property Name: {property.property_name}
Location: {property.location}
Property Type: {property.property_type_raw}
BHK: {property.bhk}
Size: {property.size_sqft} sqft
Price: ₹{property.price_total_inr}
Details: {property.details}
Furnishing: {property.furnishing}
Additional Details: {property.miscellaneous_details}
"""

            context_parts.append(property_text.strip())

        return "\n\n---\n\n".join(context_parts)