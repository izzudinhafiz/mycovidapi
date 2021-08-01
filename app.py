from flask import render_template
from main import app, api
from main import Cases, Deaths, Tests, Checkins, Healthcares, Traces


api.add_resource(Cases, "/api/v1/cases/<location>")
api.add_resource(Deaths, "/api/v1/deaths/<location>")
api.add_resource(Tests, "/api/v1/tests")
api.add_resource(Checkins, "/api/v1/checkins/<location>")
api.add_resource(Healthcares, "/api/v1/healthcares/<location>/<facility>")
api.add_resource(Traces, "/api/v1/traces")


@ app.route("/")
def home_route():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
