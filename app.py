#!/usr/bin/python
from flask import Flask, jsonify, make_response, request, abort
from models import User
import json

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def api_get_users():
    return jsonify({'users': User.get_users()})


@app.route('/users/<int:user_id>', methods=['GET'])
def api_get_user_by_id(user_id):
    user = User.get_user_by_id(user_id)
    if user:
        return jsonify({'user': user[0]})

    abort(404)


@app.route('/create_user', methods=['POST'])
def api_create_user():
    if not request.json or not 'name' in request.json:
        abort(400)

    if 'age' in request.json:
        new_user = User(request.json['name'], request.json['age'])
    else:
        new_user = User(request.json['name'])
    new_user.create_user()
    return jsonify({'result': True})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def api_delete_user(user_id):

    user = User.get_user_by_id(user_id)
    all_users = User.get_users()
    if not user:
        abort(404)

    all_users.remove(user[0])
    User.write_in_file_users(all_users)
    return jsonify({'result': True})


@app.route('/users/<int:user_id>', methods=['PUT'])
def api_update_user(user_id):

    user = User.get_user_by_id(user_id)
    all_users = User.get_users()

    if not user:
        abort(404)
    if not request.json:
        abort(400)

    if 'name' in request.json:
        if type(request.json['name']) != str:
            abort(400)
        all_users[all_users.index(user[0])]['name'] = request.json['name']
        User.write_in_file_users(all_users)

    if 'age' in request.json:
        if type(request.json['age']) != int:
            abort(400)

        all_users[all_users.index(user[0])]['age'] = request.json['age']
        User.write_in_file_users(all_users)

    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    app.run(debug=True)
