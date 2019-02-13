import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.output(13,True)
GPIO.output(15,False)
time.sleep(5)

GPIO.output(13,False)
GPIO.output(15,True)
time.sleep(5)

GPIO.output(13,False)
GPIO.output(15,False)

time.sleep(2)
GPIO.cleanup()

