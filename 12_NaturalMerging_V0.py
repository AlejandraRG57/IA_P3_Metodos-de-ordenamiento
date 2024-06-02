#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo de ordenación Natural Merging es una extensión del algoritmo MergeSort que aprovecha las subsecuencias ya ordenadas en la lista para mejorar el rendimiento.

def natural_merge_sort(arr):
    #Si el arreglo tiene longitud 0 o 1, está automáticamente ordenado.
    if len(arr) <= 1:
        return arr
    
    #Función para encontrar y devolver las "runs" (subsecuencias ordenadas) en el arreglo.
    def find_runs(arr):
        runs = [] #Lista para almacenar las runs.
        new_run = [arr[0]] #Inicializamos una nueva run con el primer elemento.
        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]:
                #Si el elemento actual es mayor o igual que el anterior, pertenece a la misma run.
                new_run.append(arr[i])
            else:
                #Si no, finalizamos la run actual y comenzamos una nueva run.
                runs.append(new_run)
                new_run = [arr[i]]
        runs.append(new_run) #Agregamos la última run al arreglo de runs.
        return runs
    
    #Función para fusionar dos listas ordenadas.
    def merge(left, right):
        result = [] #Lista para almacenar la fusión de las dos listas.
        i = j = 0
        #Iteramos sobre las dos listas mientras haya elementos en ambas.
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        #Agregamos los elementos restantes de left y right a result.
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    #Encontramos las runs en el arreglo.
    runs = find_runs(arr)
    #Fusionamos las runs hasta que solo quede una run.
    while len(runs) > 1:
        new_runs = []
        #Fusionamos las runs dos a la vez.
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                #Si hay dos runs disponibles, las fusionamos.
                new_runs.append(merge(runs[i], runs[i + 1]))
            else:
                #Si solo hay una run disponible, no necesita ser fusionada.
                new_runs.append(runs[i])
        runs = new_runs

    return runs[0] #Devolvemos la run final, que es el arreglo ordenado.

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función natural_merge_sort para ordenar el arreglo.
sorted_arr = natural_merge_sort(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado:", sorted_arr)