import urllib.request

import requests
import json
import pyttsx3
import speech_recognition
from termcolor import colored

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    try:
        urllib.request.urlopen('http://google.com')
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, 0, 4)

        try:
            print("Understanding..")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query
    except Exception as e:
        speak("have you connected to the Internet")
        print(colored('No connection', 'red'))
        speak("Sorry, for the timing I am not able to work offline")
def latestnews():
    api_dict = {"business" :"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=f160a8e45c9443df997d28761652599c" ,#Enter Your OWN API ,
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=f160a8e45c9443df997d28761652599c",#Enter Your OWN API ,
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=f160a8e45c9443df997d28761652599c",#Enter Your OWN API,
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=f160a8e45c9443df997d28761652599c",#Enter Your OWN API,
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=f160a8e45c9443df997d28761652599c",#Enter Your OWN API,
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=f160a8e45c9443df997d28761652599c"#Enter Your OWN API
}

    content = None
    url = None
    speak("Which field news do you want")
    print("[business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = takeCommand().lower()
    # field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            # print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        print("say continue or stop")
        a = takeCommand().lower()
        if str(a) == "continue":
            pass
        elif str(a) == "stop":
            break
        
    speak("thats all")

