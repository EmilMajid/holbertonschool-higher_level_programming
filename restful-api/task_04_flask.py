from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with an empty user database (as expected by the tests)
users = {}

@app.route('/')
def home():
    """
    Root endpoint.
    Returns a welcome message to confirm the API is working.
    """
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    """
    Status check endpoint.
    Returns a simple "OK" message to indicate the server is running.
    """
    return "OK"

@app.route('/data')
def get_users():
    """
    Returns a list of all usernames currently in the system.
    The result is returned as a JSON array.
    """
    return jsonify(list(users.keys()))

@app.route('/users/<username>')
def get_user(username):
    """
    Retrieves information about a specific user by username.
    
    Args:
        username (str): The username to search for.
    
    Returns:
        JSON object with the user's data if found,
        or an error message with 404 status code.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the in-memory database.
    
    Expects:
        JSON data with the key "username", and optional "name" and "age".
    
    Returns:
        JSON message indicating success with 201 status,
        or error message with 400 status if data is missing or invalid.
    """
    data = request.get_json()
    
    # Ensure the request body is valid JSON and contains a username
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
    """
    Starts the Flask development server on localhost:5000 with debug mode enabled.
    """
    app.run(debug=True)
