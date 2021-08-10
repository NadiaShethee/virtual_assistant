import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr
import cv2
import random
from requests import get
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<6:
        speak("good night")

    elif hour>=6 and hour<11:
        speak("Good morning")

    elif hour>=11 and hour<15:
        speak("It's About midday.")
    elif hour>=15 and hour<17:
        speak("Good Afternoon.")
    else:
        speak("Good Evening")
    speak("I'm your virtual Assistant. How may I help you!!")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....!")
        r.pause_threshold = 1
        audio = r.listen(source)
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing.........!")
        query = r.recognize_google(audio, language='en')
        print(f"user said: {query} \n")
    except Exception as e:
        print(e)
        print("Please say that again.......!")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.echo()
    server.starttls()
    server.login('')
    server.sendmail('nadyashithy@gmail,com', to, content)
    server.close()


if _name__ == "__main_":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching.......')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('what should I search?')
            cm = takeCommand().lower()
            webbrowser.open(f'{cm}')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'open command prompt' in query:
            os.system('start cmd')
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"ma'am, the time is{strTime}")
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
                cap.release()
                cv2.destroyAllWindows()


        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\Visual Studio Code"
            os.startfile(codePath)
        elif 'email to nadia' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = 'nadyashithy@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak('sorry! I faild.')

        elif 'ip address' in query:
            ip = get('https//api.//ipify.org').text
            speak(f"your ip address is{ip}")