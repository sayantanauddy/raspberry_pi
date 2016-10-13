
import gamepad
import socket

''' Run a while loop, continuously checking for events from the controller.
    When the event comes, call the appropriate service on the server
'''

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
        
    if left or right or forward or backward:
        s.send(msg.encode()) 
        data = ''
        data = s.recv(1024).decode()
        print(data)
        
    continue
            
s.close()

        
    
    
