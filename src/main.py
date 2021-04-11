
from configuration.app import app
from flask import jsonify
import constant.values as VALUES

@app.route("/", methods=['GET'])
def home():
    return jsonify(VALUES.RESPONSE)

if __name__ == "__main__":
    app.run(debug=True)