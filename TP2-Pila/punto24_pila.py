from stack import Stack

pila = Stack()
pila.push({"nombre": "Iron Man", "peliculas": 10})
pila.push({"nombre": "Capitan America", "peliculas": 7})
pila.push({"nombre": "Rocket Raccoon", "peliculas": 5})
pila.push({"nombre": "Black Widow", "peliculas": 6})
pila.push({"nombre": "Groot", "peliculas": 4})
pila.push({"nombre": "Doctor Strange", "peliculas": 3})

def posiciones(pila, buscados):
    aux = Stack()
    pos = {}
    i = 1
    while pila.size() > 0:
        p = pila.pop()
        if p["nombre"] in buscados:
            pos[p["nombre"]] = i
        aux.push(p)
        i += 1
    while aux.size() > 0:
        pila.push(aux.pop())
    return pos


def mas_de_5(pila):
    aux = Stack()
    r = []
    while pila.size() > 0:
        p = pila.pop()
        if p["peliculas"] > 5:
            r.append((p["nombre"], p["peliculas"]))
        aux.push(p)
    while aux.size() > 0:
        pila.push(aux.pop())
    return r

def black_widow(pila):
    aux = Stack()
    cant = 0
    while pila.size() > 0:
        p = pila.pop()
        if p["nombre"] == "Black Widow":
            cant = p["peliculas"]
        aux.push(p)
    while aux.size() > 0:
        pila.push(aux.pop())
    return cant

def por_letra(pila, letras):
    aux = Stack()
    r = []
    while pila.size() > 0:
        p = pila.pop()
        if p["nombre"][0].upper() in letras:
            r.append(p["nombre"])
        aux.push(p)
    while aux.size() > 0:
        pila.push(aux.pop())
    return r

pos = posiciones(pila, ["Rocket Raccoon", "Groot"])
print("Rocket Raccoon está en la posición", pos["Rocket Raccoon"])
print("Groot está en la posición", pos["Groot"])

print("Personajes con más de 5 películas:")
for nombre, cant in mas_de_5(pila):
    print(nombre, ":", cant, "películas")

bw = black_widow(pila)
print("Black Widow participó en", bw, "películas")

print("Personajes que empiezan con C, D o G:")
for nombre in por_letra(pila, {"C", "D", "G"}):
    print(nombre)