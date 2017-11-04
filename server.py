import socket
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ( '0.0.0.0', 10000)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)
#sock.settimeout(2)
sock.listen(20)

while True:
    connection, client_address = sock.accept()          
    print client_address
    while True:
        try:
            data = connection.recv(16)
	    print data
            if not data:
		print "no data"
                connection.close()                
            state = str(GPIO.input(4))
            connection.send(state)        
            
            
        except:
            print "closing"           
            break

