# /usr/bin/env python
# -*- coding: utf-8 -*-

#Подключаем необходимые библиотеки
import time
import RPi.GPIO as GPIO

#Установим номера пинов GPIO , с которыми будем работать
LED =23
KEY =17

#Дедаем сброс состояний портов(все порты конфигурируются на вход - INPUT)
GPIO.cleanup()
#Режим нумерации пинов по названию(не по порядковому номеру на разьеме)
GPIO.setmode(GPIO.BCM)
#сконфигурируем пин Led на выход(output)
GPIO.setup(LED,GPIO.OUT)
#Устанвоим низкий уровень (0- LOW) на пине  LED
GPIO.output(LED,GPIO.LOW)
#Сконфигурируем пин Key на вход (Input)
GPIO.setup(KEY,GPIO.IN)
#выведем на экран текст-приветсвие
print 'Hello Blink...blink'

#Проверка на прерывание программы с клавиатуры (Ctrl+C)
try:
    #Вечный цикл
    while True:
        #если кнопка нажата(на пине Key низкий уровень)
        if GPIO.input(KEY)==False:
            # Уставнавливаем задержку 0,1 сек и выводим сообщение timeout -0.1
            timeout=0.05
            print 'KEY pressed'
        else:
            #в противном случае задержка  0.5 сек
            timeout=0.5
        #Засветим светодиод,подключеный к пину  LED
        GPIO.output(LED,GPIO.HIGH)
        #подождем выполним заданную задержку
        time.sleep(timeout)
        #Погасим светодиод подключеный к пину LED
        GPIO.output(LED,GPIO.LOW)
        time.sleep(timeout)
# если комбинация клавиш CTRL+C была надата -сброс пинов и завершение
except KeyboardInterrupt:
    GPIO.cleanup()
