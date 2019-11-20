Achtung: 
Dieses Projekt wird derzeit noch entwickelt, trotzdem hier schon einmal ein erster Einblick:

Aufbau: 

Für dieses Projekt ist die Hardware essentiell:

4 Raspberry Pis mit ADC und Potentiometer sind über Netzwerk mit einem Dispatcher Raspberry verbunden.
Über die 4 Raspberries wird Sound ausgegeben.

Die Potentiometer sind mit einem Adapter an Ferngläser befestigt, dessen Guckwinkel dann als Werte an die 4 Raspberries übergeben werden. 

Die Winkel der Ferngläser bestimmen letztlich welche Audiodatei am lautesten abgespielt wird.

Am Dispatcher Raspberry sind jeweil 4 Arduinos über Seriellen Port angeschlossen, mit welchen bestimmt werden kann auf welchen der 4 Raspberries ein bestimmter Sound in welchem Winkel gespielt wird. 

Die Kommunikation erfolgt über OSC.


Zum Programm: 

Im Hauptordner finden sich drei Programme, die sich Code teilen:

ChannelMain.py : Dieses Programm liest die analogen Werte eines Potentiometers aus und wandelt diesen in Grad um. Auf der Bandbreite von 0 bis 210 Grad sind dabei 3 Audiofiles gelegt, zwischen denen stufenlos genixed wird, wird der Wert des Potentiometers geändert. 
Die Audiofiles werden über OSC aufgerufen und auf verschiedene Kanäle gelegt. ´

SoundMessageMain.py : Dieses Prgogramm erhält von 4 Aurduinos mit NFC Interface über den Seriellen Port Nachricht darüber welche Nfc Id eingelesen wurde. Daraufhin wird in einer Liste die dazugehörige Audiodatei ermittelt und über OSC an verschiedene Empfänger Ips gesendet. 

UtilSoftware: 

NFCLogger: Mit dieser können NFC Karten über Arduino eingelesen  und dann mit jeweiligen Audiodatei gelisten werden. ( Diese wird als Json in Assets gespreichert)

PotiTreshReader:
Mit dieser kann man den Potentiometer auslesen und die "rohen" Werte anzeigen.
In der Assets/channelPrefs.json können dann die Grenzwerte eingetragen werden.