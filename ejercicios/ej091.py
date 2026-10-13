# 91. Calculadora que permita realizar operaciones hasta seleccionar Salir. Usar: Repetir + Según.
import sys


def leer(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Ingresa un número válido.")


def main():
    while True:
        print("\nCALCULADORA: 1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
        op = input("Opción: ").strip()
        match op:
            case "1":
                print("Resultado:", leer("Primer número: ") + leer("Segundo número: "))
            case "2":
                print("Resultado:", leer("Primer número: ") - leer("Segundo número: "))
            case "3":
                print("Resultado:", leer("Primer número: ") * leer("Segundo número: "))
            case "4":
                a = leer("Primer número: ")
                b = leer("Segundo número: ")
                print("Resultado:", a / b if b != 0 else "No se puede dividir entre 0")
            case "5":
                print("Hasta luego.")
                break
            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    main()
    sys.exit(0)
