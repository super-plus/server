from flask import Blueprint, jsonify
from api.Drives import Partitions

drives_routes = Blueprint('drives', __name__)


@drives_routes.route('/get')
def get_drives():
    return jsonify(Partitions.get_all())


@drives_routes.route('/get/<drive>')
def get_drive(drive):
    return jsonify(Partitions.get_drive(drive))
