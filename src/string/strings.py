class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto = texto.lower()

        caracteres = []
        for c in texto:
            if c.isalnum():
                caracteres.append(c)

        limpio = "".join(caracteres)

        return limpio == limpio[::-1]
        
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        invertida = ""
        for caracter in texto:
            invertida = caracter + invertida 
        return invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0
    
        for caracter in texto:
            if caracter in vocales:
                contador += 1
        
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0

        for caracter in texto:
            if caracter.isalpha() and caracter not in vocales:
                contador += 1

        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        texto1 = texto1.replace(" ", "").lower()
        texto2 = texto2.replace(" ", "").lower()

        if len(texto1) != len(texto2):
            return False
        
        return sorted(texto1) == sorted(texto2)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        texto = texto.strip()

        if not texto:
            return 0

        palabras = texto.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        resultado = []
        nueva_palabra = True

        for caracter in texto:
            if caracter == " ":
                resultado.append(caracter)
                nueva_palabra = True 
            elif nueva_palabra:
                resultado.append(caracter.upper())
                nueva_palabra = False
            else:
                resultado.append(caracter.lower())
        
        return "".join(resultado)
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        resultado = []
        ultimo_espacio = False

        for caracter in texto:
            if caracter == " ":
                if not ultimo_espacio:  
                    resultado.append(caracter)
                ultimo_espacio = True
            else:
                resultado.append(caracter)
                ultimo_espacio = False

        return "".join(resultado)
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        
        numeros = "-0123456789"
        for elemento in texto:
            if elemento not in numeros:
                return False
        
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        resultado = []

        for caracter in texto:
            if caracter.isalpha(): 
                base = ord('A') if caracter.isupper() else ord('a')
                nuevo_codigo = (ord(caracter) - base + desplazamiento) % 26 + base
                resultado.append(chr(nuevo_codigo))
            else:
                resultado.append(caracter)

        return "".join(resultado)
        
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        resultado = []

        for caracter in texto:
            if caracter.isalpha():  
                base = ord('A') if caracter.isupper() else ord('a')
                nuevo_codigo = (ord(caracter) - base - desplazamiento) % 26 + base
                resultado.append(chr(nuevo_codigo))
            else:
                resultado.append(caracter)

        return "".join(resultado)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        posiciones = []
        len_sub = len(subcadena)

        if len_sub == 0:
            return posiciones
        
        for i in range(len(texto) - len_sub + 1):
            if texto[i:i+len_sub] == subcadena:
                posiciones.append(i)

        return posiciones