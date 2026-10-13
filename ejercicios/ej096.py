# 96. Ingresar productos y precios hasta seleccionar Finalizar. Mostrar total. Usar: Repetir + Según + acumulador.
import sys


def leer(msg):
    while True:
        try:
            v = float(input(msg))
            if v < 0:
                print("El precio no puede ser negativo.")
                continue
            return v
        except ValueError:
            print("Ingresa un número válido.")


def main():
    total = 0  # acumulador
    while True:
        print("\n1.Agregar producto  2.Finalizar")
        op = input("Opción: ").strip()
        match op:
            case "1":
                nombre = input("Producto: ")
                total += leer("Precio: ")
                print(f"{nombre} agregado. Subtotal: {total:.2f}")
            case "2":
                print(f"TOTAL A PAGAR: {total:.2f}")
                break
            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    main()
    sys.exit(0)
