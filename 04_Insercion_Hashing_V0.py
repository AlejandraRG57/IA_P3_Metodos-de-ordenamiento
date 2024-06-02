#Alejandra Rodriguez Guevara 21310127 6E1

#El hashing es una técnica utilizada para convertir una entrada (o clave) en un valor de longitud fija, que generalmente es un número entero, utilizando una función hash. 
#Este valor se llama "hash code" o "hash value". El hashing es ampliamente utilizado en estructuras de datos como tablas hash (hash tables) para realizar búsquedas rápidas.

class ListNode:
    def __init__(self, key):
        #Constructor de la clase ListNode que inicializa un nodo con una clave y un puntero a None.
        self.key = key
        self.next = None

#Tamaño de la tabla hash.
table_size = 10

#Definimos un arreglo desordenado.
data = [10, 4, 2, 5, 3, 1, 7, 6, 8, 0, 9, 100]

#Creamos una tabla hash con listas enlazadas.
hash_table = [None] * table_size

#Función hash simple que toma el módulo del valor clave respecto al tamaño de la tabla hash.
def simple_hash(key):
    return key % table_size

#Almacenamos datos en la tabla hash con resolución de colisiones.
for key in data:
    #Obtenemos el índice de la tabla hash utilizando la función hash.
    index = simple_hash(key)
    if hash_table[index] is None:
        #Si el índice está vacío, creamos un nuevo nodo en ese índice.
        hash_table[index] = ListNode(key)
    else:
        #Si hay colisión en el índice, añadimos el nodo a la lista enlazada en ese índice.
        node = hash_table[index]
        while node.next is not None:
            node = node.next
        node.next = ListNode(key)

#Imprimimos la tabla hash con resolución de colisiones.
for i, node in enumerate(hash_table):
    print(f"Índice {i}:", end=" ")
    while node is not None:
        #Imprimimos las claves de los nodos en la lista enlazada en el índice actual.
        print(node.key, end=" , ")
        node = node.next
    print("")