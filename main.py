from flask import Flask
from flask_restful import Resource, Api, reqparse
from datareader import DataReader, load_data_from_github

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


api.add_resource(Timeseries, "/api/v1/timeseries")
api.add_resource(Cases, "/api/v1/cases")
api.add_resource(Deaths, "/api/v1/deaths")
api.add_resource(Tests, "/api/v1/tests")
api.add_resource(Checkins, "/api/v1/checkins")
api.add_resource(Healthcares, "/api/v1/healthcares")
api.add_resource(Traces, "/api/v1/traces")
api.add_resource(Clusters, "/api/v1/clusters")


@app.route("/")
def home_route():
    return '<h1>Covid-19 Malaysia Data API V1. Created by <a href="https://izzudinhafiz.com">Izzudin Hafiz</a></h1>\
            <p>Documentation on how to use is hosted on <a href="https://documenter.getpostman.com/view/13724658/TzsbKn2w">Postman</a></p>\
            <p>This is an open source project. For source code visit <a href="https://github.com/izzudinhafiz/mycovidapi">Github Repo</a></p>'


if __name__ == "__main__":
    app.run()
