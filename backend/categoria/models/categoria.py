class Categoria():
    def __init__(self, id, nombre, descripcion , carga_trabajo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.carga_trabajo = carga_trabajo

    def getid(self):
        return self.id
        
    def getnombre(self):
        return self.nombre


    def getdescripcion(self):
        return self.descripcion


    def getcargatrabajo(self):
        return self.carga_trabajo

    def getData(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "carga_trabajo": self.carga_trabajo
        }
