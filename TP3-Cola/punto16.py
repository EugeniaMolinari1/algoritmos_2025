from heap import HeapMax


EMPLEADO = 1
TI       = 2
GERENTE  = 3


def cargar(heap, nombre_doc, prioridad):
    heap.arrive(nombre_doc, prioridad)   

def imprimir_doc(heap):
    prio_val = heap.attention()
    nombre = prio_val[1] if isinstance(prio_val, list) and len(prio_val) == 2 else prio_val
    print(nombre)

def imprimir_n(heap, n):
    for _ in range(min(n, heap.size())):
        imprimir_doc(heap)

def imprimir_todos(heap):
    while heap.size() > 0:
        imprimir_doc(heap)

cola = HeapMax()

cargar(cola, "Doc empleado n°1", EMPLEADO)
cargar(cola, "Doc empleado n°2", EMPLEADO)
cargar(cola, "Doc empleado n°3", EMPLEADO)


print("Imprimir 1 documento:")
imprimir_doc(cola)


cargar(cola, "Doc TI n°1", TI)
cargar(cola, "Doc TI n°2", TI)

cargar(cola, "Doc Gerente n°1", GERENTE)

print("Imprimir 2 documentos:")
imprimir_n(cola, 2)


cargar(cola, "Doc empleado n°4", EMPLEADO)
cargar(cola, "Doc empleado n°5", EMPLEADO)
cargar(cola, "Doc Gerente n°2", GERENTE)

print("Imprimir todos los documentos:")
imprimir_todos(cola)
