import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
        else :
            speak("Good Evening!")
        speak("Hello,boss! friday here. Please tell me how may i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in') 
        print(f"user said: {query}\n")
        #speak("i'm fine sir, what is the task for me today?")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
        
    return query

#Put your own details    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia" , "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/watch?v=4cSPrIC1lTo")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.org")


        elif 'play music' in query:
            music_dir='R:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[5]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open visual studio' in query:
            visualstudioPath ="R:\\Microsoft VS Code\\Code.exe"
            os.startfile(visualstudioPath)

        elif 'close visual studio' in query:
            exit(1)

        elif 'open eclipse' in query:
            eclipsePath="C:\\Users\\Roshan\\eclipse\\java-2020-06\\eclipse\\eclipse.exe"
            os.startfile(eclipsePath)

         elif 'email to roshan' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="roshan.jha4321@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry boss, email is not sent!")