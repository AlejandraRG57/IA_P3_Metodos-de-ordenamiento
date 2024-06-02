#Alejandra Rodriguez Guevara 21310127 6E1

#Funciona de manera similar a cómo organizarías un mazo de cartas en tu mano: tomas una carta a la vez y la insertas en el lugar correcto.

def insertion_sort(arr):
    #Comenzamos un bucle que recorre el arreglo desde el segundo elemento (índice 1) hasta el último.
    for i in range(1, len(arr)):
        #Guardamos el valor del elemento actual del arreglo en la variable 'key'.
        key = arr[i]
        #Establecemos el índice 'j' en una posición antes del elemento actual.
        j = i - 1
        #Comenzamos un bucle que mueve los elementos mayores que 'key' una posición hacia adelante.
        while j >= 0 and arr[j] > key:
            #Muovemos el elemento actual de 'arr[j]' una posición hacia adelante.
            arr[j + 1] = arr[j]
            #Decrementamos 'j' para verificar el siguiente elemento hacia atrás.
            j -= 1
        #Colocamos 'key' en su posición correcta en el arreglo.
        arr[j + 1] = key

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función 'insertion_sort' pasando el arreglo como argumento para ordenarlo.
insertion_sort(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado es:", arr)