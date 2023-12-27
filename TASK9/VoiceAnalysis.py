import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 150)    
engine.setProperty('volume', 0.9)  

text = input().strip()

engine.save_to_file(text, 'output.mp3')
engine.runAndWait()

r = sr.Recognizer()

with sr.AudioFile('output.mp3') as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)
