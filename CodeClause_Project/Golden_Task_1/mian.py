#From  Hemant
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[0].id) #Male voice
#print(voices[1].id) #Female voice
engine.setProperty('voice', voices[1].id) #Details of current voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening")

    speak("I am a Simple Assistance. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        return "None"   #Say that again will be printed in case of improper voice 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_EMAIL@XYZ', 'caob oejj ddjg zbev') #PROVIDE YOUR EMAIL
    server.sendmail('RECIVER_EMAIL@XYZ', to, content) #PROVIDE SENDER EMAIL
    server.close()

if __name__=="__main__" :
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            print("Opening youtube...")
            speak("Opening youtube")

        elif "open google" in query:
            webbrowser.open("google.com")
            print("Opening google...")
            speak("Opening google")
        
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
            print("Opening stack overflow...")
            speak("Opening stack overflow")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "open spotify" in query:
            spotifyPath = "YOUR_FILE_PATH_TO_OPEN_SPOTIFY.EXE" #PROVIDE FILE PATH TO OPEN SPOTIFY <USE DOUBLE BACKSLASH>
            os.startfile(spotifyPath)
            print("Opening Spotify...")
            speak("Opening Spotifi")

        elif "open code" in query:
            codePath = "YOUR_FILE_PATH_TO_OPEN_VS_CODE.EXE" #PROVIDE FILE PATH TO OPEN VS_CODE <USE DOUBLE BACKSLASH>
            os.startfile(codePath)
            print("Opening VS code..")
            speak("Opening vs code")
            
        elif "play music" in query:
            musicPath = "YOUR_FILE_PATH_TO_OPEN_SPOTIFY.EXE" #PROVIDE FILE PATH TO OPEN SPOTIFY <USE DOUBLE BACKSLASH>
            os.startfile(musicPath)
            print("Opening Spotify...")
            speak("Opening spotifi")

        elif "open vs code" in query:
            vscodePath = "YOUR_FILE_PATH_TO_OPEN_VS_CODE.EXE" #PROVIDE FILE PATH TO OPEN VS_CODE <USE DOUBLE BACKSLASH>
            os.startfile(vscodePath)
            print("Opening VS code..")
            speak("Opening vs code")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "YOUR_EMAIL@XYZ"    #PROVIDE YOUR EMAIL <ABC@gmail.com>
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")
            
