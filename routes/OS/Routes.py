from flask import Blueprint, jsonify
from api.OS import Linux

os_routes = Blueprint('os', __name__)


@os_routes.route('/get/distribution')
def get_distribution():
    return jsonify(Linux.__get_distribution())


@os_routes.route('/get/distribution/name')
def get_distribution_name():
    return jsonify(Linux.get_os_distribution_name())


@os_routes.route('/get/distribution/version')
def get_distribution_version():
    return jsonify(Linux.get_os_distribution_version())


@os_routes.route('/get/kernel')
def get_kernel():
    return jsonify(Linux.get_kernel_version())


