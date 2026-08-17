function PropertyCard({ property }) {
  return (
    <div>
      <h3>{property.property_name}</h3>

      <p>{property.location}</p>

      <p>
        {property.bhk ? `${property.bhk} BHK` : "BHK not specified"}
        {" · "}
        {property.size_sqft
          ? `${property.size_sqft} sqft`
          : "Size not specified"}
      </p>

      <p>
        {property.price_total_inr
          ? `₹${property.price_total_inr.toLocaleString("en-IN")}`
          : "Price not specified"}
      </p>

      <small>Property ID: {property.property_id}</small>
    </div>
  )
}

export default PropertyCard