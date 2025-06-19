from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)

# Secret key for JWT token signature
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-this'  # İstehsalatda daha güclü və gizli açar istifadə edin

# Initialize extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users data with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Basic Authentication verify callback
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

# Route protected by Basic Auth
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Login route for JWT token issuance
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Bad username or password"}), 401

    # Create JWT token with user's identity and role embedded
    access_token = create_access_token(identity={"username": username, "role": user['role']})
    return jsonify(access_token=access_token)

# JWT-protected route - any logged in user
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Admin-only route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# Custom error handlers for JWT errors to always return 401 on auth errors
@jwt.unauthorized_loader
def unauthorized_response(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token_response(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_response(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def revoked_token_response(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def needs_fresh_token_response(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# Run app
if __name__ == '__main__':
    app.run(debug=True)
