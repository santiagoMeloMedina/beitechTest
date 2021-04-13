
from flask import Flask
from configuration.blueprint import registerBlueprints
from configuration.swagger import route as swaggerRoute

app = Flask(__name__, static_folder='static')
registerBlueprints(app)

## Registering swagger doc endpoint
app.register_blueprint(swaggerRoute)