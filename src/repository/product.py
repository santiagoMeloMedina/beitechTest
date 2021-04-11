
from configuration.db import db_client

def getEligibleProductsForCustomer(customer_id, products, **kwargs):
    product_ids = ','.join([f"{product['id']}" for product in products])
    query = f"""SELECT P.* FROM product P INNER JOIN customer_product CP 
                ON (P.product_id = CP.product_id) WHERE CP.customer_id = {customer_id} 
                AND CP.product_id IN ({product_ids})"""
    result = db_client.query(query)
    return result

def getProduct(product_id):
    query = f"""SELECT * FROM product WHERE product_id = {product_id}"""
    result = db_client.query(query)[0]
    return result