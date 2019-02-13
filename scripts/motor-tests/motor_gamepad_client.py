
''' Author - Sayantan Auddy'''

''' Client script - Run a while loop, continuously checking for events from the game controller.
    When the event comes, send the appropriate message to the server (running on the RPi).
    
    The client script runs on the PC to which the USB game controller is attached.
    
    The server needs to be started first, and then the client.
    
    Set the same host ip address in both the client and server scripts
    
    Game controller code derived from http://yameb.blogspot.de/2013/01/gamepad-input-in-python.html
'''

import gamepad
import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.102' #ip of raspberry pi (server)
port = 12346
s.connect((host,port))

while(True):
    
    print 'Loop start'
    msg = ''
    left = False
    right = False
    forward = False
    backward = False
    stop = False
            
    controller = gamepad.get()
    print controller
    if controller[0] < -0.9:
        left = True
        msg = 'l'
    elif controller[0] > 0.9:
        right = True
        msg = 'r'
    elif controller[1] < -0.9:
        forward = True
        msg = 'f'
    elif controller[1] > 0.9:
        backward = True
        msg = 'b'
    elif controller[5] == 1:
        stop = True
        msg = 's'
     
    if left or right or forward or backward or stop:
        s.send(msg.encode()) 
        data = ''
        data = s.recv(1024).decode()
        print(data)
        
    continue
            
s.close()

        
    
    
