from list__ import List
from queuee import Queue
from datos_superheroes import superheroes  

personajes = List()
personajes.extend(superheroes)

def nombre_personaje(personaje):
    return personaje["name"]

def nombre_real_personaje(personaje):
    return personaje["real_name"] or ""

def anio_aparicion_personaje(personaje):
    return personaje["first_appearance"]


personajes.add_criterion("nombre", nombre_personaje)
personajes.add_criterion("nombre_real", nombre_real_personaje)
personajes.add_criterion("aparicion", anio_aparicion_personaje)

personajes.sort_by_criterion("nombre")
personajes_ordenados_por_nombre = personajes.copy()

posicion_the_thing = personajes.search("The Thing", "nombre")
posicion_rocket = personajes.search("Rocket Raccoon", "nombre")

villanos = List([personaje for personaje in personajes if personaje["is_villain"]])

cola_de_villanos = Queue()
for villano in villanos:
    cola_de_villanos.arrive(villano)

villanos_anteriores_a_1980 = []
for _ in range(cola_de_villanos.size()):
    villano = cola_de_villanos.move_to_end()
    if villano["first_appearance"] < 1980:
        villanos_anteriores_a_1980.append(villano)

prefijos_validos = ["Bl", "G", "My", "W"]
personajes_con_prefijo = []
for personaje in personajes:
    for prefijo in prefijos_validos:
        if personaje["name"][:len(prefijo)] == prefijo:
            personajes_con_prefijo.append(personaje["name"])
            break

personajes.sort_by_criterion("nombre_real")
personajes_ordenados_por_nombre_real = personajes.copy()

personajes.sort_by_criterion("aparicion")
personajes_ordenados_por_anio = personajes.copy()

antman_modificado = None
for personaje in personajes:
    if personaje["name"] == "Ant Man":
        personaje["real_name"] = "Scott Lang"
        antman_modificado = personaje

personajes_con_palabras_clave = []
for personaje in personajes:
    bio = personaje["short_bio"].lower()
    if "time-traveling" in bio or "suit" in bio:
        personajes_con_palabras_clave.append(personaje)

personajes_eliminados = []
for nombre_a_eliminar in ["Electro", "Baron Zemo"]:
    eliminado = personajes.delete_value(nombre_a_eliminar, "nombre")
    if eliminado:
        personajes_eliminados.append(eliminado)


print("1. Personajes ordenados por nombre:")
for personaje in personajes_ordenados_por_nombre:
    print(personaje)

print()
print(f"2. Posición de The Thing: {posicion_the_thing}")
print(f"Posición de Rocket Raccoon: {posicion_rocket}")

print()
print("3. Lista de villanos:")
for villano in villanos:
    print(villano)

print()
print("4. Villanos con aparición antes de 1980:")
for villano in villanos_anteriores_a_1980:
    print(villano["name"])

print()
print("5. Personajes cuyos nombres empiezan con Bl, G, My o W:")
for nombre in personajes_con_prefijo:
    print(nombre)

print()
print("6. Personajes ordenados por nombre real:")
for personaje in personajes_ordenados_por_nombre_real:
    print(personaje)

print()
print("7. Personajes ordenados por año de aparición:")
for personaje in personajes_ordenados_por_anio:
    print(personaje)

print()
print("8. Ant Man modificado:")
if antman_modificado:
    print(antman_modificado)

print()
print("9. Personajes cuya biografía menciona 'time-traveling' o 'suit':")
for personaje in personajes_con_palabras_clave:
    print(personaje["name"])

print()
print("10. Personajes eliminados:")
for personaje in personajes_eliminados:
    print(personaje)

