class Consumo():
    def __init__(self, nit_cliente, id_instancia, tiempo, fecha_hora):
        self.nit_cliente = nit_cliente
        self.id_instancia = id_instancia
        self.tiempo = tiempo
        self.fecha_hora = fecha_hora

    def getnitcliente(self):
        return self.nit_cliente

    def getidinstancia(self):
        return self.id_instancia
    
    def gettiempo(self):
        return self.tiempo

    def getfechahora(self):
        return self.fecha_hora
    
    
    def getData(self):
        return{
            "nit_cliente": self.nit_cliente,
            "id_instancia": self.id_instancia,
            "tiempo": self.tiempo,
            "fecha_hora": self.fecha_hora
        }
