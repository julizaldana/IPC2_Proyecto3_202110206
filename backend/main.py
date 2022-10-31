import json
from flask import Flask, request
from flask_cors import CORS
from cliente.routes.cliente_Route import cliente
from flask.json import jsonify

from gestor import Gestor
from xml.etree import ElementTree as ET

app = Flask(__name__)
CORS(app)

gestor=Gestor()

@app.route('/')
def index():
    return {"msg" : "This api works!"}


@app.route('/crearCliente', methods=['POST'])
def crearCliente():
    json=request.get_json()
    gestor.agregar_cliente(json['nit'],json['nombre'],json['usuario'],json['clave'],json['direccion'],json['email'])
    return jsonify({'ok': True, 'msg':'Cliente agregado con exito'}),201


@app.route('/obtenerClientes', methods=['GET'])
def get_clientes():
    c=gestor.obtener_clientes()
    return jsonify(c),200

@app.route('/eliminarCliente', methods=['DELETE'])
def eliminarCliente():
    json=request.get_json()
    gestor.eliminar_cliente(json['nit'],json['nombre'],json['usuario'],json['clave'],json['direccion'],json['email'])
    return jsonify({'ok': True, 'msg':'Cliente eliminado con exito'}),20




if __name__ == '__main__':
    app.run(debug = True)