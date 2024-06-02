#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo de ordenamiento por selección (Selection Sort) es un algoritmo sencillo e intuitivo que divide la lista de elementos en dos partes: 
#una sublista ordenada y otra sublista no ordenada. En cada iteración, el algoritmo busca el elemento mínimo de la sublista no ordenada y lo intercambia 
#con el primer elemento de la sublista no ordenada. Este proceso continúa hasta que toda la lista esté ordenada.

def selection_sort(arr):
    #Obtenemos la longitud del arreglo.
    n = len(arr)
    #Comenzamos un bucle que recorre el arreglo hasta el penúltimo elemento.
    for i in range(n - 1):
        #Establecemos el índice del mínimo inicialmente en el índice actual.
        min_index = i
        #Comenzamos un bucle que busca el índice del mínimo entre el índice actual y el final del arreglo.
        for j in range(i + 1, n):
            #Si el elemento en el índice actual es menor que el mínimo registrado, actualizamos el índice mínimo.
            if arr[j] < arr[min_index]:
                min_index = j
        #Intercambiamos el elemento en el índice actual con el mínimo encontrado.
        arr[i], arr[min_index] = arr[min_index], arr[i]

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función 'selection_sort' pasando el arreglo como argumento para ordenarlo.
selection_sort(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado:", arr)