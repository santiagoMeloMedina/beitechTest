
from repository.order import createOrder
from util.test import ANY

any_data = ANY()

def test_create_order():
    response = createOrder(1, [], "Calle 20 #20-20", 500.0)
    expected_response = {'rows': 1, 'lastid': any_data}
    assert expected_response == response