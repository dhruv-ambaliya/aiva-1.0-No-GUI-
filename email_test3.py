import smtplib
import ssl
from email.message import EmailMessage

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


# Define email sender and receiver
email_sender = 'aivademoemail@gmail.com'
email_password = 'pjytfyzigbaqlehg'

speak("From contacts ??")
print("If no then you need to provide email address")
gettext = takeCommand().lower()
if gettext == "yes":
    while True:
        try:
            email_list = {
            'test': 'ambaliyadhruv123@gmail.com',
            'aiva': 'aivademoemail@gmail.com'
            }
            name = takeCommand().lower()
            email_receiver = email_list[name]
            break
        except Exception as e:
            speak("This is not from our Contacts list try again")
            continue
else:
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
    speak("Want to add attachment or not")
    attach = takeCommand()
    if attach == "yes":
       import attachment

    speak("What should I say?")
    body = takeCommand()

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    try:
        # content = takeCommand()
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        # to = "aivademoemail@gmail.com"
        # sendEmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry my friend. I am not able to send this email")
