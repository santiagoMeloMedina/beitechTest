
from flask import Flask
from configuration.blueprint import registerBlueprints

app = Flask(__name__)
registerBlueprints(app)