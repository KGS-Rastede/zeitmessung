#!/usr/bin/env python
# -*- coding: utf8 -*-
"""Erfasse und speichere RFID-Transponder und die Anzahl der Erfassungen in einer CSV-Datei.

License: GPL 3
Author: Wiebke Dirksen

Dieses Script eignet sich zur Zählung der gelaufenen Runden beim Cooper-Test im Sportunterricht mit
Hilfe der RFID-Identifikation. Die zu verwendenden Transponder/Chips, werden über ihre "Unique Identification
Number" (UID) identifiziert.

Im Script gespeichert sind acht Transponder. Sollen zusätzliche Transponder verwendet werden, muss
die UID des Chips vereinfacht als Variable eingespeichert werden. Die UID kann über den Befehl:
"print uid" beispielsweise nach Zeile 150, also nach "print 'Falscher Chip'" angezeigt werden. Zudem muss
eine neue Liste unter Zeile 58 hinzugefügt werden.
In der Funktion aufhoeren muss eine neue Zeile unter die Zeile 78, aber vor die letzte runde Klammer der Zeile
78 mit dem Element des Chipnamens mit:
            + '\n' + <Listenname>[0] + ',' + str(len(<Listenname>[1:-1])) + str(' Runden') 
hinzugefügt werden.  
Zudem muss nach der Zeile 147 der Befehl
         elif uid == <Chipname>:
            Liste_erweitern(<Chipname>)  
hinzugefügt werden.

Gespeicherte Transponder, für welche zudem eine Liste erstellt wurde, werden registriert und die
aktuelle Zeit wird der Liste hinzugefügt. Eine grüne LED leuchtet auf. Zudem wird der Chipname sowie die
Länge der Liste ausgegeben. Diese entspricht in der Praxis der Anzahl der gelaufenen Runden.
Ist der Transponder nicht eingespeichert, leuchtet eine rote LED auf.
Beträgt die Zeitdifferenz zwischen der ersten und der letzten Autorisierung mehr als 720 Sekunden, also
mehr als zwölf Minuten, wird der Liste kein weiteres Element mehr hinzugefügt. Auch dann leuchtet eine
rote LED auf.
Wird über die Tastenkombination Strg + C das SIGINT Signal ausgelöst, werden die GPIO Pins wieder frei und
der Chipname wird zusammen mit der Rundenanzahl in einer CSV-Datei gespeichert. 
"""

import RPi.GPIO as GPIO 
import MFRC522
import signal
import csv
import time

Chip1 = [100, 100,187, 150, 45]
Chip2 = [211, 153, 104,0, 34]
Chip3 = [240,175,82,17,28]
Chip4 = [35,245,139,0,93]
Chip5 = [51,214,8,3,238]
Chip6 = [132,179,250,110,163]
Chip7 = [148,126,42,111,175]
Chip8 = [148,75,248,110,73]

L1 = ['Chip1']
L2 = ['Chip2']
L3 = ['Chip3']
L4 = ['Chip4']
L5 = ['Chip5']
L6 = ['Chip6']
L7 = ['Chip7']
L8 = ['Chip8']

weiterlesen = True

def aufhoeren(signal, frame):
    """Höre auf zu lesen und speichere die Transponderlisten.

    Wird das SIGINT-Signal ausgelöst, schreibe den Chipnamen mit der dazu gehörigen
    Rundenzahl in eine CSV-Datei, gebe die belegten GPIO-Pins frei und höre auf zu lesen.     
    """
    global weiterlesen
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
    d.close()
    print 'Programm beendet'
    weiterlesen = False
    GPIO.cleanup()

def LED(x):
    """Lasse eine LED aufleuchten.

    Die grüne LED wird über das Argument x = 7 gesteuert,
    die rote LED über das Argument x = 11.
    """
    GPIO.setmode (GPIO.BOARD)
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x, GPIO.HIGH)

    time.sleep(0.5)
    GPIO.output(x,GPIO.LOW)

def Liste_erweitern(x):
    """Erweitere die zum Transponder gehörende Liste.

    x = Name der Liste des Transponders.
    Wenn noch keine zwölf Minuten gelaufen worden sind, füge der Liste des Transponders ein weiteres
    Element hinzu, welches die Zeit enthält.Gebe den Chipnamen und die Anzahl der gelaufenen Runden aus
    und lasse die grüne LED aufblinken. Höre anschließend für eine Sekunde auf zu lesen, um eine
    versehentliche doppelte Registrierung zu vermeiden.
    Wenn mehr als zwölf Minuten gelaufen sind, füge der Liste kein weiteres Element mehr zu, lasse eine
    rote LED aufleuchten und gebe die Nachricht:"Zeit abgelaufen!" heraus. 
    """
    x.append(time.time())
    if ((x[-1]-x[1])>720):
        x.remove(x[-1])
        LED(11)
        print 'Zeit abgelaufen!'
        return
    else:
        print x[0], ':' , len(x[1:-1]), 'Runden'
        LED(7)
        time.sleep(1)

signal.signal(signal.SIGINT, aufhoeren)

MIFAREReader = MFRC522.MFRC522()

print ('Herzlich Willkommen!' '\n'
         'Zum Beenden Strg + C druecken')

while weiterlesen:
    (Status,Kartentyp) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
  
    (Status, uid) = MIFAREReader.MFRC522_Anticoll()
  
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
            LED(11)
            print 'Falscher Chip'
