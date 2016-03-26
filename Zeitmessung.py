#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO 
import MFRC522
import signal
from time import *
import csv

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

def neue_CSV():
    d = open ('Zeitmessung.csv', 'w+')
    Titel = ['Chipname','Zeit']
    d.write(str('Chipname') + ',' + str('Zeit') + '\n' + '\n')
    d.close()

neue_CSV()

def Zeit_einfuegen(Chip):
    d = open ('Zeitmessung.csv','a')
    d.write (Chip + ',' + str(strftime('%H:%M:%S', localtime())) + '\n')
    d.close()
    print Chip
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
            Zeit_einfuegen('Chip1')
        elif uid == Chip2:
            Zeit_einfuegen('Chip2')
        elif uid == Chip3:
            Zeit_einfuegen('Chip3')
        elif uid == Chip4:
            Zeit_einfuegen('Chip4')
        elif uid == Chip5:
            Zeit_einfuegen('Chip5')
        elif uid == Chip6:
            Zeit_einfuegen('Chip6')
        elif uid == Chip7:
            Zeit_einfuegen('Chip7')
        elif uid == Chip8:
            Zeit_einfuegen('Chip8')
        else:
            print 'Falscher Chip'

        
