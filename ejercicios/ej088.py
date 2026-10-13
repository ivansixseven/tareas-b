# 88. Leer N números y calcular suma y promedio. Usar: Para + acumulador.
import sys


def leer(msg, tipo=float, minimo=None):
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
    N = leer("¿Cuántos números? ", int, 1)
    suma = 0  # acumulador
    for i in range(N):
        suma += leer(f"Número {i + 1}: ")
    print(f"Suma: {suma} | Promedio: {suma / N:.2f}")


if __name__ == "__main__":
    main()
    sys.exit(0)
