import RPi.GPIO as GPIO
from adxl345 import ADXL345
from time import sleep
  
GPIO.setmode(GPIO.BCM)

adxl345 = ADXL345()

pX_up = 6
pX_dn = 5
pY_up = 22
pY_dn = 27
pZ_up = 21
pZ_dn = 20

GPIO.setup(pX_up, GPIO.OUT)
GPIO.setup(pX_dn, GPIO.OUT)
GPIO.setup(pY_up, GPIO.OUT)
GPIO.setup(pY_dn, GPIO.OUT)
GPIO.setup(pZ_up, GPIO.OUT)
GPIO.setup(pZ_dn, GPIO.OUT)

def set_leds(x,y,z):
    GPIO.output(pX_up, x>=0)
    GPIO.output(pX_dn, x<0)
    GPIO.output(pY_up, y>=0)
    GPIO.output(pY_dn, y<0)
    GPIO.output(pZ_up, z>=0)
    GPIO.output(pZ_dn, z<0)

try:
    print "ADXL345 on address 0x{:02X}".format(adxl345.address)
    while True:    
        axes = adxl345.getAxes(True)
        print "x={:0.3f}G  y={:0.3f}G  z={:0.3f}G ".format(axes['x'],axes['y'],axes['z'])
        
        set_leds(axes['x'], axes['y'], axes['z'])
        sleep(0.5)
            
except KeyboardInterrupt:
    GPIO.cleanup()
