#! /usr/bin/env python
import sys
import time
import socket
import RPi.GPIO as GPIO

TALLYPIN=4
STATUSPIN=20

GPIO.setmode(GPIO.BCM)
GPIO.setup(TALLYPIN, GPIO.OUT)
GPIO.setup(STATUSPIN, GPIO.OUT)

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("10.2.1.1", 10000)
    sock.settimeout(1)
    try:
        #print "connecting"
        sock.connect(server_address)
        GPIO.output(STATUSPIN, 0)
        #print "connected"
        while True:
            try:
                #print "sending"
                sock.sendall("?")
               #print "receiving"
                data = sock.recv(16)
                if not data:
	           #print "nodataCLOSE"
                    sock.close()
                    #time.sleep(1)
                    break
		
                datanum = 1 - int(data.strip())
                print datanum
                GPIO.output(TALLYPIN, int(data.strip()))
                #time.sleep(0.2)
            except Exception as e:
                print "SENDRECVEXCEPTION: " + str(e)
                sock.close()
                time.sleep(1)
                break
    except Exception as e:
        print "Can't connect: " + str(e)
	GPIO.output(STATUSPIN, 1)
	time.sleep(0.5)
	GPIO.output(STATUSPIN,0)
        time.sleep(0.5)

