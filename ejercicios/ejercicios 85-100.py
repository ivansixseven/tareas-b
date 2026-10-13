import math

NOTA_APROBACION = 51  # escala 0-100 (cambia a 60 si tu escala es distinta)


# ---------- utilidades de lectura con validacion ----------
def leer_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("  Valor invalido, intenta de nuevo.")


def leer_int(msg, minimo=None):
    while True:
        try:
            n = int(input(msg))
            if minimo is not None and n < minimo:
                print(f"  Debe ser >= {minimo}.")
                continue
            return n
        except ValueError:
            print("  Ingresa un numero entero.")


# ---------- 86 ----------
def ej86():
    pares = impares = 0
    for i in range(10):
        n = leer_int(f"Numero {i + 1}: ")
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"Pares: {pares} | Impares: {impares}")


# ---------- 87 ----------
def ej87():
    for i in range(10):
        n = leer_float(f"Numero {i + 1}: ")
        if i == 0:
            mayor = menor = n  # asignar
        else:
            if n > mayor:
                mayor = n
            if n < menor:
                menor = n
    print(f"Mayor: {mayor} | Menor: {menor}")


# ---------- 88 ----------
def ej88():
    N = leer_int("Cuantos numeros? ", 1)
    suma = 0  # acumulador
    for i in range(N):
        suma += leer_float(f"Numero {i + 1}: ")
    print(f"Suma: {suma} | Promedio: {suma / N:.2f}")


# ---------- 89 ----------
def ej89():
    N = leer_int("Cuantos numeros? ", 1)
    pos = neg = cero = 0
    for i in range(N):
        n = leer_float(f"Numero {i + 1}: ")
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            cero += 1
    print(f"Positivos: {pos} | Negativos: {neg} | Ceros: {cero}")


# ---------- 90 ----------
def ej90():
    while True:
        n = leer_int("Numero para la tabla de multiplicar: ")
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
        if input("Otra tabla? (s/n): ").strip().lower() != "s":
            break


# ---------- 91 ----------
def ej91():
    while True:
        print("\nCALCULADORA: 1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
        op = input("Opcion: ").strip()
        match op:
            case "1" | "2" | "3" | "4":
                a = leer_float("Primer numero: ")
                b = leer_float("Segundo numero: ")
                if op == "1":
                    print("Resultado:", a + b)
                elif op == "2":
                    print("Resultado:", a - b)
                elif op == "3":
                    print("Resultado:", a * b)
                else:
                    print("Resultado:", a / b if b != 0 else "No se puede dividir entre 0")
            case "5":
                print("Hasta luego.")
                break
            case _:
                print("Opcion invalida.")


# ---------- 92 ----------
def ej92():
    while True:
        print("\nFIGURAS: 1.Cuadrado 2.Rectangulo 3.Triangulo 4.Circulo 5.Salir")
        op = input("Opcion: ").strip()
        match op:
            case "1":
                l = leer_float("Lado: ")
                print(f"Area: {l ** 2:.2f}")
            case "2":
                b = leer_float("Base: ")
                h = leer_float("Altura: ")
                print(f"Area: {b * h:.2f}")
            case "3":
                b = leer_float("Base: ")
                h = leer_float("Altura: ")
                print(f"Area: {b * h / 2:.2f}")
            case "4":
                r = leer_float("Radio: ")
                print(f"Area: {math.pi * r ** 2:.2f}")
            case "5":
                break
            case _:
                print("Opcion invalida.")


# ---------- 93 ----------
def ej93():
    print("Ingresa notas (usa -1 para finalizar).")
    suma = cantidad = 0
    mayor = menor = None
    nota = leer_float("Nota: ")
    while nota != -1:
        if nota < 0 or nota > 100:
            print("  Nota fuera de rango (0-100).")
        else:
            suma += nota
            cantidad += 1
            if mayor is None or nota > mayor:
                mayor = nota
            if menor is None or nota < menor:
                menor = nota
        nota = leer_float("Nota: ")
    if cantidad > 0:
        print(f"Promedio: {suma / cantidad:.2f} | Mayor: {mayor} | Menor: {menor}")
    else:
        print("No se ingresaron notas.")


# ---------- 94 ----------
def ej94():
    mayores = menores = 0
    edad = leer_int("Edad (0 para terminar): ", 0)
    while edad != 0:
        if edad >= 18:
            mayores += 1
        else:
            menores += 1
        edad = leer_int("Edad (0 para terminar): ", 0)
    print(f"Mayores de edad: {mayores} | Menores de edad: {menores}")


# ---------- 95 ----------
def ej95():
    pares = impares = pos = neg = 0
    n = leer_int("Numero (0 para terminar): ")
    while n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        if n > 0:
            pos += 1
        else:
            neg += 1
        n = leer_int("Numero (0 para terminar): ")
    print(f"Pares: {pares} | Impares: {impares} | Positivos: {pos} | Negativos: {neg}")


# ---------- 96 ----------
def ej96():
    total = 0  # acumulador
    while True:
        print("\n1.Agregar producto  2.Finalizar")
        op = input("Opcion: ").strip()
        match op:
            case "1":
                nombre = input("Producto: ")
                precio = leer_float("Precio: ")
                if precio < 0:
                    print("  Precio invalido.")
                else:
                    total += precio
                    print(f"  {nombre} agregado. Subtotal: {total:.2f}")
            case "2":
                print(f"TOTAL A PAGAR: {total:.2f}")
                break
            case _:
                print("Opcion invalida.")


# ---------- 97 ----------
def ej97():
    saldo = 0.0
    while True:
        print("\nBANCO: 1.Consultar saldo 2.Depositar 3.Retirar 4.Salir")
        op = input("Opcion: ").strip()
        match op:
            case "1":
                print(f"Saldo actual: {saldo:.2f}")
            case "2":
                m = leer_float("Monto a depositar: ")
                if m > 0:
                    saldo += m
                    print(f"Deposito exitoso. Saldo: {saldo:.2f}")
                else:
                    print("El monto debe ser positivo.")
            case "3":
                m = leer_float("Monto a retirar: ")
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
                print("Opcion invalida.")


# ---------- 98 ----------
def ej98():
    aprobadas = reprobadas = 0
    suma = 0
    notas = []
    for i in range(10):
        n = leer_float(f"Nota {i + 1}: ")
        notas.append(n)
        suma += n
        if n >= NOTA_APROBACION:
            aprobadas += 1
        else:
            reprobadas += 1
    print(f"Aprobadas: {aprobadas} ({aprobadas * 10}%)")
    print(f"Reprobadas: {reprobadas} ({reprobadas * 10}%)")
    print(f"Promedio: {suma / 10:.2f} | Mayor: {max(notas)} | Menor: {min(notas)}")


# ---------- 99 ----------
def ej99():
    N = leer_int("Cuantas edades? ", 1)
    ninos = adolescentes = adultos = mayores = 0
    for i in range(N):
        e = leer_int(f"Edad {i + 1}: ", 0)
        if e <= 11:
            ninos += 1
        elif e <= 17:
            adolescentes += 1
        elif e <= 59:
            adultos += 1
        else:
            mayores += 1
    print(f"Ninos (0-11): {ninos}")
    print(f"Adolescentes (12-17): {adolescentes}")
    print(f"Adultos (18-59): {adultos}")
    print(f"Adultos mayores (60+): {mayores}")


# ---------- 100 ----------
def ej100():
    while True:
        print("\n1.Factorial 2.Tabla de multiplicar 3.Paridad 4.Cuadrado 5.Salir")
        op = input("Opcion: ").strip()
        match op:
            case "1":
                n = leer_int("Numero: ", 0)
                print(f"{n}! = {math.factorial(n)}")
            case "2":
                n = leer_int("Numero: ")
                for i in range(1, 11):
                    print(f"{n} x {i} = {n * i}")
            case "3":
                n = leer_int("Numero: ")
                print("Par" if n % 2 == 0 else "Impar")
            case "4":
                n = leer_float("Numero: ")
                print(f"{n}^2 = {n ** 2}")
            case "5":
                break
            case _:
                print("Opcion invalida.")


# ---------- menu principal ----------
EJERCICIOS = {
    86: ej86, 87: ej87, 88: ej88, 89: ej89, 90: ej90,
    91: ej91, 92: ej92, 93: ej93, 94: ej94, 95: ej95,
    96: ej96, 97: ej97, 98: ej98, 99: ej99, 100: ej100,
}

if __name__ == "__main__":
    while True:
        n = leer_int("\nNumero de ejercicio (86-100, 0 para salir): ", 0)
        if n == 0:
            break
        if n in EJERCICIOS:
            print(f"\n--- Ejercicio {n} ---")
            EJERCICIOS[n]()
        else:
            print("Ejercicio fuera de rango.")

