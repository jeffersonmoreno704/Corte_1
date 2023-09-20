# Creamos la funcion de la suma de Fibonacci
def suma_fibonacci(n):
    if n == 0 or n == 1:
        return n

    a = 1
    b = 1
    suma = a + b

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        suma += c

    return suma

# Solicitar el número de términos
n = int(input("Ingresa el número de términos: "))

# Calcular la suma
suma = suma_fibonacci(n)

# Imprimir el resultado con f string
print(f"La suma de los primeros {n} términos de la serie Fibonacci es: {suma}")

