from flask import Blueprint, jsonify
from api.Users import User

user_routes = Blueprint('user', __name__)


@user_routes.route('/get')
def get_users():
    return jsonify(User.get_all_users())


@user_routes.route('/get/user/<username>/processes')
def get_user_procs(username):
    return jsonify(User.get_user_procs(username))


@user_routes.route('/get/user/<username>/groups')
def get_user_groups(username):
    return jsonify(User.get_user_groups(username))


@user_routes.route('/get/user/<username>/history')
def get_user_history(username):
    return jsonify(User.get_user_history(username))

