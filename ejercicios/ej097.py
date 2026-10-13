# 97. Menú bancario: consultar saldo, depositar, retirar y salir; validar fondos. Usar: Repetir + Según + Si.
import sys


def leer(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Ingresa un número válido.")


def main():
    saldo = 0.0
    while True:
        print("\nBANCO: 1.Consultar saldo 2.Depositar 3.Retirar 4.Salir")
        op = input("Opción: ").strip()
        match op:
            case "1":
                print(f"Saldo actual: {saldo:.2f}")
            case "2":
                m = leer("Monto a depositar: ")
                if m > 0:
                    saldo += m
                    print(f"Depósito exitoso. Saldo: {saldo:.2f}")
                else:
                    print("El monto debe ser positivo.")
            case "3":
                m = leer("Monto a retirar: ")
                if m <= 0:
                    print("El monto debe ser positivo.")
                elif m > saldo:
                    print("Fondos insuficientes.")
                else:
                    saldo -= m
                    print(f"Retiro exitoso. Saldo: {saldo:.2f}")
            case "4":
                print("Gracias por usar el banco.")
                break
            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    main()
    sys.exit(0)
