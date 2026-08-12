from app.database.session import get_session
from app.models.property import Property
from app.services.vector_indexer import VectorIndexer


def main():

    session = get_session()

    try:
        properties = session.query(Property).all()

        print(f"Loaded {len(properties)} properties from PostgreSQL.")

        indexer = VectorIndexer()

        indexed_count = indexer.index_properties(properties)

        print(f"Indexed {indexed_count} properties into ChromaDB.")

    finally:
        session.close()


if __name__ == "__main__":
    main()