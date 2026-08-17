import PropertyCard from "./PropertyCard"

function PropertyResults({ properties }) {
  return (
    <div>
      {properties.map((property) => (
        <PropertyCard
          key={property.property_id}
          property={property}
        />
      ))}
    </div>
  )
}

export default PropertyResults