class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n < 0:
            raise ValueError("n debe ser un entero no negativo")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        if n <= 0:
            return []
        elif n == 1:
            return [0]

        fib = [0, 1] 
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2]) 
        return fib
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        cont = 0
        for i in range(1,n+1):
            if n % i == 0:
                cont +=1

        if cont == 2:
            return True
        else:
            return False
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        lista = []
        cont = 0
        for i in range(1,n+1):
            for x in range(1, i+1):
                if i % x == 0:
                    cont +=1

            if cont == 2:
                lista.append(i)
            
            cont = 0
        
        return lista
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n == 0 or n == 1:
            return False
        suma = 0
        for i in range(1,n):
            if n % i == 0:
                suma += i

        if suma == n:
            return True
        else:
            return False
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        triangulo = []

        for i in range(filas):
            fila = [1] * (i + 1)

            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]

            triangulo.append(fila)

        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        fac = 1
        for i in range(1,n+1):
            fac = fac * i

        return fac
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        a = abs(a)
        b = abs(b)

        while b != 0:
            resto = a % b
            a = b          
            b = resto       
        return a
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        if a == 0 or b == 0:
             return 0  

        mcd_ab = self.mcd(a, b)
        return abs(a * b) // mcd_ab
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        numeroS = str(n)
        arreglo = []
        suma = 0
        for x in numeroS:
            arreglo.append(int(x))
        
        for x in arreglo:
            suma += x
        
        return suma
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        digitos = str(n)
        num_digitos = len(digitos)

        suma = 0
        for d in digitos:
            suma += int(d) ** num_digitos

        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        n = len(matriz)
        for fila in matriz:
            if len(fila) != n:
                return False

        suma_objetivo = sum(matriz[0])

        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False

        for col in range(n):
            suma_columna = 0
            for fila in range(n):
                suma_columna += matriz[fila][col]
            if suma_columna != suma_objetivo:
                return False

        suma_diag_principal = 0
        for i in range(n):
            suma_diag_principal += matriz[i][i]
        if suma_diag_principal != suma_objetivo:
            return False

        suma_diag_secundaria = 0
        for i in range(n):
            suma_diag_secundaria += matriz[i][n - 1 - i]
        if suma_diag_secundaria != suma_objetivo:
            return False

        return True