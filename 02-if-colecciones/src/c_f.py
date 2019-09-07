# Imprimimos mensaje de bienvenida
print("Convertidor de ºC -> ºF")

# Pedimos al usuario entrada
print("Ingrese cantidad de ºC")
c = input("> ")

# Hacemos casting a `float`
c = float(c)

# Aplicamos la fórmula
f = (c * (9/5)) + 32

# Mostramos salida al usuario
print(f"{c}ºC = {f}ºF")