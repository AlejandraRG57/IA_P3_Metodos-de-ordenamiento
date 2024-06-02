#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo ShellSort es una mejora del algoritmo de ordenamiento por inserción, diseñada para abordar la ineficiencia de este último cuando se trata de grandes cantidades de datos.
#ShellSort introduce el concepto de "intervalos" (gaps) para comparar y mover elementos, reduciendo estos intervalos progresivamente hasta que se convierte en una inserción directa.

def shell_sort(arr):
    #Obtenemos la longitud del arreglo.
    n = len(arr)
    #Calculamos el tamaño del intervalo inicial (gap) dividiendo la longitud del arreglo entre 2.
    gap = n // 2
    #Comenzamos un bucle mientras el intervalo (gap) sea mayor que 0.
    while gap > 0:
        #Comenzamos un bucle que recorre el arreglo desde el índice 'gap' hasta el final.
        for i in range(gap, n):
            #Guardamos el valor del elemento actual en 'temp'.
            temp = arr[i]
            #Guardamos el índice actual en 'j'.
            j = i
            #Comenzamos un bucle que ordena los elementos con el intervalo actual.
            while j >= gap and arr[j - gap] > temp:
                #Desplazamos los elementos hacia la derecha en el intervalo actual.
                arr[j] = arr[j - gap]
                #Movemos 'j' hacia atrás en el arreglo con el intervalo actual.
                j -= gap
            #Insertamos el valor guardado en 'temp' en su posición correcta en el arreglo.
            arr[j] = temp
        #Reducimos a la mitad el tamaño del intervalo (gap).
        gap //= 2

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función 'shell_sort' pasando el arreglo como argumento para ordenarlo.
shell_sort(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado es:", arr)