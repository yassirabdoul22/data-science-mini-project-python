import pandas as pd
from pandas import DataFrame


class DataLoader:
    def __init__(self, input_file: str) -> None:
        self.input_file = input_file

    def load(self) -> pd.DataFrame:
        return pd.read_csv(self.input_file)

    def show_infos(self, df: pd.DataFrame) -> None:
        print("Shape:", df.shape)
        df.info()