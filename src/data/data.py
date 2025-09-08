class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        invertida = []
        i = len(lista) - 1
        while i >= 0:
            invertida.append(lista[i])
            i -= 1
        return invertida
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        resultado = []
        vistos = []
        for elemento in lista:
            if id(elemento) not in vistos:
                resultado.append(elemento)
                vistos.append(id(elemento))
        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        for elemento in lista2:
            lista1.append(elemento)

        lista1.sort()
        return lista1
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:  
            return []
        
        n = len(lista)
        k = k % n
        
        resultado = [None] * n
        
        for i in range(n):
            nuevo_indice = (i + k) % n
            resultado[nuevo_indice] = lista[i]
        
        return resultado
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        n = len(lista) + 1 
        suma_total = n * (n + 1) // 2
        suma_lista = sum(lista)
        return suma_total - suma_lista
            
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila = []

        def push(x):
            pila.append(x)

        def pop():
            if pila:
                return pila.pop()
            return None

        def peek():
            if pila:
                return pila[-1]
            return None 

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola = []

        def enqueue(x):
            cola.append(x) 

        def dequeue():
            if cola:
                return cola.pop(0) 
            return None 

        def peek():
            if cola:
                return cola[0]
            return None

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        if not matriz:  
            return []
        
        filas = len(matriz)
        columnas = len(matriz[0])
        
        transpuesta = [[0] * filas for _ in range(columnas)]
        
        for i in range(filas):
            for j in range(columnas):
                transpuesta[j][i] = matriz[i][j]
        
        return transpuesta