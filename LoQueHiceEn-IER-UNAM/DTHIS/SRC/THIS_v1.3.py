######################### Importar librerías
import time
import busio
import board
import numpy as np
import SDL_Pi_HDC1000
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import gy30_bh1750
import paho.mqtt.client as mqtt
import json
from datetime import datetime
import cv2
import camarapi_THIS as camera
######################### Fin

######################### Configuración sensor temperatura y humedad
hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000()
######################### Fin

######################### Configuracíon para sensor de sonido
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 1
chan = AnalogIn(ads, ADS.P0)

def readSPL():
    value = ((chan.value * 32768) / 1023) * 0.000001250039
    if value <= 0:
        value = 0.000020
    spl_dB = (np.log10(value/0.000020)) * 20
    return spl_dB
######################### Fin

######################### Thingsboard
THINGSBOARD_HOST = 'iot.ier.unam.mx'
UNIQUE_ID = 'a5194240-081a-11eb-9c3f-d1ead9980bc3'
ACCESS_TOKEN = 'JpaErOQ6qDid8JXZW1Lu'

sensor_data = {'Humedad Relativa': 0, 'Temperatura': 0, 'Iluminacion': 0, 'Promedio Pixeles': 0, 'Nivel Sonoro': 0} #Debe poseer el mismo texto que "sensor_data" para poderse sobre escribir el valor 
client = mqtt.Client(UNIQUE_ID, False)
client.username_pw_set(ACCESS_TOKEN, password=None)

######################### Tiempo entre mediciones
INTERVAL = 300 #Intervalo entre mediciones en segundos
next_reading = time.time() #Tiempo al iniciar

client.connect(THINGSBOARD_HOST, 1883, 60, "")
client.loop_start()
try:
    while True:
        TL = hdc1000.readTemperature()       # Lectura temperatura
        HL = hdc1000.readHumidity()          # Lectura humedad
        lightLevel = gy30_bh1750.readLight() # Lectura iluminación
        dB = readSPL()                       # Lectura sonido
        
        ######################### Camara Pi
        nombre_foto = 'foto.png'
        
        camera.captura_foto(nombre_foto) # Captura foto
        imagen = cv2.imread(nombre_foto)
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('foto_grises.png',gris)
        alto = gris.shape[0]
        ancho = gris.shape[1]
        
        avg1 = camera.prom_pixeles(gris,alto,ancho)       # Promedio de pixeles único
        
        cuadrantes = 16
        avg_cuadrantes = camera.cuadrantes_pix(gris,cuadrantes,alto,ancho) # Promedio por cuadrantes
        ######################### Fin
        
        ###### Escribir la fecha
        fecha = datetime.now()
        formato = fecha.strftime('Hora: %H:%M:%S Fecha: %d/%m/%Y, ')
        print(formato)
        ###### Fin
        
        ######################### Escribir lecturas
        print()
        print("Temperatura        : " + format(TL, '.4f') + " °C")
        print("Humedad Relativa   : " + format(HL, '.4f') + " %")
        print("Nivel de Luz       : " + format(lightLevel,'.4f')       + " lx")
        print("Nivel sonoro       : " + format(dB, '.4f')         + ' dB')
        print()
        print("Promedio de pixeles único: " + format(avg1,'.4f'))
        print("Por cuadrantes: ")
        camera.escribe_matriz(cuadrantes,avg_cuadrantes)
        print()
        print()
        ######################### Fin
        
        ######################### Publicar en Thingsboard
        sensor_data['Temperatura']      = TL
        sensor_data['Humedad Relativa'] = HL
        sensor_data['Iluminacion']      = lightLevel
        sensor_data['Promedio Pixeles'] = avg1
        sensor_data['Nivel Sonoro']     = dB
        time.sleep(1)
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data))
        time.sleep(1)
        ######################### Fin
        
        next_reading += INTERVAL #Siguiente medición
        sleep_time = next_reading - time.time() #Tiempo restante para la siguiente medición
        if sleep_time > 0:
            time.sleep(sleep_time) #Tiempo de espera para la siguiente medición
            
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()