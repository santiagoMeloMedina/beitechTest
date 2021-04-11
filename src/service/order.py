
import repository.order as OrderRepo
import repository.product as ProductRepo
from flask import request
import constant.values as VALUES
import constant.messages as MESSAGES
from model.order import Order
from model.orderDetail import OrderDetail
from model.product import Product
from datetime import datetime

def createOrder():
    result = { "order": None, "details": [] }
    body = dict(request.get_json())

    #Mapping all units to products
    units_map = {}
    for product in body["products"]:
        units_map[product["id"]] = product["units"]
    
    #Getting all eligible for customer products and the total of units they amount
    products = [Product(**product) for product in ProductRepo.getEligibleProductsForCustomer(**body)]
    considered_units = set([product.getId() for product in products])
    total_units = sum([product["units"] if product["id"] in considered_units else 0 for product in body["products"]])

    if total_units <= VALUES.MAX_ORDER_UNITS and total_units > 0:
        total_price = sum([product.getPrice()*units_map[product.getId()] for product in products])
        create = OrderRepo.createOrder(body["customer_id"], products, body["delivery_address"], total_price)
        rows, order_id = create["rows"], create["lastid"]
        if rows > 0:
            order = Order(**OrderRepo.getOrder(order_id))
            for product in products:
                create = OrderRepo.createOrderDetail(order.getId(), product.getId(), product.getProductDescription(), product.getPrice(), units_map[product.getId()])
                rows, order_detail_id = create["rows"], create["lastid"]
                if rows > 0:
                    result["details"].append(OrderDetail(order_detail_id, order_id, product.getId(), units_map[product.getId()]).__dict__)
            result["order"] = order.__dict__
    else:
        raise Exception(MESSAGES.ABOVE_MAX_UNIT(total_units))
    return result

def listOrders():
    result = []
    args = dict(request.args)

    #Tranform date into MYSQL readable format
    parseDate = lambda val: datetime.strptime(val, "%d/%m/%Y").date()
    startDate, endDate = parseDate(args["from"]), parseDate(args["to"])
    
    orders = [ Order(**order) for order in OrderRepo.getCustomerOrdersOnDateRange(args["customer_id"], str(startDate), str(endDate))]
    for order in orders:
        order_details = [ OrderDetail(**detail) for detail in OrderRepo.getOrderDetails(order.getId())]
        order_products = []
        for detail in order_details:
            product = Product(**ProductRepo.getProduct(detail.getProductId()))
            order_products.append((product, detail.getQuantity()))

        #Organizing data to deliver resposne
        order_data = { 
            "creation_date": order.getCreationDate(), 
            "order_id": order.getId(), 
            "total": order.getTotal(), 
            "delivery_address": order.getDeliveryAddress(), 
            "products": [ { "name": product.getName(), "units": units } for product, units in order_products ]
        }
        result.append(order_data)
    return result
