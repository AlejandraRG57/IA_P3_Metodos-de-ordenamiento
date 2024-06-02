#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo de ordenamiento QuickSort es un algoritmo de ordenamiento eficiente y ampliamente utilizado que utiliza la estrategia de "divide y vencerás" 
#para ordenar elementos de una lista. Funciona seleccionando un elemento como pivote y particionando la lista alrededor del pivote de manera que los elementos 
#menores que el pivote estén a su izquierda y los elementos mayores estén a su derecha. Luego, aplica recursivamente QuickSort a las sublistas resultantes.

def quick_sort(arr, low, high):
    #Verificamos si hay al menos dos elementos para ordenar.
    if low < high:
        #Obtenemos el índice del pivote después de realizar la partición.
        pivot = partition(arr, low, high)
        #Llamamos a quick_sort para la parte izquierda del pivote.
        quick_sort(arr, low, pivot - 1)
        #Llamamos a quick_sort para la parte derecha del pivote.
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    #Elegimos el elemento más a la derecha como pivote.
    pivot = arr[high]
    #Índice del elemento más pequeño.
    i = low - 1
    #Iteramos sobre los elementos de low a high.
    for j in range(low, high):
        #Si el elemento actual es menor o igual que el pivote.
        if arr[j] <= pivot:
            #Incrementamos el índice del elemento más pequeño.
            i += 1
            #Intercambiamos arr[i] y arr[j].
            arr[i], arr[j] = arr[j], arr[i]
    #Intercambiamos arr[i + 1] y arr[high] (el pivote).
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    #Retornamos el índice del pivote después de la partición.
    return i + 1

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función quick_sort para ordenar el arreglo.
quick_sort(arr, 0, len(arr) - 1)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado:", arr)