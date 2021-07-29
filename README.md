# MYCovidAPI

## Introduction
JSON [API Site](https://mycovidapi.izzudinhafiz.com) for Malaysian Covid statistics hosted at https://mycovidapi.izzudinhafiz.com.

The project builds upon the Covid and MySejahtera dataset by [MoH Malaysia](https://github.com/MoH-Malaysia/covid19-public).

The intent is to allow any developer to easily develop dashboards using the comprehensive data supplied with a JSON friendly interface.

## Documentation
Documentation is hosted on Postman and can be found [here](https://documenter.getpostman.com/view/13724658/TzsbKn2w). There are examples both on Postman and further down this document.

## Overview
The current _V1_ API presents all the raw data from MoH as is with no normalization or bucketing. This is to allow developers full access to the underlying data. 

The API uses [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format dates `YYYY-MM-DD`.

Generally for each endpoint:
- Omitting the `state_id` in the query will return the nationwide data. 
- Omitting both `start_date` and `end_date` will return all the data. 
- Omitting `start_date` will return data from the start of the dataset.
- Omitting `end_date` will return data up to the current date.

The API uses standardized abbreviation for Malaysian state that is based on this [Wikipedia table](https://en.wikipedia.org/wiki/States_and_federal_territories_of_Malaysia#States).

|    State Name     | State Code |
| :---------------: | :--------: |
|       Johor       |    JHR     |
|       Kedah       |    KDH     |
|     Kelantan      |    KTN     |
|      Melaka       |    MLK     |
|  Negeri Sembilan  |    NSN     |
|      Pahang       |    PHG     |
|   Pulau Pinang    |    PNG     |
|       Perak       |    PRK     |
|      Perlis       |    PLS     |
|       Sabah       |    SBH     |
|      Sarawak      |    SWK     |
|     Selangor      |    SGR     |
|    Terengganu     |    TRG     |
| W.P. Kuala Lumpur |    KUL     |
|    W.P. Labuan    |    LBN     |
|  W.P. Putrajaya   |    PJY     |



## Authentication
No authentication is required. Everyone is free to use this API.

## Rate Limit
There is no rate limit currently, however, we expect users to use the API respectfully. We reserve the right to limit API calls if we detect excessive call rate.

Developer should also cache the data as the data is updated only once a day.


# Examples

1. How do I get a state's new Covid cases for a particular date?

	You can use the same start and end date in the API query. 
	
	E.g. `/api/v1/cases?state_id=KUL&start_date=2021-01-01&end_date=2021-01-01`

2. How do I get the nationwide new Covid cases for a particular date range?

	You can omit the `state_id` field to get nationwide data for any of the endpoints

	E.g. `/api/v1/cases?start_date=2021-01-01&end_date=2021-01-01`

3. How do I get all the data for new Covid cases since the start?

	You can omit the `start_date` and `end_date` in the queries

	E.g. (state) `/api/v1/cases?state_id=KUL`

	E.g. (nation) `/api/v1/cases`

# Local Setup

## Clone the repo locally
`git clone https://github.com/izzudinhafiz/mycovidapi.git`

## Set up a local Python environment
```bash
cd ~/mycovidapi

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Run a local data sync

```bash
mkdir localdata

python data_sync.py localdata/
```

## Start the application
```bash
python main.py
```
## Updating the local data
Once a day, you should run the `data_sync.py` to update the local data. The script will automatically download the new data and back up the old dataset.

# Deployment Setup

TODO: nginx setup

TODO: gunicorn systemd service setup

TODO: Auto local data update

# Sources

[Open data on COVID-19 in Malaysia](https://github.com/MoH-Malaysia/covid19-public) - [MoH Malaysia](https://github.com/MoH-Malaysia)

# Roadmap
- [ ] Integrate [CITF](https://github.com/CITF-Malaysia/citf-public) data
- [ ] V2 API with consolidated and bucketed data