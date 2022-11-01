class Instancia():
    def __init__(self, id, nombre, idconfig ,fecha_inicial, fecha_final, estado):
        self.__id = id
        self.__nombre = nombre
        self.__idconfig = idconfig
        self.__fecha_inicial = fecha_inicial
        self.__fecha_final = fecha_final
        self.__estado = estado

    def getidinstancia(self):
        return self.__id
        
    def getnombre(self):
        return self.__nombre
    
    def getidconfig(self):
        return self.__idconfig

    def getfechainicial(self):
        return self.__fecha_inicial

    def getfechafinal(self):
        return self.__fecha_final

    def getestado(self):
        return self.__estado        

    def getData(self):
        return{
            "id": self.__id,
            "nombre": self.__nombre,
            "idconfig": self.__idconfig,
            "fecha_inicial": self.__fecha_inicial,
            "fecha_final": self.__fecha_final,
            "estado": self.__estado
        }

