# Creamos la clase figura
class Figura:
    # Creamos el constructor y le damos dos tributos y los inicializamos
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    # Metodo dibujar que imprime el nombre y el color de la figura
    def dibujar(self):
        print(f"Figura {self.nombre} de color {self.color}")

# Creamos la clase Cirulo que ereda los atributos de 'figura'
class Círculo(Figura):
    def __init__(self, nombre, color, radio):
        # Llama al método __init__() de la clase base y heredamos
        super().__init__(nombre, color)
        self.radio = radio
    # Metodo dibujar() imprime el radio de la clase figura
    def dibujar(self):
        print(f"Radio: {self.radio}")

# Crea una instancia de la clase figura y circulo
figura = Figura("Romboide","Verde")
circulo = Círculo("Semicirculo", "Morado", 100)

# Imprime los atributos de las instancias
print(f"Figura: {figura.nombre}\nColor: {figura.color}")
print(f"\nCirculo: {circulo.nombre}\nColor: {circulo.color}\nRadio°: {circulo.radio}")
