import RPi.GPIO as GPIO
import time

#Set pins for Trigger and Echo
portTrig = 23
portEcho = 24

#Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(portTrig, GPIO.OUT)                            #Sets pin as output
GPIO.setup(portEcho, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Sets pin as input and activates 10K Pull Down resistor

#reset Trigger and let settle
GPIO.output(portTrig, False)
time.sleep(0.5)

#Start ranging
try:
    while True:
        GPIO.output(portTrig, True)
        time.sleep(0.00001)
        GPIO.output(portTrig, False)

        pulse_start = time.time()
        while not GPIO.input(portEcho):
            pulse_start = time.time()
            
        pulse_end = pulse_start
        while GPIO.input(portEcho):
            pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_start

        if pulse_duration  < 0.023:                                 #Otherwise timeout
            distance = (pulse_duration / 2) * 13504                 #Calculates the "one-way" distance in inches
            print ("Distance:","{:0.2f}".format(distance),"inches") #Prints the value of the variable Distance as a floating point value with two places
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
