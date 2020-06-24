# -*- coding: utf-8 -*-

import time, datetime
from time import sleep # для импульса в 0,5 сек у светодиода
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

gpio5_pin29 = 5 #Управление 1
gpio6_pin31 = 6 #Управление 2
gpio20_pin38 = 20 #Статус 1
gpio21_pin40 = 21 #Статус 2

now = datetime.datetime.now() # получение даты
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(gpio5_pin29, GPIO.OUT) #gpio5_pin29 выход
GPIO.output(gpio5_pin29, 0) #Off initially
GPIO.setup(gpio6_pin31, GPIO.OUT) #gpio6_pin31 выход
GPIO.output(gpio6_pin31, 0) #Off initially
GPIO.setup(gpio20_pin38, GPIO.IN, pull_up_down=GPIO.PUD_UP) #gpio20_pin38 вход
GPIO.setup(gpio21_pin40, GPIO.IN, pull_up_down=GPIO.PUD_UP) #gpio21_pin40 вход

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/short_imp_rig1':
        GPIO.output(gpio5_pin29, 1)
        #sleep(0.3)
        #GPIO.output(gpio5_pin29, 0)
        telegram_bot.sendMessage (chat_id, str("Подан короткий импульс на 1"))
    elif command == '/long_imp_rig1':
        #GPIO.output(gpio5_pin29, 1)
        #sleep(3)
        GPIO.output(gpio5_pin29, 0)
        telegram_bot.sendMessage (chat_id, str("Подан длинный импульс на 2"))
    elif command == '/short_imp_rig2':
        GPIO.output(gpio6_pin31, 1)
        sleep(0.3)
        GPIO.output(gpio6_pin31, 0)
        telegram_bot.sendMessage (chat_id, str("Подан короткий импульс на 2"))
    elif command == '/long_imp_rig2':
        GPIO.output(gpio6_pin31, 1)
        sleep(3)
        GPIO.output(gpio6_pin31, 0)
        telegram_bot.sendMessage (chat_id, str("Подан длинный импульс на 2"))
    elif command == '/status_rig1':
        value1 = GPIO.input(gpio20_pin38) #В переменную value будет записано состояние пина 20
        telegram_bot.sendMessage (chat_id, str("Статус 1: ")+str(value1))
    elif command == '/status_rig2':
        value2 = GPIO.input(gpio21_pin40) #В переменную value будет записано состояние пина 21
        telegram_bot.sendMessage (chat_id, str("Статус 2: ")+str(value2))

bot = telepot.Bot('1023899509:AAHSDEZaop4490O84oFiOuvMHdprM8uVs-g')
print (bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()

while 1:
    time.sleep(10)

