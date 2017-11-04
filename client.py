##TODO - What a mess
##TODO - Read and assign all pins
##TODO - Set pins high or low depending on state of some setup pin
##TODO - Verify proper implementation of sockets
##TODO - Needs proper logging

#! /usr/bin/env python
import sys
import time
import socket
import RPi.GPIO as GPIO

TALLYPIN=4
STATUSPIN=20
SERVERADDRESS="10.2.1.1"
SERVERPORT=10000

#Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(TALLYPIN, GPIO.OUT)
GPIO.setup(STATUSPIN, GPIO.OUT)

#Continuously attempt to connect
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVERADDRESS, SERVERPORT)
    sock.settimeout(1)
    try:
        sock.connect(server_address)
	#Set Status Pin to indicate connection
        GPIO.output(STATUSPIN, 0)
	#When connected, continuously attempt to get state
        while True:
            try:
                sock.sendall("?")
                data = sock.recv(16)
                if not data:
	            sock.close()
                    break
		#Reverse incoming State so High Becomes low
		#TODO - Make more versatile for different types of systems
                datanum = 1 - int(data.strip())
                print datanum
                GPIO.output(TALLYPIN, int(data.strip()))                
            except Exception as e:
                print "SENDRECVEXCEPTION: " + str(e)
                sock.close()
                time.sleep(1)
                break
    except Exception as e:
        #Wait 1 second before attempting reconnection, flash status pin during
        print "Can't connect: " + str(e)
	GPIO.output(STATUSPIN, 1)
	time.sleep(0.5)
	GPIO.output(STATUSPIN,0)
        time.sleep(0.5)

