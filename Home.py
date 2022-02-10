import os

from Funtions import Titulo, ReadJson, RegistrarCliente, CalcularDia, VisualizarClientes, Actualizar, Eliminar

docCalendario="Calendario.json"
lecturaCalendario= ReadJson(docCalendario)
calendario=lecturaCalendario
mes={}


docClientes = "BaseDatos.json"
lecturaClientes= ReadJson(docClientes)
clientes=lecturaClientes


seguir=True
while(seguir):
    
    Titulo("Menu Principal")

    print("1- Ingresar Cliente")
    print("2- Visualizar informacion ")
    print("3- Actualizar informacion")
    print("4- Eliminar informacion")
    print("5- Calcular Dia")
    print("6- Salir")
    print("")

    try:
        o=int(input("Escoge una opcion: "))

        if(o==1): #Calcular dia
            RegistrarCliente(docClientes, clientes)
        elif(o==2):
            VisualizarClientes(clientes)

        elif(o==3):
            Actualizar(docClientes, clientes)

        elif(o==4):
            Eliminar(docClientes, clientes)    

        elif(o==5):
            CalcularDia(docClientes, calendario, clientes)

        elif(o==6): #Salir
            Titulo("Gracias por usar nuestros servicios")
            input()
            seguir=False
        else:
            input("Esa opcion no se encuentra")
    except:
        input("Esa opcion no es valida")
