#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo de ordenamiento por intercambio, comúnmente conocido como Bubble Sort (o burbuja), es un algoritmo simple que recorre repetidamente una lista de elementos 
#y compara pares adyacentes, intercambiándolos si están en el orden incorrecto. Este proceso se repite hasta que no se realicen más intercambios, lo que indica que la 
#lista está ordenada.

def bubble_sort(arr):
    #Obtenemos la longitud del arreglo.
    n = len(arr)
    #Comenzamos un bucle que recorre el arreglo.
    #En cada iteración, se compara y se intercambian los elementos adyacentes si están en el orden incorrecto.
    #Después de cada iteración, el elemento más grande "burbujea" hasta su posición correcta al final del arreglo.
    for i in range(n - 1):
        swapped = False #Variable para rastrear si se realizaron intercambios en esta iteración.
        #Comenzamos un bucle que recorre el arreglo hasta el penúltimo elemento.
        for j in range(0, n - i - 1):
            #Comparamos los elementos adyacentes y los intercambia si están en el orden incorrecto.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  #Marcamos que se realizó un intercambio en esta iteración.
        #Si no se realizó ningún intercambio en esta iteración, el arreglo ya está ordenado y podemos salir del bucle.
        if not swapped:
            break

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función 'bubble_sort' pasando el arreglo como argumento para ordenarlo.
bubble_sort(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado:", arr)