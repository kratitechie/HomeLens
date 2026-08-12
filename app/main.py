from pathlib import Path
from app.schemas.property import Property
from app.ingestion.csv_loader import CSVLoader
from app.ingestion.property_mapper import map_to_model
from app.repositories.property_repository import PropertyRepository
from app.database.session import get_session


def main():

    csv_path = Path("data/homelens_properties_cleaned_v2.csv")

    loader = CSVLoader(csv_path)

    dataframe = loader.load()

    dataframe = dataframe.where(dataframe.notna(), None)

    sqlalchemy_properties = []

    for _, row in dataframe.iterrows():

        row_dict = row.to_dict()

        cleaned_row = {
            key: (None if str(value) == "nan" else value)
            for key, value in row_dict.items()
        }

        # Step 1: Validate using Pydantic
        schema_property = Property(**cleaned_row)

        # Step 2: Convert to SQLAlchemy model
        db_property = map_to_model(schema_property)

        sqlalchemy_properties.append(db_property)

    session = get_session()

    repository = PropertyRepository(session)

    repository.create_many(sqlalchemy_properties)

    session.close()

    print(f"Saved {len(sqlalchemy_properties)} properties to PostgreSQL.")


if __name__ == "__main__":
    main()