from flask import Blueprint, jsonify, request
from gestor import Gestor
from cliente.models.cliente_Model import Cliente

cliente= Blueprint('cliente', __name__, url_prefix='/client')
gestor=Gestor

#METODO POST - CREAR CLIENTE

@cliente.route('/crearCliente', methods = ['POST'])

def crear_cliente():
    body = request.get_json()
    try:
        if("nit" in body and "nombre" in body and "usuario" in  body and "clave" in body and "direccion" in body and "email" in body):
            if(body["nit"] != "" and body["nombre"] != "" and body["usuario"] != "" and body["clave"] != "" and body["direccion"] != "" and body["email"] != ""):
                cliente = Cliente(body["nit"], body["nombre"], body["usuario"], body["clave"] ,body["direccion"] , body["email"] , False)
                if(gestor.agregar_cliente(cliente)):
                    return{'msg': 'El cliente ha sido creado exitosamente'}, 201     #Petición completada - created
                else:
                    return{'msg': 'Ya existe un cliente con el mismo número de NIT'}, 400       #Error al procesar solicitud - badrequest 
            else:
                return{'msg': 'Procure que todos los campos sean correctos'}, 400           #Error al procesar solicitud - badrequest
        else:
            return{'msg': 'Procure ingresar todos los campos correspondientes, para crear al cliente'}, 400         #Error al procesar solicitud - badrequest
    except:
        return {'msg': 'Ocurrió un error inesperado en el servidor'}, 500       #Internal Server Error
