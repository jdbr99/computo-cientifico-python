# Módulos e Introducción a Herramientas para Cómputo Científico

## Presentación
Las diapositivas mostradas durante esta sesión se encuentran [aquí.](diapositivas-04-modulos-anaconda.pdf)

## Temario
1. Módulos
    1. Armado de Módulos
    2. Métodos de Importación
2. Instalación de Anaconda
    1. Administración en Entornos Virtuales
    2. Administración de Paquetes con `conda`
3. Introducción a **Jupyter Notebook**
    1. Ejecución
    2. Guía de Interfáz

## Módulos
En Python, usamos la palabra _modulos_ para referirnos a código _empaquetado_ que se puede consumir (_importar_) para extender las funciones del lenguaje.

### Armado de Módulos
Todo programa de Python es un módulo. Cuando un módulo es importado, todo el código de este es ejecutado, por lo que si se ejecutan funciones en este, las veremos reflejadas en la ejecución de nuestro programa contenedor.

### Métodos de Importación
Existen varias formas de importar un módulo e incluso archivos específicos de un módulo. Las principales son:
- `import <nombre_del_módulo>`
- `import <nombre_del_módulo> as <nombre_reasignado>`
- `from <nombre_del_módulo> import <nombre_del_submódulo>`
- `from <nombre_del_módulo> import <nombre_del_submódulo> as <nombre_reasignado>`

# Introducción a Herramientas de Cómputo Científico

## Instalación de Anaconda
1. Ingresar al [sitio web de _anaconda_](https://anaconda.com).
2. Descargar el instalador para su SO

## Administración de Entornos Virtuales con `conda env`
Crear entornos virtuales nos permite tener diferentes versiones de paquetes y programas instalados en diferentes directorios. Esto es útil para no mezclar las dependencias de algún proyecto con las de los demás y mantener ordenado el sistema.

Para crear un nuevo entorno utilizamos el comando `conda create --name myenv`. Esto crea un entorno virtual nuevo llamado `myenv`. Para activarlo utiizamos el comando `conda activate myenv`.

## Administración de Paquetes con `conda`
Para instalar paquetes utilizando `conda` en el entorno activo, utilizamos el comando `conda install <nombre_del_paquete>`. Para remover un paquete utilizamos `conda remove <nombre_del_paquete>`.

## Introducción a Jupyter Notebook
Jupyter Notebook son una herramienta que nos permite programar de forma literaria. Es por esto que es una gran herramienta para el cómputo científico

### Ejecución de Jupyter Notebook
Para lanzar una instancia de Jupyter Notebook, utilizamos el comando `jupyter notebook` y esperamos a que se abra en nuestro navegador defualt.
