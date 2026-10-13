# 87. Leer 10 números y determinar el mayor y menor. Usar: Para + Si + Asignar.
import sys


def leer(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Ingresa un número válido.")


def main():
    mayor = menor = 0
    for i in range(10):
        n = leer(f"Número {i + 1}: ")
        if i == 0:
            mayor = n  # asignar
            menor = n
        else:
            if n > mayor:
                mayor = n
            if n < menor:
                menor = n
    print(f"Mayor: {mayor} | Menor: {menor}")


if __name__ == "__main__":
    main()
    sys.exit(0)
