import smbus

###################### GY-30 BH1750 Sensor de iluminacion
DEVICE     = 0x23 # Dirección por defecto del sensor en el I2C, sensor BH1750.
POWER_DOWN = 0x00 # Sin estado activo
POWER_ON   = 0x01 # Encendido
RESET      = 0x07 # Restablecer el valor del registro de datos

# Comenzar la medición en resolución 4lx. Tiempo típicamente 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13
# Iniciar la medición a 1lx de resolución. Tiempo típicamente 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
# Comience la medición a una resolución de 0.5lx. Tiempo típicamente 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
# Iniciar la medición a 1lx de resolución. Tiempo típicamente 120ms
# El dispositivo se configura automáticamente en Apagado después de la medición.
ONE_TIME_HIGH_RES_MODE_1 = 0x20
# Comience la medición a una resolución de 0.5lx. Tiempo típicamente 120ms
# El dispositivo se configura automáticamente en Apagado después de la medición.
ONE_TIME_HIGH_RES_MODE_2 = 0x21
# Iniciar la medición a 1lx de resolución. Tiempo típicamente 120ms
# El dispositivo se configura automáticamente en Apagado después de la medición.
ONE_TIME_LOW_RES_MODE = 0x23

bus = smbus.SMBus(1)  # Rev 1 Pi utiliza 1 para verificar los sensores en el bus 
###################### Fin

###################### Funcion del sensor GY-30 BH1750
def readLight(addr=DEVICE):                                     # Función perteneciente a BH1750. 
    # Leer datos de la interfaz I2C
    data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
    light =(data[1] + (256 * data[0])) / 1.2
    return(light)
###################### Fin