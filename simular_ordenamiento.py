import re

class SimularOrdenamiento:

    def _extraer_extension(self,nombre_archivo):
        patron=r"\.([a-z]+)"
        respuesta= re.search(patron, nombre_archivo)
        return respuesta.group()[1:]
        

    def procesar(self, archivos):        
        lista_extensiones =[]

        for archivo in archivos:
            extension = self._extraer_extension(archivo.name)
            lista_extensiones.append(extension)

        lista_extensiones = list(set(lista_extensiones))    

    
        dict_carpetas = {}
        for extension in lista_extensiones:
            lista_arch_carpeta = []
            lista_name_arch = []
            dir_key = extension + "s"

            for archivo in archivos:
                ext_archivo = self._extraer_extension(archivo.name)
                if extension == ext_archivo:
                    lista_name_arch.append(archivo.name)
                    lista_arch_carpeta.append(archivo)


            
            dict_carpetas[dir_key] = lista_arch_carpeta
            print(f"El directorio a crear es {dir_key} y la lista de archivos que contiene: {lista_name_arch}")

        return dict_carpetas  

