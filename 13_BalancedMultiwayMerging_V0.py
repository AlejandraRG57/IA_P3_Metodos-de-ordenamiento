#Alejandra Rodriguez Guevara 21310127 6E1

#El "Balanced Multiway Merging" es un algoritmo que generaliza el proceso de mezcla de dos listas ordenadas a 
#k listas ordenadas. Se basa en dividir las listas en grupos más pequeños, mezclarlos y luego combinar los resultados.

import heapq

def balanced_multiway_merge(runs):
    min_heap = [] #Inicializamos un heap vacío.
    
    #Inicializamos el heap con el primer elemento de cada run.
    for i, run in enumerate(runs):
        if run: #Verificamos si la run no está vacía.
            heapq.heappush(min_heap, (run[0], i, 0)) #Añadimos el primer elemento de la run al heap.
    
    sorted_result = [] #Lista para almacenar el resultado ordenado.
    
    #Realizamos la mezcla multi-caminos hasta que el heap esté vacío.
    while min_heap:
        #Extraemos el elemento más pequeño del heap.
        value, run_idx, elem_idx = heapq.heappop(min_heap)
        sorted_result.append(value) #Añadimos el valor al resultado.
        
        #Si hay más elementos en la run actual, añadimos el siguiente al heap.
        if elem_idx + 1 < len(runs[run_idx]):
            next_tuple = (runs[run_idx][elem_idx + 1], run_idx, elem_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return sorted_result #Devolvemos el resultado ordenado.

def find_runs(arr):
    runs = [] #Lista para almacenar las runs.
    new_run = [arr[0]] #Inicializamos una nueva run con el primer elemento del arreglo.
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]: #Si el elemento actual es mayor o igual que el anterior, pertenece a la misma run.
            new_run.append(arr[i])
        else:
            runs.append(new_run) #Finalizamos la run actual y la añadimos a la lista de runs.
            new_run = [arr[i]] #Comenzamos una nueva run.
    runs.append(new_run) #Añadimos la última run al arreglo de runs.
    return runs #Devolvemos las runs encontradas.

def natural_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    runs = find_runs(arr) #Encontramos las runs en el arreglo.
    
    while len(runs) > 1:
        #Combinamos todos los runs usando mezcla multi-caminos.
        runs = [balanced_multiway_merge(runs)]
    
    return runs[0] #Devolvemos la run final, que es el arreglo ordenado.

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función natural_merge_sort para ordenar el arreglo.
sorted_arr = natural_merge_sort(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado:", sorted_arr)