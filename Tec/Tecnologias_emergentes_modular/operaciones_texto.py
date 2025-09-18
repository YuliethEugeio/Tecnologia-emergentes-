from transformers import pipeline  # Modelos de IA desde Hugging Face
import pyttsx3  # Texto a voz
from traductor import traductor  # Función local de traducción


def gen_text():
    """
    Traduce un texto del usuario, genera una continuación con GPT-2 y traduce el resultado de vuelta al español.
    """
    # 1. Entrada del usuario
    texto = traductor("Digite el texto base :", "es|en")

    # 2. Cargar modelo GPT-2
    generador = pipeline("text-generation", model="gpt2")

    # 3. Generar texto en inglés
    resultado = generador(texto, max_length=250, num_return_sequences=1, truncation=True)
    texto_generado = resultado[0]['generated_text']

    # 4. Mostrar resultado traducido al español
    print("\nTexto generado en español:")
    print(traductor(texto_generado[:500], "en|es", 0))


def traductor_nlp(texto):
    """
    Traduce un texto del español al inglés con modelo neuronal.
    """
    trad = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
    resultado = trad(texto)[0]['translation_text']
    print("Traducción:", resultado)


def text_to_audio(texto):
    """
    Convierte un texto en audio y lo guarda como archivo WAV.
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.save_to_file(texto, "output.wav")
    engine.runAndWait()
    print("Audio generado: output.wav")


def audio_to_text():
    """
    Transcribe un archivo de audio a texto usando Whisper.
    """
    stt = pipeline("automatic-speech-recognition", model="openai/whisper-small")
    audio_path = "audio.mp3"
    resultado = stt(audio_path)
    print("Texto transcrito:", resultado["text"])


def traducir():
    texto = input("Introduzca el texto a traducir: ")

    while True:
        lang = input(
            "Seleccione una operación:\n"
            "1 -> Español a inglés\n"
            "2 -> Inglés a español\n"
            "3 -> Español a portugués\n"
            "4 -> Portugués a español\n"
            "5 -> Español a italiano\n"
            "6 -> Italiano a español\n"
            "7 -> Español a francés\n"
            "8 -> Francés a español\n"
            "0 -> Salir\n"
            "Opción: "
        ).strip()

        if lang == '1':
            print(traductor(texto, "es|en"))
        elif lang == '2':
            print(traductor(texto, "en|es"))
        elif lang == '3':
            print(traductor(texto, "es|pt"))
        elif lang == '4':
            print(traductor(texto, "pt|es"))
        elif lang == '5':
            print(traductor(texto, "es|it"))
        elif lang == '6':
            print(traductor(texto, "it|es"))
        elif lang == '7':
            print(traductor(texto, "es|fr"))
        elif lang == '8':
            print(traductor(texto, "fr|es"))
        elif lang == '0':
            print("Fin traductor")
            break
        else:
            print("Seleccione una opción válida")

if __name__ == "__main__":
    gen_text()

