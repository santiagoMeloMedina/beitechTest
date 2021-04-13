
from datetime import datetime
import json

# TODO(Santiago): fix for any date

def test_create_order(client):
    data = {
        "customer_id":1,
        "delivery_address": "Calle 40 #20-40",
        "products": [
            {
                "id": 10,
                "units": 1
            },
            {
                "id": 15,
                "units": 2
            }
        ]
    }
    response = client.post("/order/create", data=json.dumps(data), content_type='application/json').get_json()
    expected_response = {
        'details': [
            {
                'order_detail_id': 1, 
                'order_id': 1, 
                'product_id': 10, 
                'quantity': 1
            }, 
            {
                'order_detail_id': 2, 
                'order_id': 1, 
                'product_id': 15, 
                'quantity': 2
            }
        ], 
        'order': {
            'creation_date': datetime.today().date(), 
            'customer_id': 1, 
            'delivery_address': 'Calle 40 #20-40', 
            'order_id': 1, 
            'total': 162000.0
        }
    }
    assert expected_response == response["response"]

def test_create_order_too_many_units(client):
    data = {
        "customer_id":1,
        "delivery_address": "Calle 40 #20-40",
        "products": [
            {
                "id": 10,
                "units": 4
            },
            {
                "id": 15,
                "units": 2
            }
        ]
    }
    response = client.post("/order/create", data=json.dumps(data), content_type='application/json').get_json()
    expected_response = "Products must sum up to 5 or less units, now 6"
    assert expected_response == response["response"]

def test_list_orders(client):
    data = {
        "customer_id": 1,
        "from": datetime.today().date().strftime("%d/%m/%Y"),
        "to": datetime.today().date().strftime("%d/%m/%Y")
    }
    response = client.get("/order/list", query_string=data).get_json()
    expected_response = [
        {
            'creation_date': datetime.today().date(), 
            'order_id': 1, 'total': 162000.0, 
            'delivery_address': 'Calle 40 #20-40', 
            'products': [
                {'name': 'producto j', 'units': 1}, 
                {'name': 'producto z', 'units': 2}
            ]
        }
    ]
    assert expected_response == response["response"]