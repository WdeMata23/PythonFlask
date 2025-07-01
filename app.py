from flask import Flask, jsonify

app = Flask(__name__)

from productos import productos


@app.route("/ping")
def ping():
    return jsonify({"message": "prueba"})


@app.route("/productos")
def getProductos():
    return jsonify({"productos": productos, "message": "lista de productos"})


if __name__ == "__main__":
    app.run(debug=True, port=3000)
