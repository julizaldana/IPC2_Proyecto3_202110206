class Cliente():
    def __init__(self, nit, nombre, usuario, clave, direccion, email):
        self.__nit = nit
        self.__nombre = nombre
        self.__usuario = usuario
        self.__clave = clave
        self.__direccion = direccion
        self.__email = email

    def getnit(self):
        return self.__nit
        
    def getnombre(self):
        return self.__nombre
    
    def getusuario(self):
        return self.__usuario

    def getclave(self):
        return self.__clave
    
    def getdireccion(self):
        return self.__direccion

    def getemail(self):
        return self.__email

    def getdatos(self):
        return{
            "nit": self.__nit,
            "nombre": self.__nombre,
            "usuario": self.__usuario,
            "clave": self.__clave,
            "direccion": self.__direccion,
            "email": self.__email
        }

