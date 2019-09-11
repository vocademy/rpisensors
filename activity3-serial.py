import time    #Allows us to control timing of the script
import board   #Imports a libray from Adafruit which helps us know what pins are available on a device
import busio   #Imports a mondule that contains libraries for various serial protocols like I2C
import adafruit_adxl34x    #Allos us to communicate with the accelerometer

i2c = busio.I2C(board.SCL, board.SDA)    #Estabilishes a varible that contains the I2C communication information
accelerometer = adafruit_adxl34x.ADXL345(i2c)    #Creates an object that represents the accelerometer
#The following while loop takes a reading from the ADXL345 and prints the results
while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(1)
