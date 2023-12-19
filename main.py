from sayText import sayText
from speechListen import getSpeechToText
import speech_recognition as sr
import keyboard
import requests
from dotenv import load_dotenv
import os

load_dotenv()

headers = {
    'x-api-key': os.getenv('API_KEY'),
    "Content-Type": "application/json",
}

recognizer = sr.Recognizer()

def key_pressed(event):
    if(event.name == "l" and event.event_type == keyboard.KEY_DOWN):
        print("Listening")
        textInput = getSpeechToText()
        data = {
            'sourceId': os.getenv('DOC_SOURCE'),
            'messages': [
                {
                    'role': 'user',
                    'content': textInput
                }
            ]
        }
        res = requests.post(
            'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data
        )
        answer = res.json()['content']
        print(answer)
        sayText(answer)


def main():
    try:
        print("Press 'l' to chat with the chatPDF API, and press '`' to exit")
        keyboard.hook(key_pressed)
        keyboard.wait('`')
        sayText("Closing program")
        keyboard.unhook_all()
    except Exception as e:
        sayText(e)



if __name__ == "__main__":
    main()