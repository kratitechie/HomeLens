import { useState } from "react"
import { askHomeLens } from "../services/api"
import PropertyResults from "./PropertyResults"

function Hero() {

  const [query, setQuery] = useState("")
  const [answer, setAnswer] = useState("")
  const [properties, setProperties] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const suggestions = [
    "Luxury villa with pool",
    "4 BHK under ₹2 crore",
    "Commercial property near Vijay Nagar",
  ]

  async function handleSearch() {

    if (!query.trim()) {
      return
    }

    setLoading(true)
    setError("")
    setAnswer("")
    setProperties([])

    try {

      const data = await askHomeLens(query)

      setAnswer(data.answer)
      setProperties(data.properties)

    } catch (error) {

      console.error("HomeLens search error:", error)

      setError(
        "Something went wrong while searching. Please try again."
      )

    } finally {

      setLoading(false)

    }
  }

  function handleSuggestionClick(suggestion) {
    setQuery(suggestion)
  }

  return (
    <section className="hero">

      <div className="hero-badge">
        ✦ AI-powered property search
      </div>

      <h1>
        Find the right
        <span> property.</span>
      </h1>

      <p>
        An AI-powered real estate search engine that understands
        what you're looking for in natural language.
      </p>

      <div className="hero-search">

        <span className="search-icon">⌕</span>

        <input
          type="text"
          value={query}
          placeholder="Try “4 BHK villa with a garden under ₹2 crore”"
          onChange={(event) => setQuery(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === "Enter") {
              handleSearch()
            }
          }}
        />

        <button
          onClick={handleSearch}
          disabled={loading}
        >
          {loading ? "Searching..." : "Search →"}
        </button>

      </div>

      <div className="examples">

        <span>Try:</span>

        {suggestions.map((suggestion) => (
          <button
            key={suggestion}
            onClick={() => handleSuggestionClick(suggestion)}
          >
            {suggestion}
          </button>
        ))}

      </div>

      {loading && (
        <div className="search-status">
          <span className="status-dot"></span>
          HomeLens is finding the best properties...
        </div>
      )}

      {error && (
        <div className="search-error">
          {error}
        </div>
      )}

      {answer && !loading && (
        <div className="search-results">

          <div className="ai-label">
            ✦ HomeLens recommendation
          </div>

          <p className="ai-answer">
            {answer}
          </p>

          {properties.length > 0 && (
            <PropertyResults properties={properties} />
          )}

        </div>
      )}

    </section>
  )
}

export default Hero