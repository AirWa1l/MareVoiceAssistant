import datetime
from identity.information import username
from speech.speech import speech
from voiceRecognition import command

def time():
    #Time = datetime.datetime.now().strftime("%I:%M")
    hour = datetime.datetime.now().hour
    match hour:
        case _ if hour >= 6 and hour < 12:
            speech("Buenos días!")
        case _ if hour >= 12 and hour < 18:
            speech("Buenas tardes!")
        case _ if hour >= 18 and hour < 24:
            speech("Buenas noches!")

    #return Time

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    date_time = f"{year}, {month} y {day}"
    # date_time = [year, month, day] es preferible no pasar listas, pyttsx3 procesa solo texto, por eso se daba ese error
    return date_time

def greetings():
    speech(f"{time()} {username}")
    speech(date())
    speech("En que puedo ayudarte?")

# Por alguna razón esto no funciona como debería, pues pronuncia todo de forma incompleta
# adicionalmente, el speaker habla usando el idioma del computador

if __name__ == "__main__":
    greetings()
    command()