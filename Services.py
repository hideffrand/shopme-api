from DTOs import ResponseTemplate
import requests
import base64

class MidtransService:
    def __init__(self, midtrans_server_key):
        self.midtrans_server_key = midtrans_server_key

    def create_transaction(self, order_id, amount):
        url = "https://app.sandbox.midtrans.com/snap/v1/transactions"

        payload = {
            "transaction_details": {
                "order_id": order_id,
                "gross_amount": amount
            },
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Basic {base64.b64encode(f'{self.midtrans_server_key}:'.encode()).decode()}"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()
            return ResponseTemplate(response.status_code, 'Transaction created successfully', response_data)

        except requests.exceptions.RequestException as e:
            return ResponseTemplate(500, f'Error creating transaction: {str(e)}')


class GraphhopperService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.graphhopper_url = "https://graphhopper.com/api/1/route"

    def get_shipping_cost(self, points):
        query_params = {
            "profile": "car",
            "point": points,
            # ... other parameters ...
            "key": self.api_key
        }

        response = requests.get(self.graphhopper_url, params=query_params)
        data = response.json()

        status_code = response.status_code
        message = "Shipping cost calculated successfully" if status_code == 200 else "Failed to calculate shipping cost"
        return ResponseTemplate(status_code, message, data)
