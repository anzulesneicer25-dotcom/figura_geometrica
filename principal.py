
from cuadrado import Cuadrado
from rectangulo import Rectangulo
''' 4. Programa principal: main.py
'''

def sumar_areas(figuras: list):
    return sum(figura.area() for figura in figuras)

def sumar_perimetros(figuras: list):
    return sum(figura.perimetro() for figura in figuras)

if __name__ == "__main__":
    print(" Creación de figuras válidas:")

    cuadrado1 = Cuadrado(4)
    cuadrado2 = Cuadrado(6)

    rectangulo1 = Rectangulo(3, 5)
    rectangulo2 = Rectangulo(2, 7)

    figuras = [cuadrado1, cuadrado2, rectangulo1, rectangulo2]

    for figura in figuras:
        print(figura)
        print(f"Área: {figura.area()}")
        print(f"Perímetro: {figura.perimetro()}")
        print("-" * 30)

    print("Intento de creación inválida:")
    try:
        cuadrado_invalido = Cuadrado(-3)
    except ValueError as error:
        print(f"Error: {error}")

        print("-" * 30)
        print(" Modificación de valores:")
    try:
        cuadrado1.ancho = 15
        cuadrado1.alto = 10
        print(f"Nuevo {cuadrado1}")
        print(f"Área modificada: {cuadrado1.area()}")
        print(f"Perímetro modificado: {cuadrado1.perimetro()}")
    except ValueError as error:
        print(f"Error al modificar: {error}")

    print("-" * 30)
    print("Suma total de áreas:", sumar_areas(figuras))
    print(" Suma total de perímetros:", sumar_perimetros(figuras))