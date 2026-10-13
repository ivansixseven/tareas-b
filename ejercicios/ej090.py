# 90. Mostrar la tabla de multiplicar de un número y permitir repetir el proceso. Usar: Repetir + Para.
import sys


def leer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Ingresa un número entero.")


def main():
    while True:
        n = leer("Número para la tabla de multiplicar: ")
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
        if input("¿Otra tabla? (s/n): ").strip().lower() != "s":
            break


if __name__ == "__main__":
    main()
    sys.exit(0)
