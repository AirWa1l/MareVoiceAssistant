import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)

def speech(audio):
    engine.say(audio)
    engine.runAndWait()

speech("Hola, como estas")