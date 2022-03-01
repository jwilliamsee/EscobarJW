from machine import Pin       #libreria para utilizar los GPIO's de la esp
from funcion import *         #importar la función para publicar el thingsboard
from wifi import do_connect   #importa función para conexión wifi de wifi.py
import time


#-------------Datos del dispositivo----------------------#
#Datos de la red de internet
red = 'INFINITUMjpdm'                #Red de internet
clave = '5cbbb04d21'      #contraseña de la red
#red = 'IER'                #Red de internet
#clave = 'acadier2014'      #contraseña de la red

#credenciales del dispositivo configurado en thingsboard
unique_id = 'fd382bc0-49d5-11ea-9ffe-35550336f914'
token = 'Njk5bs2q53mUSXfdvlqc'
#-------------------------------------------------------#


#---------------Clase para el conteo digital del pin-----------------#
class Conteo:
  
#Variables iniciales de la clase
  contador = 0
  T = 0
  data = 0
  constant = 0
  con = 0
  estado_anterior = 0
  contat = 0
  contboot = 0

#Función que inicializa los valores de la clase unicos de cada sensor
  def __init__(self,pin=0,seg=0,k=0,label=''):
    self.inpt = Pin(pin, Pin.IN)
    self.seg = seg
    self.k = k    
    self.label = label
    self.inpt.irq(trigger=Pin.IRQ_RISING, handler=self.my_callback)
   
#Metodo callback que realiza el conteo digital del pin
  def my_callback(self,l):
    self.contador = self.contador +1

#Metodo de constantes del sensor
  def ecuacion(self):
      self.T = (self.contador*self.k)

#Metodo que empaqueta los datos para ser publicados en Thingsboard
  def datos(self):
      self.data  = {self.label: 0}
      self.data[self.label] = self.T 

#Metodo que realiza la publicación de datos por persona
  def publica(self):
    self.ecuacion()
    self.datos()
    if self.inpt.value() != self.estado_anterior:  #entrada ON
        self.con = 0
    else:                          #entrada OFF
        if self.T != 0:                    #si flujo >0
            self.con = self.con +1
            if self.con == self.seg*10:               #si contador = 10
                print("Publicando datos del sensor ",self.label[-1])
                publish_thingsboard(token,unique_id,self.data,'telemetry')
                self.contador = 0
                self.con = 0
    print('sensor ',self.label[-1],' /conteo= ',self.con,' /estado= ',self.inpt.value(),' /consumo= ',self.T)
    self.estado_anterior = self.inpt.value()

#Metodo para publicar la constante del sensor, lo intenta 10 veces
  def atributo(self):
    self.constant  = {self.label[-1]: 0}
    self.constant[self.label[-1]] = self.k 
    while self.contat == 0:
      try:
        publish_thingsboard(token,unique_id,self.constant,'attributes')
        print("Constante Sensor ",self.label[-1])
        self.contat = 1
      except Exception as inst:
        print(inst)
        do_connect(red,clave);
        self.contboot += 1
        print("Fail {}".format(self.contboot))
        if self.contboot > 10: 
          machine.reset()
        time.sleep(1)
      time.sleep(1)
#-------------------------------------------------------------------------#

