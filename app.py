from flask import Flask, jsonify, request

app = Flask(__name__)

from productos import productos


@app.route("/ping")
def ping():
    return jsonify({"message": "error"})


@app.route("/productos")
def getProductos():
    return jsonify({"productos": productos, "message": "lista de productos"})


@app.route("/productos/<string:product_nombre>")
def getProducto(product_nombre):
    productosFound = [
        producto for producto in productos if producto["nombre"] == product_nombre
    ]
    return jsonify({"producto": productosFound[0]})


@app.route("/productos", methods=["POST"])
def agregarproducto():
    nuevo_producto = {
        "nombre": request.json["nombre"],
        "precio": request.json["precio"],
        "cantidad": request.json["cantidad"],
    }
    productos.append(nuevo_producto)
    return "recibido"


@app.route("/productos/<string:product_nombre>", methods=["PUT"])
def actualizarproducto(product_nombre):
    productosFound = [
        producto for producto in productos if producto["nombre"] == product_nombre
    ]
    if len(productosFound) > 0:
        productosFound[0]["nombre"] == request.json["nombre"],
        productosFound[0]["precio"] == request.json["precio"],
        productosFound[0]["cantidad"] == request.json["cantidad"]
        return jsonify(
            {"message": "producto actualizado", "producto": productosFound[0]}
        )
    return jsonify({"message": "producto no encontrado"})


@app.route("/productos/<string:product_nombre>", methods=["DELETE"])
def Eliminarprodu(product_nombre):
    productosFound = [
        producto for producto in productos if producto["nombre"] == product_nombre
    ]
    if len(productosFound) > 0:
        productos.remove(productosFound)
        return jsonify({"message": "producto Eliminado"})
    return jsonify({"message": "producto no encontrado"})


if __name__ == "__main__":
    app.run(debug=True, port=3000)
