##TODO Needs Proper Logging
##TODO Get and send state of ALL pins
##TODO Verify proper implementation of sockets, especially around closing
##TODO Check one pin to expect low or high for trigger

import socket
import sys
import RPi.GPIO as GPIO
import time

#Define Ports
TRIGGERPIN=4
BINDADDRESS='0.0.0.0'
BINDPORT=10000

#Initialize GPIO Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGERPIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Setup Server Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ( BINDADDRESS, BINDPORT)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)
sock.listen(20)

#Primary Loop
while True:
    #Always Accept New Connections
    connection, client_address = sock.accept()    
    print client_address          
    #When Connected, Continuously expect requests
    while True:
        try:
            data = connection.recv(16)
	    print data
            #Close connection if no data
            if not data:
		print "no data"
                connection.close()                
            #Send current Trigger Pin State
            state = str(GPIO.input(TRIGGERPIN))
            connection.send(state)        
        #Close on problems                
        except:
            print "closing"
	    ##TODO I had this connection.close() line removed for some reason?
	    connection.close()
            break

