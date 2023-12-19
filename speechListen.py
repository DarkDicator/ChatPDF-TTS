import speech_recognition as sr
from sayText import sayText

recognizer = sr.Recognizer()

def listenToMic():
    with sr.Microphone() as mic:
        audio = recognizer.listen(mic, 2, 7)
        return audio
    
def convertVoiceToText(voice):
    try:
        text = recognizer.recognize_google(voice)
        print(text)
    except sr.UnknownValueError:
        text = "Sorry, I didn't understand that."
    except Exception as e:
        print(e)
        text = e
    return text

def getSpeechToText():
    sayText("I'm Listening")
    voice = listenToMic()
    text = convertVoiceToText(voice)
    return text