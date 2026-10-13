# 100. Menú para factorial, tabla de multiplicar, paridad y cuadrado; repetir hasta Salir. Usar: Repetir + Según + Si.
import math
import sys


def leer(msg, tipo=int, minimo=None):
    while True:
        try:
            v = tipo(input(msg))
            if minimo is not None and v < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return v
        except ValueError:
            print("Valor inválido.")


def main():
    while True:
        print("\n1.Factorial 2.Tabla de multiplicar 3.Paridad 4.Cuadrado 5.Salir")
        op = input("Opción: ").strip()
        match op:
            case "1":
                n = leer("Número: ", int, 0)
                print(f"{n}! = {math.factorial(n)}")
            case "2":
                n = leer("Número: ")
                for i in range(1, 11):
                    print(f"{n} x {i} = {n * i}")
            case "3":
                n = leer("Número: ")
                print("Par" if n % 2 == 0 else "Impar")
            case "4":
                n = leer("Número: ", float)
                print(f"{n}^2 = {n ** 2}")
            case "5":
                break
            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    main()
    sys.exit(0)
