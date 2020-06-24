import datetime 
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
from time import sleep

red_led_pin = 23
green_led_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led_pin,GPIO.OUT)
GPIO.setup(green_led_pin,GPIO.OUT)

now = datetime.datetime.now()
limit=0.05
limit2=0.05
led=red_led_pin
count=10

def blink_f(count):
    i=0
    while i<count:
        GPIO.output(led,GPIO.HIGH)
        sleep(limit)
        GPIO.output(led,GPIO.LOW)
        sleep(limit2)
        i=i+1
        print('print i')
        print(i)
    i=count
def handle(msg):
    chat_id=msg['chat']['id']
    command=msg['text']

    print('Recived:')
    print(command)


    if command=='hi':
        bot.sendMessage(chat_id,str("Hi! Makepro"))
    elif command=='time':
        bot.sendMessage(chat_id,str("Time:")+str(now.hour)+str(":")+str(now.second))
    elif command=='date':
        bot.sendMessage(chat_id,str("Date:")+str(now.day)+str("/")+str(now.month)+str("/")+str(now.year))
    elif command=='red1':
        bot.sendMessage(chat_id,str("Red led is ON"))
        GPIO.output(red_led_pin,True)
    elif command=='red0':
        bot.sendMessage(chat_id,str("Red led is OFF"))
        GPIO.output(red_led_pin,False)
    elif command=='blink':
        blink_f(count)
bot = telepot.Bot('1023899509:AAHSDEZaop4490O84oFiOuvMHdprM8uVs-g')
print(bot.getMe())

MessageLoop(bot,handle).run_as_thread()
print('Listening....')

while 1:
    sleep(10)

