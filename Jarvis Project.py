import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init() 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def voicechange():
    voice = engine.getProperty('voices')
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    newVoiceRate = 170
    engine.setProperty('rate',newVoiceRate)

def date():
    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Day = datetime.datetime.now().day
    speak("The present day is {} and the month is {} and the year is {}".format(Day,Month,Year))  

def greet():
    speak("Aapki kya hukum hain mere aaka?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        speak(query)
    except Exception as e:
        print(e)
        speak("Unable to recognize sir")
        return "None"
    
    return query

def sendemail(to = "arnavjha07@gmail.com", content = "Python se mail"):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("athakur42u@gmail.com","CSE2019/109")
    server.sendmail("athakur42u@gmail.com",to,content)
    server.close()
 

voicechange()
greet()
engine.runAndWait()

if __name__=="__main__":

    while True:
        query = takecommand().lower()
        
        if "time" in query:
            time()
        elif "date" in query:
            date()
        
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "email" in query:
            speak("What should be the content of the email?")    
            result = takecommand().lower()
            sendemail(content = result)
            speak("Email sent successfully")
            
        elif "google" in query:
            speak("What should I search sir?")
            chromepath = "C://Program Files//Google//Chrome//Application//chrome.exe %s"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
            
        elif "song" in query:
            songs_dir = "C://Users//arnav//Music//PYTHON_MUSIC"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        
        elif "remember" in query:
            speak("What should I remember?")
            data = takecommand()
            remember = open("data.txt","w")  
            remember.write(data) 
            remember.close()
            speak("You said me to remember ")
            speak(data)
            
        elif "recall" in query:
              remember = open("data.txt","r")  
              speak("You told me to remember " + remember.read())
              
              
        elif "exit" in query:
            break    
        else:
            speak("Could you repeat that again?")          
