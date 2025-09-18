import requests  # Importa requests para hacer peticiones HTTP

def traductor(txt, lan, entrada=1):
    """
    Traduce un texto de un idioma a otro usando la API gratuita de MyMemory.

    Parámetros:
        txt (str): Texto o mensaje para solicitar el texto a traducir.
        lan (str): Lenguaje de traducción (por ejemplo: es|en, en|es, es|fr, etc.).
        entrada (int): 1 si se solicita entrada por teclado, 0 si se recibe el texto como parámetro.

    Retorna:
        str: Texto traducido.
    """
    try:
        if entrada == 1:
            entrada = input(f"{txt}")
        else:
            entrada = txt

        url = "https://api.mymemory.translated.net/get"
        params = {"q": entrada, "langpair": f"{lan}"}

        response = requests.get(url, params=params)
        response.raise_for_status()

        texto_traducido = response.json()["responseData"]["translatedText"]
        return texto_traducido

    except requests.exceptions.RequestException as e:
        print(f" Error en la traducción: {e}")
        return entrada


# ----------- EJEMPLO AUTOMÁTICO DE TRADUCCIÓN -----------

texto_programacion = (
    "La programación orientada a objetos (POO) es un paradigma de programación basado en el concepto de "
    "\"objetos\", que pueden contener datos y código. Los datos se representan en forma de atributos, y el código "
    "en forma de métodos. Uno de los principales beneficios de la POO es que permite reutilizar el código y "
    "organizar programas de manera más estructurada."
)

# Traduce automáticamente el texto de programación del español al inglés
resultado = traductor(texto_programacion, "es|en", entrada=0)

print(" Texto original en español:\n", texto_programacion)
print("\n Texto traducido al inglés:\n", resultado)
