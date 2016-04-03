# Zeitmessung

Dieses Repository enthält zwei verschiedene Python-Codes. 
Der Code Cooper_Test.py eignet sich für das Zählen der Runden im Sportunterricht.
Der Code Zeitmessung.py eignet sich für den Orientierungslauf und wahlweise für Leichtathletik. 
Benötigt wird ein Raspberry Pi sowie das RFID-Lesegerät MFRC-522. Des weiteren werden zwei LEDs, 
wahlweise in Grün und in Rot, mit zwei ausreichend großen Widerständen benötigt.

# Verkabelung

MFRC-522  - Raspberry Pi (Physikalische Pin-Nummer)

SDA       - 24
SCK       - 23
MOSI      - 19
MISO      - 21
GND       - jeder "Ground" Anschluss
RST       - 22
3.3V      - jeder 3.3 Volt Anschluss

Die grüne LED wird an den Pin 7, die rote LED an den Pin 11 angeschlossen und die Kathode wird mit 
Ground verbunden.

#Ausführen
Während das Programm ausgeführt wird, ist nichts weiter zu beachten. Zum Beenden des Programmes muss 
die Tastenkombination Strg + C gedrückt werden. 


