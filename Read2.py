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
'''
ordnet den jeweiligen Chip-UIDs Namen zu
'''

weiterlesen = True

def aufhoeren(signal, frame):
'''
Diese Funktion wird aufgerufen, wenn das Programm mit Strg + C beendet wird
'''
    global weiterlesen
    d = open ('Cooper-Test.csv','w')
    '''
    Erstellt, bzw. wenn diese Datei bereits vorhanden ist,
    überschreibt eine CSV-Datei mit dem Namen Cooper-Test

    HIER Z.B. IST DAS KOMMENTAR STOEREND. WENN ICH ALLE KOMMENTARE WEGLASSE, DIE 
    INNERHALB SOLCHE EINER FUNKTION STEHEN, FUNKTIONIERT ES WIEDER.
    '''
    d.write (str('Chipname') + ',' + str('Rundenanzahl') + '\n' + '\n' + 
                 L1[0] + ',' + str(len(L1[1:-1])) + str(' Runden') + '\n' +
                 L2[0] + ',' + str(len(L2[1:-1])) + str(' Runden') + '\n' +
                 L3[0] + ',' + str(len(L3[1:-1])) + str(' Runden') + '\n' +
                 L4[0] + ',' + str(len(L4[1:-1])) + str(' Runden') + '\n' +
                 L5[0] + ',' + str(len(L5[1:-1])) + str(' Runden') + '\n' +
                 L6[0] + ',' + str(len(L6[1:-1])) + str(' Runden') + '\n' +
                 L7[0] + ',' + str(len(L7[1:-1])) + str(' Runden') + '\n' +
                 L8[0] + ',' + str(len(L8[1:-1])) + str(' Runden'))
    '''
    In die CSV-Datei wird in die erste Spalte jeweils der Chipname geschrieben.
    In der zweiten Spalte steht nun die Anzahl der Runden
    '''
    print 'Programm beendet'
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
'''
Acht verschiedene Listen mit einer String als Inhalt werden erzeugt. 
'''

def Liste_erweitern(x):
    x.append(strftime('%H:%M:%S', localtime()))
    '''
    STOERT

    Diese Funktion fügt zu der für das Argument x eingegebenen Liste ein neues Element,
    welches die aktuelle Zeit im hh:mm:ss Format ausgibt zu.
    '''
    print x[0], ':' , len(x[1:-1]), 'Runden'
    '''
    Auf dem Bildschirm wird der Chipname, welcher dem ersten Element
    der für das Argument x eingegebenen Liste entspricht,  ein Doppelpunkt
    sowie die Anzahl der Runden angezeigt. Der Befehl len(x[1:-1]) zählt die Anzahl der Elemente
    vom zweiten Element  bis zum letzten Element.
    '''
##    Runde1 = x[1]
##    letzteRunde = x[-1])
##    diff_sek = letzteRunde - Runde1
##    print diff_sek
    sleep(1)
    '''
    Dieser Befehl pausiert das Lesegerät für eine Sekunde, sodass ein Chip nicht aus Versehen
    zweimal hintereinander gelesen wird. Somit wird das Ergebnis nicht verfälscht.
    '''

signal.signal(signal.SIGINT, aufhoeren)

MIFAREReader = MFRC522.MFRC522()

print ('Herzlich Willkommen!' '\n'
         'Zum Beenden Strg + C druecken')

"""
Nachricht beim Starten des Programmes erscheint auf dem Bildschirm
"""
while weiterlesen:
    (Status,Kartentyp) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    """
    nach Karten scannen
    """
    (Status, uid) = MIFAREReader.MFRC522_Anticoll()
    """
    UID bekommen
    """
    
    if Status == MIFAREReader.MI_OK:
    '''
    STOERT

    Der Chipname wird als Bestätigung ausgegeben
    '''
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
        '''
        -   Wenn die vom Chip an das Lesegerät gesendete UID der UID von einem der Chips entspicht,
            wird die Funktion Liste_erweitern mit dem Argument der dem Chipnamen entsprechenden
            Liste aufgerufen.  
        -   Wenn die vom Chip an das Lesegerät gesendete UID nicht der UID von einem der Chips entspicht,
            erscheint die Nachricht: "Falscher Chip" auf dem Bildschirm.
        '''

        
