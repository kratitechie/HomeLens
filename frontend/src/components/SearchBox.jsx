import { useState } from "react"
import { askHomeLens } from "../services/api"
import PropertyResults from "./PropertyResults"

function SearchBox() {

  const [query, setQuery] = useState("")
  const [answer, setAnswer] = useState("")
  const [properties, setProperties] = useState([])

  async function handleSearch() {
    const data = await askHomeLens(query)

    setAnswer(data.answer)
    console.log("API DATA:", data)
    setProperties(data.properties)
  }

  return (
    <div>
      <input
        type="text"
        value={query}
        placeholder="What kind of property are you looking for?"
        onChange={(event) => setQuery(event.target.value)}
      />

      <button onClick={handleSearch}>
        Search
      </button>

      <p>You are searching for: {query}</p>

      <p>{answer}</p>

      <PropertyResults properties={properties} />
    </div>
  )
}

export default SearchBox