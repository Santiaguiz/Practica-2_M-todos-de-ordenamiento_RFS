# Se crea una lista desordenada que será ordenada de menor a mayor.
lista = [6, 8, 2, 3, 1, 9, 4, 7, 5]

# Se obtiene la longitud de la lista para usarla en los ciclos.
longitud = len(lista)

# Ciclo externo para recorrer la lista desde el primer elemento hasta el penúltimo.
for i in range(longitud - 1):
    # Muestra el estado actual de la lista en cada iteración del ciclo externo.
    print(lista)
    
    # Inicialmente, se asume que el elemento actual es el menor.
    menor = i
    print("El numero menor a evaluar actualmente es: ", menor)
    
    # Ciclo interno para comparar el elemento actual con los elementos restantes.
    for j in range(i + 1, longitud):
        # Si se encuentra un elemento menor al actual, se actualiza el índice `menor`.
        if lista[j] < lista[menor]:
            menor = j
            print("Recorriendo la lista, el menor numero actual es: ", menor)
    
    # Intercambia el elemento actual con el menor encontrado.
    temp = lista[menor]     # Guarda temporalmente el valor del menor.
    lista[menor] = lista[i] # Asigna el valor actual al lugar del menor.
    lista[i] = temp         # Asigna el menor al lugar actual.
    print(f"Se cambia el numero: {lista[menor]} con: {lista[i]}")

# Muestra la lista ya ordenada después de completar el ciclo.
print(lista)
