
from configuration.app import app
from flask import jsonify, send_from_directory
import constant.values as VALUES
import constant.connection as CONN

@app.route("/", methods=['GET'])
def home():
    return jsonify(VALUES.RESPONSE)

@app.route("/<path:filename>", methods=['GET'])
def send_file(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(debug=False, port=CONN.PORT)