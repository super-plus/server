import flask
from config import server, requests

app = flask.Flask(__name__)
app.config["DEBUG"] = server["DEBUG"]


@app.route('/', methods=['GET'])
def root():
    return '''<h1> <3 </h1>'''


@app.route(requests["GET"] + "drives/all", methods=['GET'])
def get_all_drives():
    from api.Drives import Partitions
    return flask.jsonify(Partitions.all())


@app.route(requests["GET"] + "drives/<drive>", methods=['GET'])
def get_drive(drive):
    from api.Drives import Partitions
    return flask.jsonify(Partitions.get_drive(drive))


@app.route(requests["GET"] + "processor", methods=['GET'])
def get_processor():
    from api.Processors import Processor
    return flask.jsonify(Processor.get_proc_info())


@app.route(requests["GET"] + "processor/name", methods=['GET'])
def get_proc_name():
    from api.Processors import Processor
    return flask.jsonify(Processor.get_proc_name())


@app.route(requests["GET"] + "processors/count", methods=['GET'])
def get_num_proc():
    from api.Processors import Processor
    return flask.jsonify(Processor.get_num_proc())


app.run(host=server["HOST"], port=server["PORT"])
