#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO 
import MFRC522
import signal
from time import *
import csv

Chip1 = [100, 100,187, 150, 45]
Chip2 = [211, 153, 104,0, 34]
Chip3 = [240,175,82,17,28]
Chip4 = [35,245,139,0,93]
Chip5 = [51,214,8,3,238]
Chip6 = [132,179,250,110,163]
Chip7 = [148,126,42,111,175]
Chip8 = [148,75,248,110,73]

weiterlesen = True

def aufhoeren(signal, frame):
    global weiterlesen
    print 'Programm beendet'
    weiterlesen = False
    GPIO.cleanup()

##def csv_Datei_lesen(Runden):
##    with open ('Cooper-Test.csv','r') as Cooper-Test:
##        Runden_ablesen = csv.reader(Runden)
##        Rundenanzahl = []
##        print len('row')

##def csv_Datei_schreiben(Runden):
##    with open ('Cooper_Test.csv','w') as Cooper-Test:
##        Cooper-TestWriter = cs.writer(Cooper-Test)
##        Cooper-TestWriter.writerow[(Chipnummer , Runden)]
##    Cooper-Test.close()
##    
## def Zeit():
##    print strftime("%H:%M:%S", localtime())
##
##print (Zeit())
##"""da wird immer None angezeigt"""
            
##"""
##csv-Datei erstellen/beschreiben (kommt noch weiter nach hinten)
##"""
##Cooper-Test = open('Cooper-Test.csv','w')
##"""DATEN (UID, Zeit"""
##Cooper-Test.close()


signal.signal(signal.SIGINT, aufhoeren)

MIFAREReader = MFRC522.MFRC522()

"""
Nachricht beim Starten des Programmes
"""
print ('Herzlich Willkommen!' '\n'
         'Zum Beenden Strg + C druecken')

while weiterlesen:
    """
    nach Karten scannen
    """
    (Status,Kartentyp) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    """
    UID bekommen
    """
    (Status, uid) = MIFAREReader.MFRC522_Anitcoll()

    if Status == MIFAREReader.MI_OK:
        if uid == Chip1:
            print 'Chip1'
        elif uid == Chip2:
            print 'Chip2'
        elif uid == Chip3:
            print 'Chip3'
        elif uid == Chip4:
            print 'Chip4'
##         elif uid == Chip5:
##             print 'Chip5'
        elif uid == Chip6:
            print 'Chip6'
        elif uid == Chip7:
            print 'Chip7'
        elif uid == Chip8:
            print 'Chip8'
        else:
            print 'Falscher Chip'
        
