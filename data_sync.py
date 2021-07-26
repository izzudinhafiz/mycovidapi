import pandas as pd
from name_map import data_map
from dataset import DataSet
from datetime import date
import os
from shutil import rmtree
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Base path to folder to save the data")

if __name__ == "__main__":
    args = parser.parse_args()

    base_path = args.path
    today = date.today()
    data_path = f"{base_path}/{today.isoformat()}"

    if os.path.exists(data_path):
        rmtree(data_path)

    os.mkdir(data_path)

    ds = DataSet()

    for name, url in data_map.items():
        df = pd.read_csv(url)
        df.to_csv(f"{data_path}/{name}.csv")
        if "date" in df.index:
            df = df.set_index("date")

        ds[name] = df

    with open(f"{data_path}/dataset", "wb") as f:
        pickle.dump(ds, f)
