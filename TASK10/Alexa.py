import speech_recognition as sr
import pyttsx3
import datetime
import pytz

r = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        return text

def respond(text):
    if "hello" in text:
        reply = "Hello, how can I help you?"
    elif "what is your name" in text:
        reply = "I'm a virtual assistant."
    elif "what time is it" in text:
        now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        reply = "The current time is " + now.strftime("%H:%M:%S")
    elif "goodbye" in text:
        reply = "Goodbye!"
        engine.say(reply)
        engine.runAndWait()
        return False
    else:
        reply = "I'm sorry, I didn't understand that."
    
    engine.say(reply)
    engine.runAndWait()
    return True

while True:
    text = listen()
    if not respond(text):
        break
