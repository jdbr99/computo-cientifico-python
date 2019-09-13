# Escribir código que genere una lista 5...30 con cada número
# elevado a la 5

# Escribir un diccionario que haga lo mismo que arriba pero 
# imprimiendo la relación valor - valor^5
list_sliced = list
dict = {num: num**5 for num in range(5, 31)}
for key, val in dict.items():
    print(key, val)