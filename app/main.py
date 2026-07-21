from pathlib import Path
from app.models.property import Property
from app.ingestion.csv_loader import CSVLoader


def main():
    csv_path = Path("data/homelens_properties_cleaned_v2.csv")

    loader = CSVLoader(csv_path)
    dataframe = loader.load()
    dataframe = dataframe.where(dataframe.notna(), None)
    
    properties = []
    #print(dataframe.columns.tolist())
    #print(dataframe.head())
    #print()

    for _, row in dataframe.iterrows():

        row_dict = row.to_dict()

        cleaned_row = {
            key: (None if str(value) == "nan" else value)
            for key, value in row_dict.items()
        }

        property_obj = Property(**cleaned_row)

        properties.append(property_obj)

        print(properties[0].model_dump())

    print()

    print(f"Validated {len(properties)} properties.")


if __name__ == "__main__":
    main()
    
