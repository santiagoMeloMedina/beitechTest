
from flask import Blueprint, jsonify
import constant.routes as ROUTES
import constant.values as VALUES
import service.order as OrderService

route = Blueprint(ROUTES.ORDER, __name__)

@route.route(f"/{ROUTES.ORDER}/create", methods=['POST'])
def createOrder():
    result = VALUES.RESPONSE.copy()
    try:
        result["response"] = OrderService.createOrder()
    except Exception as e:
        result["response"] = str(e)
    return jsonify(result)

@route.route(f"/{ROUTES.ORDER}/list", methods=['GET'])
def listOrders():
    result = VALUES.RESPONSE.copy()
    try:
        result["response"] = OrderService.listOrders()
    except Exception as e:
        result["response"] = str(e)
    return jsonify(result)