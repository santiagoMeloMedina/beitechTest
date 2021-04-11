
class Product:
    def __init__(self, product_id, name, product_description, price, **kwargs):
        self.product_id = product_id
        self.name = name
        self.product_description = product_description
        self.price = price

    def getId(self):
        return self.product_id
    
    def getName(self):
        return self.name
    
    def getProductDescription(self):
        return self.product_description
    
    def getPrice(self):
        return self.price