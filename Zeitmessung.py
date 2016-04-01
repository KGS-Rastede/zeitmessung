#!/usr/bin/env python
# -*- coding: utf8 -*-
"""Erfasse und speichere  RFID-Transponder und Zeit in einer CSV-Datei.

License: GPL 3
Author: Wiebke Dirksen

Dieses Script eignet sich zur Zeitmessung im Sportunterricht mit Hilfe der RFID-Identifkation.
Die zu verwendenen Transponder, werden über ihre "Unique Identification Number" (UID) identifiziert.

Im Script gespeichert sind acht Transponder. Sollen zusätzliche Transponder verwedet werden, muss
die UID des Transponders vereinfacht als Variable eingespeichert werden. Die UID kann
über den Befehl:"print uid" beispielsweise nach Zeile 138, also nach "print 'Falscher Chip'" erfahren
werden. Der Befehl sollte ebenfalls dreimal, also um 12 Stellen eingerückt sein. 
Zudem muss nach der Zeile 135 der Befehl
         elif uid == <Chipname>:
            LED(7)
            Zeit_einfuegen('<Chipname>')   
hinzugefügt werden.

Gespeicherte Transponder werden registriert und mit Name und Zeit der Registrierung in eine CSV-Datei
geschrieben. Durch das kurze Aufblinken einer grünen LED sowie dem Erscheinen des Chipnamens auf dem
Bildschirm wird die Authentifikation bestätigt.
Ist die Transponder-UID dem Script nicht bekannt, leuchtet eine rote LED auf.

Beendet wird das Programm durch das Drücken der Tastenkombination 'Strg' + 'C'. Dadurch wird das Signal
SIGINT ausgelöst und die verwendeten GPIO-Pins werden freigegeben. 
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
    """Höre auf zu lesen und gebe die belegten GPIO-Pins frei.

    Parameter:
    - signal: SIGINT-Signal, welches über Strg + C ausgelöst wird. 
    """
    global weiterlesen
    print 'Programm beendet'
    weiterlesen = False
    GPIO.cleanup()

def Zeitmessung_CSV():
    """öffne, leere und beschreibe die CSV-Datei Zeitmessung mit den Spaltenüberschriften.

    Die Spaltenüberschriften sollen in der Variable Titel gespeichert werden. Nach dem Titel soll eine
    Zeile freigelassen werden. 
    """
    d = open ('Zeitmessung.csv', 'w+')
    Titel = ['Chipname','Zeit']
    d.write(str('Chipname') + ',' + str('Zeit') + '\n' + '\n')
    d.close()

Zeitmessung_CSV()

def Zeit_einfuegen(Chip):
    """Füge den Chipnamen und die aktuelle Zeit zu der Datei Zeitmessung.csv hinzu.

    Das Argument "Chip" steht für die eingespeicherte Variable der Transponder-UID.
    Höre anschließend für eine Sekunde auf zu lesen, um eine versehentliche doppelte Registrierung
    zu vermeiden. 
    """
    d = open ('Zeitmessung.csv','a')
    d.write (Chip + ',' + str(strftime('%H:%M:%S', localtime())) + '\n')
    d.close()
    print Chip
    sleep(1)

def LED(x):
    """Lasse eine LED aufleuchten.

    Die grüne LED wird über das Argument x = 7 (Pin-Nummer 7) gesteuert,
    die rote LED über das Argument x = 11 (Pin-Nummer 11).
    """
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

    (Status,Kartentyp) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

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
