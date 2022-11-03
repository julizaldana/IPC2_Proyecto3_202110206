import json
from flask import Flask, request
from flask_cors import CORS
from flask.json import jsonify
from cliente.models.cliente import Cliente
from instancia.models.instancia import Instancia
from recurso.models.recurso import Recurso
from configuracion.models.configuracion import Configuracion
from categoria.models.categoria import Categoria
from consumos.models.consumo import Consumo
from factura.models.factura import Factura
from generarfacturas import PDF
 #Clase fpdf

from gestor import Gestor
from xml.etree import ElementTree as ET

app = Flask(__name__)
CORS(app)

gestor=Gestor()
pdf = PDF()


@app.route('/')
def index():
    return {"msg" : "This api works!"}


#LOGIN
@app.route('/login/<user>/<password>')
def login(user=None,password=None):
    res=gestor.obtener_usuario(user,password)
    if res==None:
        return '{"data":false,"message":"Tu usuario no existe o es invalido"}'
    return '{"data":true,"message":"¡Bienvenido!"}'



#METODOS PARA CLIENTES

@app.route('/crearCliente', methods = ['POST'])
def crearCliente():
    body = request.get_json()
    try:
        if("nit" in body and "nombre" in body and "usuario" in  body and "clave" in body and "direccion" in body and "email" in body):
            cliente = Cliente(body["nit"], body["nombre"],body["usuario"],body["clave"],body["direccion"],body["email"])
            if(gestor.agregar_cliente(cliente)):
                return{'msg': "Cliente creado exitosamente"}, 201 #created
            else:
                return{'msg': 'El NIT ya se encuentra registrado.'}, 406 #not acceptable
        else:
            return{'msg': 'Faltan campos por rellenar'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500
 


@app.route('/consultarDatos/cliente/<nit>', methods=['GET'])
def ver(nit):
    try:
        cliente = gestor.obtener_clientes(nit)
        if (cliente != None):
            return jsonify(cliente.getData()),200
        else:
            return {'msg': 'No se encontró el cliente'}, 404
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500



#METODOS PARA INSTANCIAS

'''
@app.route('/crearInstancia', methods=['POST'])
def crearInstancia():
    json=request.get_json()
    gestor.crear_instancia(json['id'],json['nombre'],json['idconfig'],json['fecha_inicial'],json['fecha_final'],json['estado'])
    return jsonify({'ok': True, 'msg':'Instancia creada con exito'}),201
'''


@app.route('/crearInstancia', methods = ['POST'])
def crearInstancia():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in body and "idconfig" in  body and "fecha_inicial" in body and "fecha_final" in body and "estado" in body and "nit" in body):
            cliente = gestor.obtener_clientes((body["nit"]))
            if (cliente != None):
                instancia = Instancia(body['id'],body['nombre'],body['idconfig'],body['fecha_inicial'],body['fecha_final'],body['estado'],body['nit'])
                cliente.crear_instancia(instancia)                
                if(gestor.crear_instancia(instancia)):
                    return{'msg': "Instancia creada exitosamente"}, 201 #created
                else:
                    return{'msg': 'El id de la instancia ya existe.'}, 406 #not acceptable
            else:
                return{'msg': 'Cliente con nit ingresado no existe'}, 406 #not acceptable
        else:
            return{'msg': 'Faltan campos por rellenar'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500
 


@app.route('/consultarDatos/instancia', methods=['GET']) #-> consultarDatos GET
def get_instancias():
    c=gestor.obtener_instancias()
    return jsonify(c),200



# METODOS PARA RECURSOS

@app.route('/crearRecurso', methods = ['POST'])
def crearRecurso():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in body and "abreviatura" in  body and "metrica" in body and "tipo" in body and "valor_hora" in body):
            recurso = Recurso(body["id"], body["nombre"],body["abreviatura"],body["metrica"],body["tipo"],body["valor_hora"])
            gestor.crear_recurso(recurso)
            return{'msg': "Recurso creado exitosamente"}, 201 #created
        else:
            return{'msg': 'Faltan campos por rellenar'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500
 

@app.route('/consultarDatos/recurso', methods=['GET']) #-> consultarDatos GET
def get_recursos():
    c=gestor.obtener_recursos()
    return jsonify(c),200



# METODOS PARA CATEGORIAS


@app.route('/crearCategoria', methods = ['POST'])
def crearCategoria():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in body and "descripcion" in  body and "carga_trabajo" in body):
            categoria = Categoria(body["id"], body["nombre"],body["descripcion"],body["carga_trabajo"])
            if(gestor.crear_categoria(categoria)):
                return{'msg': "Categoría creada exitosamente"}, 201 #created
            else:
                return{'msg': 'El id para esa categoría ya se encuentra registrada.'}, 406 #not acceptable
        else:
            return{'msg': 'Faltan campos por rellenar'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500



'''
@app.route('/consultarDatos/categoria', methods=['GET']) #-> consultarDatos GET
def get_categorias():
    c=gestor.obtener_categorias()
    return jsonify(c),200
'''

@app.route('/consultarDatos/categoria/<id>', methods=['GET'])
def get_categorias(id):
    try:
        categoria = gestor.obtener_categorias(id)
        if (categoria != None):
            return jsonify(categoria.getData()),200
        else:
            return {'msg': 'No se encontró la categoría'}, 404
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500

# METODOS PARA CONFIGURACIONES

@app.route('/crearConfiguracion', methods = ['POST'])
def crearConfiguracion():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in body and "descripcion" in  body and "cant_recursos" in body and "id_categoria" in body):
            categoria = gestor.obtener_categorias((body["id_categoria"]))
            if (categoria != None):
                config = Configuracion(body["id"], body["nombre"],body["descripcion"],body["cant_recursos"],body["id_categoria"])
                categoria.crear_configuracion(config)
                gestor.crear_configuracion(config)
                return{'msg': "Configuracion creado exitosamente"}, 201 #created
            else: 
                return{'msg': 'Categoria con el id ingresado no existe'}, 406 #not acceptable
        else:
            return{'msg': 'Faltan campos por rellenar'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500
 

@app.route('/consultarDatos/configuracion', methods=['GET']) #-> consultarDatos GET
def get_configuracion():
    c=gestor.obtener_configuracion()
    return jsonify(c),200


# METODOS PARA CONSUMOS

@app.route('/crearConsumo', methods = ['POST'])
def crearConsumo():
    body = request.get_json()
    try:
        if("nit_cliente" in body and "id_instancia" in body and "tiempo" in  body and "fecha_hora" in body):
            consumo = Consumo(body["nit_cliente"], body["id_instancia"],body["tiempo"],body["fecha_hora"])
            gestor.crear_consumo(consumo)
            return{'msg': "Consumo creado exitosamente"}, 201 #created
        else:
            return{'msg': 'Faltan campos por rellenar'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500



@app.route('/consultarDatos/consumo/<nit>/<idinstancia>', methods=['GET'])
def ver_consumo(nit,idinstancia):
    try:
        cliente = gestor.obtener_clientes(nit)
        instancia = gestor.obtener_instancias(idinstancia)
        consumo = gestor.obtener_consumo()
        if (cliente != None) and (instancia != None):
            return jsonify(consumo.getData()),200
        else:
            return {'msg': 'No se encontró el cliente o la instancia'}, 404
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500





#METODOS PARA GENERACION DE FACTURA


@app.route('/generarFactura', methods = ['POST'])
def generarFactura():
    body=request.get_json()
    try:
        if ("nit" in body and "fecha" in body and "monto" in body):
            cliente = gestor.obtener_clientes(body["nit"])
            if (cliente != None):
                factura = Factura(body["nit"], body["fecha"], body["monto"])
                cliente.generar_factura(factura)
                gestor.generar_factura(factura)
                return {'msg': f"Factura id. '{factura.getUuid()}' creada exitosamente"}, 201
            else:
                return {'msg': 'Cliente con nit ingresado no existe'}, 404
        else:
            return {'msg': 'Faltan campos en la petición'}, 400
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500


@app.route('/verFactura/<factura>', methods=['GET'])
def view(factura):
    try:
        factura = gestor.obtener_factura(factura)
        if (factura != None):
            f = open("factura.txt", "a")
            print(factura.getData(), file=f)
            f.close()
            pdf.add_page()
            pdf.texts('factura.txt')
            pdf.titles("GENERACIÓN DE FACTURA")
            pdf.set_author('Julio Zaldaña')
            pdf.output('factura.pdf','F')
            return factura.getData(), 200         
        else: 
            return {'msg': 'No se encontró la factura'},404
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500



@app.route('/imprimirFactura', methods=['POST'])
def imprimir():
    factura = gestor.imprimir_factura()
    return factura


#METODOS PARA MOSTRAR LISTA DE CATEGORIAS Y CONFIGURACIONES

@app.route('/verListas/categorias/<idcat>', methods=['GET'])
def ver_analisis(idcat):
    try:
        categ=gestor.obtener_categorias(idcat)
        if (categ != None):
            f = open("lista_analisis1.txt", "a")
            print(categ.getData(), file=f)
            f.close()
            pdf.add_page()
            pdf.texts('lista_analisis1.txt')
            pdf.titles("ANALISIS DE LISTAS DE CATEGORIAS Y CONFIGURACIONES")
            pdf.set_author('Julio Zaldaña')
            pdf.output('lista_analisis1.pdf','F')
            return categ.getData(),200
        else: 
            return {'msg': 'No se encontró la categoría'},404   
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500




#METODOS PARA MOSTRAR LISTA DE RECURSOS MAS UTILIZADOS


@app.route('/verRecursos', methods=['GET'])
def ver_recursos():
    try:
        listarec = gestor.obtener_recursos()
        f = open("factura.txt", "a")
        print(listarec, file=f)
        f.close()
        pdf.add_page()
        pdf.texts('lista_analisis2.txt')
        pdf.titles("ANALISIS DE LISTA DE RECURSOS MAS UTILIZADOS")
        pdf.set_author('Julio Zaldaña')
        pdf.output('lista_analisis2.pdf','F')
        return jsonify(listarec), 200         
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500





'''
@app.route('/consultarDatos/categoria', methods=['GET']) #-> consultarDatos GET
def get_categorias():
    c=gestor.obtener_categorias()
    return jsonify(c),200
'''


#CARGAR ARCHIVO CONFIGURACION XML
@app.route('/cargarArchivo', methods = ['POST'])
def cargaCompleta():
    xml = request.data.decode('utf-8')
    raiz = ET.XML(xml)
    for firstchild in raiz:
        if(firstchild.tag.lower() == "listarecursos"):
            #en lista de recursos
            for recurso in firstchild:
                id = recurso.attrib["id"]
                for params in recurso:
                    parametro = params.tag.lower()
                    if(parametro == "nombre"):
                        nombre = params.text.strip()
                    elif(parametro == "abreviatura"):
                        abreviatura = params.text.strip()
                    elif(parametro == "metrica"):
                        metrica = params.text.strip()
                    elif(parametro == "tipo"):
                        tipo = params.text.strip()
                    elif(parametro == "valorxhora"):
                        valor = params.text.strip()
                nrecurso = Recurso(id, nombre, abreviatura, metrica, tipo, valor)
                gestor.crear_recurso(nrecurso)
        elif(firstchild.tag.lower() == "listacategorias"):
            for categoria in firstchild:
                id_categoria = categoria.attrib["id"]
                for params in categoria:
                    parametro = params.tag.lower()
                    if(parametro == "nombre"):
                        nombre = params.text.strip()
                    elif(parametro == "descripcion"):
                        descripcion = params.text.strip()
                    elif(parametro == "cargatrabajo"):
                        cargatrabajo = params.text.strip()
                    elif(parametro == "listaconfiguraciones"):
                        ncategoria = Categoria(id_categoria, nombre, descripcion,cargatrabajo)
                        gestor.crear_categoria(ncategoria)
                        for configs in params:
                            idconfig = configs.attrib["id"]
                            for paramconfig in configs:
                                if(paramconfig.tag == "nombre"):
                                    nombreconfig = paramconfig.text.strip()
                                elif(paramconfig.tag == "descripcion"):
                                    descripconfig = paramconfig.text.strip()
                                elif(paramconfig.tag == "recursosConfiguracion"):
                                    for nrecur in paramconfig:
                                        idrecur = nrecur.attrib["id"]
                                        cantidad = nrecur.text.strip()                                    
                                    nconfig = Configuracion(idconfig,nombreconfig, descripconfig, cantidad,id_categoria)
                                    gestor.crear_configuracion(nconfig)
        elif(firstchild.tag.lower() == "listaclientes"):
            for clientes in firstchild:
                nit = clientes.attrib["nit"]
                for params in clientes:
                    parametro = params.tag.lower()
                    if(parametro == "nombre"):
                        nombre = params.text.strip()
                    elif(parametro == "usuario"):
                        usuario = params.text.strip()
                    elif(parametro == "clave"):
                        clave = params.text.strip()
                    elif(parametro == "direccion"):
                        direccion = params.text.strip()
                    elif(parametro == "correoelectronico"):
                        mail = params.text.strip()
                    elif(parametro == "listainstancias"):
                        ncliente = Cliente(nit, nombre, usuario, clave, direccion, mail)
                        gestor.agregar_cliente(ncliente)
                        for instancia in params:
                            idinstancia = instancia.attrib["id"]
                            for paraminstancia in instancia:
                                if(paraminstancia.tag == "idConfiguracion"):
                                    idconfig = paraminstancia.text.strip()
                                elif(paraminstancia.tag == "nombre"):
                                    nombreins = paraminstancia.text.strip()
                                elif(paraminstancia.tag == "fechaInicio"):
                                    fechainicio = paraminstancia.text.strip()
                                elif(paraminstancia.tag == "estado"):
                                    estado = paraminstancia.text.strip()
                                elif(paraminstancia.tag == "fechaFinal"):
                                    fechafin = paraminstancia.text.strip()
                            ninstancia = Instancia(idinstancia, nombreins, idconfig, fechainicio, fechafin, estado, nit)
                            gestor.crear_instancia(ninstancia)
    return {'msg': 'Se ha completado la carga de todos los datos'},200



#CARGA DE ARCHIVO DE CONSUMOS
@app.route('/cargarConsumos', methods = ['POST'])
def cargarConsumos():
    xml = request.data.decode('utf-8')
    raiz = ET.XML(xml)
    for consumo in raiz:
        nitcliente =  consumo.attrib['nitCliente']
        idinstancia = consumo.attrib['idInstancia']
        for params in consumo:
            if(params.tag == "tiempo"):
                tiempo = params.text.strip()
            elif(params.tag == "fechaHora"):
                fechaHora = params.text.strip()
        nuevoconsumo = Consumo(nitcliente, idinstancia, tiempo, fechaHora)
        gestor.crear_consumo(nuevoconsumo)
    return {'msg': 'Se ha completado la carga de los datos'}, 200





if __name__ == '__main__':
    app.run(debug = True)
