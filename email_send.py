import email.encoders
import smtplib
import ssl
from email.message import EmailMessage
import mimetypes
from tkinter import *
from tkinter import filedialog
import form as form
import pyttsx3
import speech_recognition
from bs4 import BeautifulSoup
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    try:
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
        print("No connection")
        speak("Sorry, for the timing i not able to work offline")


# Define email sender and receiver
email_sender = 'aivademoemail@gmail.com'
email_password = 'pjytfyzigbaqlehg'

speak("From contacts ??")
print("If no then you need to provide email address")
gettext = takeCommand().lower()
if gettext == "yes":
    while True:
        try:
            name = takeCommand().lower()
            email_list = {
                'taste': 'ambaliyadhruv123@gmail.com',
                'test': 'ambaliyadhruv123@gmail.com',
                'aiva': 'aivademoemail@gmail.com'
            }
            email_receiver = email_list[name]
            break
        except Exception as e:
            speak("Sorry i have not understand that perfectly")
            continue
else:
    # if you have to provide custom mail id
    speak("Then please give me an email id")
    get_email = takeCommand().lower()
    query = get_email.replace(" ", "")

    speak("to which service provider")
    while True:
        service = takeCommand().lower()
        if service == "gmail":
            query_gmail = "@gmail.com"
            email_receiver = query + query_gmail
            print(email_receiver)
            break
        elif service == "yahoo":
            query_yahoo = "@yahoo.com"
            email_receiver = query + query_yahoo
            print(email_receiver)
            break
        elif service == "outlook":
            query_out = "@outlook.com"
            email_receiver = query + query_out
            print(email_receiver)
            break
        else:
            speak("Sorry it's not from service provider try again")
            continue

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Set the subject and body of the email
    speak("Give me a subject")
    subject = takeCommand()

    speak("What should I say?")
    body = takeCommand()
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    speak("Want to add attachment or not")
    attach = takeCommand()
    if attach == "yes":
        while True:
            try:
                open_file = filedialog.askopenfilename(initialdir="C:\\")
                file_name = os.path.basename(open_file)
                mime_type, _ = mimetypes.guess_type(open_file)
                mime_type, mime_subtype = mime_type.split('/')
                with open(open_file, 'rb') as file:
                    em.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype, filename=file_name)
                print(em)
                break
            except Exception as e:
                speak("Have you not selected File yet !!")
                speak("or something wrong Please select once again ")
                continue

    try:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        speak("Email has been sent!")
    except Exception as e:
        speak("Sorry my friend. I am not able to send this email")
