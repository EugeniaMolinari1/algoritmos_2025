from estructuras_stack import Stack
from qqueue import Queue  

cola = Queue()
cola.arrive({"hora": "11:45", "aplicacion": "Facebook", "mensaje": "Mirá esta foto"})
cola.arrive({"hora": "14:00", "aplicacion": "Twitter", "mensaje": "Python es genial"})
cola.arrive({"hora": "16:00", "aplicacion": "Instagram", "mensaje": "Nuevo post"})
cola.arrive({"hora": "12:30", "aplicacion": "Twitter", "mensaje": "Curso de Python"})
cola.arrive({"hora": "10:00", "aplicacion": "Facebook", "mensaje": "Recordatorio de evento"})

def eliminar_facebook():
    for _ in range(cola.size()):
        noti = cola.attention()
        if noti["aplicacion"] != "Facebook":
            cola.arrive(noti)

def mostrar_twitter():
    for _ in range(cola.size()):
        noti = cola.attention()
        if noti["aplicacion"] == "Twitter" and "python" in noti["mensaje"].lower():
            print(noti)
        cola.arrive(noti)

def contar_horas() -> int:
    pila = Stack()
    for _ in range(cola.size()):
        noti = cola.attention()
        if "11:43" <= noti["hora"] <= "15:57":
            pila.push(noti)
        cola.arrive(noti)
    return pila.size()

print("a) las notificaciones de facebook fueron eliminadas ")
eliminar_facebook()
print()
print("b) las notificaciones de twitter que tienen la palabra pyhton son: ")
mostrar_twitter()
print()
print(f"c) las notificaciones entre las 11:43 y las 15:57 son: ", contar_horas())
