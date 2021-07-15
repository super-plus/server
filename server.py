import flask
from config import server, api
from routes.OS.Routes import os_routes
from routes.User.Routes import user_routes
from routes.Sensors.Routes import sensors_routes

app = flask.Flask(__name__)
app.config["DEBUG"] = server["DEBUG"]


@app.route('/', methods=['GET'])
def root():
    return '''<h1> <3 </h1>'''


app.register_blueprint(os_routes, url_prefix=api["BASE"] + 'os')
app.register_blueprint(user_routes, url_prefix=api["BASE"] + 'users')
app.register_blueprint(sensors_routes, url_prefix=api["BASE"] + 'sensors')


app.run(host=server["HOST"], port=server["PORT"])
