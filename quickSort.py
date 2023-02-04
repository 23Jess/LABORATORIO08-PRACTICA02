lista=[8,12,10,4,3,5,10]
def particionado(lista):

    pivote=lista[0]
    menores=[]
    mayores=[]

    for i in range(1, len(lista)):  
        if lista[i]< pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return menores,pivote,mayores

def quicksort(lista):
    if len(lista)<2:
        return lista
    
    menores, pivote, mayores = particionado(lista)
    return quicksort(menores) + [pivote]+quicksort(mayores)
    
print(quicksort(lista))