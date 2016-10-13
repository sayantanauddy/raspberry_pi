 #!/usr/bin/env python

import socket
from threading import *

# RPi related imports
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

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.102"
port = 12346
print (host)
print (port)
serversocket.bind((host, port))

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
                
                GPIO.output(GPIO_LEFT_FORWARD, False)
                GPIO.output(GPIO_RIGHT_FORWARD, True)
                
                GPIO.output(GPIO_LEFT_BACKWARD, False)
                GPIO.output(GPIO_RIGHT_BACKWARD, False) 
            
            elif client_msg_ascii == 'r':
                # Turn right

                GPIO.output(GPIO_LEFT_FORWARD, True)
                GPIO.output(GPIO_RIGHT_FORWARD, False)

                GPIO.output(GPIO_LEFT_BACKWARD, False)
                GPIO.output(GPIO_RIGHT_BACKWARD, False)


            elif client_msg_ascii == 'f':
                # Go forward
                
                GPIO.output(GPIO_LEFT_FORWARD, True)
                GPIO.output(GPIO_RIGHT_FORWARD, True)
                
                GPIO.output(GPIO_LEFT_BACKWARD, False)
                GPIO.output(GPIO_RIGHT_BACKWARD, False)
            
            elif client_msg_ascii == 'b':
                # Go backward
                
                GPIO.output(GPIO_LEFT_BACKWARD, True)
                GPIO.output(GPIO_RIGHT_BACKWARD, True)
                
                GPIO.output(GPIO_LEFT_FORWARD, False)
                GPIO.output(GPIO_RIGHT_FORWARD, False)
            
            elif client_msg_ascii == 's':
                # Stop

                GPIO.output(GPIO_LEFT_BACKWARD, False)
                GPIO.output(GPIO_RIGHT_BACKWARD, False)

                GPIO.output(GPIO_LEFT_FORWARD, False)
                GPIO.output(GPIO_RIGHT_FORWARD, False)

            self.sock.send(b'Command received')

serversocket.listen(5)
print ('server started and listening')
while True:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
