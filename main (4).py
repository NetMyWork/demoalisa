import datetime
import os
import time

import speech_recognition as sr
import pyttsx3
import subprocess
import wolframalpha
import tkinter
import json
import random
import operator
import pyjokes
import webbrowser
import winshell
import feedparser
import smtplib
import ctypes
import requests
import shutil
from utils import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from twilio.rest import Client
from clint.textui import progress, columns
from ecapture import ecapture as ec
from bs4 import BeautifulSoup as bs
import win32com.client as wincl
from urllib.request import urlopen
import pywhatkit
import wikipedia
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import pyaudio

engine = pyttsx3.init()
listener = sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voices', 1)
lisom = 'listening'
ser = {'hi': 'hello my friend', 'how are you doing': 'i am fine thanks',
       'what is your name': 'my name is net it was given me by my creater mr Bakhtiyorbek',
       'okay what can you do': 'i can play a song if you are bored',
       "what if i don't pay taxes": 'i dont know actually but i can assume that if you dont pay the government makes you to pay it',
       'why you were created': 'my creator created me while learning python and he wants me to be artificial intelect',
       'hello': 'hi my friend',
       'what do you want': 'if you can please help my creator to develop me i actually want to be very helpful'}


class lisaApp(App):
    def get_latest_news(self, instance):
        Polygon = requests.get('https://www.bbc.com/')
        html_Polygon = bs(Polygon.content, 'html.parser')
        for i in html_Polygon.select('#page.content'):
            global price_Polygon
            price = str(i.select('.module__content')[0].text)
            print(price)
            self.speak(price)

    def file(self, instance):
        engine.say('which file')
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.lbl.text = 'listening...'
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                self.lbl.text = 'Recognizing...'
                command = listener.recognize_google(audio, language='en_EN').lower()
                self.lbl.text = command
            except Exception as e:

                self.lbl.text = 'sorry i couldnt catch'
                return 'None'
        global file
        file = open(command + '.txt')
        print(command)
        self.lbl.text = file.read()

    def build(self):
        global bl
        bl = BoxLayout(orientation='vertical', padding=1)
        global button
        button = Button(text='start', on_press=self.wait, size_hint=(.1, .1))

        self.lbl = Label(text='how can i help you', font_size=15, halign='left', size_hint=(1, .4), valign='center',
                         text_size=(400, 500 * .4))
        bl.add_widget(self.lbl)
        bl.add_widget(button)

        engine.say('you are welcome')
        engine.runAndWait()

        return bl

    def whts(self, instance):
        try:
            engine.say("What should I say?")
            engine.runAndWait()
            r = sr.Recognizer()
            with sr.Microphone() as source:
                self.lbl.text = 'listening...'
                r.pause_threshold = 1
                audio = r.listen(source)
                try:
                    self.lbl.text = 'Recognizing...'
                    command = listener.recognize_google(audio, language='en_EN').lower()
                    self.lbl.text = command
                except Exception as e:

                    self.lbl.text = ' sorry i couldnt catch'
                    return self.whts(instance=True)
            content = command
            engine.say("what is the number")
            engine.runAndWait()
            with sr.Microphone() as source:
                self.lbl.text = 'listening...'
                r.pause_threshold = 1
                audio = r.listen(source, phrase_time_limit=15)
                try:
                    self.lbl.text = 'Recognizing...'
                    command = listener.recognize_google(audio, language='en_EN').lower()
                    self.lbl.text = command
                except Exception as e:

                    self.lbl.text = ' sorry i couldnt catch'
                    return
            to = ('+' + command)
            print(to)
            self.whatsapp(message=content, number=to)
        except:
            return

    def ask(self, instance):
        engine.say("What should I say?")
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.lbl.text = 'listening...'
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                self.lbl.text = 'Recognizing...'
                command = listener.recognize_google(audio, language='en_EN').lower()
                self.lbl.text = command
            except Exception as e:

                self.lbl.text = ' sorry i couldnt catch'
                return
        content = command
        engine.say("whome should i send")
        engine.runAndWait()
        with sr.Microphone() as source:
            self.lbl.text = 'listening...'
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                self.lbl.text = 'Recognizing...'
                command = listener.recognize_google(audio, language='en_EN').lower()
                self.lbl.text = command
            except Exception as e:

                self.lbl.text = ' sorry i couldnt catch'
                return
        to = command
        self.sendEmail(to, content)

    def wait(self, instance):
        self.lbl.text = 'listenin..'
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                self.lbl.text = 'Recognizing...'
                command = listener.recognize_google(audio, language='en_EN').lower()
            except Exception as e:

                self.lbl.text = ' sorry i couldnt catch'
                return self.wait(instance=True)
            self.wakeapp(instance=True, comman=command)

    def wakeapp(self, instance, comman):
        print(comman)
        if 'hey' in comman or 'hello' in comman:
            self.lbl.text = 'here i am listening...'
            engine.say('here i am listening...')
            engine.runAndWait()
            self.hear(instance=True)
        else:
            return self.wait(instance=True)

    def whatsapp(self, number, message):
        pywhatkit.sendwhatmsg_instantly(phone_no=number, message=message, wait_time=5, close_time=8)
        time.sleep(5)
        self.speak('message has been sent')

    def sendEmail(self, to, content):
        to = to.replace(' ', '')
        pywhatkit.send_mail(email_sender='baxtiyorbekxbiag@gmail.com', password='tbrgnteobkprbiar', subject='hi',
                            message=content, email_receiver=to + '@gmail.com')
        self.speak('email has been sent!')

    def wish(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak("Good Morning Sir !")

        elif hour >= 12 and hour < 18:
            self.speak("Good Afternoon Sir !")

        else:
            self.speak("Good Evening Sir !")
        global assname
        assname = ("Networker")
        self.speak("I am your Assistant")
        self.speak(assname)

    def speak(self, audio):
        engine.say(audio)
        engine.runAndWait()
        self.wait(instance=True)

    def username(self):
        self.speak("What should i call you sir")
        global uname
        uname = self.hear(instance=True)
        self.speak("Welcome Mister")
        self.speak(uname)
        columns = shutil.get_terminal_size().columns

        self.lbl.text = "#####################".center(columns) + "Welcome Mr.", uname.center(
            columns) + "#####################".center(columns)

        self.speak("How can i Help you, Sir")

    def note(self, instance):
        engine.say("What should i write, sir")
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.lbl.text = 'listening...'
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                self.lbl.text = 'Recognizing...'
                command = listener.recognize_google(audio, language='en_EN').lower()
                self.lbl.text = command
            except Exception as e:

                self.lbl.text = ' sorry i couldnt catch'
                return
        note = command

        file = open('networker.txt', 'w')
        engine.say("Sir, Should i include date and time")
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.lbl.text = 'listening...'
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                self.lbl.text = 'Recognizing...'
                command = listener.recognize_google(audio, language='en_EN').lower()
                self.lbl.text = command
            except Exception as e:

                self.lbl.text = ' sorry i couldnt catch'
                return
        snfm = command
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)
        self.speak('i have written')

    def conversation(self, instance):
        engine.say('ok')
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.lbl.text = 'listening...'
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                self.lbl.text = 'Recognizing...'
                comm = listener.recognize_google(audio, language='en_EN').lower()
                self.lbl.text = comm
                self.con(comm=comm)
            except Exception as e:

                self.lbl.text = ' sorry i couldnt catch'
                return 'None'

    def con(self, comm):
        if comm in ser:
            self.lbl.text = ser[comm]
            engine.say(ser[comm])
            engine.runAndWait()
        elif 'command' in comm:
            engine.say('ok i am ready to take a command')
            engine.runAndWait()
            self.hear(instance=True)
        else:
            self.lbl.text = 'sorry i dont know this word'
            engine.say('sorry i dont know this word')
        return self.conversation(instance=True)

    def weather(self, instance):
        print('sghjqakK')
        weather = requests.get('https://www.timeanddate.com/weather/uzbekistan/tashkent/ext')
        html_weather = bs(weather.content, 'html.parser')
        for i in html_weather.select('.main-content-div'):
            price = str(i.select('.alert__content')[0].text)
            self.speak('the weather' + price)

    def hear(self, instance):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.lbl.text = 'listening...'
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                self.lbl.text = 'Recognizing...'
                command = listener.recognize_google(audio, language='en_EN').lower()
                self.lbl.text = command
            except Exception as e:

                self.lbl.text = ' sorry i couldnt catch'
                return 'None'
            self.answer(command)
            return command

    def answer(self, command):
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M:%p')
            self.lbl.text = time
            self.speak('the current is ' + time)
        elif 'tell me about' in command:
            command = command.replace('tell me about', '')
            info = wikipedia.summary(command, 1)
            self.lbl.text = info
            self.speak(info)
        elif 'file' in command:
            self.file(instance=True)
        elif 'open' in command:
            command = command.removeprefix('open ')
            webbrowser.open('https://' + command)
            self.lbl.text = "Here you go " + command
            self.speak("Here you go " + command)
        elif 'send an email' in command:
            self.ask(instance=True)
        elif 'send a message' in command:
            self.whts(instance=True)
        elif "change my name to" in command:
            command = command.replace("change my name to", "")
            global assname
            assname = command
            print("My friends call me", assname)
        elif 'exit' in command:
            engine.say("Thanks for giving me your time")
            engine.runAndWait()
            exit()
        elif 'joke' in command:
            self.speak(pyjokes.get_joke())
        elif "calculate" in command:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = command.lower().split().index('calculate')
            command = command.split()[indx + 1:]
            res = client.query(' '.join(command))
            answer = next(res.results).text
            print("The answer is " + answer)
            self.speak("The answer is " + answer)
        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open(command)
            self.lbl.text = command
            self.speak('here what i found for ' + command)
        elif 'news' in command:
            self.get_latest_news(instance=True)
        elif 'lock window' in command:
            self.lbl.text = "locking the device"
            ctypes.windll.user32.LockWorkStation()
            self.speak("locking the device")
        elif 'empty recycle bin' in command:
            self.lbl.text = "Recycle Bin Recycled"
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            self.speak("Recycle Bin Recycled")
        elif "where is" in command:
            command = command.replace("where is ", "")
            location = command
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            self.lbl.text = location
            self.speak("User asked to Locate" + location)
        elif "camera" in command or "take a photo" in command:
            self.lbl.text = 'Here ive taken a photo'
            ec.capture(0, "networker Camera ", "img.jpg")
            self.speak('Here ive taken a photo')
        elif "restart" in command:
            self.lbl.text = 'here I ll restart your device'
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in command or "sleep" in command:
            self.lbl.text = "Hibernating"
            subprocess.call("shutdown / h")
            self.speak("Hibernating")
        elif "log off" in command or "sign out" in command:
            self.lbl.text = "Make sure all the application are closed before sign-out"
            subprocess.call(["shutdown", "/l"])
            self.speak("Make sure all the application are closed before sign-out")
        elif "write a note" in command:
            self.note(instance=True)
        elif "show note" in command:
            file = open("networker.txt", "r")
            self.speak('showing notes' + file.read())
        elif "weather" in command:
            self.weather(instance=True)
        elif 'who' in command:
            theme = command.replace('who ', '')
            info = wikipedia.summary(theme, 1)
            self.lbl.text = info
            self.speak(info)
        elif 'play' in command:
            song = command
            pywhatkit.playonyt(song)
            self.lbl.text = 'playing'
            self.speak('playing')
        elif 'off' in command:
            self.lbl.text = 'Your computer is going to shut down'
            self.speak('your device is going to shut down')
        elif 'okay bye' == command:
            self.speak('good bye sir')
            os.system('shutdown -s')
        elif 'speak' in command:
            self.conversation(instance=True)
        else:
            self.lbl.text = 'i dont know that command'
            self.speak('i dont know that command')
        return self.wait(instance=True)


if __name__ == '__main__':
    while True:
        lisaApp().run()
