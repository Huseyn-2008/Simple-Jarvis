import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
from time import sleep
import pyautogui



start = pyttsx3.init()

finish = ["всегда к  вашим услугам сэр", "сделано сэр", "готово", "все  сделано", "пожалуйста сэр"]


opts = {
    "alias": ('джарвис','не спишь','ты тут','здравствуй','ты нужен мне'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "note": ('блокнот','открой блокнот'),
    "calc": ('калькулятор', 'открой калькулятор'),
    "sublime": ('открой редактор кода','открой редактор'),
    "pixel": ('пиксельный редактор', 'открой пиксельный редактор', 'открой камни пиксельный редактор'),
    "ctime": ('текущее время','сейчас времени','который час','который год'),
    "radio": ('включи музыку','воспроизведи радио','включи радио'),
    "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты'),
    "chrome": ('браузер', 'открой браузер'),
    "bye": ('пока джарвис','спокойной ночи'),
    "google": ('открой google'),
    "camcam": ('камера', 'включи камеру', 'открой доступ к камере'),
    "thank": ('спасибо')

}



def listen():
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration= 0.5)
        audio = r.listen(source)
        try:
            task = r.recognize_google(audio, language="ru-RU").lower()
            print("[log]: " + task)
        except:
            task = listen()
        return task




def hi(task):
    if task.startswith(opts["alias"]):
        start.say("всегда к вашим услугам сэр")
        start.runAndWait()

    if task.startswith(opts["ctime"]):
        now = datetime.datetime.now()
        start.say("Сейчас " + str(now.hour) + "часов" + str(now.minute) + "минут")
        start.runAndWait()
    if task.startswith(opts["note"]):
        os.system(' start notepad')
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
        start.say("пока сэр")
        start.runAndWait()
        sleep(0.1)
        exit()
    if task.startswith(opts["google"]):
        webbrowser.open(task)
        start.say(random.choice(finish))
        start.runAndWait()
    if task.startswith(opts["camcam"]):
        os.startfile("C:\Program Files\dist\calc2077.exe")
        start.say(random.choice(finish))
        start.runAndWait()
    if task.startswith(opts["thank"]):
        start.say("всё что угодно")
        start.runAndWait()



def request(task):
    hi(task)

while True:
    request(listen())
