import sys
import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(7,True)
time.sleep(1)
GPIO.output(7,False)
time.sleep(1)
GPIO.output(11,True)
time.sleep(1)
GPIO.output(11,False)
time.sleep(1)
GPIO.output(13,True)
time.sleep(1)
GPIO.output(13,False)
time.sleep(1)
GPIO.output(15,True)
time.sleep(1)
GPIO.output(15,False)
time.sleep(1)
GPIO.cleanup()

