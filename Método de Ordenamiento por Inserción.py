# Lista desordenada que se desea ordenar
lista = [6, 8, 2, 3, 1, 9, 4, 7, 5]

# Muestra la lista inicial antes de comenzar el ordenamiento
print("Lista inicial:", lista)

# Ciclo externo que recorre cada elemento de la lista, comenzando desde el segundo elemento
for i in range(1, len(lista)):
    # El elemento actual que se va a comparar e insertar en su posición correcta
    actual = lista[i]
    # Índice que usaremos para comparar el elemento actual con los anteriores
    indice = i

    # Muestra el inicio de la iteración
    print(f"\nIteración {i}:")
    print(f"Elemento actual: {actual}")

    # Ciclo interno que recorre los elementos a la izquierda del actual
    # para encontrar su posición correcta
    while indice > 0 and lista[indice - 1] > actual:
        # Muestra el proceso de comparación
        print(f"Comparando {lista[indice - 1]} > {actual}: Sí")

        # Si el elemento de la izquierda es mayor, se desplaza hacia la derecha
        lista[indice] = lista[indice - 1]
        indice -= 1  # Se mueve hacia la izquierda para seguir comparando

        # Muestra el estado actual de la lista después del desplazamiento
        print("Estado actual de la lista:", lista)

    # Cuando se encuentra la posición correcta, se inserta el elemento actual
    lista[indice] = actual

    # Muestra el resultado de la inserción
    print(f"Insertado {actual} en posición {indice}")
    print("Lista después de esta iteración:", lista)

# Muestra la lista final después de completar todas las iteraciones
print("\nLista ordenada:", lista)
