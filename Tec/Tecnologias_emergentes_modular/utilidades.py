import os
import msvcrt

def clrscr():
    """Limpia la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def getch():
    """Pausa hasta que el usuario presione una tecla"""
    print("Presione cualquier tecla para continuar ...")
    msvcrt.getch()

# ----------- PRUEBA -----------
print("¡Bienvenido al sistema!")
getch()       # Espera una tecla
clrscr()      # Limpia pantalla
print("Pantalla limpia. Fin del programa.")
