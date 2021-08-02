from flask import Flask
from flask_restful import Resource, Api, reqparse, marshal_with, abort, marshal
import sqlalchemy as db
from sqlalchemy import func
from datetime import date
from sqlalchemy.orm import sessionmaker
from database.db_model import *
from common.name_map import state_map
from os import getenv
import responses
from typing import List, Dict, Optional


app = Flask(__name__)
app.config["RESTFUL_JSON"] = {
    "indent": 2,
}
if getenv("FLASK_DEBUG"):
    app.config["DEBUG"] = False

api = Api(app)
engine = db.create_engine("sqlite:///moh_data.sqlite")
Session = sessionmaker(bind=engine)


parser = reqparse.RequestParser()
state_parser = reqparse.RequestParser()
healthcare_parser = reqparse.RequestParser()

parser.add_argument("from_date", type=lambda x: date.fromisoformat(x))
parser.add_argument("to_date", type=lambda x: date.fromisoformat(x))
state_parser.add_argument("state_id", choices=state_map.keys(), required=True)
healthcare_parser.add_argument("facility", choices=["hospital", "icu", "quarantine"], required=True)


def standard_query(location):
    output = []

    args = parser.parse_args()
    from_date = args.from_date
    to_date = args.to_date

    with Session() as s:
        if location == "state":
            source = State
            state_args = state_parser.parse_args()
            state_id = state_map[state_args.state_id]

            if not state_id:
                abort(400)

            q = s.query(source)
            q = q.filter(source.state == state_id)
        elif location == "country":
            source = Nation
            q = s.query(source)
        else:
            abort(404)

        if from_date:
            q = q.filter(source.date >= from_date)

        if to_date:
            q = q.filter(source.date <= to_date)

        for row in q:
            output.append(row.as_dict())

    return output


def get_states_aggregate(session, model, from_date: Optional[date] = None,
                         to_date: Optional[date] = None, ignore_keys=["date", "state"]) -> List[Dict[str, int]]:

    columns = model.__table__.c
    agg_func = []
    for column in columns:
        if column.key not in ignore_keys:
            agg_func.append(func.sum(column).label(column.name))

    agg_func = tuple(agg_func)

    q = session.query(model.date, *agg_func).group_by(model.date)

    if from_date:
        q = q.filter(model.date >= from_date)

    if to_date:
        q = q.filter(model.date <= to_date)

    out = []

    for row in q.all():
        out.append(row._asdict())

    return out


class Cases(Resource):
    def get(self, location):
        output = standard_query(location)
        if location == "country":
            return marshal(output, responses.cases_country)
        else:
            return marshal(output, responses.cases_state)


class Deaths(Resource):
    @marshal_with(responses.deaths)
    def get(self, location):
        return standard_query(location)


class VaxRegistration(Resource):
    @marshal_with(responses.vax_registration)
    def get(self, location):
        return standard_query(location)


class Vaccination(Resource):
    @marshal_with(responses.vaccination)
    def get(self, location):
        return standard_query(location)


class Tests(Resource):
    @marshal_with(responses.tests)
    def get(self):
        return standard_query("country")


class Checkins(Resource):
    @marshal_with(responses.checkins)
    def get(self, location):
        return standard_query(location)


class Traces(Resource):
    @marshal_with(responses.traces)
    def get(self):
        return standard_query("country")


class Healthcares(Resource):
    def get(self, location, facility):
        output = []

        args = parser.parse_args()
        from_date = args.from_date
        to_date = args.to_date

        if facility not in ["hospital", "icu", "quarantine"]:
            abort(404)

        with Session() as s:
            if location == "state":
                source = State
                state_args = state_parser.parse_args()
                state_id = state_map[state_args.state_id]

                if not state_id:
                    abort(400)

                q = s.query(source)
                q = q.filter(source.state == state_id)

                if from_date:
                    q = q.filter(source.date >= from_date)

                if to_date:
                    q = q.filter(source.date <= to_date)

                for row in q:
                    if facility == "hospital":
                        row = row.facility_hospital
                    elif facility == "icu":
                        row = row.facility_icu
                    else:
                        row = row.facility_quarantine

                    if row is not None:
                        output.append(row.as_dict())

            elif location == "country":
                if facility == "hospital":
                    output = get_states_aggregate(s, Hospital, from_date, to_date)
                elif facility == "icu":
                    output = get_states_aggregate(s, ICU, from_date, to_date)
                else:
                    output = get_states_aggregate(s, Quarantine, from_date, to_date)
            else:
                abort(404)

        if facility == "hospital":
            return marshal(output, responses.hospital)
        elif facility == "icu":
            return marshal(output, responses.icu)
        elif facility == "quarantine":
            return marshal(output, responses.quarantine)


class TimeseriesEndpoint(Resource):
    @marshal_with(responses.timeseries)
    def get(self):
        output = []

        args = parser.parse_args()
        from_date = args.from_date
        to_date = args.to_date

        with Session() as s:

            source = Timeseries
            q = s.query(source)

            if from_date:
                q = q.filter(source.date >= from_date)

            if to_date:
                q = q.filter(source.date <= to_date)

            for row in q:
                output.append(row.as_dict())

        return output
