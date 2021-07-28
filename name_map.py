base_url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public"
e_url = base_url + "/main/epidemic/"        # Epidemic Files URL
m_url = base_url + "/main/mysejahtera/"     # MySejahtera Files URL

e_files = ["cases_malaysia.csv", "cases_state.csv", "tests_malaysia.csv", "clusters.csv", "deaths_malaysia.csv", "deaths_state.csv", "pkrc.csv", "hospital.csv", "icu.csv"]
m_files = ["checkin_malaysia.csv", "checkin_malaysia_time.csv", "checkin_state.csv", "trace_malaysia.csv"]

data_map = {"cases_msia": e_url + "cases_malaysia.csv",
            "cases_state": e_url + "cases_state.csv",
            "tests_msia": e_url + "tests_malaysia.csv",
            "deaths_msia": e_url + "deaths_malaysia.csv",
            "deaths_state": e_url + "deaths_state.csv",
            "checkin_msia": m_url + "checkin_malaysia.csv",
            "checkin_state": m_url + "checkin_state.csv",
            "trace_msia": m_url + "trace_malaysia.csv",
            "checkin_time": m_url + "checkin_malaysia_time.csv",
            "clusters": e_url + "clusters.csv",
            "quarantine_io": e_url + "pkrc.csv",
            "hospital_io": e_url + "hospital.csv",
            "icu_io": e_url + "icu.csv"}

state_map = {"JHR": "Johor", "KDH": "Kedah", "KTN": "Kelantan", "MLK": "Melaka", "NSN": "Negeri Sembilan", "PHG": "Pahang", "PNG": "Pulau Pinang", "PRK": "Perak", "PLS": "Perlis",
             "SBH": "Sabah", "SWK": "Sarawak", "SGR": "Selangor", "TRG": "Terengganu", "KUL": "W.P. Kuala Lumpur", "LBN": "W.P. Labuan", "PJY": "W.P. Putrajaya", }
