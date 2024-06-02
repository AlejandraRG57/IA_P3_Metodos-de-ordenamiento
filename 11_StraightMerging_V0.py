#Alejandra Rodriguez Guevara 21310127 6E1

#"Straight Merging" es un algoritmo de ordenamiento que combina los principios del "Merging" (mezcla) y el "Insertion Sort" (ordenamiento por inserción). 
#Funciona dividiendo la lista en sublistas pequeñas, las cuales se ordenan utilizando el algoritmo de ordenamiento por inserción. Luego, estas sublistas 
#ordenadas se mezclan de manera similar a como lo harían en el algoritmo MergeSort.

def straight_merging(arr):
    #Obtenemos la longitud del arreglo.
    n = len(arr)
    #Inicializamos el tamaño de las sublistas en 1.
    sublist_size = 1
    #Iteramos hasta que el tamaño de la sublista sea menor que la longitud del arreglo.
    while sublist_size < n:
        #Iteramos sobre las sublistas de tamaño sublist_size y las fusiona.
        for i in range(0, n - sublist_size, 2 * sublist_size):
            start1 = i
            end1 = i + sublist_size - 1
            start2 = i + sublist_size
            end2 = min(i + 2 * sublist_size - 1, n - 1)
            #Llamamos a la función merge para fusionar las sublistas.
            merge(arr, start1, end1, start2, end2)
        #Duplicamos el tamaño de la sublista para la próxima iteración.
        sublist_size *= 2

def merge(arr, start1, end1, start2, end2):
    #Fusionamos dos subarreglos ordenados.
    temp = [] #Arreglo temporal para almacenar la fusión.
    i = start1
    j = start2
    #Iteramos mientras haya elementos en ambas subarreglos.
    while i <= end1 and j <= end2:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    #Agregamos los elementos restantes del primer subarreglo.
    while i <= end1:
        temp.append(arr[i])
        i += 1
    #Agregamos los elementos restantes del segundo subarreglo.
    while j <= end2:
        temp.append(arr[j])
        j += 1
    #Copiamos los elementos fusionados del arreglo temporal al arreglo original.
    for k in range(len(temp)):
        arr[start1 + k] = temp[k]

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función straight_merging para ordenar el arreglo.
straight_merging(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado:", arr)