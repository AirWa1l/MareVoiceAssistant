import pyttsx3

# Para hacer varias ejecuciones se debe iniciarlizar el motor en cada iteración para evitar atascos
# Creamos una función para inicializar el motor y poder hacer varias iteraciones e invocaciones del Asistente de voz
def init_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    newVoiceRate = 150
    engine.setProperty('rate', newVoiceRate)
    return engine

def speech(audio):
    engine = init_engine()
    engine.say(audio)
    engine.runAndWait()
    engine.stop()