#Motion Detection
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)  #LED output
GPIO.setup(24,GPIO.IN)  #PIR input

try:
    while True:
        if GPIO.input(24):
            GPIO.output(17,True)
        else:
            GPIO.output(17,False)
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
