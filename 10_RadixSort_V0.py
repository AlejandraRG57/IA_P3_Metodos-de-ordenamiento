#Alejandra Rodriguez Guevara 21310127 6E1

#El algoritmo RadixSort es un algoritmo de ordenamiento no comparativo que ordena los elementos procesándolos dígito por dígito, de menor a mayor o de mayor a menor, 
#dependiendo de la implementación. Se puede aplicar a elementos enteros o de longitud fija, como cadenas de longitud fija.

def radix_sort(arr):
    #Encontramos el valor máximo en el arreglo para determinar el número máximo de dígitos.
    max_value = max(arr)
    digit_count = len(str(max_value))
    
    #Iteramos sobre cada posición de dígito, desde el dígito menos significativo hasta el más significativo.
    for digit_position in range(digit_count):
        #Inicializamos 10 cubetas (buckets) para cada dígito (0-9).
        buckets = [[] for _ in range(10)]
        #Colocamos cada número en la cubeta correspondiente según el dígito en la posición actual.
        for num in arr:
            digit = (num // (10 ** digit_position)) % 10
            buckets[digit].append(num)
        #Reorganizamos el arreglo utilizando los números de las cubetas en orden.
        arr = [num for bucket in buckets for num in bucket]
    #Retornamos el arreglo ordenado.
    return arr

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Llamamos a la función radix_sort para ordenar el arreglo.
sorted_arr = radix_sort(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado:", sorted_arr)