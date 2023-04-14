error_validacion="la opcion no es válida"

def imprimir_menu():
    print("Este es el menú de ordenamiento de archivos: ")
    print("1. Introduce el directorio a ordenar")
    print("2. Simular ordenamiento")
    print("3. Ejecutar ordenamiento")
    print("4. Salir del programa" )

def menu():
    opcion=0
    while opcion<4:
        imprimir_menu()
        opcion=validar_opcion("Elije una opcion: ")
    
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