from flask import Flask
from flask_restful import Resource, Api, reqparse
from datareader import DataReader

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("state_id")
parser.add_argument("from_date")
parser.add_argument("to_date")
parser.add_argument("facility")

data_source = DataReader("githubdata")


class Timeseries(Resource):
    def get(self):
        args = parser.parse_args()
        return data_source.get_timeseries(args.from_date, args.to_date)


class Cases(Resource):
    def get(self):
        args = parser.parse_args()
        return data_source.get_cases(args.state_id, args.from_date, args.to_date)


class Deaths(Resource):
    def get(self):
        args = parser.parse_args()
        return data_source.get_deaths(args.state_id, args.from_date, args.to_date)


class Tests(Resource):
    def get(self):
        args = parser.parse_args()
        return data_source.get_tests(args.from_date, args.to_date)


class Checkins(Resource):
    def get(self):
        args = parser.parse_args()
        return data_source.get_checkins(args.state_id, args.from_date, args.to_date)


class Healthcares(Resource):
    def get(self):
        args = parser.parse_args()
        return data_source.get_healthcares(args.state_id, args.facility, args.from_date, args.to_date)


class Traces(Resource):
    def get(self):
        args = parser.parse_args()
        return data_source.get_traces(args.from_date, args.to_date)


class Clusters(Resource):
    def get(self):
        args = parser.parse_args()
        return data_source.get_clusters(args.from_date, args.to_date)


api.add_resource(Timeseries, "/timeseries")
api.add_resource(Cases, "/cases")
api.add_resource(Deaths, "/deaths")
api.add_resource(Tests, "/tests")
api.add_resource(Checkins, "/checkins")
api.add_resource(Healthcares, "/healthcares")
api.add_resource(Traces, "/traces")
api.add_resource(Clusters, "/clusters")


@app.route("/")
def home():
    return "Covid-19 Malaysia Data API V1. Created by Izzudin Hafiz"
# Add CITF data source


if __name__ == "__main__":
    app.run()
