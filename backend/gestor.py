from instancia.models.instancia import Instancia
import json
import datetime


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

    def crear_instancia(self,instancia):
        self.instancias.append(instancia)
        return True

    def validar_fecha(date_text):
        try:
            datetime.datetime.strptime(date_text, '%d/%m/%y')
        except ValueError:
            raise ValueError("El formato debe de ser YYYY/MM/DD")




    #def modificar_instancia(self,id,nombre,fecha_inicial,fecha_final,estado):

    
    #def eliminar_instancia(self,id,nombre,fecha_inicial,fecha_final,estado):


    def obtener_instancias(self):
        json=[]
        for ins in self.instancias:
            instancia={
                'id': ins.id,
                'nombre': ins.nombre,
                'idconfig': ins.idconfig,
                'fecha_inicial': ins.fecha_inicial,
                'fecha_final': ins.fecha_final,
                'estado': ins.estado
            }
            json.append(instancia)
        return json