import pandas as pd


class DataSet:
    def __init__(self):
        self.data = {}

    def __getitem__(self, name: str) -> pd.DataFrame:
        return self.data[name]

    def __setitem__(self, name: str, value: pd.DataFrame):
        self.data[name] = value
