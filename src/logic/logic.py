class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        """
        Implementa la operación lógica AND.
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a AND b
        """
        resultado = a and b
        return resultado
    
    def OR(self, a, b):
        """
        Implementa la operación lógica OR.
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a OR b
        """
        resultado = a or b
        return resultado
    
    def NOT(self, a):
        """
        Implementa la operación lógica NOT.
        
        Args:
            a (bool): Valor booleano
            
        Returns:
            bool: Resultado de NOT a
        """
        resultado = not a
        return resultado
    
    def XOR(self, a, b):
        """
        Implementa la operación lógica XOR (OR exclusivo).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XOR b
        """
        resultado = a ^ b
        return resultado
    
    def NAND(self, a, b):
        """
        Implementa la operación lógica NAND (NOT AND).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a NAND b
        """
        resultado = not(a and b)
        return resultado
    
    def NOR(self, a, b):
        """
        Implementa la operación lógica NOR (NOT OR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a NOR b
        """
        resultado = not(a or b)
        return resultado
    
    def XNOR(self, a, b):
        """
        Implementa la operación lógica XNOR (NOT XOR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XNOR b
        """
        resultado = not(a ^ b)
        return resultado
    
    def implicacion(self, a, b):
        """
        Implementa la operación lógica de implicación (a -> b).
        
        Args:
            a (bool): Primer valor booleano (antecedente)
            b (bool): Segundo valor booleano (consecuente)
            
        Returns:
            bool: Resultado de la implicación
        """
        resultado = (not a) or b
        return resultado
    
    def bi_implicacion(self, a, b):
        """
        Implementa la operación lógica de bi-implicación (a <-> b).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de la bi-implicación
        """
        resultado = a == b
        return resultado
    
    
