![]( https://github.com/GonzaloGaona/sensor_flujo_calor/blob/main/Imagenes/logo_IER_UNAM.png)

## Universidad Nacional Autónoma de México.
### Instituto de Energías Renovables.
### Manual de operación.
## Dispositivo medidor de flujo de calor.

------------

#### Tabla de contenido

1. Resumen ...................................................................................................................................... 3
2. Sensor de flujo de calor ................................................................................................................ 3
3. Descripción general del Hardware .............................................................................................. 4
4. Objetivo general del dispositivo .............................................................................................. 4
5. Conexión del circuito de amplificación ......................................................................................... 5
6. Comunicación serial para el proyecto con PSoC 5LS .................................................................... 6
7. ¿Cómo cargar firmware y códigos en Linux?..................................................................................7

------------

**1. Resumen**

En el Instituto de Energías Renovables de la UNAM en Temixco Morelos, se tiene planeado construir un edificio sustentable, por lo que hay variables que tendrán que ser medidas y ser compatibles con el medio ambiente, para esto se tiene contemplado la construcción de dispositivos electrónicos que ayuden a medir dichas variables como: agua, consumo eléctrico, flujo de calor, luminosidad de espacios, nivel sonoro entre otras, con la intención de poder manipular los datos para posteriormente tener control sobre ellas y lograr el confort de los usuarios.
Cabe mencionar que un edificio sustentable debe cumplir con ciertas normas para que pueda ser considerado como sustentable, es por eso la necesidad de controlar dichas variables.

**2. Sensor de flujo de calor**

Los sensores de flujo de calor termopilas de temperatura diferencial. Operan creando una diferencia de temperatura relativamente pequeña a través de una capa de resistencia térmica (TRL) que es el material del núcleo del sensor de flujo de calor. Usando la ley de Fourier de conducción de calor con un supuesto de transferencia de calor unidimensional en condiciones de estado estacionario, la diferencia de temperatura a través del TRL es proporcional al flujo de calor.
Este sensor se conecta a dos cables; rojo y negro, es decir, corriente y tierra, respectivamente.


![]( https://github.com/GonzaloGaona/sensor_flujo_calor/blob/main/Imagenes/sensor_calor.png)

*Pág. 3*

------------

**3. Descripción general del hardware**

El dispositivo lee el voltaje, lo amplifica y lo convierte a unidades de flujo de calor y posteriormente envía información a Thingsboard para visualizar los datos de manera gráfica en tiempo real.

**4. Objetivo general del dispositivo**

Este dispositivo se elaboró con la intención de medir el flujo de calor existente en muros para tener control sobre esta variable.

*Pág. 4*

------------

**5. Conexión del circuito de amplificación **

Como se muestra en el siguiente diagrama, el sensor de flujo de calor va conectado 2 y 3 del primer AD620, siendo pin 3 el que va al cable de corriente (rojo) y el cable blanco a tierra. Posteriormente, se conectan los AD620 y el LM741 a la fuente de alimentación que en los tres corresponden a los pines 7 para la parte positiva y 4 para la parte negativa. También, en la última etapa, R6(1) se alimenta con -1.65, esto se puede realizar con un divisor de voltaje. Finalmente, se conecta al ESP32 en los pines 32 y GND para leer los valores.
Nota: Se recomienda realizar las conexiones antes de alimentar el circuito.

![](https://github.com/GonzaloGaona/sensor_flujo_calor/blob/main/Diagramas/diagrama_circuito_amplificacion.png)

*Pág. 5*

------------

**6. Comunicación serial para el proyecto con PSoC 5LS **

Teniendo el PSoC 5LS ya programado, se conecta a una fuente independiente de 5V y posteriormente se realizan las conexiones como se muestra en el diagrama. Las tierras de ambos dispositivos se conectan a un pin común, es decir, GND con GND. Seguido de eso, se conecta RX2 del ESP32 con TX del PSoC 5LS y TX2 del ESP32 con RX del PSoC 5LS.
Se carga el programa con la función “put (nombre del programa)” y se corre con la función “repl”, se da un “enter” y se presiona las teclas “Ctrl+D”.

![](https://github.com/GonzaloGaona/sensor_flujo_calor/blob/main/Diagramas/serial.jpg)

*Pág. 6*

------------

**7. ¿Cómo cargar firmware y códigos en Linux? **

El primer paso es abrir la terminal. Se debe actualizar los paquetes con el comando “sudo apt update”, seguido de esto se instala el programa “PIP3” con “sudo apt install python3-pip” el programa pedirá la contraseña del usuario, posteriormente, se instala el programa “ESPTOOL” con el comando “sudo pip3 install esptool”. Una vez instalado el ESPTOOL, se instala el programa “MPFSHELL” con “sudo pip3 install mpfshell”.
Para más información, visitar los siguientes links:
https://github.com/espressif/esptool
https://github.com/wendlers/mpfshell

Una vez instalados, los anteriores programas se tiene que instalar el firmware.
Para instalar el firmware, primero se debe de borrar la memoria flash con la instrucción “esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash” y luego, se carga el firmware buscando en el siguiente link “https://micropython.org/download/esp32/”. Se debe de descargar alguno que no diga “unstable” ya que podría traer problemas.

Se procede a cargar los programas.
Limpiamos la terminal y escribimos “ls” para enlistar las carpetas, se selecciona la carpeta deseada con “cd” y el nombre de la carpeta. Una vez estando en la carpeta, se escribe “mpfshell”. Se conecta el ESP32 en algún puerto USB y se escribe “open ttyUSB0” y se escribe “put NOMBRE DEL PROGRAMA”. Finalmente, se presionan las teclas “Ctrl+D”.
 

*Pág. 7*

-----------

