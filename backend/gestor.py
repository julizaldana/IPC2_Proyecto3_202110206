from cliente.models.cliente_Model import Cliente
import json


class Gestor:
    def __init__(self):
        self.clientes = []


## Funciones para Clientes

    def agregar_cliente(self, nit, nombre, usuario, clave, direccion, email):
        nuevocliente = Cliente(nit,nombre,usuario,clave,direccion,email)
        self.clientes.append(nuevocliente)
        return True

    def obtener_clientes(self):
        json=[]
        for i in self.clientes:
            cliente={
                "nit": i.nit,
                "nombre": i.nombre,
                "usuario": i.usuario,
                "clave": i.clave,
                "direccion": i.direccion,
                "email": i.email
            }
            json.append(cliente)
        return json

    def eliminar_cliente(self, nit, nombre, usuario, clave, direccion, email):
        nuevocliente = Cliente(nit,nombre,usuario,clave,direccion,email)
        self.clientes.remove(nuevocliente)
        return True

