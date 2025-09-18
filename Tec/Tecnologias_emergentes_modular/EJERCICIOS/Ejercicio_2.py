import hashlib  # Para calcular el hash SHA-256 (función de seguridad criptográfica)
import time     # Para medir el tiempo (opcional en este código)
from datetime import datetime # Para registrar la fecha y hora de cada acción

# Lista con los nombres de los tres candidatos
candidatos = ["Ana", "Luis", "Maria"]

# -------------------------- CLASE VOTO --------------------------
# Clase que representa un voto emitido por un votante
class Voto:
    def __init__(self, votante_id, candidato):
        self.votante_id = votante_id # ID del votante (simula un identificador único)
        self.candidato = candidato   # Nombre del candidato por el que se vota
        self.timestamp = datetime.utcnow().isoformat() # Fecha y hora del voto en formato ISO (UTC)

    def __str__(self):
        # Representación del voto como cadena legible
        return f"{self.votante_id} vota por \
        {self.candidato} ({self.timestamp})"


# -------------------------- CLASE BLOQUE ------------------------
# Clase que representa un bloque dentro de la blockchain
class Bloque:
    def __init__(self, votos, hash_anterior="0"*64):
        self.votos = votos           # Lista de objetos de tipo Voto
        self.hash_anterior = hash_anterior # Hash del bloque anterior (por defecto 64 ceros)
        self.timestamp = datetime.utcnow().isoformat() # Fecha y hora de creación del bloque
        self.nonce = 0           # Número de intento usado para "minar" el bloque
        self.hash = self.calcular_hash() # Hashinicial del bloque (antes de minar)

    def calcular_hash(self):
        # Concatena los votos, hash anterior, tiempo y
        # nonce, y luego calcula el hash
        contenido = "".join(str(voto) for voto in \
        self.votos) + self.hash_anterior + self.timestamp + \
        str(self.nonce)
        return \
        hashlib.sha256(contenido.encode()).hexdigest()

    def minar(self, dificultad=4):
        # Prueba de trabajo: busca un hash que comience con
        # cierto número de ceros
        print("Minando bloque...")
        while not self.hash.startswith("0" * dificultad):
            self.nonce += 1 # Incrementa el nonce hasta que el hash sea válido
            self.hash = self.calcular_hash()
        print(f"Bloque minado con hash: {self.hash}") # Muestra el hash válido una vez encontrado

# -------------------------- CLASE BLOCKCHAIN --------------------
# Clase que representa la cadena de bloques (blockchain)
class Blockchain:
    def __init__(self):
        self.cadena = [] #Lista para almacenar Los bloques

    def agregar_bloque(self, bloque):
        bloque.minar() # Minar el bloque antes de añadirlo
        self.cadena.append(bloque) # Añadir el bloque a la cadena
    
    def verificar_integridad(self):
        # Revisa que cada bloque esté correctamente encadenado
        for i in range(1, len(self.cadena)):
            actual = self.cadena[i]
            anterior = self.cadena[i - 1]
            
            if actual.hash_anterior != anterior.hash: #Verifica el enlace entre bloques
                    return False
            
            if actual.hash != actual.calcular_hash(): #Verifica que el hash no haya sido manipulado
                    return False

        return True # Si pasa todas las verificaciones, la cadena es válida  
                
    

# -------------------------- CREACIÓN DE VOTOS SIMULADOS ---------------------
votos_bloque1 = [
    Voto("ID001", "Ana"),
    Voto("ID002", "Luis"),
    Voto("ID003", "Ana"),
    Voto("ID004", "Ana")
]

votos_bloque2 = [
    Voto("ID005", "Maria"),
    Voto("ID006", "Luis"),
    Voto("ID007", "Ana"),
    Voto("ID008", "Luis")
]

# -------------------------- CREACIÓN DE LA BLOCKCHAIN -----------------------
cadena_votacion = Blockchain() # Se crea la instancia de la cadena

# Crear el primer bloque (bloque génesis)
bloque1 = Bloque(votos_bloque1)

cadena_votacion.agregar_bloque(bloque1) # Se agrega el primer bloque

# Crear y agregar el segundo bloque (referencia al hash del primero)
bloque2 = Bloque(votos_bloque2, cadena_votacion.cadena[-1].hash)
cadena_votacion.agregar_bloque(bloque2)

# -------------------------- VERIFICACIÓN DE LA CADENA -------------------
print("¿Cadena válida?:", cadena_votacion.verificar_integridad()) # Verifica si la cadena está íntegra

# -------------------------- MOSTRAR RESULTADOS --------------------------
print("\n--- Resultados de votación ---")
conteo = {candidato: 0 for candidato in candidatos} # Diccionario para contar los votos por candidato

# Recorre cada bloque y cuenta los votos
for bloque in cadena_votacion.cadena:
    for voto in bloque.votos:
        conteo[voto.candidato] += 1 # Incrementa el conteo para el candidato correspondiente

# Imprime los resultados finales
for c, v in conteo.items():
    print(f"{c}: {v} votos")