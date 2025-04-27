def usar_la_fuerza(mochila):

    if not mochila:
        return False, 0

    objeto = mochila.pop(0)


    if objeto.lower() == "sable de luz":
        return True, 1

    encontrado, cont = usar_la_fuerza(mochila)
    return encontrado, cont + 1


mochila = ["gorro", "agua","remera", "botella","sable de luz", "lapiz"]
encontrado, cantidad = usar_la_fuerza(mochila)

if encontrado:
    print(f"Sable de luz encontrado tras extraer {cantidad} objetos.")
else:
    print("No se encontró sable de luz; mochila vaciada tras extraer todos los objetos.")
