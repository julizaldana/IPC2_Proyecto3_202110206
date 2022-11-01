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


    def obtener_clientes(self, nitClient):
        if int(nitClient) in self.nitclientes:
            for client in self.clientes:
                if client.getnit() == int(nitClient):
                    return client
        return None



## FUNCIONES PARA INSTANCIAS

    def crear_instancia(self,id,nombre,fecha_inicial,fecha_final,estado):
        nuevainstancia = Instancia(id,nombre,fecha_inicial,fecha_final,estado)
        self.instancias.append(nuevainstancia)
        return True


    #def modificar_instancia(self,id,nombre,fecha_inicial,fecha_final,estado):

    
    #def eliminar_instancia(self,id,nombre,fecha_inicial,fecha_final,estado):




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