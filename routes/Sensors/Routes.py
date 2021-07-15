from flask import Blueprint, jsonify
from api.Sensors import Fans, Temperatures

sensors_routes = Blueprint('sensors', __name__)


@sensors_routes.route('/get/fans')
def get_fans():
    return jsonify(Fans.get_fans())


@sensors_routes.route('/get/fan/num')
def get_num_fans():
    return jsonify(Fans.get_num_fans())


@sensors_routes.route('/get/fan/rpm/<fan>')
def get_fan_rpm(fan):
    return jsonify(Fans.get_fan_rpm(fan))


@sensors_routes.route('/get/temps/<fahrenheit>')
def get_temps(fahrenheit):
    return jsonify(Temperatures.get_hw_temps(fahrenheit))

