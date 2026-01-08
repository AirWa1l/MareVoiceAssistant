# import speech_recognition as sr
import pyttsx3
import datetime
import os
from identity.information import username

# Para hacer varias ejecuciones se debe iniciarlizar el motor en cada iteración para evitar atascos
# Creamos una función para inicializar el motor y poder hacer varias iteraciones e invocaciones del Asistente de voz
def init_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    newVoiceRate = 190
    engine.setProperty('rate', newVoiceRate)
    return engine

def speech(audio):
    engine = init_engine()
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    return Time

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    date_time = f"{year}, {month} and {day}"
    # date_time = [year, month, day] es preferible no pasar listas, pyttsx3 procesa solo texto, por eso se daba ese error
    return date_time

def greetings():
    speech(f"Bienvenido! {username}")
    speech(date())
    speech(time())
    speech("En que puedo ayudarte?")

# Por alguna razón esto no funciona como debería, pues pronuncia todo de forma incompleta
# adicionalmente, el speaker habla usando el idioma del computador

#date()
#test = f"{date()}, {time()} y hola, como estas?"
#speech(test)

greetings()