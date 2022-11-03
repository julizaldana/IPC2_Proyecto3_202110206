from uuid import uuid4

class Factura():
    def __init__(self, nit,fecha, monto):
        self.uuid = uuid4()
        self.nit = nit
        self.fecha = fecha
        self.monto = monto

    def getUuid(self):
        return self.uuid

    def getFecha(self):
        return self.fecha

    def getMonto(self):
        return self.monto

    def getData(self):
        return{
            "uuid": self.uuid,
            "nit": self.nit,
            "fecha": self.fecha,
            "monto": self.monto
        }