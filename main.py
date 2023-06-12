import telebot
import os
import time
import keyboard
import pyautogui
import psutil
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
y = open('C:\\Users\\' + config.get('main', 'Name') +'\\Downloads\\screen2.png', 'rb')
def checkProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
direct = 'C:\\Users\\' + config.get('main', 'Name') + '\\AppData\\Local\\Programs\\"Arizona Games Launcher"\\"Arizona Games Launcher.exe"'
bot = telebot.TeleBot(config.get('main', 'Token'))
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Work")
@bot.message_handler(regexp="старт")
def echo_all(message):
        os.system(direct)
        for i in range(2):
                pyautogui.click(1425, 829)
        time.sleep(5)
        if checkProcessRunning('gta_sa'):
                bot.reply_to(message, "done")
        else:
                bot.reply_to(message, "error")
@bot.message_handler(regexp="закрыть")
def echo_all(message):
        os.system("taskkill /f /im gta_sa.exe")
        bot.reply_to(message, "done")
@bot.message_handler(regexp="статус")
def echo_all(message):
        if checkProcessRunning('gta_sa'):
           bot.reply_to(message, 'Yes gta process was running')
        else:
           bot.reply_to(message, 'No gta process was running')
@bot.message_handler(regexp="скрин")
def echo_all(message):
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        f = open('screenshot.png', 'rb')
        bot.send_photo(config.get('main', 'ChatId'), f)
bot.infinity_polling()
