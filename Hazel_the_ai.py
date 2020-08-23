import pyttsx3
import wikipedia
import datetime
import speech_recognition as sr
import webbrowser
import os
import tkinter as tk

root = tk.Tk()

webbrowser.register('firefox', None,webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("I am Hazel. please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 800
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()

    mybutton = tk.Button(root, text="listen", command=takeCommand, fg="green", bg="black")
    true = True
    while true:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            try:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                print(results)
                speak(results)
            except Exception:
                speak("connection error...please try again...")


        elif 'open youtube' in query:
            try:
                webbrowser.get('firefox').open("youtube.com")
            except Exception:
                speak("connection error...please try again...")

        elif 'open google' in query:
            try:
                webbrowser.get('firefox').open("google.com")
            except Exception:
                speak("connection error...please try again...")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is:{strTime}")

        elif 'play music' in query:
            path = "C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(path)

        elif 'youtube' in query:
            try:
                query=query.replace("youtube","")
                query=query.replace(" ","+")
                webbrowser.get('firefox').open(f"youtube.com/results?search_query={query}")
            except Exception:
                speak("connection error...please try again...")

        elif 'google' in query:
            try:
                query=query.replace("google","")
                query=query.replace(" ","+")
                webbrowser.get('firefox').open(f"google.com/search?channel=crow2&client=firefox-b-d&q={query}")
            except Exception:
                speak("connection error...please try again...")

        elif 'open Firefox' in query:
            webbrowser.get('firefox')

        elif 'open literature chart' in  query:
            webbrowser.get('firefox').open("litcharts.com")

        elif 'beep' in query:
            os.startfile("C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python38")

        elif 'stop' in query:
            true = False


    
