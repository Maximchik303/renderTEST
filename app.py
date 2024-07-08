from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)
users = []

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    if name and password:
        users.append({'name': name, 'password': password})
        return jsonify({'message': 'User added successfully!'}), 201
    else:
        return jsonify({'error': 'Name and password are required!'}), 400

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
