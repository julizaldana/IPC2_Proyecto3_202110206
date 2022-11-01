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
    
