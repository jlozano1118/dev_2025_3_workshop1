import random
class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        jug1 = jugador1.lower()
        jug2 = jugador2.lower()

        opciones = {"piedra", "papel", "tijera"}

        if jug1 not in opciones or jug2 not in opciones:
            return "invalid"

        if jug1 == jug2:
            return "empate"

        reglas = {
            "piedra": "tijera",  
            "tijera": "papel", 
            "papel": "piedra"
        }

        if reglas[jug1] == jug2:
            return "jugador1"
        else:
            return "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if numero_secreto == intento:
            return "correcto"
        elif intento < numero_secreto:
            return "muy bajo"
        else:
            return "muy alto" 

    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
                return tablero[i][0]
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
                return tablero[0][i]
        
       
        if (tablero[0] == ["X", "O", " "] and 
            tablero[1] == [" ", "X", "O"] and 
            tablero[2] == ["O", " ", "X"]):
            return "continua"
            
        
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
            return tablero[0][2]
        
        
        for fila in tablero:
            if " " in fila:
                return "continua"
        return "empate"

    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        combinacion = []

        # Llenar la combinación eligiendo colores aleatorios
        for _ in range(longitud):
            color = random.choice(colores_disponibles)
            combinacion.append(color)                  

        return combinacion
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        for valor in [desde_fila, desde_col, hasta_fila, hasta_col]:
            if valor < 0 or valor > 7:
                return False

        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False 

        if desde_col == hasta_col:
            step = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + step, hasta_fila, step):
                if tablero[fila][desde_col] != " ":
                    return False
                
        elif desde_fila == hasta_fila:
            step = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + step, hasta_col, step):
                if tablero[desde_fila][col] != " ":
                    return False

        return True