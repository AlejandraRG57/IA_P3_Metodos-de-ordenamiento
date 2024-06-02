#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo de ordenamiento por polifase (Polyphase Sort) es una técnica de ordenamiento externa que se utiliza para manejar grandes volúmenes de datos 
#que no caben en la memoria principal. Este método divide los datos en múltiples fases de mezcla y utiliza un número limitado de archivos temporales.

#La distribución de los runs iniciales es una parte crítica del algoritmo de ordenamiento por polifase. En este proceso, los runs se generan a partir de la 
#lista original y se distribuyen de manera equilibrada entre un número especificado de archivos temporales.

import heapq

def distribute_runs(arr, num_files):
    runs = [] #Lista para almacenar las runs.
    run = [arr[0]] #Inicializamos una nueva run con el primer elemento del arreglo.
    #Encontramos las runs en el arreglo.
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            run.append(arr[i]) #Si el elemento actual es mayor o igual que el anterior, pertenece a la misma run.
        else:
            runs.append(run) #Finalizamos la run actual y la añadimos a la lista de runs.
            run = [arr[i]] #Comenzamos una nueva run.
    runs.append(run) #Añadimos la última run al arreglo de runs.
    
    #Distribuimos las runs entre los archivos.
    files = [[] for _ in range(num_files)] #Inicializamos una lista de listas para los archivos temporales.
    for i, run in enumerate(runs):
        files[i % num_files].extend(run) #Asignamos cada run a un archivo temporal.
    
    return files #Devolvemos los archivos temporales con las runs distribuidas.

def polyphase_merge(files):
    min_heap = [] #Inicializamos un heap vacío.
    
    #Inicializamos el heap con el primer elemento de cada run en cada archivo.
    for file_idx, file in enumerate(files):
        if file: #Verificamos si el archivo no está vacío.
            run = file.pop(0) #Extraemos el primer elemento de la run del archivo.
            heapq.heappush(min_heap, (run, file_idx)) #Añadimos el primer elemento de la run al heap.
    
    sorted_result = [] #Lista para almacenar el resultado ordenado.
    
    #Realizamos la mezcla de polifase hasta que el heap esté vacío.
    while min_heap:
        run, file_idx = heapq.heappop(min_heap) #Extraemos el elemento más pequeño del heap.
        sorted_result.append(run) #Añadimos la run al resultado.
        
        #Si hay más elementos en el archivo actual, añadimos el siguiente al heap.
        if files[file_idx]:
            run = files[file_idx].pop(0) #Extraemos el siguiente elemento del archivo.
            heapq.heappush(min_heap, (run, file_idx))
    
    return sorted_result #Devolvemos el resultado ordenado.

def polyphase_sort(arr, num_files):
    #Ordenamos el arreglo antes de distribuir las runs entre los archivos temporales.
    arr.sort()
    #Distribuimos las runs del arreglo entre los archivos temporales.
    files = distribute_runs(arr, num_files)
    #Realizamos la mezcla de polifase para ordenar las runs.
    sorted_arr = polyphase_merge(files)
    return sorted_arr #Devolvemos el arreglo ordenado.

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
num_files = 3 #Número de archivos temporales.
#Llamamos a la función polyphase_sort para ordenar el arreglo.
sorted_arr = polyphase_sort(arr, num_files)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado:", sorted_arr)