
class Order:
    def __init__(self, order_id, customer_id, 
                creation_date, delivery_address, total, **kwargs):
        self.order_id = order_id
        self.customer_id = customer_id
        self.creation_date = creation_date
        self.delivery_address = delivery_address
        self.total = total
    
    def getId(self):
        return self.order_id
    
    def getCustomerId(self):
        return self.customer_id
    
    def getCreationDate(self):
        return self.creation_date
    
    def getDeliveryDate(self):
        return self.delivery_address
    
    def getTotal(self):
        return self.total