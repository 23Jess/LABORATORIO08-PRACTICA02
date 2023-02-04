
def bubbleSort (array): #definimos la función
    length = len(array) - 1 #longitud de lista con la funcion len

    #bucle para las pasadas
    for i in range(0, length): #recorrer la lista del inicio hats el final (menos un elemento)
        print(f"pasada #{i + 1}")

        # Comparaciones e intercambios
        for j in range (0, length): #
            print(f"Comparación: {array[j]} > { array[ j + 1]}")
            if array[j] > array[j + 1]: #Se realiza el cambio cuando el adyacente es menor
                print(f"Intercambiar: {array[j]} x {array[j + 1]}")
                auxiliar = array[j] #variable temporal
                array[j] = array[j + 1]
                array[j + 1] = auxiliar 

    return array

scores = [12, 24, 17, 1, 44, 8]
print("Antes de ordenar: ")
print(scores)
print(" Después de ordenar: ")
print(bubbleSort(scores))