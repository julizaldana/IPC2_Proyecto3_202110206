class Instancia():
    def __init__(self, id, nombre, idconfig ,fecha_inicial, fecha_final, estado, nit):
        self.id = id
        self.nombre = nombre
        self.idconfig = idconfig
        self.fecha_inicial = fecha_inicial
        self.fecha_final = fecha_final
        self.estado = estado
        self.nit = nit
        self.configuraciones = []


    def crear_configuracion(self, configuracion):
        self.configuraciones.append(configuracion)

    def getidinstancia(self):
        return self.id
        
    def getnombre(self):
        return self.nombre
    
    def getidconfiguracion(self):
        return self.idconfig

    def getfechainicial(self):
        return self.fecha_inicial

    def getfechafinal(self):
        return self.fecha_final

    def getestado(self):
        return self.estado


    def getConfiguracion(self, idConfig):
        for configuracion in self.configuraciones:
            if configuracion.getIdconfiguracion() == idConfig:
                return configuracion
        return None


    def getData(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "idconfig": self.idconfig,
            "fecha_inicial": self.fecha_inicial,
            "fecha_final": self.fecha_final,
            "estado": self.estado,
            "nit": self.nit
        }

