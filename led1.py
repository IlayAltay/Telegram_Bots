
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23,GPIO.OUT)
while True:
    str=input('Enter - on, else- exit');
    if str !="":
        break
    else:
        GPIO.output(23,1)
    str=input("Enter - off led,else - exit");
    if str !="":
        break
    else:
        GPIO.output(23,0)
GPIO.cleanup()
