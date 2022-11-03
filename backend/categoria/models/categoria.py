class Categoria():
    def __init__(self, id, nombre, descripcion , carga_trabajo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.carga_trabajo = carga_trabajo
        self.configuraciones = []



    def crear_configuracion(self,configuracion):
        self.configuraciones.append(configuracion)
        

    def getidcategoria(self):
        return self.id
        
    def getnombre(self):
        return self.nombre

    def getdescripcion(self):
        return self.descripcion

    def getcargatrabajo(self):
        return self.carga_trabajo

    def getConfiguracion(self, idConfiguracion):
        for configuracion in self.configuraciones:
            if configuracion.getIdconfiguracion() == idConfiguracion:
                return configuracion
        return None


    def getData(self):
        list_configuraciones = []
        for conf in self.configuraciones:
            list_configuraciones.append(conf.getData())
        return{
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "carga_trabajo": self.carga_trabajo,
            "configuraciones": list_configuraciones
        }
