import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes
import time 

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-US')
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

def jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        kit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('current time is ' + time)
        print(time)
    elif "today's date" in command:
        today = datetime.datetime.now().strftime('%d %m %Y')
        talk('The date today is ' + today)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'who are you' or 'who created you' or 'who made you' in command:
        talk('Hello, I am a virtual assistant, created by Wale')
    elif 'insult' or 'roast' in command:
        talk('you are a worm')
    else:
        talk('Please say the command again.')

if __name__ == "__main__":
  while True and take_command() != "goodbye":
    jarvis()
    time.sleep(10)
