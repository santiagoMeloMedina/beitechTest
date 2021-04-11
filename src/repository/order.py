
from configuration.db import db_client

def createOrder(customer_id, products, address, total):
    query = f"""INSERT INTO `order` (customer_id, creation_date, delivery_address, total) 
                values ({customer_id}, NOW(), '{address}', {total})"""
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

def getOrderDetails(order_id):
    query = f"""SELECT * FROM order_detail WHERE order_id = {order_id}"""
    result = db_client.query(query)
    return result

def getCustomerOrdersOnDateRange(customer_id, startDate, endDate):
    query = f"""SELECT * FROM `order` WHERE customer_id = {customer_id} AND creation_date BETWEEN '{startDate}' AND '{endDate}'"""
    result = db_client.query(query)
    return result