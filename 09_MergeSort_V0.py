#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo MergeSort es un algoritmo de ordenamiento eficiente y de comparación que sigue el paradigma de "divide y vencerás". 
#Divide repetidamente la lista en sublistas más pequeñas, las ordena de forma recursiva y luego combina las sublistas ordenadas para obtener la lista completa ordenada.

def merge_sort(arr):
    #Si la longitud del arreglo es mayor que 1, se necesita ordenar.
    if len(arr) > 1:
        #Calculamos el punto medio del arreglo.
        mid = len(arr) // 2
        #Dividimos el arreglo en dos mitades.
        left_half = arr[:mid]
        right_half = arr[mid:]

        #Llamamos a merge_sort recursivamente para ordenar cada mitad.
        merge_sort(left_half)
        merge_sort(right_half)

        #Combinamos las mitades ordenadas.
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                #Si el elemento en la mitad izquierda es menor, lo colocamos en la posición k del arreglo original.
                arr[k] = left_half[i]
                i += 1
            else:
                #Si el elemento en la mitad derecha es menor, lo colocamos en la posición k del arreglo original.
                arr[k] = right_half[j]
                j += 1
            k += 1

        #Agregamos los elementos restantes de left_half si los hay.
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        #Agregamos los elementos restantes de right_half si los hay.
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función merge_sort para ordenar el arreglo.
merge_sort(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado:", arr)