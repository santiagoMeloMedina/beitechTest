
from configuration.db import db_client
from model.product import Product

def getEligibleProductsForCustomer(customer_id, products, **kwargs):
    result = []
    product_ids = ','.join([f"{product['id']}" for product in products])
    query = f"""SELECT P.* FROM product P INNER JOIN customer_product CP 
                ON (P.product_id = CP.product_id) WHERE CP.customer_id = {customer_id} 
                AND CP.product_id IN ({product_ids})"""
    for product in db_client.query(query):
        result.append(Product(**product))
    return result

def createOrder(customer_id, products, address):
    total_price = sum([product.getPrice() for product in products])
    query = f"""INSERT INTO `order` (customer_id, creation_date, delivery_address, total) 
                values ({customer_id}, NOW(), '{address}', {total_price})"""
    result = db_client.crud(query)
    return result

def getOrder(order_id):
    query = f"""SELECT * FROM `order` WHERE order_id = {order_id}"""
    result = db_client.query(query)[0]
    return result

def createOrderDetail(order_id, product_id, product_description, price, quantity):
    query = f"""INSERT INTO order_detail (order_id, product_id, product_description, price, 
                quantity) values ({order_id}, {product_id}, '{product_description}', {price}, {quantity})"""
    result = db_client.crud(query)
    return result