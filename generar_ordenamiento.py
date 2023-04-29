from simular_ordenamiento import SimularOrdenamiento
from directorio import Directorio
import shutil
import os


class GenerarOrdenamiento:

    def procesar(self, directorio: Directorio):

        if directorio.directorio_valido:
            simular_ordenamiento = SimularOrdenamiento()
            carpetas = simular_ordenamiento.procesar(directorio.archivos)

            for carp, lista_arch in carpetas.items():
                nuevo_directorio = os.path.join(directorio.ruta_directorio, carp)
                os.mkdir(nuevo_directorio)

                for archivo in lista_arch:
                    destino = os.path.join(nuevo_directorio, archivo.name)
                    shutil.move(archivo.path, destino)
            
            print("El directorio fue ordenado satisfactoriamente. ¡Felicidades!")
        else:
            print("El directorio que se quiere procesar no es válido")