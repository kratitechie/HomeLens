from pathlib import Path

from app.ingestion.csv_loader import CSVLoader


def main():

    csv_path = Path("data/homelens_properties_cleaned_v2.csv")

    loader = CSVLoader(csv_path)

    dataframe = loader.load()

    print(dataframe.head())

    print()

    print(f"Loaded {len(dataframe)} properties.")


if __name__ == "__main__":
    main()