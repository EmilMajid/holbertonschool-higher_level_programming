from flask import Flask, jsonify, request

app = Flask(__name__)

# Predefined users for testing consistency
users = {
    "john": {"name": "John Doe", "age": 30}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    return "OK"

@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    global users
    data = request.get_json()

    if not isinstance(data, dict) or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "name": data.get("name", ""),
        "age": data.get("age", 0)
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == '__main__':
    app.run(debug=False)
