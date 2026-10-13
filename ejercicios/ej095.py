# 95. Leer números hasta 0 y determinar pares, impares, positivos y negativos. Usar: Mientras + operadores.
import sys


def leer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Ingresa un número entero.")


def main():
    pares = impares = pos = neg = 0
    n = leer("Número (0 para terminar): ")
    while n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        if n > 0:
            pos += 1
        else:
            neg += 1
        n = leer("Número (0 para terminar): ")
    print(f"Pares: {pares} | Impares: {impares} | Positivos: {pos} | Negativos: {neg}")


if __name__ == "__main__":
    main()
    sys.exit(0)
