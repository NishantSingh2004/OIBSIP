import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Welcome, I am your personal assistant.")

def VoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query.lower()
if __name__ == '__main__':
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        greet()

        while True:
            work = VoiceCommand()
            if 'hello' in work:
                speak('Hi, how can I help you?')

            elif "wikipedia" in work:
                speak("Searching Wikipedia...")
                work = work.replace("wikipedia", "")
                results = wikipedia.summary(work, sentences=5)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open notepad' in work:
                speak('Opening Notepad...')
                path = "c:\\windows\\system32\\notepad.exe"
                os.startfile(path)

            elif 'close notepad' in work:
                speak('Closing Notepad...')
                os.system('taskkill /F /IM notepad.exe')

            elif 'open youtube' in work:
                speak("Opening YouTube...")
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in work:
                speak("Opening Google...")
                webbrowser.open("https://www.google.co.in")

            elif 'play music' in work:
                speak('Opening music player...')
                path = "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"
                os.startfile(path)

            elif 'open mail' in work:
                speak("Opening Gmail...")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif 'open whatsapp' in work:
                speak("Opening WhatsApp...")
                webbrowser.open("https://web.whatsapp.com/")

            elif 'exit' in work:
                speak("Thanks for your time. Have a nice day!")
                break

    except BaseException as ex:
        print(f"Error occurred: {ex}")

    finally:
        print("Thank you! Bye, have a nice day.")
