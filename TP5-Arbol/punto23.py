from tree import BinaryTree
from qqueue import Queue
from datos_criaturas import criaturas


def cargar_arbol_criaturas(registros) -> BinaryTree:
    t = BinaryTree()
    for it in registros:
        t.insert(
            it["name"],
            {
                "defeated_by": it.get("defeated_by"),
                "capturada": None,   
                "description": "",     
            },
        )
    return t

def listado_inorden_y_derrotados(t: BinaryTree):
    salida = []
    def _in(root):
        if root is None: return
        _in(root.left)
        salida.append((root.value, root.other_values.get("defeated_by")))
        _in(root.right)
    if t.root: _in(t.root)
    return salida

def descripcion_criatura(t: BinaryTree, criatura: str, descripcion: str) -> bool:
    nodo = t.search(criatura)
    if not nodo: return False
    nodo.other_values["description"] = descripcion
    return True

def info_talos(t: BinaryTree):
    n = t.search("Talos")
    return (n.value, n.other_values.copy()) if n else None

def top3_derrotadores(t: BinaryTree):
    from collections import Counter
    cont = Counter()
    def _in(root):
        if root is None: return
        _in(root.left)
        h = root.other_values.get("defeated_by")
        if h: cont[h] += 1
        _in(root.right)
    if t.root: _in(t.root)
    return cont.most_common(3)

def criaturas_derrotadas_por_heracles(t: BinaryTree):
    salida = []
    def _in(root):
        if root is None: return
        _in(root.left)
        if root.other_values.get("defeated_by") == "Heracles":
            salida.append(root.value)
        _in(root.right)
    if t.root: _in(t.root)
    return salida

def criaturas_no_derrotadas(t: BinaryTree):
    salida = []
    def _in(root):
        if root is None: return
        _in(root.left)
        if not root.other_values.get("defeated_by"):
            salida.append(root.value)
        _in(root.right)
    if t.root: _in(t.root)
    return salida

def campo_capturada(t: BinaryTree, criatura: str):
    n = t.search(criatura)
    return n.other_values.copy() if n else None

def marcar_capturas_heracles(t: BinaryTree):
    objetivos = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
    ok = True
    for nombre in objetivos:
        n = t.search(nombre)
        if n: n.other_values["capturada"] = "Heracles"
        else: ok = False
    return ok

def buscar_por_coincidencia(t: BinaryTree, subcadena: str):
    resultados = []
    patron = subcadena.casefold()  

    def _inorden_coincidencia(n):
        if n is None:
            return
        _inorden_coincidencia(n.left)
        if isinstance(n.value, str) and patron in n.value.casefold():
            resultados.append(n.value)
        _inorden_coincidencia(n.right)

    if t.root:
        _inorden_coincidencia(t.root)
    return resultados

def eliminar_basilisco_y_sirenas(t: BinaryTree):
    borradas = []
    for nombre in ["Basilisco", "Sirenas"]:
        deleted, _ = t.delete(nombre)
        if deleted is not None:
            borradas.append(deleted)
    return borradas

def modificar_aves_estinfalo(t: BinaryTree):
    n = t.search("Aves del Estínfalo")
    if not n: return False
    prev = n.other_values.get("defeated_by")
    if prev and "Heracles" not in prev:
        n.other_values["defeated_by"] = f"{prev}; Heracles (derrotó a varias)"
    else:
        n.other_values["defeated_by"] = "Heracles (derrotó a varias)"
    return True

def renombrar_ladon(t: BinaryTree):
    deleted, other = t.delete("Ladón")
    if deleted is None: return False
    t.insert("Dragón Ladón", other)
    return True

def listado_por_nivel(t: BinaryTree):
    if not t.root: return []
    orden = []
    q = Queue()
    q.arrive(t.root)
    while q.size() > 0:
        n = q.attention()
        orden.append(n.value)
        if n.left:  q.arrive(n.left)
        if n.right: q.arrive(n.right)
    return orden

def capturadas_por_heracles(t: BinaryTree):
    salida = []
    def _in(root):
        if root is None: return
        _in(root.left)
        if root.other_values.get("capturada") == "Heracles":
            salida.append(root.value)
        _in(root.right)
    if t.root: _in(t.root)
    return salida

if __name__ == "__main__":
    arbol = cargar_arbol_criaturas(criaturas)

    print("a)", listado_inorden_y_derrotados(arbol))
    descripcion_criatura(arbol, "Talos", "Autómata de bronce que custodiaba Creta.")
    print("c)", info_talos(arbol))
    print("d)", top3_derrotadores(arbol))
    print("e)", criaturas_derrotadas_por_heracles(arbol))
    print("f)", criaturas_no_derrotadas(arbol))
    print("g) Cerbero ->", campo_capturada(arbol, "Cerbero"))
    print("h)", marcar_capturas_heracles(arbol))
    print("i)", buscar_por_coincidencia(arbol, "Ja"))
    print("j)", eliminar_basilisco_y_sirenas(arbol))
    print("k)", modificar_aves_estinfalo(arbol))
    print("l)", renombrar_ladon(arbol))
    print("m)", listado_por_nivel(arbol))
    print("n)", capturadas_por_heracles(arbol))
