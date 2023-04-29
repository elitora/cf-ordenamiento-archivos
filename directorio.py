import os

class Directorio:
    def __init__(self) -> None:
        self.ruta_directorio=""
        self.directorio_valido=False
        self.archivos=[]

    def _valida_directorio(self):
        if os.path.isdir(self.ruta_directorio):
            print(f"\nEl directorio {self.ruta_directorio} fue capturado correctamente" )
            self.directorio_valido=True
        else: 
            print("\nDirectorio invalido")
            self.directorio_valido=False

    def _capturar_archivos(self, ruta_directorio):
        with os.scandir(ruta_directorio) as archivos:
            archivos_en_dir = [archivo for archivo in archivos if archivo.is_file()]
            for archivo in archivos_en_dir:
                self.archivos.append(archivo)

        with os.scandir(ruta_directorio) as subdirs:
            subdirectorios =  [subdir for subdir in subdirs if subdir.is_dir()]
            for subdir in subdirectorios:
                self._capturar_archivos(subdir.path)
                
        return

    def capturar_directorio(self):
        self.ruta_directorio=input("\nteclea el directorio a ordenar: ")
        self._valida_directorio()
        if self.directorio_valido:
            self._capturar_archivos(self.ruta_directorio)
