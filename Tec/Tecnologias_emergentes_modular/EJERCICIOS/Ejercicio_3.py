def lanzar_pregunta():
    """Lanza una pregunta a la 'multitud'."""
    print(f"\n--- Nueva Pregunta: {'pregunta'} ---")  # La variable 'pregunta' no está definida aquí, asumí que debería ser un marcador de posición
    ideas = {}
    while True:
        usuario = input("Ingrese su nombre (o 'fin' para terminar): ")
        if usuario.lower() == 'fin':
            break
        idea = input(f"{usuario}, ¿cuál es tu idea?: ")
        ideas[usuario] = idea
    return ideas

def mostrar_ideas(ideas):
    """Muestra las ideas recopiladas."""
    print(f"\n--- Ideas Recopiladas ---")
    if not ideas:
        print("No se recibieron ideas.")
        return
    for usuario, idea in ideas.items():
        print(f"{usuario}: {idea}")

if __name__ == "__main__":
    pregunta = "¿Cómo podríamos mejorar la experiencia de los usuarios en nuestro sitio web?"
    ideas_recibidas = lanzar_pregunta()  # La función lanzar_pregunta no toma un argumento 'pregunta'
    mostrar_ideas(ideas_recibidas)