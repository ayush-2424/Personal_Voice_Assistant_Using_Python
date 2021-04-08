import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import numpy as numpy


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)

   
     if hour>=0 and hour<=12:
        speak("Good Morning!")

     elif hour>=12 and hour<=18:
        speak("Good Afternoon")

     else:
        speak("Good Evening!")

     speak("My name is Steven sir. I am your personal assistant")
     speak("Please tell me how can I help you")

def takeCommand():
     # it takes command from user.
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening.....")
         r.pause_threshold = 1
         r.energy_threshold =300
         audio = r.listen(source)

     try:
         print("Recognizing.....")
         query = r.recognize_google(audio,language='en-in')
         print(f"user said: {query}\n")
     except:

         #print(e)

         print("say that again please...")
         return "None"
     return query

def sendEmail(do,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sanidhyasaxena73@gmail.com','9045695056')
    server.sendmail('sanidhyasaxena73@gmail.com',to,content)
    server.close()

def myself():
    speak(" I am a personel voice assistant which is built and develop by aayush saxena")
    speak("he is currently pursuing B.tech from KIET group of institution,Ghaziabad")








if __name__ == "__main__":
    print("----------assistant start-------------")
    wishMe()
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('searching wikipedia.....')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
        
    elif 'open youtube' in query:
        speak("Youtube is open for you sir")
        webbrowser.open("https://www.youtube.com/")
        
        # speak("what do you wants to search in youtube.Please tell me")
        # commmand= takeCommand().lower()
        # webbrowser.open("https://www.youtube.com/results?search_query="+str(commmand))
    elif 'open google' in query:
        webbrowser.open("https://www.google.com/")

    elif 'open facebook' in query:
        webbrowser.open("https://www.facebook.com/")
    
    elif 'open google maps' in query:
        webbrowser.open("https://www.google.com/maps/place/India/@20.0114083,64.4398422,4z/data=!3m1!4b1!4m5!3m4!1s0x30635ff06b92b791:0xd78c4fa1854213a6!8m2!3d20.593684!4d78.9628")
    elif 'open hacker rank' in query:
        webbrowser.open("https://www.hackerrank.com/")


    elif 'play music' in query:
        speak("sorry sir No music is found in your system")
        #music_dir=

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir,the time is {strTime}")

    elif 'open google chrome' in query:
        chrome="C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"
        os.startfile(chrome)
    
    elif 'email to ayush' in query:
        try:
            speak("sir tell me. which you wanted to written in email")
            content = takeCommand()
            print(content)
            to ="sanidhyasaxena73@gmail.com"
            sendEmail(to,content)
            speak("email has been sent.....!!")
        except Exception as e:
            print(e)
            speak("sorry sir.I am unable to send this email")
            print("sorry sir.I am unable to send this email")

    elif 'about developer' in query:
        myself()
