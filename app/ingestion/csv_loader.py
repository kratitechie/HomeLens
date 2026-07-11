from pathlib import Path

import pandas as pd


class CSVLoader:
    """
    Responsible for loading property data from a CSV file.
    """

    def __init__(self, csv_path: Path):
        self.csv_path = csv_path

    def load(self) -> pd.DataFrame:
        """
        Load the property CSV into a pandas DataFrame.
        """

        dataframe = pd.read_csv(self.csv_path)

        return dataframe