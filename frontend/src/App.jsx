import Header from "./components/Header"
import Hero from "./components/Hero"
import "./App.css"

function App() {
  return (
    <div className="app">

      <Header />

      <main>
        <Hero />

        <section className="trust-section">
          <p>Powered by modern AI retrieval technology</p>

          <div className="tech-stack">
            <span>Semantic Search</span>
            <span>RAG</span>
            <span>AI Reranking</span>
            <span>Natural Language</span>
          </div>
        </section>
      </main>

    </div>
  )
}

export default App