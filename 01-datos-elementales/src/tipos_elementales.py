# Los números enteros se llaman `int`
my_int = 9
print(my_int)
print(f"El tipo de my_int es: {type(my_int)}")
print()

# Los números con decimales se llaman `float`
my_float = 3.14159
print(my_float)
print(f"El tipo de my_float es: {type(my_float)}")
print()

# Los números complejos tienen parte real e imaginaria
my_complex = 9 + 3j
print(my_complex)
print(f"El tipo de my_complex es: {type(my_complex)}")
print()

# Las cadenas de texto se llaman `string`
my_str = "Hola, mundo!"
print(my_str)
print(f"El tipo de my_str es: {type(my_str)}")
print()

# Los booleanos pueden valer `True` o `False`
my_bool = True
print(my_bool)
print(f"El tipo de my_bool es: {type(my_int)}")
print()

# Podemos hacer operaciones con ellos! :D
print(my_int + my_float)

# También es útil, saber cambiar el tipo de dato con el que trabajamos
age = input("¿Cuál es tu edad?: ")
print(age)
print(f"El tipo de age es {type(age)}")
# Notemos que el tipo es `str`, por lo que sumarlo no resultaría en lo esperado
# print(age + 1)
# Debemos hacer un 'cast' para que esto tenga sentido
print(int(age) + 1)