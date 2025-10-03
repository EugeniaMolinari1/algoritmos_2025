from tree import BinaryTree
from datos_superheroes import superheroes

def cargar_arbol(registros) -> BinaryTree:
    arbol = BinaryTree()
    for it in registros:
        name = it["name"]
        is_villain = bool(it.get("is_villain", False))
        other = {
            "is_villain": is_villain,
            "is_hero": not is_villain, 
        }
        arbol.insert(name, other)
    return arbol


def villanos_ordenados(arbol: BinaryTree):
    villanos = []
    def _inorder_villains(root):
        if root is not None:
            _inorder_villains(root.left)
            if root.other_values and root.other_values.get("is_villain", False):
                villanos.append(root.value)
            _inorder_villains(root.right)
    if arbol.root:
       _inorder_villains(arbol.root)
    return villanos

def superheroes_con_c(arbol: BinaryTree):
    heroes_c = []
    def _inorder_heroes_c(root):
        if root is not None:
            _inorder_heroes_c(root.left)
            if root.other_values and root.other_values.get("is_hero", False):
                if isinstance(root.value, str) and root.value.startswith("C"):
                    heroes_c.append(root.value)
            _inorder_heroes_c(root.right)
    if arbol.root:
        _inorder_heroes_c(arbol.root)
    return heroes_c

def contar_superheroes(arbol: BinaryTree):
    return arbol.count_heroes()

def modificar_DrStrange(arbol: BinaryTree):
    arbol.proximity_search("Dr")
    deleted_name, other = arbol.delete("Dr Strange")
    if deleted_name is not None:
        arbol.insert("Doctor Strange", other if other else {"is_villain": False, "is_hero": True})
        return True
    return False

def lista_descendente(arbol: BinaryTree):
    heroes_desc = []
    def _reverse_inorder_heroes(root):
        if root is not None:
            _reverse_inorder_heroes(root.right)
            if root.other_values and root.other_values.get("is_hero", False):
                heroes_desc.append(root.value)
            _reverse_inorder_heroes(root.left)
    if arbol.root:
        _reverse_inorder_heroes(arbol.root)
    return heroes_desc

def contar_nodos(arbol: BinaryTree) -> int: 
    def _count(root):
        return 0 if root is None else 1 + _count(root.left) + _count(root.right)
    return _count(arbol.root)

def lista_alfabeticamente(arbol: BinaryTree):
    lista = []
    def _inorder_collect(root):
        if root is not None:
            _inorder_collect(root.left)
            lista.append(root.value)
            _inorder_collect(root.right)
    if arbol.root:
        _inorder_collect(arbol.root)
    return lista

def crear_bosque(arbol: BinaryTree):

    arbol_heroes = BinaryTree()
    arbol_villanos = BinaryTree()

    arbol.divide_tree(arbol_heroes, arbol_villanos)
    cant_h = contar_nodos(arbol_heroes)
    cant_v = contar_nodos(arbol_villanos)
    return {
        "nodos_heroes": cant_h,
        "nodos_villanos": cant_v,
        "heroes_inorder": lista_alfabeticamente(arbol_heroes),
        "villanos_inorder": lista_alfabeticamente(arbol_villanos),
    }

arbol = cargar_arbol(superheroes) 

print("b) Villanos ordenados alfabéticamente:", villanos_ordenados(arbol))
print("c) Superhéroes que comienzan con 'C':", superheroes_con_c(arbol))
print("d) Cantidad de superhéroes en el árbol:", contar_superheroes(arbol))
print("e) Se corrigió 'Dr Strange' a 'Doctor Strange':", modificar_DrStrange(arbol))
print("f) Superhéroes en orden descendente:", lista_descendente(arbol))
respuesta_g = crear_bosque(arbol)
print("g-I) Cantidad de nodos en árbol de HÉROES:", respuesta_g["nodos_heroes"])
print("g-I) Cantidad de nodos en árbol de VILLANOS:", respuesta_g["nodos_villanos"])
print("g-II) Héroes in-order:", respuesta_g["heroes_inorder"])
print("g-II) Villanos in-order:", respuesta_g["villanos_inorder"])
