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
    d = open ('Cooper-Test.csv','w')
    d.write (str('Chipname') + ',' + str('Rundenanzahl') + '\n' + '\n' + 
                 L1[0] + ',' + str(len(L1[1:-1])) + str(' Runden') + '\n' +
                 L2[0] + ',' + str(len(L2[1:-1])) + str(' Runden') + '\n' +
                 L3[0] + ',' + str(len(L3[1:-1])) + str(' Runden') + '\n' +
                 L4[0] + ',' + str(len(L4[1:-1])) + str(' Runden') + '\n' +
                 L5[0] + ',' + str(len(L5[1:-1])) + str(' Runden') + '\n' +
                 L6[0] + ',' + str(len(L6[1:-1])) + str(' Runden') + '\n' +
                 L7[0] + ',' + str(len(L7[1:-1])) + str(' Runden') + '\n' +
                 L8[0] + ',' + str(len(L8[1:-1])) + str(' Runden'))
    weiterlesen = False
    GPIO.cleanup()

L1 = ['Chip1']
L2 = ['Chip2']
L3 = ['Chip3']
L4 = ['Chip4']
L5 = ['Chip5']
L6 = ['Chip6']
L7 = ['Chip7']
L8 = ['Chip8']

def csv_datei(Chip):
    f = open('Cooper-Test.csv','w')
    Titel = ['Chipname''Zeit']
    f.write(Titel[0] + ';' + Titel[1] + '\n')

def Liste_erweitern(x):
    x.append(strftime('%H:%M:%S', localtime()))
    print x[0], ':' , len(x[1:-1]), 'Runden'
##    Runde1 = x[1]
##    letzteRunde = x[-1])
##    diff_sek = letzteRunde - Runde1
##    print diff_sek
    sleep(1)


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

            Liste_erweitern(L1)
        elif uid == Chip2:
            Liste_erweitern(L2)
        elif uid == Chip3:
            Liste_erweitern(L3)
        elif uid == Chip4:
            Liste_erweitern(L4)
        elif uid == Chip5:
            Liste_erweitern(L5)
        elif uid == Chip6:
            Liste_erweitern(L6)
        elif uid == Chip7:
            Liste_erweitern(L7)
        elif uid == Chip8:
            Liste_erweitern(L8)
        else:
            print 'Falscher Chip'

        
