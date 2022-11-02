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

from gestor import Gestor
from xml.etree import ElementTree as ET

app = Flask(__name__)
CORS(app)

gestor=Gestor()

@app.route('/')
def index():
    return {"msg" : "This api works!"}


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


tree = ET.parse('ArchivoConfig.xml')
root = tree.getroot()

#Cargar archivo
@app.route('/crearClientes', methods=['POST'])
def crearClientes():
    json=request.get_json()
    for client in root.iter('cliente'):
        nit = client.get('nit')
        nombre = client.find('nombre').text
        usuario = client.find('usuario').text
        clave = client.find('clave').text
        direccion = client.find('direccion').text
        email = client.find('correoElectronico').text
        gestor.agregar_cliente(json[nit],json[nombre],json[usuario],json[clave],json[direccion],json[email])
        return jsonify({'ok':True, 'msg':'Clientes cargados con exito'}),200


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
                gestor.crear_instancia(instancia)
                return{'msg': "Instancia creada exitosamente"}, 201 #created
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
 



# METODOS PARA CATEGORIAS

@app.route('/crearCategoria', methods = ['POST'])
def crearCategoria():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in body and "descripcion" in  body and "carga_trabajo" in body):
            categoria = Categoria(body["id"], body["nombre"],body["descripcion"],body["carga_trabajo"])
            gestor.crear_categoria(categoria)
            return{'msg': "Categoria creada exitosamente"}, 201 #created
        else:
            return{'msg': 'Faltan campos por rellenar'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500
 


# METODOS PARA CONFIGURACIONES

@app.route('/crearConfiguracion', methods = ['POST'])
def crearConfiguracion():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in body and "descripcion" in  body and "cant_recursos" in body):
            config = Configuracion(body["id"], body["nombre"],body["descripcion"],body["cant_recursos"])
            gestor.crear_configuracion(config)
            return{'msg': "Configuracion creado exitosamente"}, 201 #created
        else:
            return{'msg': 'Faltan campos por rellenar'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'},500
 

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





#METODOS PARA GENERACION DE FACTURA






#CARGA DE ARCHIVO DE CONFIGURACION
@app.route('/cargarArchivo', methods = ['POST'])
def cargarArchivo():
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
                nuevorecurso = Recurso(id, nombre, abreviatura, metrica, tipo, valor)
                gestor.crear_recurso(nuevorecurso)
        elif(firstchild.tag.lower() == "listacategorias"):
            for categoria in firstchild:
                id = categoria.attrib["id"]
                for params in categoria:
                    parametro = params.tag.lower()
                    if(parametro == "nombre"):
                        nombre = params.text.strip()
                    elif(parametro == "descripcion"):
                        descripcion = params.text.strip()
                    elif(parametro == "cargatrabajo"):
                        cargatrabajo = params.text.strip()
                    elif(parametro == "listaconfiguraciones"):
                        nuevacategoria = Categoria(id, nombre, descripcion,cargatrabajo)
                        gestor.crear_categoria(nuevacategoria)
                        for configs in params:
                            idconfig = configs.attrib["id"]
                            for paramconfig in configs:
                                if(paramconfig.tag == "nombre"):
                                    nombreconfig = paramconfig.text.strip()
                                elif(paramconfig.tag == "descripcion"):
                                    descripconfig = paramconfig.text.strip()
                                elif(paramconfig.tag == "recursosConfiguracion"):
                                    nuevaconfig = Configuracion(idconfig,nombreconfig, descripconfig)
                                    gestor.crear_configuracion(nuevaconfig)
                                    for nrecur in paramconfig:
                                        idrecur = nrecur.attrib["id"]
                                        cantidad = nrecur.text.strip()
                                        gestor.asignar_recurso(idconfig,idrecur,cantidad)
                            #gestor.asignarConfiguracion(id, idconfig)
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
                        nuevocliente = Cliente(nit, nombre, usuario, clave, direccion, mail)
                        gestor.agregar_cliente(nuevocliente)
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
                            nuevainstancia = Instancia(idinstancia,nombreins,idconfig, fechainicio,fechafin, estado, nit)
                            gestor.crear_instancia(nuevainstancia)
    return {'msg': 'Se ha completado la carga de todos los datos'},200



#CARG DE ARCHIVO DE CONSUMOS
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
    return {'msg': 'Carga completa'}, 200





if __name__ == '__main__':
    app.run(debug = True)
