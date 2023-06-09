# Proyecto de ordenamiento de archivos

Repositorio público del proyecto final del Bootcamp de Python de código facilito

## Version de Python

    3.10.9


## Requerimientos

El programa debe cumplir con los siguientes requerimientos:

1. El programa deberá poder ejecutarse directamente en terminal
2. El usuario podrá ingresar (via teclado) el directorio que desea ordenar
3. Una vez el programa finalice, se mostrarán en pantalla todas las nuevas carpetas creadas.
4. El nombre de las carpetas deberá ser en plural. (pdfs - pngs - txts)
5. El programa será capaz de clasificar los archivos en nuevas carpetas

## Funcionamiento 

Se le mostrará en la pantalla al usuario el siguiente menú:

```bash
Este es el menú de ordenamiento de archivos:
1. Introduce el directorio a ordenar
2. Simular ordenamiento
3. Ejecutar ordenamiento
4. Salir del programa
Elije una opcion:
```

Con la opcion 1
Es necesario que el usuario introduzca un  directorio válido y que realmente contenga archivos para poder ser ordenado.

Con la opcion 2
Simular ordenamiento le permite ver al usuario lo que haria el ordenamiento de archivos

Con la opcion 3
Se ejecuta el ordenamiento y los archivos son agrupados en las carpetas correspondientes

Con la opcion 4
El programa termina


## Proceso de desarrollo

### Día 1 
1. Crear repositorio git público
2. Clonarlo en mi local
3. Crear menú del sistema

Desafios: El sistema me envio mensajes de instalación de git

### Día 2
1. Capturar el directorio
2. Validar que exista el directorio
3. Recorrer todos los archivos 
4. Almacenarlos en una lista

Desafios
1. Encontrar las funciones adecuadas para capturar los archivos
2. Debugear el programa

### Día 3
1. Encontrar extensiones de archivos
2. Crear una lista con los plurales de las extensiones
3. Crear la simulación de ordenamiento

Desafios 
1. Crear un diccionario para agrupar los archivos en un directorio

### Dia 4
1. Generar el ordenamiento de los archivos
2. Crear carpetas
3. Mover los archivos

Desafios
1. La libreria shutil y entender de mejor manera los diccionarios y listas

## Agradecimientos

A mis maestros por dar buenas clases