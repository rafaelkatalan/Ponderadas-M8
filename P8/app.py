import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from io import BytesIO
import pygame
from deep_translator import GoogleTranslator

engine = pyttsx3.init()

def speech_to_text():
    # Crie um objeto de reconhecimento de fala
    recognizer = sr.Recognizer()
    # Abra o microfone para captura de áudio
    with sr.Microphone() as source:
        # Ajuste o nível de ruído para a melhor captura
        recognizer.adjust_for_ambient_noise(source)
        print("Capturando áudio...")
        # Capture o áudio do microfone
        audio = recognizer.listen(source)
        try:
            print("Convertendo fala em texto...")
            # Use o Google Web Speech API para converter áudio em texto
            text = recognizer.recognize_google(audio, language="pt-BR")
            return text
        except sr.UnknownValueError:
            print("Não foi possível reconhecer a fala.")
        except sr.RequestError as e:
            print("Erro na requisição ao Google Web Speech API; {0}".format(e))

pygame.mixer.init()


def speak(text, language):
    mp3_fp = BytesIO()
    tts = gTTS(text=text, lang=language)      
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

while True:
    Input = speech_to_text()
    print(Input)
    try:
        translator = GoogleTranslator(source='pt', target='iw')
        traduzido = translator.translate(text=Input)
        print(traduzido)

        speak(traduzido, 'iw')
    except Exception as e:
        print(e)
        speak("Não entendi. Repita por favor para eu poder traduzir corretamente", 'pt')
