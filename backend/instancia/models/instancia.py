class Instancia():
    def __init__(self, id, nombre, idconfig ,fecha_inicial, fecha_final, estado):
        self.id = id
        self.nombre = nombre
        self.idconfig = idconfig
        self.fecha_inicial = fecha_inicial
        self.fecha_final = fecha_final
        self.estado = estado

    def getIdinstancia(self):
        return self.id
        
    def getnombre(self):
        return self.nombre
    
    def getidconfig(self):
        return self.idconfig



