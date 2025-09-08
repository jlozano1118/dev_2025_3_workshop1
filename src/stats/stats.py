import math
class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La media aritmética de los números
            
        Ejemplo:
            promedio([1, 2, 3, 4, 5]) -> 3.0
        """
        if numeros == []:
            return 0
        else:
            suma = 0
            cantidad = len(numeros)
            for numero in numeros:
                suma = suma + numero

            media = suma / cantidad
            return media

        
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: El valor mediano
            
        Ejemplo:
            mediana([1, 2, 3, 4, 5]) -> 3.0
            mediana([1, 2, 3, 4]) -> 2.5
        """
        if numeros == []:
            return 0
        else:
            numeros = sorted(numeros) 
            n = len(numeros)
            mid = n // 2

            if n % 2 == 0: 
                return (numeros[mid - 1] + numeros[mid]) / 2
            else: 
                return numeros[mid]
                    
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: El valor más frecuente
            
        Ejemplo:
            moda([1, 2, 2, 3, 3, 3]) -> 3
        """
        if not numeros: 
            return None

        frecuencias = {}
        max_frecuencia = 0
        moda_valor = numeros[0]

        for num in numeros:
            if num not in frecuencias:
                frecuencias[num] = 1
            else:
                frecuencias[num] += 1

            if frecuencias[num] > max_frecuencia:
                max_frecuencia = frecuencias[num]
                moda_valor = num

        return moda_valor
        
        


    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La desviación estándar
            
        Ejemplo:
            desviacion_estandar([1, 2, 3, 4, 5]) -> 1.41...
        """
        if numeros == []:
            return 0
        else:
            n = len(numeros)
            media = sum(numeros) / n
            suma_cuadrados = 0
            for x in numeros:
                suma_cuadrados += (x - media) ** 2

            resultado = suma_cuadrados / n
            return math.sqrt(resultado)
        
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        desviacion = self.desviacion_estandar(numeros)
        return pow(desviacion,2)
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        if numeros == []:
            return 0
        else:
            maximo = max(numeros)
            minimo = min(numeros)
            return maximo - minimo