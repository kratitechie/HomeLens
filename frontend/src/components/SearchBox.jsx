import { useState } from "react"
import { askHomeLens } from "../services/api"
import PropertyResults from "./PropertyResults"

function SearchBox() {

  const [query, setQuery] = useState("")
  const [answer, setAnswer] = useState("")
  const [properties, setProperties] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  async function handleSearch() {

    if (!query.trim()) {
      return
    }

    setLoading(true)
    setError("")

    try {
      const data = await askHomeLens(query)

      console.log("API DATA:", data)

      setAnswer(data.answer)
      setProperties(data.properties)

    } catch (error) {

      console.error("HomeLens error:", error)

      setError(
        "Something went wrong while searching. Please try again."
      )

    } finally {

      setLoading(false)

    }
  }

  return (
    <div>

      <input
        type="text"
        value={query}
        placeholder="What kind of property are you looking for?"
        onChange={(event) => setQuery(event.target.value)}
      />

      <button
        onClick={handleSearch}
        disabled={loading}
      >
        {loading ? "Searching..." : "Search"}
      </button>

      <p>You are searching for: {query}</p>

      {loading && (
        <p>HomeLens is finding the best properties...</p>
      )}

      {error && (
        <p>{error}</p>
      )}

      {answer && !loading && (
        <p>{answer}</p>
      )}

      {!loading && properties.length > 0 && (
        <PropertyResults properties={properties} />
      )}

    </div>
  )
}

export default SearchBox