#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO 
import MFRC522
import signal
from time import *
import csv
import sys

'''ordnet den jeweiligen Chip-UIDs Namen zu'''
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

def Zeit():
    print strftime("%H:%M:%S", localtime())

def Datei_oeffnen():
    e = open('Cooper-Test.csv', 'w+')
    '''öffnet und leert die Datei Cooper-Test.csv zum Lesen und Schreiben'''
                                                             
    '''Überschrift der Spalten'''
    Titel = ['Chipname','Zeit']
    e.write(Titel[0] + ';' + Titel[1] + '\n')
    e.close()

def Messdaten(Chip):
    f = open('Cooper-Test.csv','a')
    li = [Chip]
    li.append(strftime("%H:%M:%S", localtime()))
    f.write(li[0] + ';' + str(li[1]) + '\n')    
    f.close()
    print (Chip)
    sleep(1)

Datei_oeffnen()

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
    (Status, uid) = MIFAREReader.MFRC522_Anticoll()

    '''Der Chipname wird als Bestätigung ausgegeben'''
    if Status == MIFAREReader.MI_OK:
        if uid == Chip1:
            Messdaten('Chip1')
        elif uid == Chip2:
            Messdaten('Chip2')
        elif uid == Chip3:
            Messdaten('Chip3')
        elif uid == Chip4:
            Messdaten('Chip4')
        elif uid == Chip5:
            Messdaten('Chip5')
        elif uid == Chip6:
            Messdaten('Chip6')
        elif uid == Chip7:
            Messdaten('Chip7')
        elif uid == Chip8:
            Messdaten('Chip8')
        else:
            print 'Falscher Chip'
