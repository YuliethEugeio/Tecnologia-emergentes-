from hashlib import sha256
from datetime import datetime, timezone
import time

# Clase para representar una transacción
class Transaccion:
    def __init__(self, emisor, receptor, cantidad):
        self.emisor = emisor
        self.receptor = receptor
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.emisor} le envia {self.cantidad} a {self.receptor}"

# Transacciones para cada bloque
transacciones_bloque1 = [
    Transaccion("Jose", "Jorge", 5),
    Transaccion("Jorge", "Jairo", 10),
    Transaccion("Jorge", "Daniela", 4)
]

transacciones_bloque2 = [
    Transaccion("Jose", "Jairo", 5),
    Transaccion("Juan", "Jairo", 10),
    Transaccion("Jorge", "Jose", 4)
]

# Clase para representar un bloque
class Bloque:
    def __init__(self, bloque_anterior, transacciones):
        self.bloque_anterior = bloque_anterior
        self.transacciones = transacciones
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.intento_hash = 0

    def calcular_hash(self):
        transacciones_str = "#".join(str(t) for t in self.transacciones)
        info = transacciones_str + self.bloque_anterior + self.timestamp + str(self.intento_hash)
        return sha256(info.encode()).hexdigest()

# Clase que representa la cadena de bloques
class Blockchain:
    dificultad = 5

    def __init__(self):
        self.cadena = []

    def agregar_bloque(self, bloque):
        self.cadena.append(bloque)

    def minar_bloque(self, bloque):
        inicio = time.time()
        while True:
            hash_actual = bloque.calcular_hash()
            if hash_actual.startswith("0" * self.dificultad):
                self.agregar_bloque(bloque)
                print(f"Bloque minado con éxito: {hash_actual}")
                print(f"Nonce encontrado: {bloque.intento_hash}")
                print(f"Tiempo de minado: {round(time.time() - inicio, 2)} segundos\n")
                break
            else:
                bloque.intento_hash += 1

    def verificar_integridad(self):
        for i in range(1, len(self.cadena)):
            bloque_anterior = self.cadena[i - 1]
            bloque_actual = self.cadena[i]
            if bloque_actual.bloque_anterior != bloque_anterior.calcular_hash():
                return False
        return True

# Función principal
def cadena_bloques():
    mi_blockchain = Blockchain()

    bloque1 = Bloque("0" * 64, transacciones_bloque1)
    mi_blockchain.minar_bloque(bloque1)

    bloque2 = Bloque(mi_blockchain.cadena[-1].calcular_hash(), transacciones_bloque2)
    mi_blockchain.minar_bloque(bloque2)

    print("¿Cadena íntegra?:", mi_blockchain.verificar_integridad())

# 🔽 Ejecutar el programa
cadena_bloques()
