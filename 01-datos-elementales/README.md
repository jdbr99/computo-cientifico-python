# Primer Sesión del Curso de Cómputo Científico con Python

## Diapositivas de la Sesión
Las diapositivas mostradas durante la sesión se encuentran 
[aquí](https://slides.com/jdbr99/computo-cientifico-con-python-3#/).

## Temas a Ver:
- [x] ¿Qué es Python?
- [x] ¿Por qué programar?
- [x] Instalación de Python y `pip`
- [ ] Creación de Entornos Virtuales con `venv`
- [x] Editores de texto e IDE recomendados
- [x] Tipos de Datos Elementales en Python

## Uso de la Terminal
La terminal es una herramienta que nos resultará indispensable durante el curso.
Es por ello importante saber encontrarla en nuestro SO y algunos comandos 
básicos. A continuación se encuentran enlistados los comando básicos de las
terminales de SO de familia *nix y Windows:

### Windows
Para ejecutar la consola se cuenta con dos opciones:
1. Buscar en el menú de Windows `cmd` y seleccionar la opción que dice 
*Command Prompt* o *Símbolo del Sistema*.
2. Presionar las teclas `windows + r`. Eso abrirá el cuadro de *correr*. En
la caja de diálogo se debe escribir `cmd` y presionar en *Ok*.
Los principales comandos de la terminal de windows son:
- `cd [Nombre del directorio]` - Ingresa al directorio especificado
- `dir` - Imprime la estructura del directorio actual
- `mkdir [Nombre del directorio]` - Crea un directorio con el nombre especificado
- `rmdir [Nombre del directorio]` - Borra el directorio especificado
[Este cortovideo]() contiene un poco más información sobre los comandos mostrados.

### Mac OS X en adelante
Para abrir la terminal, podemos ejecutar *Spotlight* (⌘ + [Barra Espaciadora])
y buscar `Terminal`. Los comandos serán los de sistemas *nix que se encuentran 
enlistados en la siguiente sección.

### Comandos para sistemas *nix
- `ls` - Enlista los archivos del directorio actual
- `cd [Nombre del directorio]` - Ingresa al directorio especificado
- `mkdir [Nombre del directorio]` - Crea un directorio con el nombre especificado.
- `rm [Nombre de archivo]` - Borra el archivo especificado (directorios con `-r`).   

## Hello World
La versión del clásico programa introductorio de programación, *Hello, world!*
es demasiado sencilla en Python. Debido a esto, la versión mostrada es
ligeramente más complicada y por ende más *divertida*.
```python
name = input("¿Cómo te llamas?")
print(f"Hola, {name}")
```

## Tipos de Datos Elementales, Operaciones Aritméticas y Comparaciones  
El archivo [tipos_elementales.py](./tipos_elementales.py) contiene ejemplos de
cuáles son los tipos de datos elementales, algunas operacionesaritméticas y
comparaciones en `Python 3`.