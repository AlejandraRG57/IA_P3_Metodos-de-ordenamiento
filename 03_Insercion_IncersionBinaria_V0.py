#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo de inserción binaria es una variación del algoritmo de ordenamiento por inserción (Insertion Sort) que utiliza la búsqueda binaria para encontrar 
#la posición correcta donde insertar el elemento. Esto reduce el número de comparaciones necesarias para encontrar la posición de inserción, aunque no cambia el 
#número total de movimientos.

def binary_search(arr, key, start, end):
    #Comenzamos un bucle mientras el índice de inicio sea menor o igual al índice final.
    while start <= end:
        #Calculamos el índice medio del subarreglo.
        mid = (start + end) // 2
        #Si el elemento en el índice medio es menor que la clave, actualizamos el inicio.
        if arr[mid] < key:
            start = mid + 1
        #Si el elemento en el índice medio es mayor o igual que la clave, actualizamos el final.
        else:
            end = mid - 1
    #Retornamos la posición de inicio, que será la posición donde se debe insertar la clave.
    return start

def binary_insertion_sort(arr):
    #Comenzamos un bucle que recorre el arreglo desde el segundo elemento hasta el último.
    for i in range(1, len(arr)):
        #Guardamos el valor del elemento actual en 'key'.
        key = arr[i]
        #Encontramos la posición donde insertar el elemento actual usando búsqueda binaria.
        pos = binary_search(arr, key, 0, i - 1)
        #Moevemos los elementos para hacer espacio para 'key'.
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        #Insertamos 'key' en la posición calculada.
        arr[pos] = key

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función 'binary_insertion_sort' pasando el arreglo como argumento para ordenarlo.
binary_insertion_sort(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado es:", arr)