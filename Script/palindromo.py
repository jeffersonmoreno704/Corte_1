# Asignamos dos variables en 0 que serán los contadores
igual, aux = 0, 0

# Tomamos datos por consola
texto = input("Ingrese la palabra que desea evaluar: ")

# Iteramos sobre el rango inverso de los índices del texto
for ind in reversed(range(0, len(texto))):
    # Comparamos los caracteres en posiciones correspondientes
    if texto[ind].lower() == texto[aux].lower():
        igual += 1
    aux += 1

# Comprobamos si el número de caracteres iguales es igual a la longitud total del texto
if len(texto) == igual:
    print("El texto es un palíndromo!")
else:
    print("El texto no es un palíndromo!")