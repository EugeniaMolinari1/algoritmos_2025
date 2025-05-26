from qqueue import Queue

personajes_mcu = [
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
]

def nombre_capitana(cola, nombre_superheroe):
    aux = Queue()
    resultado = None
    while cola.size() > 0:
        dato = cola.attention()
        if dato["superheroe"]== nombre_superheroe:
            resultado = dato["personaje"]
        aux.arrive(dato)
    while aux.size() > 0:
        cola.arrive(aux.attention())
    return resultado

def superheroes_femeninos(cola):
    aux = Queue()
    resultado = []
    while cola.size() > 0:
        dato = cola.attention()
        if dato["genero"] == "F":
            resultado.append(dato["superheroe"])
        aux.arrive(dato)
    while aux.size() > 0:
        cola.arrive(aux.attention())
    return resultado

def personajes_masculinos(cola):
    aux = Queue()
    resultado = []
    while cola.size() > 0:
        dato = cola.attention()
        if dato["genero"] == "M":
            resultado.append(dato["personaje"])
        aux.arrive(dato)
    while aux.size() > 0:
        cola.arrive(aux.attention())
    return resultado

def nombre_ScottLang(cola, nombre_personaje):
    aux = Queue()
    resultado = None
    while cola.size() > 0:
        dato = cola.attention()
        if dato["personaje"] == nombre_personaje:
            resultado = dato["superheroe"]
        aux.arrive(dato)
    while aux.size() > 0:
        cola.arrive(aux.attention())
    return resultado

def nombres_con_s(cola):
    aux = Queue()
    resultado = []
    while cola.size() > 0:
        dato = cola.attention()
        if dato["personaje"][0] == "S" or dato["superheroe"][0] == "S":
            resultado.append(dato)
        aux.arrive(dato)
    while aux.size() > 0:
        cola.arrive(aux.attention())
    return resultado

def carol_danvers(cola):
    aux = Queue()
    superheroe = None
    while cola.size() > 0:
        dato = cola.attention()
        if dato["personaje"] == "Carol Danvers":
            superheroe = dato["superheroe"]
        aux.arrive(dato)
    while aux.size() > 0:
        cola.arrive(aux.attention())
    return superheroe

cola = Queue()
for p in personajes_mcu:
    cola.arrive(p)

print("a) Personaje de Capitana Marvel:", nombre_capitana(cola, "Capitana Marvel"))
print()
print("b) Superhéroes femeninos:", superheroes_femeninos(cola))
print()
print("c) Personajes masculinos:", personajes_masculinos(cola))
print()
print("d) Superhéroe de Scott Lang:", nombre_ScottLang(cola, "Scott Lang"))
print()
print("e) Datos de personajes/superhéroes que empiezan con 'S':", nombres_con_s(cola))
print()
print("f) ¿Está Carol Danvers?")
superheroe = carol_danvers(cola)
if superheroe:
    print(f"Sí, su superhéroe es: {superheroe}")
else:
    print("No está en la cola.")
