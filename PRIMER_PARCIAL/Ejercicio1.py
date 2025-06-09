superheroes = [
    "Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye",
    "Spider-Man", "Doctor Strange", "Black Panther", "Ant-Man", "Wasp",
    "Scarlet Witch", "Vision", "Falcon", "Winter Soldier", "Capitan America"
]

def capitan_america(lista, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Capitan America":
        return True
    return capitan_america(lista, indice + 1)

def listar(lista, indice=0):
    if indice >= len(lista):
        return[]
    return [lista[indice]] + listar(lista, indice + 1)

if capitan_america(superheroes):
    print("Capitan America está en la lista.")
else:
    print("Capitan America no está en la lista.")

print()
print("Listado de superhéroes:")
for heroe in listar(superheroes):
    print(heroe)
