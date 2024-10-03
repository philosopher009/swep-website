from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage for demo purposes
users = []

@app.route('/')
def home():
    return render_template('index.html')

import re  # Import regex module


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    print("Received signup data:", data)  # Debugging line
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Username, email, and password are required!'}), 400

    # Check if the username already exists
    if any(user['username'] == username for user in users):
        return jsonify({'error': 'Username already exists!'}), 400

    # Store the user credentials (hash password in a real app)
    users.append({'username': username, 'email': email, 'password': password})
    return jsonify({'message': 'Signup successful!'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    print("Received login data:", data)  # Debugging line
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required!'}), 400

    # Check if the user exists and the password matches
    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({'message': 'You have successfully logged in!'}), 200

    return jsonify({'error': 'Invalid username or password!'}), 401

if __name__ == '__main__':
    app.run(debug=True)
