from instancia.models.instancia import Instancia
import json
import datetime


class Gestor:
    def __init__(self):
        self.clientes = []
        self.nitclientes = []
        self.instancias = []
        self.idinstancias = []
        self.recursos = []
        self.configuraciones= []
        self.categorias = []
        self.idcategorias = []
        self.consumos = []
        self.facturas = []



## FUNCIONES PARA CLIENTES

    def agregar_cliente(self, cliente):
        if not(cliente.getnit() in self.nitclientes):
            self.clientes.append(cliente)
            self.nitclientes.append(cliente.getnit())
            return True
        return False


    def obtener_clientes(self, nitClient):
        if nitClient in self.nitclientes:
            for client in self.clientes:
                if client.getnit() == nitClient:
                    return client
        return None



## FUNCIONES PARA INSTANCIAS

    def crear_instancia(self,instancia):
        if not(instancia.getidinstancia() in self.idinstancias):
            self.instancias.append(instancia)
            self.idinstancias.append(instancia.getidinstancia())
            return True
        return False

    def validar_fecha(date_text):
        try:
            datetime.datetime.strptime(date_text, '%d/%m/%y')
        except ValueError:
            raise ValueError("El formato debe de ser YYYY/MM/DD")




    #def modificar_instancia(self,id,nombre,fecha_inicial,fecha_final,estado):

    
    #def eliminar_instancia(self,id,nombre,fecha_inicial,fecha_final,estado):


    def obtener_instancias(self):
        json=[]
        for ins in self.instancias:
            instancia={
                'id': ins.id,
                'nombre': ins.nombre,
                'idconfig': ins.idconfig,
                'fecha_inicial': ins.fecha_inicial,
                'fecha_final': ins.fecha_final,
                'estado': ins.estado
            }
            json.append(instancia)
        return json


## FUNCIONES PARA CATEGORIAS

    def crear_categoria(self, categoria):
        if not(categoria.getidcategoria() in self.idcategorias):
            self.categorias.append(categoria)
            self.idcategorias.append(categoria.getidcategoria())
            return True
        return False

    def obtener_categorias(self, idCategoria):
        if idCategoria in self.idcategorias:
            for categoria in self.categorias:
                if categoria.getidcategoria() == idCategoria:
                    return categoria
        return None


## FUNCIONES PARA CONFIGURACIONES

    def crear_configuracion(self,configuracion):
        self.configuraciones.append(configuracion)
        return True

    def obtener_configuracion(self):
        json=[]
        for ins in self.configuraciones:
            config={
                'id': ins.id,
                'nombre': ins.nombre,
                'descripcion': ins.descripcion,
                'cant_recursos': ins.cant_recursos
            }
            json.append(config)
        return json



## FUNCIONES PARA RECURSOS

    def crear_recurso(self,recurso):
        self.recursos.append(recurso)
        return True

    #def asignar_recurso(self, idconfiguracion, idrecurso, cantidad):

    def obtener_recursos(self):
        json=[]
        for rec in self.recursos:
            recurso={
                'id': rec.id,
                'nombre': rec.nombre,
                'abreviatura': rec.abreviatura,
                'metrica': rec.metrica,
                'tipo': rec.tipo,
                'valor_hora': rec.valor_hora
            }
            json.append(recurso)
        return json


# FUNCIONES PARA CONSUMOS


    def crear_consumo(self,consumo):
        self.consumos.append(consumo)
        return True

    def obtener_consumo(self,nitCliente,idInstancia):
        if nitCliente in self.nitclientes and idInstancia in self.idinstancias:
            for consumo in self.consumos:
                if consumo.getnitcliente() == nitCliente and consumo.getidinstancia() == idInstancia:
                    return consumo
        return None



# FUNCIONES PARA FACTURAS

    def generar_factura(self,factura):
        self.facturas.append(factura)
        return True
    
    def obtener_factura(self,uuidFactura):
        #Retorna una factura de la lista de facturas, usando como referencia el identificador único de factura
        for factura in self.facturas:
            if str(factura.getUuid()) == uuidFactura:
                return factura
        return None

    def imprimir_factura(self):
        for factura in self.facturas:
            print(factura)
        return None


    def obtener_listacategorias(self):
        json=[]
        for i in self.idcategorias:
            categoria={
            "id": i.id,
            "nombre": i.nombre,
            "descripcion": i.descripcion,
            "carga_trabajo": i.carga_trabajo,
            "configuraciones": i.list_configuraciones
            }
            json.append(categoria)
        return json

