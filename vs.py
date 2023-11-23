import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
from time import sleep
import winshell
import wikipedia
import subprocess


start = pyttsx3.init()

voices = start.getProperty('voices')
start.setProperty('voice', voices[2].id)

finish = ["at your service, sir", "done, sir", "completed", "all done", "here you go, sir"]

opts = {
    "alias": ('jarvis', 'are you there', 'hey', 'hello', 'you needed'),
    "tbr": ('say', 'tell me', 'show me', 'how many', 'pronounce'),
    "note": ('notepad', 'open notepad'),
    "calc": ('calculator', 'open calculator'),
    "sublime": ('open code editor', 'open code'),
    "pixel": ('pixel editor', 'open pixel editor', 'open stones pixel editor'),
    "ctime": ('current time', 'now', 'what time is it', 'what year is it'),
    "radio": ('play music', 'play radio', 'turn on radio'),
    "stupid1": ('tell a joke', 'make me laugh', 'you know any jokes'),
    "chrome": ('browser', 'open browser'),
    "bye": ('goodbye jarvis', 'good night'),
    "google": ('open google'),
    "camcam": ('camera', 'turn on camera', 'grant access to camera'),
    "thank": ('thank you'),
    "bin": ('empty recycle bin'),
    "tell": ('tell me something', 'share an interesting fact', 'give me information'),
    "how_are_you": ('how are you', 'how are you doing', 'what\'s up')
}

def custom_log(text):
    print("[log]: " + text)
    start.say(text)
    start.runAndWait()

def respond_to_need_help():
    responses = ["Of course! I'm here to help.", 
                 "Absolutely! What do you need assistance with?", 
                 "I'm ready to assist you. What can I help you with today?"]
    custom_log(random.choice(responses))

def regular_speak_greeting():
    greetings = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
    custom_log(random.choice(greetings))

def regular_speak_response():
    responses = ["Sure, what can I do for you?", "Of course!", "I'm here to help.", "How can I assist you today?"]
    custom_log(random.choice(responses))

def regular_speak_farewell():
    farewells = ["Goodbye!", "See you later!", "Take care!", "Until next time!"]
    custom_log(random.choice(farewells))

def respond_to_how_are_you():
    responses = ["I'm doing well, thank you!", "I'm functioning at optimal capacity!", "All systems are go!", "I'm great, sir!"]
    custom_log(random.choice(responses))

CHROME_PATH = r"C:\\Program Files\\Google\\Chrome\Application\\chrome.exe"

def announce_opening(url):
    url_without_https = url.replace("https://", "").replace("http://", "")
    start.say(f"Opening {url_without_https} in Google Chrome")
    start.runAndWait()

def open_website(url):
    try:
        announce_opening(url)
        subprocess.run([CHROME_PATH, url], check=True)
    except Exception as e:
        custom_log(f"Failed to open {url} in Google Chrome. Error: {e}")

def respond_to_new_project():
    responses = ["That's great! What kind of project are you thinking of starting?", 
                 "Starting a new project is always exciting! What's the focus of your project?", 
                 "Excellent! Tell me more about the project you want to start."]
    custom_log(random.choice(responses))

def listen():
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
            task = r.recognize_google(audio, language="en-US").lower()
            print("[log]: " + task)
        except:
            task = listen()
        return task

def tell_me_something():
    try:
        random_page = wikipedia.random()
        page_summary = wikipedia.summary(random_page, sentences=2)
        start.say("Did you know? " + page_summary)
        start.runAndWait()
    except wikipedia.exceptions.DisambiguationError as e:
        start.say("I found multiple options. Here are some suggestions: " + ', '.join(e.options))
        start.runAndWait()
    except wikipedia.exceptions.PageError:
        start.say("I couldn't find any information right now.")
        start.runAndWait()

def hi(task):
    if any(greeting in task for greeting in opts["alias"]):
        regular_speak_greeting()

    elif any(question in task for question in opts["alias"]):
        regular_speak_response()

    elif any(how_are_you in task for how_are_you in opts["how_are_you"]):
        respond_to_how_are_you()

    elif any(new_project in task for new_project in ["start a new project", "new project", "begin a project"]):
        respond_to_new_project()

    elif any(help_command in task for help_command in ["help me", "need help", "assist me"]):
        respond_to_need_help()

    elif any(website_command in task for website_command in ["open"]):
        url_to_open = task.replace("open", "").strip()
        open_website(url_to_open)

    elif task.startswith(opts["ctime"]):
        now = datetime.datetime.now()
        custom_log("It's " + str(now.hour) + " o'clock and " + str(now.minute) + " minutes")

    elif task.startswith(opts["note"]):
        os.system('start notepad')
        custom_log(random.choice(finish))
    if task.startswith(opts["bin"]):
        bin()
        start.say(random.choice(finish))
        start.runAndWait()
    if task.startswith(opts["sublime"]):
        os.startfile("C:\Program Files\Sublime Text 3\sublime_text.exe")
        start.say(random.choice(finish))
        start.runAndWait()
    if task.startswith(opts["calc"]):
        os.system('start calc')
        start.say(random.choice(finish))
        start.runAndWait()
    if task.startswith(opts["pixel"]):
        os.startfile("C:\Program Files\Aseprite\Aseprite.exe")
        start.say(random.choice(finish))
        start.runAndWait()
    if task.startswith(opts["chrome"]):
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        start.say(random.choice(finish))
        start.runAndWait()
    if task.startswith(opts["bye"]):
        start.say("Goodbye, sir")
        start.runAndWait()
        sleep(0.1)
        exit()
    if task.startswith(opts["tell"]):
        tell_me_something()
    if task.startswith(opts["google"]):
        webbrowser.open(task)
        start.say(random.choice(finish))
        start.runAndWait()
    if task.startswith(opts["camcam"]):
        os.startfile("C:\Program Files\dist\calc2077.exe")
        start.say(random.choice(finish))
        start.runAndWait()
    if task.startswith(opts["thank"]):
        start.say("You're welcome")
        start.runAndWait()

def bin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        start.say("Recycle bin cleared")
        start.runAndWait()
    except:
        start.say("The recycle bin was already empty")
        start.runAndWait()

def request(task):
    hi(task)

while True:
    request(listen())



