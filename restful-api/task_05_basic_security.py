#!/usr/bin/python3
'''Basic security'''

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, verify_jwt_in_request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


auth = HTTPBasicAuth()


jwt = JWTManager(app)


users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("admin_password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username


@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.expired_token_loader
def expired_token_response(callback):
    return jsonify({"error": "Token has expired"}), 401


@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({"error": "Invalid token"}), 401


@jwt.revoked_token_loader
def revoked_token_response(callback):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def fresh_token_required_response(callback):
    return jsonify({"error": "Fresh token required"}), 401


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    verify_jwt_in_request()
    current_user = get_jwt_identity()
    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run(debug=True)
