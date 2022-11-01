import json
from flask import Flask, request
from flask_cors import CORS
from flask.json import jsonify
from cliente.models.cliente import Cliente
from instancia.models.instancia import Instancia

from gestor import Gestor
from xml.etree import ElementTree as ET

app = Flask(__name__)
CORS(app)

gestor=Gestor()

@app.route('/')
def index():
    return {"msg" : "This api works!"}


#METODOS PARA CLIENTES

@app.route('/crearCliente', methods = ['POST'])
def crearCliente():
    body = request.get_json()
    try:
        if("nit" in body and "nombre" in body and "usuario" in  body and "clave" in body and "direccion" in body and "email" in body):
            cliente = Cliente(body["nit"], body["nombre"],body["usuario"],body["clave"],body["direccion"],body["email"])
            if(gestor.agregar_cliente(cliente)):
                return{'msg': "Cliente creado exitosamente"}, 201 #created
            else:
                return{'msg': 'El NIT ya se encuentra registrado.'}, 406 #not acceptable
        else:
            return{'msg': 'Faltan campos por rellenar'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500
 


@app.route('/consultarDatos/cliente/<nit>', methods=['GET'])
def ver(nit):
    try:
        cliente = gestor.obtener_clientes(nit)
        if (cliente != None):
            return jsonify(cliente.getData()),200
        else:
            return {'msg': 'No se encontró el cliente'}, 404
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500


tree = ET.parse('ArchivoConfig.xml')
root = tree.getroot()

#Cargar archivo
@app.route('/crearClientes', methods=['POST'])
def crearClientes():
    json=request.get_json()
    for client in root.iter('cliente'):
        nit = client.get('nit')
        nombre = client.find('nombre').text
        usuario = client.find('usuario').text
        clave = client.find('clave').text
        direccion = client.find('direccion').text
        email = client.find('correoElectronico').text
        gestor.agregar_cliente(json[nit],json[nombre],json[usuario],json[clave],json[direccion],json[email])
        return jsonify({'ok':True, 'msg':'Clientes cargados con exito'}),200


#METODOS PARA INSTANCIAS

'''
@app.route('/crearInstancia', methods=['POST'])
def crearInstancia():
    json=request.get_json()
    gestor.crear_instancia(json['id'],json['nombre'],json['idconfig'],json['fecha_inicial'],json['fecha_final'],json['estado'])
    return jsonify({'ok': True, 'msg':'Instancia creada con exito'}),201
'''


@app.route('/crearInstancia', methods = ['POST'])
def crearInstancia():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in body and "idconfig" in  body and "fecha_inicial" in body and "fecha_final" in body and "estado" in body):
            instancia = Instancia(body['id'],body['nombre'],body['idconfig'],body['fecha_inicial'],body['fecha_final'],body['estado'])
            if(gestor.crear_instancia(instancia)):
                return{'msg': "Instancia creada exitosamente"}, 201 #created
            else:
                return{'msg': 'La instancia con ese id ya se encuentra registrado.'}, 406 #not acceptable
        else:
            return{'msg': 'Faltan campos por rellenar'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500
 




'''
@app.route('/consultarDatos/instancia', methods=['GET']) #-> consultarDatos GET
def crearInstancia():
    json=request.get_json()
    gestor.crear_instancia(json['id'],json['nombre'],json['fecha_inicial'],json['fecha_final'],json['estado'])
    return jsonify({'ok': True, 'msg':'Instancia creada con exito'}),201
'''

if __name__ == '__main__':
    app.run(debug = True)


#---MODIFICAR Y ELIMINAR instancias






# METODOS PARA RECURSOS




# METODOS PARA CATEGORIAS




# METODOS PARA CONFIGURACIONES





#METODOS PARA GENERACION DE FACTURA

