from directorio import Directorio
from simular_ordenamiento import SimularOrdenamiento
from generar_ordenamiento import GenerarOrdenamiento


error_validacion="la opcion no es válida"

def imprimir_menu():
    print("\nEste es el menú de ordenamiento de archivos: ")
    print("1. Introduce el directorio a ordenar")
    print("2. Simular ordenamiento")
    print("3. Ejecutar ordenamiento")
    print("4. Salir del programa" )

def menu():
    opcion=0
    directorio=Directorio()
    simular_ordenamiento=SimularOrdenamiento()
    generar_ordenamiento=GenerarOrdenamiento()
    while opcion<4:
        imprimir_menu()
        opcion=validar_opcion("Elije una opcion: ")
        if opcion==1:
            directorio.capturar_directorio()
        if opcion==2:
            if len(directorio.archivos) > 0:
                simular_ordenamiento.procesar(directorio.archivos)
            else:
                print("El directorio no contiene archivo a ordenar")
        if opcion==3:
            if len(directorio.archivos) > 0:
                generar_ordenamiento.procesar(directorio)
            else:
                print("El directorio no contiene archivo a ordenar")

    
    print("\n ¡Gracias por utilizar este programa!")

def validar_opcion(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except:
            print(error_validacion)        

if __name__=="__main__":
    menu()