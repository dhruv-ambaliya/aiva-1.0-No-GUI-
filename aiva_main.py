import datetime
import time
from email import message
import webbrowser
import PyPDF2
import psutil
from numpy import tile
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest
import urllib.request
from termcolor import colored
from pywikihow import search_wikihow
import pyjokes
from wikipedia import wikipedia

# for i in range(3):
#     a = input("Enter Password to open aiva :- ")
#     pw_file = open("password.txt", "r")
#     pw = pw_file.read()
#     pw_file.close()
#     if (a == pw):
#         print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
#         break
#     elif (i == 2 and a != pw):
#         exit()
#
#     elif (a != pw):
#         print("Try Again")

# from INTRO import play_gif
# play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def comum(query):
        print(query)
        if ('hi'in query) or('hai'in query) or ('hey'in query) or ('hello' in query) :
            speak("Hello what can I help for u")
        else :
            No_result_found()
def No_result_found():
        speak('I couldn\'t understand, could you please say it again.')
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
def Fun(query):
        print(query)
        if 'your name' in query:
            speak("My name is AIVA")
        elif 'my name' in query:
            speak("your name is Dhruv")
        elif 'university name' in query:
            speak("you are studing in GEC Bhavnagar, with batcheloe in Computer Engineering")
        elif 'what can you do' in query:
            speak("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
        elif 'your age' in query:
            speak("I am very young that u")
        elif 'date' in query:
            speak('Sorry not intreseted, I am having headache, we will catch up some other time')
        elif 'are you single' in query:
            speak('No, I am in a relationship with wifi')
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'are you there' in query:
            speak('Yes  I am here')
        elif 'tell me something' in query:
            speak(', I don\'t have much to say, you only tell me someting i will give you the company')
        elif 'thank you' in query:
            speak(', I am here to help you..., your welcome')
        elif 'in your free time' in query:
            speak(', I will be listening to all your words')
        elif 'i love you' in query:
            speak('I love you too ')
        elif 'can you hear me' in query:
            speak('Yes , I can hear you')
        elif 'do you ever get tired' in query:
            speak('It would be impossible to tire of our conversation')
        else :
            speak("Its not in my features do you want me to google search it")

def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
def How():
        speak("How to do mode is is activated")
        while True:
            speak("Please tell me what you want to know")
            how = takeCommand()
            try:
                if ("exit" in how) or("close" in how):
                    speak("Ok sir how to mode is closed")
                    break

                else:
                    max_result=1
                    how_to = search_wikihow(how,max_result)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
            except Exception as e:
                speak("Sorry sir, I am not able to find this")
def pdf_reader():
        speak(" enter the name of the book which you want to read")
        n = input("Enter the book name: ")
        n = n.strip()+".pdf"
        book_n = open(n,'rb')
        pdfReader = PyPDF2.PdfFileReader(book_n)
        pages = pdfReader.numPages
        speak(f" there are total of {pages} in this book")
        speak("plsase enter the page number Which I nedd to read")
        num = int(input("Enter the page number: "))
        page = pdfReader.getPage(num)
        text = page.extractText()
        print(text)
        speak(text)
def CloseApp(query):
        print(query)
        if ('calculator'in query) :
            speak("okay , closeing caliculator")
            os.system("taskkill /f /im calc.exe")
        elif ('paint'in query) :
            speak("okay , closeing mspaint")
            os.system("taskkill /f /im mspaint.exe")
        elif ('notepad'in query) :
            speak("okay , closeing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif ('discord'
              in query) :
            speak("okay , closeing discord")
            os.system("taskkill /f /im Discord.exe")
        elif ('vs code'in query) :
            speak("okay , closeing vs code")
            os.system("taskkill /f /im Code.exe")

        elif ('media player'in query) :
            speak("okay , closeing media player")
            os.system("taskkill /f /im vlc.exe")
        else :
            speak("its not in application")

def B_S(query):
    print(query)
    try:
        # ('what is meant by' in query) or ('tell me about' in query) or ('who the heck is' in query)
        if ('wikipedia' in query):
            target1 = query.replace('search for', '')
            target1 = target1.replace('in wikipedia', '')
        elif ('what is meant by' in query):
            target1 = query.replace("what is meant by", " ")
        elif ('tell me about' in query):
            target1 = query.replace("tell me about", " ")
        elif ('who the heck is' in query):
            target1 = query.replace("who the heck is", " ")
        print("searching....")
        info = wikipedia.summary(target1, 5)
        print(info)
        speak("according to wikipedia " + info)
    except:
        speak("Its not on wikipedia")


def silenceTime(query):
        print(query)
        x = 0
        # caliculating the given time to seconds from the speech commnd string
        if ('10' in query) or ('ten' in query):
            x = 600
        elif '1' in query or ('one' in query):
            x = 60
        elif '2' in query or ('two' in query):
            x = 120
        elif '3' in query or ('three' in query):
            x = 180
        elif '4' in query or ('four' in query):
            x = 240
        elif '5' in query or ('five' in query):
            x = 300
        elif '6' in query or ('six' in query):
            x = 360
        elif '7' in query or ('seven' in query):
            x = 420
        elif '8' in query or ('eight' in query):
            x = 480
        elif '9' in query or ('nine' in query):
            x = 540
        silence(x)

    # Silence
def silence(k):
        t = k
        s = "Ok  I will be silent for " + str(t / 60) + " minutes"
        speak(s)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        speak(" " + str(k / 60) + " minutes over")


def condition():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage + " percentage")
    battray = psutil.sensors_battery()
    percentage = battray.percent
    speak(f"our system have {percentage} percentage Battery")
    if percentage >= 75:
        speak(f"we could have enough charging to continue our work")
    elif percentage >= 40 and percentage <= 75:
        speak(f"we should connect out system to charging point to charge our battery")
    elif percentage >= 15 and percentage <= 30:
        speak(f"we don't have enough power to work, please connect to charging")
    else:
        speak(f" we have very low power, please connect to charging otherwise the system will shutdown very soon")


if __name__ == "__main__":
    try:
        while True:
            query = takeCommand().lower()
            if "start" in query:
                from GreetMe import greetMe
                greetMe()

                while True:
                    query = takeCommand().lower()
                    if "go to sleep" in query:
                        speak("Ok sir , You can call me anytime")
                        break

                    #################### aiva: THe Trilogy 2.0 #####################
                    elif "send email" in query:
                        import email_send
                    elif "send mail" in query:
                        import email_send
                    elif "my email" in query:
                        import email_control
                    elif "my mail" in query:
                        import email_control
                    elif "mail" in query:
                        import email_control
                    elif "email" in query:
                        import email_control

                    elif "change password" in query:
                        speak("What's the new password")
                        new_pw = input("Enter the new password\n")
                        new_password = open("password.txt", "w")
                        new_password.write(new_pw)
                        new_password.close()
                        speak("Done sir")
                        speak(f"Your new password is{new_pw}")
                    elif 'play music' in query:
                        music_dir = 'D:\CE\Sem 6\DE\Project\songs'
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join('read', music_dir, songs[0]))
                    elif "schedule my day" in query:
                        tasks = []  # Empty list
                        speak("Do you want to clear old tasks (Plz speak YES or NO)")
                        query = takeCommand().lower()
                        if "yes" in query:
                            file = open("tasks.txt", "w")
                            file.write(f"")
                            file.close()
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            i = 0
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt", "a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                        elif "no" in query:
                            i = 0
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt", "a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                                
                    elif ('close calculator' in query) or ('close notepad' in query) or ('close paint' in query)or ('close editor' in query) or 'close media player' in query:
                        CloseApp(query)
                        
                    # command if you don't want the AIVA to spack until for a certain time
                    # Note: I can be silent for max of 10mins
                    # Eg: AIVA keep quiet for 5 minutes
                    elif ('silence' in query) or ('silent' in query) or ('keep quiet' in query) or ('wait for' in query):
                        silenceTime(query)
                    elif "show my schedule" in query:
                        file = open("tasks.txt", "r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("notification.mp3")
                        mixer.music.play()
                        notification.notify(
                            title="My schedule :-",
                            message=content,
                            timeout=15
                        )
                    elif ("read pdf" in query) or ("pdf" in query):
                        pdf_reader()
                    # command for searching for a procedure how to do something
                    # Eg:AIVA activate mod
                    #   AIVA How to make a cake (or) AIVA how to convert int to string in programming
                    elif "activate mod" in query:
                        How()

                    elif ("volume mute" in query) or ("mute the sound" in query):
                        pyautogui.press("volumemute")
                        speak('volume muted')
                    elif ('shutdown the system' in query) or ('down the system' in query):
                        speak(" shutting down the system in 10 seconds")
                        time.sleep(10)
                        os.system("shutdown /s /t 5")
                        # command for restarting the system
                        # Eg: AIVA restart the system
                    elif 'restart the system' in query:
                        speak(" restarting the system in 10 seconds")
                        time.sleep(10)
                        os.system("shutdown /r /t 5")
                        # command for make the system sleep
                        # Eg: jarvis sleep the system
                    elif 'sleep the system' in query:
                        speak(" the system is going to sleep")
                        os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
                    elif ('your age' in query) or ('are you single' in query) or (
                            'are you there' in query) or ('tell me something' in query) or (
                            'thank you' in query) or ('in your free time' in query) or (
                            'i love you' in query) or ('can you hear me' in query) or (
                            'do you ever get tired' in query):
                        Fun(query)
                    elif (('hi' in query) and len(query) == 2) or (
                            (('hai' in query) or ('hey' in query)) and len(query) == 3) or (
                            ('hello' in query) and len(query) == 5):
                        Fun(query)
                    elif ('what can you do' in query) or ('your name' in query) or (
                            'my name' in query) or ('university name' in query):
                        Fun(query)
                    elif ('joke' in query) or ('date' in query):
                        Fun(query)
                    elif "focus mode"  in query:
                        a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                        if (a == 1):
                            speak("Entering the focus mode....")
                            os.startfile("D:\\CE\\Sem 6\\DE\\aiva\\FocusMode.py\\aiva\\FocusMode.py")
                            exit()


                        else:
                            pass

                    elif "show my focus" in query:
                        from FocusGraph import focus_graph

                        focus_graph()

                    elif "translate" in query:
                        from Translator import translategl
                        query = query.replace("aiva", "")
                        query = query.replace("translate", "")
                        translategl(query)


                    elif "open" in query:  # EASY METHOD
                        query = query.replace("open", "")
                        query = query.replace("aiva", "")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")

                    # elif "open" in query:
                    #     from Dictapp import openappweb
                    #     openappweb(query)
                    # elif "close" in query:
                    #     from Dictapp import closeappweb
                        # closeappweb(query)

                    elif "internet speed" in query:
                        # wifi = speedtest.Speedtest()
                        # upload_net = wifi.upload()  # Megabyte = 1024*1024 Bytes
                        # download_net = wifi.download() / 1048576
                        # print("Wifi Upload Speed is", upload_net)
                        # print("Wifi download speed is ", download_net)
                        # speak(f"Wifi download speed is {download_net}")
                        # speak(f"Wifi Upload speed is {upload_net}")
                        st = speedtest.Speedtest()
                        dl = st.download()
                        dl = dl / (1000000)  # converting bytes to megabytes
                        up = st.upload()
                        up = up / (1000000)
                        print(dl, up)
                        speak(f"we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")

                    elif "ipl score" in query:
                        from plyer import notification  # pip install plyer
                        import requests  # pip install requests
                        from bs4 import BeautifulSoup  # pip install bs4

                        url = "https://www.cricbuzz.com/"
                        page = requests.get(url)
                        soup = BeautifulSoup(page.text, "html.parser")
                        team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                        team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                        team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
                        team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

                        a = print(f"{team1} : {team1_score}")
                        b = print(f"{team2} : {team2_score}")

                        notification.notify(
                            title="IPL SCORE :- ",
                            message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                            timeout=15
                        )

                    elif "play game" in query:
                        from game import game_play

                        game_play()

                    elif "screenshot" in query:
                        import pyautogui  # pip install pyautogui

                        speak("Please  hold the screen for few seconds, I am taking screenshot")
                        time.sleep(3)
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")

                    elif "click my photo" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")

                    ############################################################
                    # elif "hello" in query:
                    #     speak("Hello sir, how are you ?")
                    # elif "i am fine" in query:
                    #     speak("that's great, sir")
                    # elif "how are you" in query:
                    #     speak("Perfect, sir")
                    # elif "thank you" in query:
                    #     speak("you are welcome, sir")

                    elif "tired" in query:
                        speak("Playing your favourite songs, sir")
                        a = (1, 2, 3)
                        b = random.choice(a)
                        if b == 1:
                            webbrowser.open("https://www.youtube.com/watch?v=S19UcWdOA-I")

                    elif "stop" in query:
                        pyautogui.press("k")
                        speak("video paused")
                    elif "top" in query:
                        pyautogui.press("k")
                        speak("video paused")
                    elif "play" in query:
                        pyautogui.press("k")
                        speak("video played")
                    elif "mute" in query:
                        pyautogui.press("m")
                        speak("video muted")



                    elif "volume up" in query:
                        from keyboard import volumeup

                        speak("Turning volume up,sir")
                        volumeup()
                    elif "volume down" in query:
                        from keyboard import volumedown

                        speak("Turning volume down, sir")
                        volumedown()


                    elif "google" in query:
                        from SearchNow import searchGoogle
                    elif "Google" in query:
                        from SearchNow import searchGoogle

                        searchGoogle(query)
                    elif "youtube" in query:
                        from SearchNow import searchYoutube

                        searchYoutube(query)
                    elif "Youtube" in query:
                        from SearchNow import searchYoutube

                        searchYoutube(query)
                    elif "YouTube" in query:
                        from SearchNow import searchYoutube

                        searchYoutube(query)
                    elif "wikipedia" in query:
                        from SearchNow import searchWikipedia
                        searchWikipedia(query)

                    # elif ('wikipedia' in query) or ('what is meant by' in query) or (
                    #         'tell me about' in query) or ('who the heck is' in query):
                    #     B_S(query)
                    # elif "Wikipedia" in query:
                    #     from SearchNow import searchWikipedia
                    #     searchWikipedia(query)


                    elif "news" in query:
                        from NewsRead import latestnews

                        latestnews()
                    elif "new" in query:
                        from NewsRead import latestnews

                        latestnews()
                    elif "calculator" in query:
                        from Calculatenumbers import WolfRamAlpha
                        from Calculatenumbers import Calc

                        query = query.replace("calculate", "")
                        query = query.replace("aiva", "")
                        Calc(query)
                    elif "calculate" in query:
                        from Calculatenumbers import WolfRamAlpha
                        from Calculatenumbers import Calc

                        query = query.replace("calculate", "")
                        query = query.replace("aiva", "")
                        Calc(query)

                    elif "whatsapp" in query:
                        from Whatsapp import sendMessage
                        sendMessage()
                    elif "Whatsapp" in query:
                        from Whatsapp import sendMessage
                        sendMessage()
                    elif "WhatsApp" in query:
                        from Whatsapp import sendMessage
                        sendMessage()
                    elif "temperature" in query:
                        search = "temperature in bhavnagar"
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)
                        data = BeautifulSoup(r.text, "html.parser")
                        temp = data.find("div", class_="BNeawe").text
                        speak(f"current{search} is {temp}")

                    elif "weather" in query:
                        search = "weather in bhavnagar"
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)
                        data = BeautifulSoup(r.text, "html.parser")
                        temp = data.find("div", class_="BNeawe").text
                        speak(f"current{search} is {temp}")

                    elif "set an alarm" in query:
                        print("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done,sir")
                    elif "set alarm" in query:
                        print("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done,sir")

                    elif "the time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M")
                        speak(f"Sir, the time is {strTime}")
                    elif "time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M")
                        speak(f"Sir, the time is {strTime}")
                    elif "finally sleep" in query:
                        speak("Going to sleep,sir")
                        exit()
                    elif "quit" in query:
                        speak("Going to sleep,sir")
                        exit()
                    elif "exit" in query:
                        speak("Going to sleep,sir")
                        exit()
                    elif ('system condition' in query) or ('condition of the system' in query):
                        speak("checking the system condition")
                        condition()
                    elif "remember that" in query:
                        rememberMessage = query.replace("remember that", "")
                        rememberMessage = query.replace("aiva", "")
                        speak("You told me to remember that" + rememberMessage)
                        remember = open("Remember.txt", "a")
                        remember.write(rememberMessage)
                        remember.close()
                    elif "what do you remember" in query:
                        remember = open("Remember.txt", "r")
                        speak("You told me to remember that" + remember.read())

                    elif "shutdown system" in query:
                        # speak("Are You sure you want to shutdown")
                        # shutdown = input("Do you wish to shutdown your computer? (yes/no)")

                        # if shutdown == "yes":
                        #     os.system("shutdown /s /t 1")
                        os.system("shutdown /s /t 1")
                        # elif shutdown == "no":
                        #     break

                    elif "shutdown" in query:
                        # speak("Are You sure you want to shutdown")
                        # shutdown = input("Do you wish to shutdown your computer? (yes/no)")

                        # if shutdown == "yes":
                        #     os.system("shutdown /s /t 1")
                        os.system("shutdown /s /t 1")
                        # elif shutdown == "no":
                        #     break

    except Exception as e:
        print(colored("Sorry if Something is wrong with me i am still in development phase", 'red'))
        speak("I am Going to sleep,sir")
        exit()
