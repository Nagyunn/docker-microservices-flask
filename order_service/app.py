from flask import Flask, jsonify
import requests

app = Flask(__name__)

orders = {"101": {"user_id": "1", "item": "Laptop"}, "102": {"user_id": "2", "item": "Phone"}}

@app.route('/orders/<order_id>')
def get_order(order_id):
    order = orders.get(order_id)
    if not order: return (jsonify({"error": "Order not found"}), 404)
    
    # Gọi User Service bằng tên service trong docker-compose
    user_info = requests.get(f"http://user-service:5000/users/{order['user_id']}").json()
    
    return jsonify({"order": order, "user": user_info})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
