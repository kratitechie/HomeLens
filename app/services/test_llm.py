from app.services.llm_service import LLMService


def main():

    llm = LLMService()

    response = llm.generate(
        "Explain semantic search in one sentence."
    )

    print("\nGemini Response:\n")
    print(response)


if __name__ == "__main__":
    main()