# Lista desordenada que se desea ordenar
lista = [20, 2, 15, 16, 8, 1, 7, 11, 3, 9, 4, 5, 10, 6, 12, 14, 19, 13, 17, 19, 18]

# Función para dividir la lista en dos partes con base en un pivote
def particionado(lista):
    # Se selecciona el primer elemento como pivote
    pivote = lista[0]

    # Inicializamos dos listas vacías para almacenar los números menores y mayores al pivote
    menores = []
    mayores = []

    # Recorremos la lista desde el segundo elemento
    for i in range(1, len(lista)):
        # Si el elemento actual es menor que el pivote, lo agregamos a la lista 'menores'
        if lista[i] < pivote:
            menores.append(lista[i])
        # Si no, lo agregamos a la lista 'mayores'
        else:
            mayores.append(lista[i])
    
    # Muestra cómo se dividió la lista en esta iteración
    print(f"Dividiendo lista: {lista}")
    print(f"Menores: {menores}, Pivote: {pivote}, Mayores: {mayores}")
    
    # Retornamos las dos listas (menores y mayores) y el pivote
    return menores, pivote, mayores

# Función principal del algoritmo QuickSort
def quicksort(lista):
    # Caso base: Si la lista tiene menos de 2 elementos, ya está ordenada
    if len(lista) < 2:
        return lista

    # Particionamos la lista en menores, pivote y mayores
    menores, pivote, mayores = particionado(lista)

    # Recursivamente ordenamos las listas de menores y mayores
    # Luego las concatenamos con el pivote en el centro
    resultado = quicksort(menores) + [pivote] + quicksort(mayores)

    # Muestra cómo se está construyendo la lista ordenada
    print(f"Unificando: {resultado}")
    return resultado

# Llamamos a la función QuickSort con la lista inicial y mostramos el resultado final
print("\nLista ordenada final:", quicksort(lista))
