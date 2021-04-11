
import repository.order as OrderRepo
from flask import request
import constant.values as VALUES
import constant.messages as MESSAGES
from model.order import Order
from model.orderDetail import OrderDetail

def createOrder():
    result = { "order": None, "details": [] }
    body = dict(request.get_json())

    #Mapping all units to products
    units_map = {}
    for product in body["products"]:
        units_map[product["id"]] = product["units"]
    
    #Getting all eligible for customer products and the total of units they amount
    products = OrderRepo.getEligibleProductsForCustomer(**body)
    considered_units = set([product.getId() for product in products])
    total_units = sum([product["units"] if product["id"] in considered_units else 0 for product in body["products"]])

    if total_units <= VALUES.MAX_ORDER_UNITS and total_units > 0:
        create = OrderRepo.createOrder(body["customer_id"], products, body["delivery_address"])
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
