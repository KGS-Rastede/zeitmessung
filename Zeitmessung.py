#!/usr/bin/env python
# -*- coding: utf8 -*-
"""Erfasse und speichere Transponder und Zeit in einer CSV-Datei.


"""
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
    """Beende das Programm, und """
    global weiterlesen
    print 'Programm beendet'
    weiterlesen = False
    GPIO.cleanup()

def neue_CSV():
    """öffne die CSV-Datei Zeitmessung, leere ihren Inhalt und schreibe die Spaltenüberschriften."""
    d = open ('Zeitmessung.csv', 'w+')
    Titel = ['Chipname','Zeit']
    d.write(str('Chipname') + ',' + str('Zeit') + '\n' + '\n')
    d.close()

neue_CSV()

def Zeit_einfuegen(Chip):
    """Füge den Chipnamen und die aktuelle Zeit zu der Datei Zeitmessung.csv hinzu."""
    d = open ('Zeitmessung.csv','a')
    d.write (Chip + ',' + str(strftime('%H:%M:%S', localtime())) + '\n')
    d.close()
    print Chip
    sleep(1)

def LED(x):
    GPIO.setmode (GPIO.BOARD)
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x, GPIO.HIGH)

    sleep(0.5)
    GPIO.output(x,GPIO.LOW)

signal.signal(signal.SIGINT, aufhoeren)

MIFAREReader = MFRC522.MFRC522()


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

    if Status == MIFAREReader.MI_OK:
        if uid == Chip1:
            LED(7)
            Zeit_einfuegen('Chip1')
        elif uid == Chip2:
            LED(7)
            Zeit_einfuegen('Chip2')
        elif uid == Chip3:
            LED(7)
            Zeit_einfuegen('Chip3')
        elif uid == Chip4:
            LED(7)
            Zeit_einfuegen('Chip4')
        elif uid == Chip5:
            LED(7)
            Zeit_einfuegen('Chip5')
        elif uid == Chip6:
            LED(7)
            Zeit_einfuegen('Chip6')
        elif uid == Chip7:
            LED(7)
            Zeit_einfuegen('Chip7')
        elif uid == Chip8:
            LED(7)
            Zeit_einfuegen('Chip8')
        else:
            LED(11)
            print 'Falscher Chip'

        
