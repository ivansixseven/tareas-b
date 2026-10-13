# 94. Registrar edades hasta ingresar 0 y determinar cantidad de mayores y menores. Usar: Mientras + Si.
import sys


def leer(msg):
    while True:
        try:
            v = int(input(msg))
            if v < 0:
                print("La edad no puede ser negativa.")
                continue
            return v
        except ValueError:
            print("Ingresa un número entero.")


def main():
    mayores = menores = 0
    edad = leer("Edad (0 para terminar): ")
    while edad != 0:
        if edad >= 18:
            mayores += 1
        else:
            menores += 1
        edad = leer("Edad (0 para terminar): ")
    print(f"Mayores de edad: {mayores} | Menores de edad: {menores}")


if __name__ == "__main__":
    main()
    sys.exit(0)
