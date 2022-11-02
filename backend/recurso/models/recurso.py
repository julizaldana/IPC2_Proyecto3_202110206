class Recurso():
    def __init__(self, id, nombre, abreviatura, metrica, tipo, valor_hora):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.metrica = metrica
        self.tipo = tipo
        self.valor_hora = valor_hora

    def getidrecurso(self):
        return self.id
        
    def getnombre(self):
        return self.nombre
    
    def getabreviatura(self):
        return self.abreviatura

    def getmetrica(self):
        return self.metrica

    def gettipo(self):
        return self.tipo

    def getvalorhora(self):
        return self.valor_hora


    def getData(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "abreviatura": self.abreviatura,
            "metrica": self.metrica,
            "tipo": self.tipo,
            "valor_hora": self.valor_hora,
        }
