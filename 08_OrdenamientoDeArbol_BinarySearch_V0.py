#Alejandra Rodriguez Guevara 21310127 6E1

#El "Ordenamiento de árbol" se refiere a una familia de algoritmos de ordenamiento que utilizan una estructura de árbol para organizar y ordenar elementos. 
#Uno de los algoritmos más comunes en esta categoría es el "Ordenamiento de árbol binario de búsqueda" (Binary Search Tree Sort), que organiza los elementos 
#en un árbol binario de búsqueda y luego realiza un recorrido inorden para obtener los elementos ordenados.

class TreeNode:
    def __init__(self, key):
        #Constructor de la clase TreeNode que inicializa un nodo con una clave y punteros a los hijos izquierdo y derecho.
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    #Función para insertar un nuevo nodo en un árbol binario de búsqueda.
    if root is None:
        #Si el árbol está vacío, creamos un nuevo nodo como la raíz del árbol.
        return TreeNode(key)
    if key < root.key:
        #Si la clave es menor que la clave de la raíz, insertamos en el subárbol izquierdo.
        root.left = insert(root.left, key)
    elif key > root.key:
        #Si la clave es mayor que la clave de la raíz, insertamos en el subárbol derecho.
        root.right = insert(root.right, key)
    return root

def inorder_traversal(root, result):
    #Función para realizar un recorrido en orden (inorder) en un árbol binario de búsqueda.
    if root:
        #Visitamos el subárbol izquierdo.
        inorder_traversal(root.left, result)
        #Agregamos la clave del nodo actual al resultado.
        result.append(root.key)
        #Visitamos el subárbol derecho.
        inorder_traversal(root.right, result)

def tree_sort(arr):
    #Función para ordenar un arreglo utilizando un árbol binario de búsqueda.
    root = None
    #Insertamos cada elemento del arreglo en el árbol.
    for key in arr:
        root = insert(root, key)
    result = []
    #Realizamos un recorrido en orden en el árbol para obtener los elementos ordenados.
    inorder_traversal(root, result)
    return result

#Definimos un arreglo desordenado.
arr = [4, 2, 5, 3, 1, 7, 6, 8, 0, 9]
#Ordenamos el arreglo utilizando tree_sort.
sorted_arr = tree_sort(arr)
#Imprimimos el arreglo ordenado.
print("Arreglo ordenado:", sorted_arr)