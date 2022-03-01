
from funciones import *       #funciones para hacer el código modular
from wifi import do_connect   #importa función para conexión wifi de wifi.py

#importar librerías
import time
#import utime               ++++++++++++
#import network             ++++++++++++
#import sys                 ++++++++++++


#variables para los intentos de conexión
cnt_boot = 0
cont = 0

#configuración del network
#sta_if = network.WLAN(network.STA_IF)        ++++++++++++
#sta_if.active(True)                          ++++++++++++

#Conexión a internet
#ap_if = network.WLAN(network.AP_IF)         ++++++++++++
#sta_if.connect(red,clave)                   ++++++++++++

#Segundos entre persona para publicar
seg = 10
Sensor1 = Conteo(pin=15,seg=seg,k=0.003125,label='Litros 1')
Sensor1.atributo()

Sensor2 = Conteo(pin=5,seg=seg,k=0.003125,label='Litros 2')
Sensor2.atributo()

Sensor3 = Conteo(pin=19,seg=seg,k=0.003125,label='Litros 3')
Sensor3.atributo()

Sensor4 = Conteo(pin=23,seg=seg,k=0.003125,label='Litros 4')
Sensor4.atributo()

#Sensor5 = Conteo(pin=14,seg=seg,k=0.003125,label='Litros 5')
#Sensor5.atributo()

#Sensor6 = Conteo(pin=12,seg=seg,k=0.003125,label='Litros 6')
#Sensor6.atributo()

#Sensor7 = Conteo(pin=13,seg=seg,k=0.003125,label='Litros 7')
#Sensor7.atributo()

#Sensor8 = Conteo(pin=15,seg=seg,k=0.003125,label='Litros 8')
#Sensor8.atributo()

#-------------------------Loop infinito----------------------------------
while True:
  try:
#publicación de datos en thingsboard
    Sensor1.publica()
    Sensor2.publica()
    Sensor3.publica()
    Sensor4.publica()
#    Sensor5.publica()
#    Sensor6.publica()
#    Sensor7.publica()
#    Sensor8.publica()
#Reinicio de variables
    cnt_boot = 0
    cont = 1
#reintentar conexión en caso de fallo
  except Exception as inst:
    print(inst)
    do_connect(red,clave);
    cnt_boot += 1
    cont += 1
    print("Fail {}".format(cnt_boot))
    if cont >1:
        Sensor1.contador = Sensor1.contador
        Sensor2.contador = Sensor2.contador
        Sensor3.contador = Sensor3.contador
        Sensor4.contador = Sensor4.contador
        #Sensor5.contador = Sensor5.contador
        #Sensor6.contador = Sensor6.contador
        #Sensor7.contador = Sensor7.contador
        #Sensor8.contador = Sensor8.contador
    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
      machine.reset()
    time.sleep(2)
  time.sleep(0.1)

