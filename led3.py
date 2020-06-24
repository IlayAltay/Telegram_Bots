from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
limit = 0.1
commandstop="stop"
commandplus=1
comstr='1'
ledpin=23
i=0
#function on-off led 
def blink():
    GPIO.output(ledpin,GPIO.HIGH)
    sleep(limit)
    GPIO.output(ledpin,GPIO.LOW)
    sleep(limit)
    
#Osnovnaya  programma
try:
    while True:
        GPIO.output(ledpin, True)
        sleep(limit)
        GPIO.output(ledpin, False)
        sleep(limit)
        command=input('Command for Stoping process :')
        command=str(command)
        
        if command.isdigit():
            print('Vvedeno chislo?_')
            print(command.isdigit())
            print('Kakoe_')
            print(command)
            #print(command.isdigit())
            while i<int(command):
                blink()
                i=i+1
                print('00')
            i=0    
            if commandplus==int(command):
                limit=limit+0.5
            
                
        else:
            print('Vvedena stroka_')
            print(command)
            if command=='set':
                limit=float(input('Ustanovka intervala_'))
            if command=='reset':
                limit=0.1
            if command==commandstop:
               print('comanda sootvetsvuet ostanovy') 
               GPIO.output(ledpin,GPIO.HIGH)
               limit=3
               GPIO.output(ledpin,GPIO.LOW)
               GPIO.cleanup() 
               exit(0)
            else:
               GPIO.output(ledpin,GPIO.HIGH)
               sleep(1)
               GPIO.output(ledpin,GPIO.LOW)
except KeyboardInterrupt:
    print ('program stop')            
    GPIO.cleanup()
