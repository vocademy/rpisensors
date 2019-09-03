import RPi.GPIO as GPIO
import time

portTrig = 23
portEcho = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(portTrig, GPIO.OUT)
GPIO.setup(portEcho, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

        if pulse_duration  < 0.023:  # otherwise timeout
            distance = (pulse_duration / 2) * 13504
            print "Distance: {:0.2f}".format(distance)
        time.sleep(0.1)

 except KeyboardInterrupt:
    GPIO.cleanup()
