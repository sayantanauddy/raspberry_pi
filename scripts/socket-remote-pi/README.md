# socket-remote-pi

Scripts for controlling a raspberry pi robot (consisting of an RPi board, L239 motor driver, couple of DC motors and an ultrasonic sensor), remotely
from a PC (running Ubuntu 14.04 LTS) using a standard USB game controller (I use a PS3/PC compatible gamepad from CSL). I have both the PC and the RPi connected to a home WLAN.

## Running Instructions
1. Edit  robot-remote-control-server.py and robot-remote-control-client.py with the correct host ip (of the RPi)
2. Attach the gamepad to the PC and test if its functioning properly. Great instructions at http://yameb.blogspot.de/2013/01/gamepad-input-in-python.html.
3. Execute robot-remote-control-server.py on the raspberry pi.
4. Execute robot-remote-control-client.py on the PC.
5. I use the left joystick for left-right-forward-backward control and button "1" or "Y" for stopping. Using the above webpage, different buttons can also be configured.

