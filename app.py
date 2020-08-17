#!/home/maxim/projects/FAPIenv/bin/python
from flask import Flask, jsonify, make_response
from models import User
import json

app = Flask(__name__)


@app.route('/get_users', methods=['GET'])
def get_users():
    return jsonify({'users': User.get_users()})


@app.route('/get_user_by_id/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.get_user_by_id(user_id)
    if user:
        return jsonify({'user': user})
    abort(404)


@app.route('/create_user', methods=['POST'])
def create_user(user_id, name):
    pass


# @app.route('/delete_user', methods=['DELETE'])
# def delete_user():
#     pass


@app.route('/change_user', methods=['PUT'])
def delete_user(user_id):
    pass


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
