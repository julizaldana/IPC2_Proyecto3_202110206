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

    def getdescripcion(self):
        return self.descripcion

    def getcantrecursos(self):
        return self.cant_recursos

    def getData(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "cant_recursos": self.cant_recursos
        }
