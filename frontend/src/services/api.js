const API_BASE_URL = "http://127.0.0.1:8000"

export async function askHomeLens(query, nResults = 5) {
  const response = await fetch(`${API_BASE_URL}/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      query,
      n_results: nResults,
    }),
  })

  if (!response.ok) {
    throw new Error("Failed to get a response from HomeLens")
  }

  return response.json()
}