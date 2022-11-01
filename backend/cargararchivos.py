import xml.etree.ElementTree as ET
from gestor import Gestor
import json
from flask import request

gestor = Gestor

def cargar_archivo(ruta):
    tree=ET.parse(ruta)
    root=tree.getroot()

    for clientes in root.iter('cliente'):
        json=request.get_json()
        nit = clientes.get('nit')
        nombre = clientes.find('nombre').text
        usuario = clientes.find('usuario').text
        clave = clientes.find('clave').text
        direccion = clientes.find('direccion').text
        email = clientes.find('correoElectronico').text
        gestor.agregar_cliente(True,json['nit'],json['nombre'],json['usuario'],json['clave'],json['direccion'],json['email'])
        print('Se añadió correctamente',nit,nombre,usuario,clave,direccion,email)



def menu():
    opcion=''
    print("---------------------------------------------")
    print("     MENU DE APOYO - TECNOLOGIAS CHAPINAS S.A     ")
    print('1. Ingresar archivo de configuracion')
    print('2. Ingresar archivos de lista de consumos')
    print('3. Generar factura')
    print('4. Salir')
    print("---------------------------------------------")
    opcion=input('Ingrese una opcion: ')
    print(opcion)

    if opcion =='1':
        Filename=input('Ingresar nombre de archivo: ')
        file='./'+Filename
        cargar_archivo(file)
        return menu()
    
    elif opcion =='2':
        print(gestor.clientes)
    

    elif opcion=='4':
        exit()

menu()