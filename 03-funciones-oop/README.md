# Sesión 03: Funciones y OOP

## Presentación
Las diapositivas mostradas durante esta sesión se encuentran [aquí.](diapositivas-03-funciones-oop.pdf)

## Temario
1. [Iteradores](#iteradores)
2. [Funciones](#Funciones)
	1. [Estructura](#estructura)
	2. [Argumentos](#argumentos)
	3. [`return`](#return)
	4. [`*args`](#*args)
	5. [`**kwargs`](#**kwargs)
3. [OOP](#oop)
	1. [Clases](#clases)
	2. [Métodos](#métodos)
	3. [`self`](#self)
	4. [Constructor `__init__`](#constructor-__init__)
	5. [Sobrecarga de operadores](#sobrecarga-de-operadores)
4. [Ejemplos](#ejemplos)

## 1. Iteradores
Los iteradores son objetos que contienen un número contable
de valores. Son objetos que pueden ser iterados para recorrer
todos los valores de los mismos.  
- `range()`

## 2. Funciones
Las funciones son bloques de código reutilizable generalmente
asociado a un nombre o _identificador_.  
Ejemplos de ellas son:
- `print()`
- `input()`

### Estructura
Para declara una función escribimos `def` seguido del _nombre_ a 
asignarle a su vez seguido paréntesis y del caracter de inicio de bloque
(`:`). 
El código que contiene es ahora delimitado por sangría:
```python
def hello_world():
	hi = "Hello World!"
	print(hi)
```

### Argumentos
Los _argumentos_ pasados a una función son variables que se copian a
la función para ser utilizadas por la misma. Para pasar un _parámetro_
a una función debemos nombrarlo entre los paréntesis de la función.
```python
def greet(name):
	print(f"Hola, {name}")
```
También se pueden definir valores _default_ para los argumentos de las
funciones. Estos son los valores a tomarse en caso de no recibir algún
valor en esa posición:
```python
def add_n(i, n=1):
	temp = i + n
```

### `return`
La palabra reservada `return` se utiliza para _devolver_ valores desde
una función, para poder ser utilizados fuera de la misma.
```python
my_int = 9
def add_n(i, n=1):
	temp = i + n
	return temp
```

### `return` múltiple
Abusando un poco de las `tuple` y _unpacking_ de python, podemos hacer
`return` de más de un valor a la vez:
```python
	def create_pepe():
		name = "José"
		age = "20"
		country = "México"
		return name, age, country
	# unpacking de los valores:
	nombre, edad, país = create_pepe()
``` 

### `*args`
Si definimos una función que toma un argumento `*args`, agregará los 
_parámetros_ pasados desde esa posición en adelante a una lista `args`:
```python
def f(*args):
	s = 0
	for x in args:
		s += x
	return s
result = f(1, 2, 3, 4, 5) 
``` 

### `**kwargs`
Si definimos una función que toma un argumento `**kwargs`, agregará los
_parámetros_ nombrados pasados de ese punto en adelante a un diccionario 
`kwargs`:
```python
def grades_by_subject(**kwargs):
	for subject, grade in kwargs.items():
		print(f"{subject}: {grade}")
```

## OOP
La _programación orientada a objetos_ es el paradigma de programación más
prevalente actualmente. Consiste en modelar el problema como una serie de
unidades u _objetos_ con _propiedades_ y _métodos_ interactuando entre sí.
on

### Clases
Para definir un objeto o `class` en Python, escribimos `class` seguido del
_nombre_ de la clase y del caracter de incio de bloque:
```python
class Person:
```

### Métodos
Las clases pueden tener _métodos_ asignadas a ellas. Estos son funciones que
se ejecutan con la notación de punto (`clase.método()`). Estas son funciones
declaradas dentro de la misma clase:
```python
class Person:
	def say_name(self):
		print(f"Mi nombre es {self.name}")
```

### `self`
En el anterior ejemplo se definió que el método `say_name(self)` toma un _argumento_
`self`. Este argumento siempre es el primero. Es el argumento que representa al
objeto mismo dentro de la función, es la forma que utilizamos para interactuar con
las propiedades internas del método.

### Constructor `__init__()`
El método `__init__()` es una parte esencial de toda clase. Es el método que se ejecuta
cuando una clase se _instancia_. Este método generalmente se utiliza para asignar las
propiedades iniciales de una clase:
```python
class Person:
	def __init__(self, name=None, age=None, country=None):
		self.name = name
		self.age = age
		self.country = country
```

### Sobrecarga de Operadores
En python, los operadores llaman métodos de los objetos parámetro. Esto significa que
la sobrecarga de operadores se puede ejecutar de manera fácil y elegante, símplemente
definiendo los métodos pertinentes del objeto en cuestión:
```python
class Person:
	def __init__():
		...
	def __add__(self, other):
		return self.age + other.age
```

## Ejemplos
1. Ejemplo de [tabla de frecuencia](examples/freq_table.py)