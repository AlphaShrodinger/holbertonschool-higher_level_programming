#!/usr/bin/python3
'''Flask'''
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    return 'OK'


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    newuser = request.json
    username = newuser.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400
    if username == users:
        return jsonify({'error': 'User already exists'}), 400
    users[username] = newuser
    return jsonify({'message': 'User added', 'user': newuser}), 201


if __name__ == '__main__':
    app.run()
