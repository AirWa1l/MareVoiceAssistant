# import speech_recognition as sr
import pyttsx3
import datetime

# Para hacer varias ejecuciones se debe iniciarlizar el motor en cada iteración para evitar atascos

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)

def speech(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    return Time

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    date_time = f"{year}, {month} and {day}"
    # date_time = [year, month, day] es preferible no pasar listas, pyttsx3 procesa solo texto, por eso se daba ese error
    return date_time

# Por alguna razón esto no funciona como debería, pues pronuncia todo de forma incompleta
# adicionalmente, el speaker habla usando el idioma del computador

date()
test = f"{date()}, {time()} y hola, como estas?"
speech(test)