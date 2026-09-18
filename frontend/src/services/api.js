const API_BASE_URL = "https://homelens-backend-884492552799.asia-south1.run.app"

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
