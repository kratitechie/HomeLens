from pathlib import Path

from sqlalchemy.dialects.postgresql import insert

from app.database.session import get_session
from app.ingestion.csv_loader import CSVLoader
from app.ingestion.property_mapper import map_to_model
from app.models.property import Property
from app.schemas.property import Property as PropertySchema


CSV_PATH = Path("data/homelens_properties_cleaned_v2.csv")


def ingest_properties():
    loader = CSVLoader(CSV_PATH)
    dataframe = loader.load()
    dataframe = dataframe.astype(object).where(dataframe.notna(), None)

    db = get_session()

    try:
        properties = []

        for record in dataframe.to_dict(orient="records"):
            schema_property = PropertySchema(**record)
            property_model = map_to_model(schema_property)

            properties.append(
                {
                    column.name: getattr(property_model, column.name)
                    for column in Property.__table__.columns
                    if column.name != "id"
                }
            )

        if not properties:
            print("No properties found to ingest.")
            return

        stmt = insert(Property).values(properties)

        update_columns = {
            column.name: getattr(stmt.excluded, column.name)
            for column in Property.__table__.columns
            if column.name not in {"id", "property_id"}
        }

        stmt = stmt.on_conflict_do_update(
            index_elements=[Property.property_id],
            set_=update_columns,
        )

        db.execute(stmt)
        db.commit()

        print(f"Upserted {len(properties)} properties into PostgreSQL.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    ingest_properties()