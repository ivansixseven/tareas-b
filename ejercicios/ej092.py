# 92. Menú de figuras geométricas y calcular áreas repetidamente. Usar: Repetir + Según + Si.
import math
import sys


def leer(msg):
    while True:
        try:
            v = float(input(msg))
            if v <= 0:
                print("Debe ser mayor que 0.")
                continue
            return v
        except ValueError:
            print("Ingresa un número válido.")


def main():
    while True:
        print("\nFIGURAS: 1.Cuadrado 2.Rectángulo 3.Triángulo 4.Círculo 5.Salir")
        op = input("Opción: ").strip()
        match op:
            case "1":
                print(f"Área: {leer('Lado: ') ** 2:.2f}")
            case "2":
                print(f"Área: {leer('Base: ') * leer('Altura: '):.2f}")
            case "3":
                print(f"Área: {leer('Base: ') * leer('Altura: ') / 2:.2f}")
            case "4":
                print(f"Área: {math.pi * leer('Radio: ') ** 2:.2f}")
            case "5":
                break
            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    main()
    sys.exit(0)
