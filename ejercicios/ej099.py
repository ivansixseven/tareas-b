# 99. Leer N edades y contar niños, adolescentes, adultos y adultos mayores. Usar: Para + Si.
import sys


def leer(msg, minimo=0):
    while True:
        try:
            v = int(input(msg))
            if v < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return v
        except ValueError:
            print("Ingresa un número entero.")


def main():
    N = leer("¿Cuántas edades? ", 1)
    ninos = adolescentes = adultos = mayores = 0
    for i in range(N):
        e = leer(f"Edad {i + 1}: ")
        if e <= 11:
            ninos += 1
        elif e <= 17:
            adolescentes += 1
        elif e <= 59:
            adultos += 1
        else:
            mayores += 1
    print(f"Niños (0-11): {ninos}")
    print(f"Adolescentes (12-17): {adolescentes}")
    print(f"Adultos (18-59): {adultos}")
    print(f"Adultos mayores (60+): {mayores}")


if __name__ == "__main__":
    main()
    sys.exit(0)
