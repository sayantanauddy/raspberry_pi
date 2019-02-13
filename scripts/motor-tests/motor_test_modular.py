import sys
import time
import RPi.GPIO as GPIO

def init():
    # Use board numbering for pins
    GPIO.setmode(GPIO.BOARD)

    # Use pins 16 (motorA IN2), 18 (motorA IN1) for the right motor (motor A) inputs
    # Use pins 22 (motorB IN1), 24 (motorB IN2) for the left motor (motor B) inputs
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(24,GPIO.OUT)
    
def cleanup():
    # Clear pin outputs
    GPIO.cleanup()

def forward(duration=5):
    # Set motorA (right motor) forward
    GPIO.output(18,True)
    GPIO.output(16,False)
    
    # Set motorB (left motor) forward
    GPIO.output(24,True)
    GPIO.output(22,False)
    
    # Stop motion if duration is not negative
    if duration > 0:
        time.sleep(duration)
        GPIO.output(18,False)
        GPIO.output(16,False)
        GPIO.output(24,False)
        GPIO.output(22,False)
        
def backward(duration=5):
    # Set motorA (right motor) backward
    GPIO.output(18,False)
    GPIO.output(16,True)
    
    # Set motorB (left motor) backward
    GPIO.output(24,False)
    GPIO.output(22,True)
    
    # Stop motion if duration is not negative
    if duration > 0:
        time.sleep(duration)
        GPIO.output(18,False)
        GPIO.output(16,False)
        GPIO.output(24,False)
        GPIO.output(22,False)

def left_turn(duration=1):
    # Left motor - backward
    # Right motor - forward
    
    # Set motorB (left motor) backward
    GPIO.output(24,False)
    GPIO.output(22,True)
    
    # Set motorA (right motor) forward
    GPIO.output(18,True)
    GPIO.output(16,False)
    
    # Stop motion if duration is not negative
    if duration > 0:
        time.sleep(duration)
        GPIO.output(18,False)
        GPIO.output(16,False)
        GPIO.output(24,False)
        GPIO.output(22,False)

def right_turn(duration=1):
    # Left motor - forward
    # Right motor - backward
    
    # Set motorB (left motor) forward
    GPIO.output(24,True)
    GPIO.output(22,False)
    
    # Set motorA (right motor) backward
    GPIO.output(18,False)
    GPIO.output(16,True)
    
    # Stop motion if duration is not negative
    if duration > 0:
        time.sleep(duration)
        GPIO.output(18,False)
        GPIO.output(16,False)
        GPIO.output(24,False)
        GPIO.output(22,False)    

def stop():
    # Stop moving
    GPIO.output(18,False)
    GPIO.output(16,False)
    GPIO.output(24,False)
    GPIO.output(22,False)


if __name__ == '__main__':
    try:
        init()
        forward(duration=1)
        stop()
        time.sleep(2)
        backward(duration=1)
        stop()
        time.sleep(2)
        left_turn(duration=0.5)
        stop()
        time.sleep(2)
        right_turn(duration=0.5)
        time.sleep(2)
        stop()
        cleanup()
    except:
        stop()
        cleanup()

