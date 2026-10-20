class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento;
        # controla el caso de pila vacía
        if not self.items:
            print("La pila está vacía")
            return None
        return self.items.pop()

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento;
        # controla el caso de cola vacía
        if not self.items:
            print("La cola está vacía")
            return None
        return self.items.pop(0)

# Agrega tus pruebas debajo. Usa los datos asignados en tu versión.

datos = [("CI01", "Sala 1"), ("CI02", "Sala 2"), ("CI03", "Sala 3")]

print("=== Lista enlazada ===")
lista = ListaEnlazada()
for codigo, descripcion in datos:
    lista.agregar(codigo, descripcion)
lista.mostrar()

print("\n=== Pila (LIFO) ===")
pila = Pila()
for dato in datos:
    pila.apilar(dato)
for _ in range(3):
    print("Desapilado:", pila.desapilar())
pila.desapilar()  # prueba de pila vacía

print("\n=== Cola (FIFO) ===")
cola = Cola()
for dato in datos:
    cola.encolar(dato)
print("Desencolado:", cola.desencolar())
print("Desencolado:", cola.desencolar())

# Reto individual: elementos que quedan en la cola
print("\nElementos que quedan en la cola:")
for codigo, descripcion in cola.items:
    print(codigo, descripcion)

print("\nDesencolado:", cola.desencolar())
cola.desencolar()  # prueba de cola vacía