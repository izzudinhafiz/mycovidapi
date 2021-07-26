import pandas as pd
import pickle
import os
from datetime import date
from typing import List, Dict, Tuple, Union
from dataset import DataSet
from name_map import data_map


def load_data_from_github() -> DataSet:
    ds = DataSet()

    for name, url in data_map.items():
        df = pd.read_csv(url)
        ds[name] = df

    return ds


class DataReader:
    def __init__(self, path: Union[str, None], dataset: DataSet = None):
        if path is not None:
            self.base_path = path
            dirs = os.listdir(path)
            available_dates: List[date] = []
            for dir in dirs:
                try:
                    available_dates.append(date.fromisoformat(dir))
                except ValueError:
                    pass

            if len(available_dates) == 0:
                raise FileNotFoundError("No available directory with available data")

            available_dates = sorted(available_dates)
            self.current_date = available_dates[-1]

            with open(f"{self.base_path}/{self.current_date.isoformat()}/dataset", "rb") as f:
                self.data: DataSet = pickle.load(f)
        else:
            if dataset is not None:
                self.data = dataset
            else:
                raise ValueError("If path not set, must supply DataSet object")

    def get_cases(self, state_id: str, from_date: str, to_date: str) -> Tuple[List[Dict], int]:
        if state_id is None:
            df = self.data["cases_msia"]
        else:
            main_df = self.data["cases_state"]
            df = main_df.loc[main_df["state"] == state_id]
        return self._get_from_df(df, from_date, to_date).to_dict(orient="records"), 200

    def get_deaths(self, state_id: str, from_date: str, to_date: str) -> Tuple[List[Dict], int]:
        if state_id is None:
            df = self.data["deaths_msia"]
        else:
            main_df = self.data["deaths_state"]
            df = main_df.loc[main_df["state"] == state_id]
        return self._get_from_df(df, from_date, to_date).to_dict(orient="records"), 200

    def get_tests(self, from_date: str, to_date: str) -> Tuple[List[Dict], int]:
        df = self.data["tests_msia"]
        return self._get_from_df(df, from_date, to_date).to_dict(orient="records"), 200

    def get_checkins(self, state_id: str, from_date: str, to_date: str) -> Tuple[List[Dict], int]:
        if state_id is None:
            df = self.data["checkin_msia"]
        else:
            main_df = self.data["checkin_state"]
            df = main_df.loc[main_df["state"] == state_id]
        return self._get_from_df(df, from_date, to_date).to_dict(orient="records"), 200

    def get_healthcares(self, state_id: str, facility: str, from_date: str, to_date: str) -> Tuple[List[Dict], int]:
        if facility == "hospital":
            main_df = self.data["hospital_io"]
        elif facility == "icu":
            main_df = self.data["icu_io"]
        elif facility == "quarantine":
            main_df = self.data["quarantine_io"]
        else:
            return [{}], 400

        if state_id is None:
            df = main_df
        else:
            df = main_df.loc[main_df["state"] == state_id]
        return self._get_from_df(df, from_date, to_date).to_dict(orient="records"), 200

    def get_traces(self, from_date: str, to_date: str) -> Tuple[List[Dict], int]:
        df = self.data["trace_msia"]
        return self._get_from_df(df, from_date, to_date).to_dict(orient="records"), 200

    def get_clusters(self, from_date: str, to_date: str) -> Tuple[List[Dict], int]:
        df = self.data["clusters_msia"]
        return self._get_from_df(df, from_date, to_date).to_dict(orient="records"), 200

    def get_timeseries(self, from_date: str, to_date: str) -> Tuple[List[Dict], int]:
        cases = self.data["cases_msia"]
        deaths = self.data["deaths_msia"]

        df = pd.merge(cases, deaths, left_on="date", right_on="date", how="outer")[["date", "cases_new", "deaths_new"]]
        return self._get_from_df(df, from_date, to_date).to_dict(orient="records"), 200

    @ staticmethod
    def _get_from_df(df: pd.DataFrame, from_date: str, to_date: str) -> pd.DataFrame:
        if from_date is None and to_date is None:
            return df
        elif from_date is not None and to_date is None:
            return df.loc[df["date"] >= from_date]
        elif to_date is not None and from_date is None:
            return df.loc[df["date"] <= to_date]
        else:
            return df.loc[(df["date"] >= from_date) & (df["date"] <= to_date)]


# if __name__ == "__main__":
#     dr = DataReader("githubdata")
#     print(dr.get_timeseries(None, None))
