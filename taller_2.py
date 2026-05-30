# Taller de Laboratorio - Listas en Python

# Actividad 1 - Crear una lista
frutas = ["banana", "manzana", "pera", "uva", "sandia"]

print(frutas)
print("Primer elemento:", frutas[0])
print("Último elemento:", frutas[-1])


# Actividad 2 - Acceder a posiciones
print("Elemento en la posición 2:", frutas[2])

# Si intentamos acceder a una posición que no existe, aparece un error.
# Ejemplo: frutas[10]
# Esto genera IndexError porque esa posición no está en la lista.


# Actividad 3 - Agregar elementos
frutas.append("mango")
print("Después de agregar al final:", frutas)

frutas.insert(2, "piña")
print("Después de agregar en posición específica:", frutas)


# Actividad 4 - Eliminar elementos
frutas.remove("manzana")
print("Después de eliminar por nombre:", frutas)

frutas.pop()
print("Después de eliminar el último:", frutas)

frutas.pop(1)
print("Después de eliminar por posición:", frutas)

# remove elimina por el nombre del elemento.
# pop() elimina el último elemento.
# pop(posición) elimina el elemento que está en esa posición.


# Actividad 5 - Modificar elementos
print("Lista antes del cambio:", frutas)

frutas[0] = "fresa"

print("Lista después del cambio:", frutas)


# Actividad 6 - Agregar múltiples elementos
frutas.extend(["kiwi", "melon", "naranja"])

print("Lista final:", frutas)
print("Cantidad de elementos:", len(frutas))