from instancia.models.instancia import Instancia
import json


class Gestor:
    def __init__(self):
        self.clientes = []
        self.nitclientes = []
        self.instancias = []


## FUNCIONES PARA CLIENTES

    def agregar_cliente(self, cliente):
        if not(cliente.getnit() in self.nitclientes):
            self.clientes.append(cliente)
            self.nitclientes.append(cliente.getnit())
            return True
        return False


    def obtener_clientes(self, nit):
        json=[]
        if nit in self.nitclientes:
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


## FUNCIONES PARA INSTANCIAS

    def crear_instancia(self,id,nombre,fecha_inicial,fecha_final,estado):
        nuevainstancia = Instancia(id,nombre,fecha_inicial,fecha_final,estado)
        self.instancias.append(nuevainstancia)
        return True



    def obtener_instancias(self, nit):
        json=[]
        for i in self.instancias:
            instancia={
                "id": i.id,
                "nombre": i.nombre,
                "idconfig": i.idconfig,
                "fecha_inicial": i.fecha_inicial,
                "fecha_final": i.fecha_final,
                "estado": i.estado
            }
            json.append(instancia)
        return json