
from controller.order import route as OrderController

def registerBlueprints(app):
    app.register_blueprint(OrderController)