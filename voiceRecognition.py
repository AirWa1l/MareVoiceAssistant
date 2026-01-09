import speech_recognition as sr
from speech.speech import speech

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='es-ES')
        print(query)
    except Exception as e:
        print(e)
        speech("No te entendí")
        speech("Podrías decirlo de nuevo?")
        return "None"
    
    return query

if __name__ == "__main__":
    command()
