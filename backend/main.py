import json
from flask import Flask, request
from flask_cors import CORS
from flask.json import jsonify
from cliente.models.cliente import Cliente

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
def crear():
    body = request.get_json()
    if("nit" in body and "nombre" in body and "usuario" in  body and "clave" in body and "direccion" in body and "email" in body):
        if(body["nit"] != "" and body["nombre"] != "" and body["usuario"] != "" and body["clave"] != "" and body["direccion"] != "" and body["email"] != ""):
            cliente = Cliente(body["nit"], body["nombre"],body["usuario"],body["clave"],body["direccion"],body["email"])
            if(gestor.agregar_cliente(cliente)):
                return{'msg': "Cliente creado existosamente"}, 201 #created
            else:
                return{'msg': 'El NIT ya se encuentra registrado.'}, 406 #not acceptable
        else:
            return{'msg': 'Los campos deben tener contenido.'}, 400 #bad request
    else:
        return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},400 #bad request
 


@app.route('/obtenerClientes', methods=['GET'])
def get_clientes(nit):
    client=gestor.obtener_clientes(nit)
    if (client!=None):
        return jsonify(client),200
    else: 
        return{'msg': 'No se ha encontrado el NIT en el registro'}







'''
@app.route('/crearCliente', methods=['POST'])
def crearCliente():
    json=request.get_json()
    gestor.agregar_cliente(json['nit'],json['nombre'],json['usuario'],json['clave'],json['direccion'],json['email'])
    return jsonify({'ok': True, 'msg':'Cliente agregado con exito'}),201

  


#Cargar archivo
@app.route('/crearClientes', methods=['POST'])
def crearClientes():
    xml = request.get_data().decode('utf-8')
    raiz=ET.XML(xml)
    for clientes in raiz.iter('cliente'):
        nit = clientes.get('nit')
        nombre = clientes.find('nombre').text
        usuario = clientes.find('usuario').text
        clave = clientes.find('clave').text
        direccion = clientes.find('direccion').text
        email = clientes.find('correoElectronico').text
        gestor.agregar_cliente(nit,nombre,usuario,clave,direccion,email)
        return jsonify({'ok':True, 'msg':'Clientes cargados con exito'}),200
'''

#METODOS PARA INSTANCIAS


@app.route('/crearInstancia', methods=['POST'])
def crearInstancia():
    json=request.get_json()
    gestor.crear_instancia(json['id'],json['nombre'],json['idconfig'],json['fecha_inicial'],json['fecha_final'],json['estado'])
    return jsonify({'ok': True, 'msg':'Instancia creada con exito'}),201


@app.route('/obtenerInstancias', methods=['GET']) #-> consultarDatos GET
def crearInstancia():
    json=request.get_json()
    gestor.crear_instancia(json['id'],json['nombre'],json['fecha_inicial'],json['fecha_final'],json['estado'])
    return jsonify({'ok': True, 'msg':'Instancia creada con exito'}),201


if __name__ == '__main__':
    app.run(debug = True)


#---MODIFICAR Y ELIMINAR instancias



# METODOS PARA RECURSOS




# METODOS PARA CATEGORIAS




# METODOS PARA CONFIGURACIONES





#METODOS PARA GENERACION DE FACTURA

