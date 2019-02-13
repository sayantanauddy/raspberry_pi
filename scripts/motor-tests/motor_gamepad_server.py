import sys
import time
import socket
from threading import *
import RPi.GPIO as GPIO
import signal
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
    
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    # Reset GPIO settings
    cleanup()
    sys.exit(0)

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

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            client_msg = self.sock.recv(1024).decode()
            client_msg_ascii = client_msg.encode('ascii','ignore')
            print client_msg_ascii
            
            if client_msg_ascii == 'l':
                # Turn left
                left_turn(-1)
            
            elif client_msg_ascii == 'r':
                # Turn right
                right_turn(-1)

            elif client_msg_ascii == 'f':
                # Go forward
                forward(-1)
            
            elif client_msg_ascii == 'b':
                # Go backward
                backward(-1)
            
            elif client_msg_ascii == 's':
                # Stop
                stop()

            self.sock.send(b'Command received')


if __name__ == '__main__':
    try:
        signal.signal(signal.SIGINT, signal_handler)
        init()
        time.sleep(2)
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "192.168.0.102"
        port = 12346
        print (host)
        print (port)
        serversocket.bind((host, port))
        serversocket.listen(5)
        print ('server started and listening')
        while True:
            clientsocket, address = serversocket.accept()
            client(clientsocket, address)
    except:
        print('Exception')
        stop()
        cleanup()
        sys.exit(1)


