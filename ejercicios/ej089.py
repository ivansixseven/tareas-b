# 89. Leer N números y determinar cuántos son positivos, negativos y cero. Usar: Para + Si.
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
    pos = neg = cero = 0
    for i in range(N):
        n = leer(f"Número {i + 1}: ")
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            cero += 1
    print(f"Positivos: {pos} | Negativos: {neg} | Ceros: {cero}")


if __name__ == "__main__":
    main()
    sys.exit(0)
