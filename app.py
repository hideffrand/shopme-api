from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake in-memory database
users_db = {
    "user1": {
        'username': 'Coba',
        'password': 'cobapassword'
    }
}

@app.route('/users', methods=['GET'])
def get_users():
    sanitized_users = {user_id: {'username': user['username']} for user_id, user in users_db.items()}
    return jsonify(sanitized_users)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email in users_db:
        return jsonify(message='User already exists'), 400

    users_db[email] = {'email': email, 'password': password}
    print(users_db)
    return jsonify(message='User registered successfully')

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = users_db.get(email)

    if not user or user['password'] != password:
        return jsonify(message='Invalid credentials'), 401

    return jsonify(message=f'{email} logged in successfully')

if __name__ == '__main__':
    app.run(debug=True)
