from email import message
from itertools import count
import os
import json
from pickle import FALSE
from re import search
from xml.etree.ElementTree import tostring

##########################################
#######  Encabezado ######################

def Titulo(SubTitulo):
    os.system("cls")
    print("")
    print("//// Moto Carro Ferney ////")
    print("")
    print(SubTitulo)
    print("")

##########################################

#######  Archivos Json ######################

def GenerarJson(nombreDocumento, Diccionario):
    Titulo("Generar Json")
    with open(nombreDocumento,"w") as f:
        json.dump(Diccionario,f, indent=4)
    input("Se guardó el archivo")

def ReadJson(nombreDocumento):
    with open(nombreDocumento,"r") as f:
        Diccionario_json = json.load(f)
    return Diccionario_json

def LeerArchivoJson(nombreDocumento):
    Titulo("Leer archivo Json")
    input (ReadJson(nombreDocumento))

##########################################


#######  Conteo ######################

def SumaDia(nombreDia):
    x = 0
    if nombreDia != "sabado" or nombreDia != "domingo":
        x = 1
    elif nombreDia == "sabado":
        x = 3
    elif nombreDia == "domingo":
        x = 2
    
    return x
    
    
        


def Contar(calendario):
    datosCalculados = {}
    semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    dia=0
    diasTrabajar = int(input("Cuantos dias vas a trabajar: "))
    nunMes = input("Numero de mes: ")
    mesIngres = calendario[nunMes]
    nombreMesIngreso = mesIngres['mes']

    count = 0
    diaInicial=""
    if(nunMes in calendario):
        lista = calendario.get(nunMes)
        dia = int(input("Dia de ingreso: "))
        nombreDia = lista["diaUno"]
        count = semana.index(nombreDia) * -1
    
        for i in range(lista["semanas"]):
            for o in range(7):
                count += 1
                if count == dia:
                    diaInicial=semana[o]
                    print(f"dia de ingreso {diaInicial}")
                    
        diaR = dia
        diaTrabajado = 0
        index = semana.index(diaInicial)        
        while diaTrabajado < diasTrabajar:
            if diaTrabajado == 0:
                diaR += SumaDia(diaInicial)
                diaTrabajado += 1
                index += 1
            elif diaTrabajado > 0 and diaTrabajado <diasTrabajar:
                if diaR > lista["numDias"]:
                    diaR = 1
                    x = int(nunMes) + 1
                    y = str(x)
                    mes = calendario.get(y)["mes"]
                    
                else:
                    diaR += SumaDia(semana[index])
                if semana[index] == "sabado" or semana[index] == "domingo" :
                    diaTrabajado += 0
                else:
                    diaTrabajado += 1
                index += 1
                if index == 7:
                    index = 0              

                
        input(f"dia final=   {diaR} - {mes} - {semana[index-1]}")

        datosCalculados["diaIngreso"] = dia
        datosCalculados["mesIngreso"] = nombreMesIngreso
        datosCalculados["dia"]=diaR
        datosCalculados["mes"]=mes
        datosCalculados["diaSemana"]=semana[index-1]

        return datosCalculados
                


            


##########################################

##########################################

#######  Ingresar ######################

def RegistrarCliente(nombreDocumento,diccionario):
    Titulo("Registrar")
    seguir="S"
    while(seguir=="S"):
        Titulo("Registrar")
        alumno={}
        numNino=int(input("Documento: "))

        alumno["nombre"]=(input("Nombre: "))
        alumno["direccion"]=(input("Direccion: ")) 
        alumno["pariente"]=(input("Pariente: ")) 
        alumno["celular"]=(input("Numero de Celular: "))
        alumno["calculado"] = False
        diccionario[numNino]=alumno
        GenerarJson(nombreDocumento,diccionario)
        
        seguir=input("Seguir?S/N: ").upper()


#######  Visualizar Clientes ############



def BuscarCliente(diccionario, id):

        alumno = diccionario[id]
        nombre = alumno['nombre']
        direccion = alumno['direccion']
        pariente = alumno['pariente']
        celular = alumno['celular']

        calculado = alumno["calculado"]
        
        if(calculado):
            calculado = alumno['datosCalculados']
            diaIngreso = calculado['diaIngreso']
            mesIngreso = calculado['mesIngreso']
            dia = calculado['dia']
            mes = calculado['mes']
            diaSemana = calculado['diaSemana']
            
            print(f"|     {id}     |  {nombre}  |  {direccion}   |  {pariente}   |  {celular}  |  {diaIngreso}  |  {mesIngreso}  |  {dia}  |  {mes}  |  {diaSemana}  |")
            
        else:
            print(f"|     {id}     |  {nombre}  |  {direccion}   |  {pariente}   |  {celular}  |")
            



def VisualizarClientes(diccionario):
    Titulo("Clientes")
    print("_____________________________________________________________________________________________________________________________")
    print("")
    print("| Documento |  Nombre  |  Direccion  |  Pariente  |  Celular  |  Dia Ingreso  |  Mes Ingreso  |  Dia  |  Mes  |  Dia Semana  |")
    print("______________________________________________________________________________________________________________________________")
    for i in diccionario:
        BuscarCliente(diccionario,i)
    input("Presione enter para salir ") 
##########################################


##########################################
################opcion calcular dia ######

def CalcularDia(nombreDocumento, calendario, diccionario):
    Titulo("Calcular Dia")
    id = input("Ingrese el Id: ")
    alumno = diccionario[id]
    datosCalculados={}
    datosCalculados = Contar(calendario)
    alumno["datosCalculados"] = datosCalculados
    alumno["calculado"] = True
    diccionario[id]=alumno
    GenerarJson(nombreDocumento,diccionario)


#################  Actualizar ###################

def Actualizar(nombreDocumento, diccionario):
    Titulo("Acutalizar Cliente")

    id = input("Ingresa el documento que quieres actualizar")
    alumno = diccionario[id]
    print(f"1- Nombre: {alumno['nombre']}")
    print(f"2- Direccion: {alumno['direccion']}")
    print(f"3- Pariente: {alumno['pariente']}")
    print(f"4- Celular: {alumno['celular']}")

    o = int(input("Elija la opcion que quieres corregir: "))
    

    if(o == 1 ):
        nombre = input("Digite el nombre a cambiar: ")
        alumno['nombre'] = nombre
    elif( o == 2 ):
        direccion = input("Digite la direccion a cambiar: ")
        alumno['direccion'] = direccion
    elif( o == 3):
        pariente = input("Digite la direccio a cambiar: ")
        alumno['pariente'] = pariente
    elif( o == 4 ):
        celular = input("Digite el celular a cambiar: ")
        alumno['celular'] = celular
    
    diccionario[id] = alumno
    GenerarJson(nombreDocumento,diccionario)

    

def Eliminar(nombreDocumento, diccionario):

    Titulo("Acutalizar Cliente")

    id = input("Ingresa el documento que quieres eliminar: ")
    alumno = diccionario[id]
    print(f"Nombre: {alumno['nombre']}")
    print(f"Direccion: {alumno['direccion']}")
    print(f"Pariente: {alumno['pariente']}")
    print(f"Celular: {alumno['celular']}")

    o = input("¿Estas seguro que quieres eliminar el registro? S/N: ").upper()
    if(o == "S"):
        del(diccionario[id])
        input("Se elimino el registro")
        GenerarJson(nombreDocumento,diccionario)


