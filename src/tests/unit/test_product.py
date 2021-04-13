
from repository.product import getEligibleProductsForCustomer, getProduct

def test_get_eligible_products():
    products = [
        {"id": 10,"units": 4},
        {"id": 15,"units": 2},
        {"id": 12,"units": 2}
    ]
    response = getEligibleProductsForCustomer(1, products)
    expected_response = [
        {
            'product_id': 10, 
            'name': 'producto j', 
            'product_description': 'descripcion del producto j', 
            'price': 50000.0
        }, 
        {
            'product_id': 15, 
            'name': 'producto z', 
            'product_description': 'descripcion del producto z', 
            'price': 56000.0
        }
    ]
    assert expected_response == response

def test_get_product():
    response = getProduct(10)
    expected_response = {
        'product_id': 10, 
        'name': 'producto j', 
        'product_description': 'descripcion del producto j', 
        'price': 50000.0
    }
    assert expected_response == response