#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO 
import MFRC522
import signal
from time import *

#moin

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

def schreib_den_kram(kram):
    datei = open("datei.csv", "w")
    datei.write(hallo.dat)
    datei.close()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522


# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

dateiinhalt = ""

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
   # if status == MIFAREReader.MI_OK:
        #print "Card detected"


    
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        #print ("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
       #print (uid)

       if uid == [100, 100,187, 150, 45]:
           print ("1") 
       if uid == [211, 153, 104,0, 34]:
           print ("2") 
       if uid == [240,175,82,17,28]:
           print ("3")
       if uid == [35,245,139,0,93]:
           print ("4")
       if uid == [51,214,8,3,238]:
           print ("5")
       if uid == [132,179,250,110,163]:
           print ("6")
       if uid == [148,126,42,111,175]:
           print ("7")
       if uid == [148,75,248,110,73]:
           print ("8")
    def Zeit():
            print strftime("%H:%M:%S", localtime())
    
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        
             print (Zeit())
            
        
        #dateiinhalt = Zeit(uid) + "" + str(uid[0]) + "\n"




    #schreib_den_kram(dateiinhalt)  
