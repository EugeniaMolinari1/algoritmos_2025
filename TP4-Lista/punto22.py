from list_ import List
from datos_jedi import JEDI_DATA

jedi = List(JEDI_DATA)

def criterio_nombre(j): 
    return j["nombre"].lower()

def criterio_especie(j):   
    return j["especie"].lower()

jedi.add_criterion("nombre", criterio_nombre)
jedi.add_criterion("especie", criterio_especie)

def listado_ordenado_por_nombre_y_especie(jedi_lista: List):
    por_nombre  = List(jedi_lista)
    por_especie = List(jedi_lista)
    por_nombre.sort_by_criterion("nombre")
    por_especie.sort_by_criterion("especie")
    return por_nombre, por_especie

def info_jedi(jedi_lista: List, nombres: list[str]) -> dict[str, dict]:
    aux = {}
    for n in nombres:
        datos = next((j for j in jedi_lista if j["nombre"] == n), None)
        aux[n] = datos if datos else {}
    return aux

def mostrar_aprendices(jedi_lista: List, maestros: list[str]):
    resultado = {}
    for m in maestros:
        maestro = next((j for j in jedi_lista if j["nombre"] == m), None)
        resultado[m] = maestro["padawans"] if maestro else []
    return resultado

def jedi_por_especie(jedi_lista: List, especies: list[str]):
    especies_lower = [e.lower() for e in especies]
    resultado = []
    for jedi in jedi_lista:
        if jedi["especie"].lower() in especies_lower:
            resultado.append(jedi)
    return resultado

def jedi_inicial_A(jedi_lista: List):
    return [j for j in jedi_lista if j["nombre"].startswith("A")]

def sable_de_luz(jedi_lista: List):
    return [j for j in jedi_lista if len(j["colores_sable"]) > 1]

def sable_amarillo_o_violeta(jedi_lista: List):
    aux = []
    for jedi in jedi_lista:
        if "amarillo" in jedi["colores_sable"] or "violeta" in jedi["colores_sable"]:
            aux.append(jedi)
    return aux

def padawans_especificos(jedi_lista: List):
    return mostrar_aprendices(jedi_lista, ["Qui-Gon Jin", "Mace Windu"])


orden_nombre, orden_especie = listado_ordenado_por_nombre_y_especie(jedi)

print("a) Ordenado por nombre:",  [jedi["nombre"] for jedi in orden_nombre])
print("   Ordenado por especie:", [jedi["nombre"] for jedi in orden_especie])

print("b) Info Ahsoka y Kit:", info_jedi(jedi, ["Ahsoka Tano", "Kit Fisto"]))
print("c) Padawans de Yoda y Luke:", mostrar_aprendices(jedi, ["Yoda", "Luke Skywalker"]))
print("d) Humanos y twi'lek:", [jedi["nombre"] for jedi in jedi_por_especie(jedi, ["humano", "twi'lek"])])
print("e) Jedi que empiezan con A:", [jedi["nombre"] for jedi in jedi_inicial_A(jedi)])
print("f) Jedi con múltiples colores:", [jedi["nombre"] for jedi in sable_de_luz(jedi)])
print("g) Jedi con sable amarillo o violeta:", [jedi["nombre"] for jedi in sable_amarillo_o_violeta(jedi)])
print("h) Padawans de Qui-Gon Jin y Mace Windu:", padawans_especificos(jedi))
