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

print ("antes")


#Segundos entre persona para publicar
seg = 10

#Declaración del sensor1
Sensor1 = Conteo(pin=2,seg=seg,k=0.003125,label='Litros 1') 

#Metodo que publica la constante del sensor
Sensor1.atributo()  
 
#-------------------------Loop infinito----------------------------------
while True:
  
  try:
   
#publicación de datos en thingsboard
    Sensor1.publica()
    
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
    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
      machine.reset()
    time.sleep(1)
  time.sleep(0.1)
#------------------------------------------------------------------------
