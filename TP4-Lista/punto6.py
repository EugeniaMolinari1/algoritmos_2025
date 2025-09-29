from list_ import List
from listanueva_superheroes import superheroes_nueva 

def crit_nombre(heroe): 
    return heroe["nombre"].lower()

def crit_anio(heroe):   
    return heroe["anio"]

superheroes = List(superheroes_nueva)        


def registrar_criterios(lista: List) -> None:
    lista.add_criterion("nombre", crit_nombre)
    lista.add_criterion("anio",   crit_anio)

registrar_criterios(superheroes)  

def buscar_por_nombre(lista: List, nombre: str):
    return lista.search(nombre.lower(), "nombre")

def obtener_por_nombre(lista: List, nombre: str):
    idx = buscar_por_nombre(lista, nombre)
    return lista[idx] if idx is not None else None

def eliminar_linterna_verde(lista: List) -> bool:
    eliminado = lista.delete_value("linterna verde", "nombre")
    return eliminado is not None

def anio_aparicion_wolverine(lista: List):
    heroe = obtener_por_nombre(lista, "Wolverine")
    return heroe["anio"] if heroe else None

def cambiar_casa_dr_strange(lista: List) -> bool:
    heroe = obtener_por_nombre(lista, "Dr. Strange")
    if heroe:
        heroe["casa"] = "Marvel"
        return True
    return False

def traje_o_armadura(lista: List) -> list[str]:
    return [heroe["nombre"] for heroe in lista if "traje" in heroe["biografia"] or "armadura" in heroe["biografia"]]

def nombre_y_casa_antes_1963(lista: List) -> list[tuple[str, str]]:
    return [(heroe["nombre"], heroe["casa"]) for heroe in lista if heroe["anio"] < 1963]

def casa_capitana_y_mujer_maravilla(lista: List) -> dict[str, str | None]:
    capitanamarvel= obtener_por_nombre(lista, "Capitana Marvel")
    mujermaravilla = obtener_por_nombre(lista, "Mujer Maravilla")
    return {
        "Capitana Marvel": capitanamarvel["casa"] if capitanamarvel else None,
        "Mujer Maravilla": mujermaravilla ["casa"] if mujermaravilla  else None,
    }

def flash_y_starlord(lista: List) -> list[dict | None]:
    return [obtener_por_nombre(lista, "Flash"), obtener_por_nombre(lista, "Star-Lord")]

def listar_iniciales_BMS(lista: List) -> dict[str, list[str]]:
    res = {"B": [], "M": [], "S": []}
    for heroe in lista:
        inicial = heroe["nombre"][0].upper()
        if inicial in res:
            res[inicial].append(heroe["nombre"])
    return res

def cuantos_super_hay_por_casa(lista: List) -> dict[str, int]:
    conteo = {"Marvel": 0, "DC": 0}
    for heroe in lista:
        if heroe["casa"] == "Marvel":
            conteo["Marvel"] += 1
        elif heroe["casa"] == "DC":
            conteo["DC"] += 1
    return conteo

print("a) Se eliminó Linterna Verde:", (eliminar_linterna_verde(superheroes)))
print("b) Año de aparición de Wolverine:", anio_aparicion_wolverine(superheroes))
print("c) Se cambió la casa de Dr. Strange a Marvel:", (cambiar_casa_dr_strange(superheroes)))
print("d) Nombres con 'traje' o 'armadura' en la biografía:", (traje_o_armadura(superheroes)))
print("e) (Nombre, Casa) con año de aparición anterior a 1963:", (nombre_y_casa_antes_1963(superheroes)))
print("f) Casa a la que pertenecen Capitana Marvel y Mujer Maravilla:", (casa_capitana_y_mujer_maravilla(superheroes)))
print("g) Información completa de Flash y Star-Lord:", (flash_y_starlord(superheroes)))
print("h) Superhéroes que comienzan con B, M y S:", (listar_iniciales_BMS(superheroes)))
print("i) Cantidad de superhéroes por casa de cómic:", (cuantos_super_hay_por_casa(superheroes)))