class Cliente():
    def __init__(self, nit, nombre, usuario, clave, direccion, email):
        self.nit = nit
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.direccion = direccion
        self.email = email


    def getNit(self):
        return self.nit
        
    def getnombre(self):
        return self.nombre
    
    def getusuario(self):
        return self.usuario



