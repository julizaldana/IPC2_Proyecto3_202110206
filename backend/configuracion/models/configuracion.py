class Configuracion():
    def __init__(self, id, nombre, descripcion, cant_recursos):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cant_recursos = cant_recursos

    def getid(self):
        return self.id
        
    def getnombre(self):
        return self.nombre


