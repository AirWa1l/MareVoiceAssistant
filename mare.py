import datetime
from identity.information import username
from speech.speech import speech
from voiceRecognition import command

def hour_of_day():
    hour = datetime.datetime.now().hour
    match hour:
        case _ if hour >= 6 and hour < 12:
            speech("Buenos días!")
        case _ if hour >= 12 and hour < 18:
            speech("Buenas tardes!")
        case _ if hour >= 18 and hour < 24:
            speech("Buenas noches!")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speech(Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    date_time = f"{year}, {month} y {day}"
    # date_time = [year, month, day] es preferible no pasar listas, pyttsx3 procesa solo texto, por eso se daba ese error
    speech(date_time)

def greetings():
    speech(f"{hour_of_day()} {username}")
    speech("En que puedo ayudarte?")

# Por alguna razón esto no funciona como debería, pues pronuncia todo de forma incompleta
# adicionalmente, el speaker habla usando el idioma del computador

if __name__ == "__main__":
    greetings()

    while True:
        query = command().lower()
        print(query)

        match query:
            case _ if "hora" in query:
                time()
            case _ if "fecha" in query:
                date()
            case _ if "apagate" in query:
                quit()