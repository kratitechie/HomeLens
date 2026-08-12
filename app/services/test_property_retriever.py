from app.database.session import get_session
from app.repositories.property_repository import PropertyRepository
from app.services.property_retriever import PropertyRetriever


def main():

    session = get_session()

    try:
        repository = PropertyRepository(session)

        retriever = PropertyRetriever(repository)

        query = "luxury villa with jacuzzi and home theatre"

        properties = retriever.search(
            query,
            n_results=3
        )

        print("\nRetrieved Properties:\n")

        for property in properties:

            print(f"Property ID: {property.property_id}")
            print(f"Name: {property.property_name}")
            print(f"Location: {property.location}")
            print(f"BHK: {property.bhk}")
            print(f"Price: {property.price_total_inr}")
            print()

    finally:
        session.close()


if __name__ == "__main__":
    main()