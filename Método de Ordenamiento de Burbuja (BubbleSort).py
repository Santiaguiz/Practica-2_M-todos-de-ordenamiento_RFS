lista = [5, 8, 7, 9, 3, 2, 1, 6, 4]

for i in range(len(lista)-1): #bucle que se encarga de darla la vuelta a la lista las veces que sea necesario
    for j in range(len(lista)-1): #bucle que compara cada elemento con el siguiente de la lista
        print(f"Comparando: {lista[j]} con: {lista[j+1]}")
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista [j+1], lista [j] #Acomoda los elementos si es que el elemento despues del primero es menor 
            
            print(f"Intercambiando: {lista[j]} por: {lista[j+1]}")

            #temporal = lista[j]
            #lista[j] = lista[j+1]
            #lista[j+1] = temporal
print ('la lista ya acomodada dado los valores iniciales temrima siendo asi', lista)