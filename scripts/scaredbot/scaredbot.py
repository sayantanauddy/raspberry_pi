#!/usr/bin/python

''' Author - Sayantan Auddy'''

''' The RPi robot advances when there is no obstacle within
    40 cm in front of it and retreats when an obstacle is 
    present within 10 cm in front of it.
'''

# Import required Python libraries
import time
import RPi.GPIO as GPIO
import signal
import sys

# Handler for cleanup
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
	# Reset GPIO settings
	GPIO.cleanup()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO_LEFT_FORWARD = 4 # Pin 7->GPIO4
GPIO_LEFT_BACKWARD = 17 # Pin 11
GPIO_RIGHT_FORWARD = 27 # Pin 13
GPIO_RIGHT_BACKWARD = 22 # Pin 15

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set output pins for driving
GPIO.setup(GPIO_LEFT_FORWARD, GPIO.OUT)
GPIO.setup(GPIO_LEFT_BACKWARD, GPIO.OUT)
GPIO.setup(GPIO_RIGHT_FORWARD, GPIO.OUT)
GPIO.setup(GPIO_RIGHT_BACKWARD, GPIO.OUT)

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle
time.sleep(0.5)

exec_time = 0

while(exec_time<60):
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO)==0:
      start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
      stop = time.time()

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000

    # That was the distance there and back so halve the value
    distance = distance / 2

    print "Distance : %.1f" % distance
    
    if(distance <= 10.0):
        # If distance is less than 10 cm, move back
        GPIO.output(GPIO_LEFT_BACKWARD, True)
        GPIO.output(GPIO_RIGHT_BACKWARD, True)
        
        GPIO.output(GPIO_LEFT_FORWARD, False)
        GPIO.output(GPIO_RIGHT_FORWARD, False)
    elif(distance>=40.0):
        # If distance is more than 40 cm, move forward
        GPIO.output(GPIO_LEFT_FORWARD, True)
        GPIO.output(GPIO_RIGHT_FORWARD, True)
        
        GPIO.output(GPIO_LEFT_BACKWARD, False)
        GPIO.output(GPIO_RIGHT_BACKWARD, False)
    else:
        # If distance is between 10 and 20 cm, do not move
        GPIO.output(GPIO_LEFT_FORWARD, False)
        GPIO.output(GPIO_RIGHT_FORWARD, False)
        
        GPIO.output(GPIO_LEFT_BACKWARD, False)
        GPIO.output(GPIO_RIGHT_BACKWARD, False)           
           
    exec_time = exec_time + 1
    time.sleep(0.5)

# Reset GPIO settings
GPIO.cleanup()

