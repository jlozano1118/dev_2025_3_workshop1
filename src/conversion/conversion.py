import math
class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        
        Args:
            celsius (float): Temperatura en grados Celsius
            
        Returns:
            float: Temperatura en grados Fahrenheit
            
        Fórmula: F = (C × 9/5) + 32
        
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        fahren = (celsius * 9/5) + 32
        return fahren
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
            
        Returns:
            float: Temperatura en grados Celsius
            
        Fórmula: C = (F - 32) × 5/9
        
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        pies = metros * 3.28084
        return pies
    
    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
        metros = pies * 0.3048
        return metros
    
    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.
        
        Args:
            decimal (int): Número decimal (positivo)
            
        Returns:
            str: Representación binaria como string
            
        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """

        if decimal == 0:
            return "0"
        elif decimal == 1:
            return "1"
        else:
            cociente = decimal
            arreglo = []
            while cociente > 1:
                residuo = cociente % 2
                arreglo.append(residuo)
                cociente = cociente // 2  

            arreglo.append(1)
            arreglo.reverse()

            binario = ""
            for x in arreglo:
                binario += str(x)

            return binario


    
    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
        arreglo = []
        cont = 0
        suma = 0
        if binario == "0":
            return 0
        elif binario == "1":
            return 1
        else:
            for x in binario:
                arreglo.append(int(x))

            arreglo.reverse()
            for x in arreglo:
                suma += ((pow(2,cont)) * x)
                cont +=1

            return suma

        
    
    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        if numero < 1 or numero > 3999:
            return "Número fuera de rango (1-3999)"

        valores = [1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4, 1]
        simbolos = ["M", "CM", "D", "CD",
                    "C", "XC", "L", "XL",
                    "X", "IX", "V", "IV", "I"]

        resultado = ""
        i = 0
        while numero > 0:
            # Restar mientras sea posible
            while numero >= valores[i]:
                resultado += simbolos[i]
                numero -= valores[i]
            i += 1

        return resultado
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        valores = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        i = 0
        while i < len(romano):
            # Caso: símbolo menor antes de uno mayor (ej: IV, IX, XL, XC, etc.)
            if i + 1 < len(romano) and valores[romano[i]] < valores[romano[i + 1]]:
                total += valores[romano[i + 1]] - valores[romano[i]]
                i += 2  # saltar los dos símbolos
            else:
                total += valores[romano[i]]
                i += 1

        return total
    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        morse = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----."
        }
    
        texto = texto.upper()
        codigo = []
    
        for char in texto:
            if char == " ":
                codigo.append("/") 
            elif char in morse:
                codigo.append(morse[char])
            

        return " ".join(codigo)
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        morse_dict = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
            "E": ".", "F": "..-.", "G": "--.", "H": "....",
            "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---", "P": ".--.",
            "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----."
        }

        # invertimos el diccionario (morse → letra)
        morse_to_text = {v: k for k, v in morse_dict.items()}

        palabras = morse.split(" / ")  # separa palabras ("/" representa espacio)
        texto = []

        for palabra in palabras:
            letras = palabra.split()  # separa letras por espacios
            texto.append("".join(morse_to_text[letra] for letra in letras if letra in morse_to_text))

        return " ".join(texto)
