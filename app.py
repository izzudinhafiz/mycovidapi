from flask import render_template
from endpoints import TimeseriesEndpoint, app, api
from endpoints import Cases, Deaths, Tests, Checkins, Healthcares, Traces, VaxRegistration, Vaccination


api.add_resource(Cases, "/api/v1/cases/<location>")
api.add_resource(Deaths, "/api/v1/deaths/<location>")
api.add_resource(Tests, "/api/v1/tests")
api.add_resource(Checkins, "/api/v1/checkins/<location>")
api.add_resource(Healthcares, "/api/v1/healthcares/<location>/<facility>")
api.add_resource(Traces, "/api/v1/traces")
api.add_resource(VaxRegistration, "/api/v1/registration/<location>")
api.add_resource(Vaccination, "/api/v1/vaccination/<location>")
api.add_resource(TimeseriesEndpoint, "/api/v1/timeseries")


@ app.route("/")
def home_route():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
