# app.py

import os
from flask import Flask, jsonify
from flask_cors import CORS
from Services import MidtransService, GraphhopperService

app = Flask(__name__)
CORS(app)
api_key = os.getenv("GRAPHHOPPER_API_KEY")
midtrans_server_key = os.getenv("MIDTRANS_SERVER_KEY")

midtrans_service = MidtransService(midtrans_server_key)
graphhopper_service = GraphhopperService(api_key)

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
    order_id = "order-id-928301928391"
    amount = 10000
    response_data, status_code = midtrans_service.create_transaction(order_id, amount)
    return jsonify(response_data), status_code


@app.route('/shipping-cost', methods=['GET'])
def get_shipping_cost():
    points = "example_points"
    response_data = graphhopper_service.get_shipping_cost(points)
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
