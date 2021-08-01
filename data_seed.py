import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from typing import List, Dict, Optional
import pandas as pd
from datetime import date

from database.dataset import DataSet
from database.db_model import *
from common.name_map import url_map


def load_data_from_github() -> DataSet:
    ds = DataSet()

    for name, url in url_map.items():
        df = pd.read_csv(url)
        ds[name] = df

    return ds


def fix_date_type(df_list: List[Dict], date_label: Optional[List] = None) -> List[Dict]:
    if date_label is None:
        for row in df_list:
            row["date"] = date.fromisoformat(row["date"])
    else:
        for row in df_list:
            for label in date_label:
                row[label] = date.fromisoformat(row[label])

    return df_list


# Renaming Map
cases_msia_rename = {"cluster_import": "cases_import",
                     "cluster_religious": "cases_religious",
                     "cluster_education": "cases_education",
                     "cluster_community": "cases_community",
                     "cluster_highRisk": "cases_highrisk",
                     "cluster_detentionCentre": "cases_detention_centre",
                     "cluster_workplace": "cases_workplace"}

quarantine_io_rename = {"discharge_pui": "discharged_pui",
                        "discharge_covid": "discharged_covid",
                        "discharge_total": "discharged_total"}

tests_msia_rename = {"rtk-ag": "tests_rtk_ag", "pcr": "tests_pcr"}

checkins_rename = {"unique_ind": "checkins_unique_ind", "unique_loc": "checkins_unique_loc"}

traces_rename = {"casual_contacts": "traces_casual", "hide_large": "traces_hide_large", "hide_small": "traces_hide_small"}

raw_data = load_data_from_github()

# Special name wrangling for checkin time labels which are 1, 2, 3 etc.
# This renames them to time_0000, time_0030 etc.
idx = 0
checkin_time_rename = {}
for i in range(24):
    for y in [0, 30]:
        checkin_time_rename[f"{idx}"] = f"time_{i:02d}{y:02d}"
        idx += 1

# Column renaming to match DB Model
raw_data["cases_msia"].rename(columns=cases_msia_rename, inplace=True, errors="raise")          # type: ignore
raw_data["quarantine_io"].rename(columns=quarantine_io_rename, inplace=True, errors="raise")    # type: ignore
raw_data["tests_msia"].rename(columns=tests_msia_rename, inplace=True, errors="raise")          # type: ignore
raw_data["checkin_msia"].rename(columns=checkins_rename, inplace=True, errors="raise")          # type: ignore
raw_data["trace_msia"].rename(columns=traces_rename, inplace=True, errors="raise")              # type: ignore
raw_data["checkin_state"].rename(columns=checkins_rename, inplace=True, errors="raise")         # type: ignore
raw_data["checkin_time"].rename(columns=checkin_time_rename, inplace=True, errors="raise")      # type: ignore
# Fixing misspelled state name
raw_data["checkin_state"]["state"].loc[raw_data["checkin_state"]["state"] == "W.P. KualaLumpur"] = "W.P. Kuala Lumpur"  # type: ignore

# Merging national data
nation_df = pd.merge(raw_data["cases_msia"], raw_data["deaths_msia"], left_on="date", right_on="date", how="outer")
nation_df = pd.merge(nation_df, raw_data["tests_msia"], left_on="date", right_on="date", how="outer")
nation_df = pd.merge(nation_df, raw_data["checkin_msia"], left_on="date", right_on="date", how="outer")
nation_df = pd.merge(nation_df, raw_data["trace_msia"], left_on="date", right_on="date", how="outer")
nation_df.sort_values(by=["date"], inplace=True)

# Merging state data
state_df = pd.merge(raw_data["cases_state"], raw_data["deaths_state"], left_on=["date", "state"], right_on=["date", "state"], how="outer")
state_df = pd.merge(state_df, raw_data["checkin_state"], left_on=["date", "state"], right_on=["date", "state"], how="outer")
state_df.sort_values(by=["date", "state"], inplace=True)

# Converting to dictionary and fixing date type
nation_data = fix_date_type(nation_df.to_dict(orient="records"))
state_data = fix_date_type(state_df.to_dict(orient="records"))
hosp_data = fix_date_type(raw_data["hospital_io"].to_dict(orient="records"))
icu_data = fix_date_type(raw_data["icu_io"].to_dict(orient="records"))
quarantine_data = fix_date_type(raw_data["quarantine_io"].to_dict(orient="records"))
cluster_data = fix_date_type(raw_data["clusters"].to_dict(orient="records"), ["date_announced", "date_last_onset"])
checkin_data = fix_date_type(raw_data["checkin_time"].to_dict(orient="records"))

engine = db.create_engine("sqlite:///moh_data.sqlite")
Session = sessionmaker(bind=engine)
s = Session()
Base.metadata.create_all(engine)

s.bulk_insert_mappings(Nation, nation_data)
s.bulk_insert_mappings(State, state_data)
s.bulk_insert_mappings(Hospital, hosp_data)
s.bulk_insert_mappings(ICU, icu_data)
s.bulk_insert_mappings(Quarantine, quarantine_data)
s.bulk_insert_mappings(Cluster, cluster_data)
s.bulk_insert_mappings(Checkin, checkin_data)
s.commit()
