import flask
from config import server, requests

app = flask.Flask(__name__)
app.config["DEBUG"] = server["DEBUG"]


@app.route('/', methods=['GET'])
def root():
    return '''<h1> <3 </h1>'''


app.run(host=server["HOST"], port=server["PORT"])
