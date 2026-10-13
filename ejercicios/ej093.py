# 93. Solicitar notas hasta finalizar y calcular promedio, mayor y menor. Usar: Mientras + Si.
import sys


def leer(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Ingresa un número válido.")


def main():
    print("Ingresa notas (escribe -1 para finalizar).")
    suma = cantidad = 0
    mayor = menor = None
    nota = leer("Nota: ")
    while nota != -1:
        if nota < 0 or nota > 100:
            print("Nota fuera de rango (0-100).")
        else:
            suma += nota
            cantidad += 1
            if mayor is None or nota > mayor:
                mayor = nota
            if menor is None or nota < menor:
                menor = nota
        nota = leer("Nota: ")
    if cantidad > 0:
        print(f"Promedio: {suma / cantidad:.2f} | Mayor: {mayor} | Menor: {menor}")
    else:
        print("No se ingresaron notas.")


if __name__ == "__main__":
    main()
    sys.exit(0)
