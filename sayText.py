import pyttsx3
def sayText(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

