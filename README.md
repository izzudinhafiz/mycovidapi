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

The API renames some of the fields that was given by MoH to be more consistent and self-descriptive. You can generally base the field name with those in MoH dataset.

Generally for each endpoint:
- For most endpoints, there are `/state/` and `/country/` sub-endpoints
- For endpoints having state data, you need to include `state_id` as below.
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
	
	E.g. `/api/v1/cases/state?state_id=KUL&start_date=2021-01-01&end_date=2021-01-01`

2. How do I get the nationwide new Covid cases for a particular date range?

	E.g. `/api/v1/cases/country?start_date=2021-01-01&end_date=2021-01-01`

3. How do I get all the data for new Covid cases since the start?

	You can omit the `start_date` and `end_date` in the queries

	E.g. (state) `/api/v1/cases/state?state_id=KUL`

	E.g. (nation) `/api/v1/cases/country`

# Local Setup for Development

## Clone the repo locally
`git clone https://github.com/izzudinhafiz/mycovidapi.git`

## Set up a local Python environment
```bash
cd ~/mycovidapi

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Seed the database

```bash
mkdir localdata

python db_sync.py
```

## Start the application
```bash
python app.py
```

## Updating the local data
To manually update local data

```bash
python db_sync.py
```

# Deployment Setup

## Clone the repo locally
`git clone https://github.com/izzudinhafiz/mycovidapi.git`

## Set up a local Python environment
```bash
cd ~/mycovidapi

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
## Seed the database

```bash
mkdir localdata

python db_sync.py
```

## Setup a gunicorn service to serve the app
Use your preferred text editor to create a service file
```bash
sudo nano /etc/systemd/system/mycovidapi.service
```

Create this  systemd Unit file
```
[Unit]
Description=MY Covid API
After=network.target

[Service]
Type=simple
ExecStart= /home/user/mycovidapi/.venv/bin/gunicorn --workers=3 --chdir  /home/user/mycovidapi/ app:app

[Install]
WantedBy=multi-user.target
```

## Setup nginx
Use your preferred text editor to create an nginx site file

```bash
sudo nano /etc/nginx/sites-available/mycovidapi.izzudinhafiz.com
```

Create this file:

```
server {
	server_name mycovidapi.izzudinhafiz.com;
	root /home/user/mycovidapi/;

	location / {
		proxy_pass http://127.0.0.1:8000;
		proxy_set_header Host $host;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	}
}
```

Link it to `sites-enabled` and allow nginx firewall access
```bash
sudo ln -s /etc/nginx/sites-available/mycovidapi.izzudinhafiz.com /etc/nginx/sites-enabled

sudo ufw allow 'Nginx Full'
```

## Start gunicorn and nginx
```bash
sudo systemctl restart nginx
sudo systemctl start mycovidapi.service
```

## Cronjob for daily database update
Create a `daily.sh` script to safely stop the service and perform update and restart service

```bash
#!/bin/bash
systemctl stop mycovidapi.service
/home/user/mycovidapi/.venv/bin/python /home/user/mycovidapi/db_sync.py
systemctl restart mycovidapi.service
```

Run `sudo crontab -e` to create a sudo cronjob to run the script. Example below runs every 6 hours

```bash
0 */6 * * * bash /home/user/mycovidapi/daily.sh >> /home/user/mycovidapi/daily_sync.log 2>&1
```

According to MoH Github page, the data is updated daily by 2359. So if you'd prefer to update the database at midnight instead, modify the cronjob to

```bash
0 0 * * * bash /home/user/mycovidapi/daily.sh >> /home/user/mycovidapi/daily_sync.log 2>&1
```

# Sources

[Open data on COVID-19 in Malaysia](https://github.com/MoH-Malaysia/covid19-public) - [MoH Malaysia](https://github.com/MoH-Malaysia)

# Roadmap
- [ ] Integrate [CITF](https://github.com/CITF-Malaysia/citf-public) data
- [ ] V2 API with consolidated and bucketed data