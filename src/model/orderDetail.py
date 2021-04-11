
class OrderDetail:
    def __init__(self, order_detail_id, order_id, product_id, quantity):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
    
    def getId(self):
        return self.order_detail_id

    def getOrderId(self):
        return self.order_id
    
    def getProductId(self):
        return self.product_id
    
    def getQuantity(self):
        return self.quantity