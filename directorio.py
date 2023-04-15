import os

class Directorio:
    def __init__(self) -> None:
        self._ruta_directorio=""
        self._directorio_valido=False
        self._archivos=[]

    def _valida_directorio(self):
        if os.path.isdir(self._ruta_directorio):
            print(f"\nEl directorio {self._ruta_directorio} fue capturado correctamente" )
            self._directorio_valido=True
        else: 
            print("\nDirectorio invalido")
            self._directorio_valido=False

    def _capturar_archivos(self, ruta_directorio):
        with os.scandir(ruta_directorio) as archivos:
            archivos_en_dir = [archivo for archivo in archivos if archivo.is_file()]
            for archivo in archivos_en_dir:
                self._archivos.append(archivo)

        with os.scandir(ruta_directorio) as subdirs:
            subdirectorios =  [subdir for subdir in subdirs if subdir.is_dir()]
            for subdir in subdirectorios:
                self._capturar_archivos(subdir.path)
        
        print(self._archivos)
        return

    def capturar_directorio(self):
        self._ruta_directorio=input("\nteclea el directorio a ordenar: ")
        self._valida_directorio()
        if self._directorio_valido:
            self._capturar_archivos(self._ruta_directorio)
