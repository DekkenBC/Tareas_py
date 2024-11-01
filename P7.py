import random
import pprint
from operator import itemgetter
import os
import json
import pandas as pd

def main():
    Trabajadores = []
    IDs = []
    extenciones = ["cvs","txt","markdown"]
    
    while True:
        
        cont = len(Trabajadores)

        print("Menu")
        print("1.- Generar 10 personas")
        print("2.- Eliminar por ID")
        print("3.- Imprimir la lista")
        print("4.- Buscar por ID")
        print("5.- Ordenar por ID")
        print("6.- Generar archivo (excel, txt, cvs, markdown)")
        print("7.- Imprimir Archivo")
        print("8.- Borrar la lista")
        print("9.- Salir")
        try:
            op = int(input("Cual es su seleccion?: "))
        except ValueError:
            print(">>>>> Seleccione una opcion disponible\n")
        else:
            match op:
                case 1:
                    print("")
                    for x in range(10):
                        ND,NI = act1(IDs)
                        Trabajadores.append(ND)
                        IDs.append(NI)
                    print("Usuarios creado con exito\n")
                
                case 2:
                    print("")
                    print("")
                    indice = buscar(Trabajadores, cont)
                    if indice == None:
                        print("No se ha encontrado a este trabajador")
                    elif indice == "NoHay":
                        print("No hay trabajadores actualmente")
                    elif indice == None:
                        print("Se ha producido un error inesperado")
                    else:
                        indice = indice - 1
                        Trabajadores.remove(Trabajadores[indice])
                        print("Trabajador eliminado correctamente")
                    print("")
                    
                case 3:
                    print("")
                    info = pd.DataFrame(Trabajadores)
                    print(info.to_string(index=False))
                    
                case 4:
                    print("")
                    indice = buscar(Trabajadores, cont)
                    if indice == None:
                        print("No se ha encontrado a este trabajador")
                    elif indice == "NoHay":
                        print("No hay trabajadores actualmente")
                    elif indice == None:
                        print("Se ha producido un error inesperado")
                    else:
                        indice = indice - 1
                        pprint.pprint(Trabajadores[indice],sort_dicts=False)
                    print("")
                       
                case 5:
                    print("")
                    Trabajadores.sort(key = itemgetter("Clave"))
                    IDs.sort()
                    print("Los trabajadores se han ordenado con exito")
                    print("")
                case 6:
                    print("")
                    nombre = input("Dame el nombre del documento a crear (Sin extencion): ")
                    while True:
                        ext = input("Dame la extencion del documento a crear (xlsx,txt, cvs, markdown, sin punto): ")
                        if ext == "xlsx" or ext == "txt" or ext == "cvs" or ext == "markdown":
                            break
                        else:
                            print("Esta no es una extencion valida")
                    documento = nombre + "." + ext
                    print (documento)
                    
                    with open(documento,"w") as file:
                        if ext == "cvs" or ext == "txt" or ext == "markdown":
                            for dic in Trabajadores:
                                json.dump(dic, file) 
                                file.write("\n")
                        else:
                            info = pd.DataFrame(Trabajadores)
                            info.to_excel(f"{documento}",index=False)
                            
                case 7:
                    print("")
                    nombre = input("Dame el nombre del documento a abrir (Sin extencion): ")
                    while True:
                        ext = input("Dame la extencion del documento a abrir (xlsx,txt, cvs, markdown, sin punto): ")
                        if ext == "xlsx" or ext == "txt" or ext == "cvs" or ext == "markdown":
                            break
                        else:
                            print("Esta no es una extencion valida")
                    documento = nombre + "." + ext
                    
                    if comprobador(documento):
                        with open(documento,"r") as file:
                            if ext == "cvs" or ext == "txt" or ext == "markdown":
                                for linea in file:
                                    print(linea.strip())
                            else:
                                info = pd.read_excel(documento)
                                print(info)
                    else:
                        print("Este documento no existe")

                case 8:
                    print("")
                    try:
                        sel = int(input("Seguro que desea eliminar la lista? (1 = Si 2 = No): "))
                    except ValueError:
                        print("Opcion no valida")
                    else:
                        if sel == 1:
                            Trabajadores.clear()
                            IDs.clear()
                            print("Los trabajadores se han borrado con exito")
                        elif sel == 2:
                            print("Ok")
                        else:
                            print("Esta no es una opcion valida pero no pasara nada")
                            
                case 9:
                    break
                
                case _:
                    print(">>>>> Seleccione una opcion disponible <<<<<\n")



def act1(Claves):
    nombresM = ["Carlos","Juan","Pedro","Alejandro","Alexis","Paul","Rodrigo","Rogelio","Daniel","Angel"]
    nombresF = ["Alexis","Damaris","Alejandra","Karla","Dayana","Paula","Daniela","Marisa","Sara","Dora"]
    nombresO = nombresM + nombresF
    Apellidos = ["Hernandez","Perez","Huerta","Bermudez","Lopez","Gonzales","Rodriguez","Sanchez","Ramirez"]

    while True:
        Clave = random.randint(1,500)
        if Clave in Claves:
            pass
        else:
            break

    select = random.randint(1,3)
    if select == 1:
        Genero = "Masculino"
    elif select == 2:
        Genero = "Femenino"
    else:
        Genero = "Otro"

    if Genero == 1:
        Nombre = random.choice(nombresM)
    if Genero == 2:
        Nombre = random.choice(nombresF)
    else:
        Nombre = random.choice(nombresO)
    
    ApellidoPat = random.choice(Apellidos)
    ApellidoMat = random.choice(Apellidos)

    Crear_Auto = {'Clave':Clave,
                  'Nombre':Nombre,
                  'Apellido Paterno':ApellidoPat,
                  'Apellido Materno':ApellidoMat,
                  'Genero':Genero}

    return Crear_Auto, Clave

def buscar(Lista, maxi):
    stop = 0
    cont = 1
    if maxi == 0:
        return "NoHay"
    while True:
        try:
            buscar = int(input("Cual es el ID?: "))
        except ValueError:
            print("Error en la busqueda, seleccione un numero entero mayor a 0")
        else:
            if buscar < 1:
                return None
            while True:
                for x in Lista:
                    if cont == maxi + 1:
                        return None
                    for key,value in x.items():
                        if buscar == value:
                            return(cont)
                        else:
                            cont = cont + 1
                            break

def comprobador(archi):
    return os.path.isfile(archi)

main()