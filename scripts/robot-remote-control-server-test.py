 #!/usr/bin/env python

import socket
from threading import *


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.104"
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
                
                print 'left'
            
            elif client_msg_ascii == 'r':
                # Turn right
                print 'right'
            
            elif client_msg_ascii == 'f':
                # Go forward
                
                print 'forward'
            
            elif client_msg_ascii == 'b':
                # Go backward
                
                print 'backward'
            
            elif client_msg_ascii == 's':
                # Stop
                
                print 'stop'
                 
            self.sock.send(b'Command received')

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
    
