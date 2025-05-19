from stack import Stack

def buscar_hulkbuster(pila):
    aux = Stack()
    peliculas = []

    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == "Mark XLIV":
            peliculas.append(traje["pelicula"])
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

    if peliculas:
        print("Mark XLIV apareció en estas películas:")
        for p in peliculas:
            print(p)
    else:
        print("No se encontró ningún Hulkbuster (Mark XLIV).")

def mostrar_daniados(pila):
    aux = Stack()
    print("Modelos dañados:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Dañado":
            print(traje["modelo"])
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())

def eliminar_destruidos(pila):
    aux = Stack()
    print("Eliminando modelos destruidos:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Destruido":
            print(traje["modelo"])
        else:
            aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())

def agregar_mark_85(pila, pelicula):
    aux = Stack()
    existe = False

    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == "Mark LXXXV" and traje["pelicula"] == pelicula:
            existe = True
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

    if not existe:
        pila.push({
            "modelo": "Mark LXXXV",
            "pelicula": pelicula,
            "estado": "Impecable"
        })
        print("Mark LXXXV agregado para", pelicula)
    else:
        print("Ya existe Mark LXXXV en", pelicula)

def mostrar_trajes_peliculas(pila, peliculas_busqueda):
    aux = Stack()
    print("Trajes usados en:")
    for pelicula in peliculas_busqueda:
        print(pelicula)
    while pila.size() > 0:
        traje = pila.pop()
        if traje["pelicula"] in peliculas_busqueda:
            print(traje["modelo"])
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())

if __name__ == "__main__":
    pila_trajes = Stack()

    pila_trajes.push({"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"})
    pila_trajes.push({"modelo": "Mark V", "pelicula": "Iron Man 2", "estado": "Destruido"})
    pila_trajes.push({"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"})
    pila_trajes.push({"modelo": "Mark XLV", "pelicula": "Avengers: Age of Ultron", "estado": "Impecable"})
    pila_trajes.push({"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Dañado"})
    pila_trajes.push({"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"})

    buscar_hulkbuster(pila_trajes)
    print()
    mostrar_daniados(pila_trajes)
    print()
    eliminar_destruidos(pila_trajes)
    print()
    agregar_mark_85(pila_trajes, "Avengers: Endgame")
    print()
    mostrar_trajes_peliculas(
        pila_trajes,
        ["Spider-Man: Homecoming", "Captain America: Civil War"]
    )
