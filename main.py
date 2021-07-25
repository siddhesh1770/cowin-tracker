"""
Developed By Siddhesh Patil
Managed By
Ranjeetsinha Patil and Anupam Patil
Follow me on Instagram for more programs like this https://www.instagram.com/siddhesh1770/
 """
import time

import pyautogui
import pyttsx3
import requests

# Voice Data
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

bookBtn = [694, 241]
found = []


def speak(audio):  # Text to Speech Speak
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def bookprocess():
    time.sleep(0.5)  # Add music
    pyautogui.click(694, 241)
    print("Hello World")
    found.append(45)


def searchByPin():
    baseurlFindByPin = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=410206&date=26-07-2021"
    h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    r = requests.get(baseurlFindByPin, headers=h)
    res = r.json()
    for i in res['sessions']:
        if int(i['available_capacity_dose2']) > 0:
            if i['vaccine'] == 'COVISHIELD' and int(i['min_age_limit']) == 18 and i['fee_type'] == 'Free':
                bookprocess()
                print(i['vaccine'], " ", i['min_age_limit'], " ", i['fee_type'], " ", i['name'])
                print("Available Cap = ", i['available_capacity_dose2'])
        print(i['name'])


count = 1
while (1):
    print("Count Number = ", count)
    searchByPin()
    print("\n")
    time.sleep(3)
    if len(found) > 0:
        break
    count += 1
