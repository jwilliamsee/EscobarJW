print("Hola, este es el programa de medición de consumo de agua")
print("Este prototipo cuenta con 8 sensores que pueden ser ultilizados")




# un sensor	
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
	Sensor1 = Conteo(pin=5,seg=seg,k=0.003125,label='Litros 1') 

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
	
	

# dos sensores

	print("Se han habilitado 2 sensores")
	print("Pines empleados: sensor1------pin 5"
	                       "sensor2------pin 4")
	
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
	Sensor1 = Conteo(pin=5,seg=seg,k=0.003125,label='Litros 1') 
	
	#Declaración del sensor2
	Sensor2 = Conteo(pin=4,seg=seg,k=0.003125,label='Litros 2') 

	#Metodo que publica la constante del sensor
	Sensor1.atributo() 
	Sensor2.atributo()  
 
	#-------------------------Loop infinito----------------------------------
	while True:
	  
	  try:
   
	#publicación de datos en thingsboard
	    Sensor1.publica()
	    Sensor2.publica()
	    
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
	    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
	      machine.reset()
	    time.sleep(1)
	  time.sleep(0.1)
		


# tres sensores

	print("hola 3")
	print("Se han habilitado 3 sensores")
	print("Pines empleados: sensor1------pin 5"
	                       "sensor2------pin 4"
	                       "sensor3------pin 0")
	
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
	Sensor1 = Conteo(pin=5,seg=seg,k=0.003125,label='Litros 1') 
	
	#Declaración del sensor2
	Sensor2 = Conteo(pin=4,seg=seg,k=0.003125,label='Litros 2') 

	#Declaración del sensor3
	Sensor3 = Conteo(pin=2,seg=seg,k=0.003125,label='Litros 3')

	#Metodo que publica la constante del sensor
	Sensor1.atributo() 
	Sensor2.atributo()  
	Sensor3.atributo()  
 
	#-------------------------Loop infinito----------------------------------
	while True:
	  
	  try:
   
	#publicación de datos en thingsboard
	    Sensor1.publica()
	    Sensor2.publica()
	    Sensor3.publica()
	    
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
	    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
	      machine.reset()
	    time.sleep(1)
	  time.sleep(0.1)





# cuatro sensores
	print("hola 4")
	print("Se han habilitado 4 sensores")
	print("Pines empleados: sensor1------pin 5"
	                       "sensor2------pin 4"
	                       "sensor3------pin 0"
	                       "sensor4------pin 2")
	
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
	Sensor1 = Conteo(pin=5,seg=seg,k=0.003125,label='Litros 1') 
	
	#Declaración del sensor2
	Sensor2 = Conteo(pin=4,seg=seg,k=0.003125,label='Litros 2') 

	#Declaración del sensor3
	Sensor3 = Conteo(pin=0,seg=seg,k=0.003125,label='Litros 3')

	#Declaración del sensor4
	Sensor4 = Conteo(pin=2,seg=seg,k=0.003125,label='Litros 4')

	#Metodo que publica la constante del sensor
	Sensor1.atributo() 
	Sensor2.atributo()  
	Sensor3.atributo()
	Sensor4.atributo()  
 
	#-------------------------Loop infinito----------------------------------
	while True:
	  
	  try:
   
	#publicación de datos en thingsboard
	    Sensor1.publica()
	    Sensor2.publica()
	    Sensor3.publica()
	    Sensor4.publica()
	    
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
	    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
	      machine.reset()
	    time.sleep(1)
	  time.sleep(0.1)




# cinco sensores 

	print("hola 5")
	
	print("Se han habilitado 5 sensores")
	print("Pines empleados: sensor1------pin  5"
	                       "sensor2------pin  4"
	                       "sensor3------pin  0"
	                       "sensor4------pin  2"
	                       "sensor5------pin 14")
	
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
	Sensor1 = Conteo(pin=5,seg=seg,k=0.003125,label='Litros 1') 
	
	#Declaración del sensor2
	Sensor2 = Conteo(pin=4,seg=seg,k=0.003125,label='Litros 2') 

	#Declaración del sensor3
	Sensor3 = Conteo(pin=0,seg=seg,k=0.003125,label='Litros 3')
	
	#Declaración del sensor4
	Sensor4 = Conteo(pin=2,seg=seg,k=0.003125,label='Litros 4') 

	#Declaración del sensor5
	Sensor5 = Conteo(pin=14,seg=seg,k=0.003125,label='Litros 5')

	#Metodo que publica la constante del sensor
	Sensor1.atributo() 
	Sensor2.atributo()  
	Sensor3.atributo()
	Sensor4.atributo()  
	Sensor5.atributo()  
 
	#-------------------------Loop infinito----------------------------------
	while True:
	  
	  try:
   
	#publicación de datos en thingsboard
	    Sensor1.publica()
	    Sensor2.publica()
	    Sensor3.publica()
	    Sensor4.publica()
	    Sensor5.publica()
	    
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
	        Sensor5.contador = Sensor5.contador
	    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
	      machine.reset()
	    time.sleep(1)
	  time.sleep(0.1)




# seis sensores 

	print("hola 6")
	print("Se han habilitado 6 sensores")
	print("Pines empleados: sensor1------pin  5"
	                       "sensor2------pin  4"
	                       "sensor3------pin  0"
	                       "sensor4------pin  2"
	                       "sensor5------pin 14"
	                       "sensor6------pin 12")
	
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
	Sensor1 = Conteo(pin=5,seg=seg,k=0.003125,label='Litros 1') 
	
	#Declaración del sensor2
	Sensor2 = Conteo(pin=4,seg=seg,k=0.003125,label='Litros 2') 

	#Declaración del sensor3
	Sensor3 = Conteo(pin=0,seg=seg,k=0.003125,label='Litros 3')
	
	#Declaración del sensor4
	Sensor4 = Conteo(pin=2,seg=seg,k=0.003125,label='Litros 4') 
	
	#Declaración del sensor5
	Sensor5 = Conteo(pin=14,seg=seg,k=0.003125,label='Litros 5') 

	#Declaración del sensor6
	Sensor6 = Conteo(pin=12,seg=seg,k=0.003125,label='Litros 6')

	#Metodo que publica la constante del sensor
	Sensor1.atributo() 
	Sensor2.atributo()  
	Sensor3.atributo()  
	Sensor4.atributo() 
	Sensor5.atributo()  
	Sensor6.atributo()  
 
	#-------------------------Loop infinito----------------------------------
	while True:
	  
	  try:
   
	#publicación de datos en thingsboard
	    Sensor1.publica()
	    Sensor2.publica()
	    Sensor3.publica()
	    Sensor4.publica()
	    Sensor5.publica()
	    Sensor6.publica()
	    
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
	        Sensor5.contador = Sensor5.contador
	        Sensor6.contador = Sensor6.contador
	    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
	      machine.reset()
	    time.sleep(1)
	  time.sleep(0.1)




# siete sensores 

	print("hola 7")
	print("Se han habilitado 7 sensores")
	print("Pines empleados: sensor1------pin 5"
	                       "sensor2------pin 4"
	                       "sensor3------pin  0"
	                       "sensor4------pin  2"
	                       "sensor5------pin 14"
	                       "sensor6------pin 12"
	                       "sensor7------pin 13")
	
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
	Sensor1 = Conteo(pin=5,seg=seg,k=0.003125,label='Litros 1') 
	
	#Declaración del sensor2
	Sensor2 = Conteo(pin=4,seg=seg,k=0.003125,label='Litros 2') 

	#Declaración del sensor3
	Sensor3 = Conteo(pin=0,seg=seg,k=0.003125,label='Litros 3')
	#Declaración del sensor4
	Sensor4 = Conteo(pin=2,seg=seg,k=0.003125,label='Litros 4') 
	
	#Declaración del sensor5
	Sensor5 = Conteo(pin=14,seg=seg,k=0.003125,label='Litros 5') 

	#Declaración del sensor6
	Sensor6 = Conteo(pin=12,seg=seg,k=0.003125,label='Litros 6')
	
	#Declaración del sensor7
	Sensor7 = Conteo(pin=13,seg=seg,k=0.003125,label='Litros 7')


	#Metodo que publica la constante del sensor
	Sensor1.atributo() 
	Sensor2.atributo()  
	Sensor3.atributo()  
	Sensor4.atributo() 
	Sensor5.atributo()  
	Sensor6.atributo()
	Sensor7.atributo()
 
	#-------------------------Loop infinito----------------------------------
	while True:
	  
	  try:
   
	#publicación de datos en thingsboard
	    Sensor1.publica()
	    Sensor2.publica()
	    Sensor3.publica()
	    Sensor4.publica()
	    Sensor5.publica()
	    Sensor6.publica()
	    Sensor7.publica()
	    
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
	        Sensor5.contador = Sensor5.contador
	        Sensor6.contador = Sensor6.contador
	        Sensor7.contador = Sensor7.contador
	        
	    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
	      machine.reset()
	    time.sleep(1)
	  time.sleep(0.1)





# ocho sensores

	print("hola 8")
	print("Se han habilitado 8 sensores")
	print("Pines empleados: sensor1------pin 5"
	                       "sensor2------pin 4"
	                       "sensor3------pin  0"
	                       "sensor4------pin  2"
	                       "sensor5------pin 14"
	                       "sensor6------pin 12"
	                       "sensor7------pin 13"
	                       "sensor8------pin  3")
	
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
	Sensor1 = Conteo(pin=5,seg=seg,k=0.003125,label='Litros 1') 
	
	#Declaración del sensor2
	Sensor2 = Conteo(pin=4,seg=seg,k=0.003125,label='Litros 2') 

	#Declaración del sensor3
	Sensor3 = Conteo(pin=0,seg=seg,k=0.003125,label='Litros 3')
	
	#Declaración del sensor4
	Sensor4 = Conteo(pin=2,seg=seg,k=0.003125,label='Litros 4') 
	
	#Declaración del sensor5
	Sensor5 = Conteo(pin=14,seg=seg,k=0.003125,label='Litros 5') 

	#Declaración del sensor6
	Sensor6 = Conteo(pin=12,seg=seg,k=0.003125,label='Litros 6')

	#Declaración del sensor7
	Sensor7 = Conteo(pin=13,seg=seg,k=0.003125,label='Litros 7') 

	#Declaración del sensor8
	Sensor8 = Conteo(pin=3,seg=seg,k=0.003125,label='Litros 8')

	#Metodo que publica la constante del sensor
	Sensor1.atributo() 
	Sensor2.atributo()  
	Sensor3.atributo()  
	Sensor4.atributo() 
	Sensor5.atributo()  
	Sensor6.atributo()
	Sensor7.atributo()  
	Sensor8.atributo()
 
	#-------------------------Loop infinito----------------------------------
	while True:
	  
	  try:
   
	#publicación de datos en thingsboard
	    Sensor1.publica()
	    Sensor2.publica()
	    Sensor3.publica()
	    Sensor4.publica()
	    Sensor5.publica()
	    Sensor6.publica()
	    Sensor7.publica()
	    Sensor8.publica()
	    
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
	        Sensor5.contador = Sensor5.contador
	        Sensor6.contador = Sensor6.contador
	        Sensor7.contador = Sensor7.contador
	        Sensor8.contador = Sensor8.contador
	    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
	      machine.reset()
	    time.sleep(1)
	  
	 time.sleep(0.1)


else:
	print("Acción no válida")

