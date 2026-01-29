from flask import Flask, jsonify
app = Flask(__name__)
users = {"1": {"name": "Alice", "email": "alice@example.com"}, "2": {"name": "Bob", "email": "bob@example.com"}}
@app.route('/users/<user_id>')
def get_user(user_id):
    user = users.get(user_id)
    return jsonify(user) if user else (jsonify({"error": "Not found"}), 404)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
