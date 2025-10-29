from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory dictionary to store users
users = {}

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'error': 'Missing username or email'}), 400

    users[username] = {'email': email}
    return jsonify({'message': f'User {username} added successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify({username: user})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
