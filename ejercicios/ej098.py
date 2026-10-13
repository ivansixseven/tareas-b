# 98. Ingresar 10 notas, clasificar aprobadas/reprobadas y mostrar estadísticas. Usar: Para + Si.
import sys

NOTA_APROBACION = 51  # escala 0-100


def leer(msg):
    while True:
        try:
            v = float(input(msg))
            if v < 0 or v > 100:
                print("La nota debe estar entre 0 y 100.")
                continue
            return v
        except ValueError:
            print("Ingresa un número válido.")


def main():
    aprobadas = reprobadas = 0
    notas = []
    for i in range(10):
        n = leer(f"Nota {i + 1}: ")
        notas.append(n)
        if n >= NOTA_APROBACION:
            aprobadas += 1
        else:
            reprobadas += 1
    print(f"Aprobadas: {aprobadas} ({aprobadas * 10}%)")
    print(f"Reprobadas: {reprobadas} ({reprobadas * 10}%)")
    print(f"Promedio: {sum(notas) / 10:.2f} | Mayor: {max(notas)} | Menor: {min(notas)}")


if __name__ == "__main__":
    main()
    sys.exit(0)
