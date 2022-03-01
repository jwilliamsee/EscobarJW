################### Librerias
import busio
import board
import numpy as np
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
################### Fin

################### ADS1115 lectura para sensor de sonido
    # Crear el bus I2C
i2c = busio.I2C(board.SCL, board.SDA)

    # Crear el objeto ADS usando el bus I2C
ads = ADS.ADS1115(i2c)
ads.gain = 1
chan = AnalogIn(ads, ADS.P0)
################### Fin

while True:
    value = ((chan.value * 32768) / 1023) * 0.000001250039
    if value <= 0:
        value = 0.000020
    dB = (np.log10(value/0.000020)) * 20

    print('Nivel sonoro: {0}'.format(dB) + ' dB')
    time.sleep(10)