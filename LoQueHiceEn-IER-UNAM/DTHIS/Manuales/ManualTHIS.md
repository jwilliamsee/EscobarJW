# Universidad Nacional Autónoma de México

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/logo-unam-4.png?raw=true)

# Instituto de Energías Renovables

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/unam-ier-logo.png?raw=true)

# Manual de uso
# Dispositivo THIS

# Oliver Stif Galvez Oliveros

# Asesor:
# Dr. Guillermo Barrios del Valle

## Temixco, Morelos Febrero 2021


------------



##### Índice
	Resumen ----------------------------------------------------------------------2
	Introducción -----------------------------------------------------------------3
	Sensores de Temperatura ------------------------------------------------------3
	Sensores de Humedad Relativa -------------------------------------------------3
	Sensores de Intensidad Luminosa ----------------------------------------------4
	Sensores de Presión Sonora ---------------------------------------------------4
	Métodos empleados para medir iluminación -------------------------------------4
	Reconocimiento de las condiciones de iluminación -----------------------------6
	Ubicación de los puntos de medición ------------------------------------------8
	Descripción general de hardware ---------------------------------------------10
	Propósito general del dispositivo -------------------------------------------10
	Esquema general del dispositivo y principio de funcionamiento ---------------10
	Descripción a detalle de cada sección que conforma al dispositivo THIS ------12
	Raspberry Pi 3 modelo B+ ----------------------------------------------------12
	Módulo CJMCU-8128 -----------------------------------------------------------13
	Módulo GY-30 ----------------------------------------------------------------14
	Micrófono (Microphone Audio & Sound Pressure) -------------------------------15
	Conversor analógico - digital ADS1115 ---------------------------------------16
	Módulo Raspberry Pi camera V2 -----------------------------------------------16
	Requerimientos necesarios para utilizar el dispositivo ----------------------17
	Descripción general del software --------------------------------------------18
	Diagrama de flujo del software en general -----------------------------------18
	Instalación de librerías ----------------------------------------------------19
	Bus I2C ---------------------------------------------------------------------19
	Requerimientos necesarios para ejecutar la programación del THIS ------------21
	REFERENCIAS -----------------------------------------------------------------22
	ANEXOS ----------------------------------------------------------------------23

### Resumen

##### El Instituto de Energías Renovables que forma parte de la UNAM se encuentra construyendo un edificio sustentable ubicado en la comunidad de Temixco, Morelos. Es necesario conocer valores de las distintas variables que permiten considerar al edificio amigable con el medio ambiente, de esta manera se podrá evaluar que la eficiencia y el cumplimiento de las normas establecidas para un edificio sustentable.

##### En este documento se describe el prototipo realizado para la medición de distintas variables como iluminación, presión sonora, temperatura y humedad relativa. Se da a conocer información relevante relacionada a la construcción del hardware y la programación del dispositivo, empleando para este propósito el uso de diagramas de flujo e imágenes representativas que brindan una visión completa del prototipo.

##### El contenido de este manual está dividido en dos secciones, hardware y software, estas abarcan toda información necesaria para construir y utilizar el dispositivo. En la sección de Hardware se observa el método de conexión de los sensores, características técnicas y una pequeña descripción del dispositivo, por otra parte, en la sección del Software se encuentran los programas para cada uno de los sensores empleados, explicado su modo de operación y los requisitos necesarios para su correcto uso. Al final del documento se encuentra la bibliografía y anexos necesarios para la comprensión del presente trabajo.

### 1. Introducción

##### En un edificio es importante mantener condiciones agradables, es decir, que los habitantes o los usuarios se sientan en confort, es decir, bienestar físico que proporcionan determinadas condiciones ambientales. Monitoreando las variables de confort adecuadas se puede determinar las condiciones favorables para un lugar de trabajo en particular.

###### 2
------------

##### En este proyecto se espera establecer los requerimientos de iluminación, temperatura, ruido y humedad en las áreas de los centros de trabajo, para que se cuente con la cantidad requerida para cada actividad a fin de proveer un ambiente seguro y saludable en la realización de las tareas que desarrollen los habitantes. El dispositivo empleado que se pretende construir para medir variables de confort y así evaluar las condiciones dentro del lugar de trabajo en un edificio sustentable, consiste en un controlador monitoreando variables en tiempo de real de sensores, siendo extraídos dichos valores hacia una base de datos para su proceso.

#### 1. 1. Sensores de Temperatura

##### Los sensores de temperatura son dispositivos que transforman los cambios de temperatura en cambios en señales eléctricas que son procesados por equipo eléctrico o electrónico, algunos de los sensores de temperatura pueden ser: Termopares, RDT, Termistores, Infrarrojo. El sensor de temperatura, típicamente suele estar formado por el elemento sensor, de cualquiera de los tipos anteriores, el recubrimiento que lo envuelve y que está rellena de un material muy conductor de la temperatura, para que los cambios se transmitan rápidamente al elemento sensor y del cable al que se conectarán el equipo electrónico. (Corona, 2014).

#### 1. 2. Sensores de Humedad Relativa

##### Humedad relativa, o HR, mide la cantidad de agua en el aire en forma de vapor, comparándolo con la cantidad máxima de agua que puede ser mantenida a una temperatura dada, el sensor de humedad relativa es un componente que manda un valor de humedad relativa en porcentaje. El sensor está hecho de una película generalmente de vidrio o de cerámica. El material aislante que absorbe el agua está hecho de un polímero que toma y libera el agua basándose en la humedad relativa de la zona dada, podemos encontrar sensores de humedad relativa capacitivos, resistivos y térmicos. (Bentley, 1998).

###### 3
------------

#### 1. 3. Sensores de Intensidad Luminosa 

##### La iluminancia es la cantidad de flujo luminoso que incide sobre una superficie por unidad de área, los sensores de intensidad luminosa nos muestran el resultado en lúmenes por metro cuadrado, es decir, Lux = lumen/m 2. El sensor funciona cuando la luz llega al sensor en el que la energía de los fotones se convierte en carga eléctrica, cuanta más luz incida sobre la superficie, más carga se construye. En términos generales, los dos están correlacionados. Una calibración en la medición electrónica convierte ya sea corriente o tensión a un valor lux algunos ejemplos de sensores de intensidad luminosa son TSL25, Foto-resistivo y bh1750 (Fernández, 2012).

#### 1. 4. Sensores de Presión Sonora 

### Es un dispositivo que actúa en el momento en que la presencia del sonido produce en el aire pequeñas variaciones de presión que se superponen a la presión atmosférica, a las que se llama presión sonora, la presión sonora actúa sobre nuestros oídos y produce la sensación de oír. El sensor mide variaciones de presión medida en decibeles (dB) que representa los sonidos audibles en las personas, tener controlada una variable de este tipo es cuidar el entorno de trabajo para una mejor calidad en el ambiente, algunos sensores que existen son el sensor 017i, Sonómetro, Transductores. (Ortega, 2002).

#### 1. 5. Métodos empleados para medir iluminación 

##### Para la medición de iluminación en un aula de trabajo se utiliza el procedimiento según la NOM 025-STPS-2008, en la siguiente tabla se pueden observar los valores de iluminación a los que se debe encontrar el lugar de trabajo según su uso, cabe aclarar que estos valores están ya establecidos dentro de la norma mencionada.

###### 4
------------


|Tarea visual del puesto de trabajo|Área de trabajo|Niveles mínimos de iluminación (lux)|
| ------------ | ------------ | ------------ |
|En exteriores: distinguir el área de tránsito, desplazarse caminando, vigilancia, movimiento de vehículos|Exteriores generales: patios y estacionamientos.|20|
|En interiores: distinguir el área de tránsito, desplazarse caminando, vigilancia, movimiento de vehículos|Interiores generales: almacenes de poco movimiento, pasillos, escaleras, estacionamientos cubiertos, labores en minas subterráneas, iluminación de emergencia|50|
|En interiores.|Áreas de circulación y pasillos; salas de espera; salas de descanso; cuartos de almacén; plataformas; cuartos de calderas|100|
|Requerimiento visual simple: inspección visual, recuento de piezas, trabajo en banco y máquina.|Servicios al personal: almacenaje rudo, recepción y despacho, casetas de vigilancia, cuartos de compresores y pailería.|200|
|Distinción moderada de detalles: ensamble simple, trabajo medio en banco y máquina, inspección simple|Talleres: áreas de empaque y ensamble, aulas y oficinas.|300|
|Empaque y trabajos de oficina.|Distinción clara de detalles: maquinado y acabados delicados, ensamble de inspección moderadamente difícil, captura y procesamiento de información, manejo de instrumentos y equipo de laboratorio.||
|Distinción clara de detalles: maquinado y acabados delicados, ensamble de inspección moderadamente difícil, captura y procesamiento de información, manejo de instrumentos y equipo de laboratorio.|Talleres de precisión: salas de cómputo, áreas de dibujo, laboratorios.|500|
|Distinción na de detalles: maquinado de precisión, ensamble e inspección de trabajos delicados, manejo de instrumentos y equipo de precisión, manejo de piezas Talleres de alta precisión: de pintura y acabado de superficies y laboratorios de control de calidad|Talleres de alta precisión: de pintura y acabado de superficies y laboratorios de control de calidad. |750|


###### 5

------------

|Alta exactitud en la distinción de detalles: ensamble, proceso e inspección de piezas pequeñas y complejas, acabado con pulidos nos.|Proceso: mensamble e inspección de piezas complejas y acabados con pulidos finos.|1000|
| ------------ | ------------ | ------------ |
|Alto grado de especialización en la distinción de detalles.|Proceso de gran exactitud. Ejecución de tareas visuales de bajo contraste y tamaño muy pequeño por periodos prolongados; exactas, muy prolongadas, muy especiales de extremadamente bajo contraste y pequeño tamaño|2000|
|**Tabla 2.1. Niveles de iluminación según la NOM 025-STPS-2008**|

##### A continuación, se presentan los requerimientos para una buena medición en las distintas áreas de trabajo.

#### 1. 6. Reconocimiento de las condiciones de iluminación

##### Se debe realizar un recorrido por todas las áreas del centro de trabajo donde los trabajadores realizan sus tareas visuales, y considerar, en su caso, los reportes de los trabajadores, así como recabar la información técnica. Para determinar las áreas y tareas visuales de los puestos de trabajo debe recabarse y registrarse la información del reconocimiento de las condiciones de iluminación de las áreas de trabajo, así como de las áreas donde exista una iluminación deficiente o se presente deslumbramiento y, posteriormente, conforme se modifiquen las características de las luminarias o las condiciones de iluminación del área de trabajo, con los datos siguientes:

	Distribución de las áreas de trabajo, del sistema de iluminación (número y distribución de luminarias), de la maquinaria y del equipo de trabajo.
	Potencia de las lámparas.
	Descripción del área iluminada: colores y tipo de superficies del local o edificio.
	Descripción de las tareas visuales y de las áreas de trabajo, de acuerdo con la Tabla anterior.
	Descripción de los puestos de trabajo que requieren iluminación localizada.
	La información sobre la percepción de las condiciones de iluminación por parte del trabajador al patrón.

###### 6
------------

##### Cuando se utilice iluminación artificial, antes de realizar las mediciones, se debe de cumplir con lo siguiente:

	Encender las lámparas con antelación, permitiendo que el flujo de luz se estabilice; si se utilizan lámparas de descarga, incluyendo lámparas fluorescentes, se debe esperar un periodo de 20 minutos antes de iniciar las lecturas. Cuando las lámparas fluorescentes se encuentren montadas en luminarias cerradas, el periodo de estabilización puede ser mayor.
	En instalaciones nuevas con lámparas de descarga o fluorescentes, se debe esperar un periodo de 100 horas de operación antes de realizar la medición.
	Los sistemas de ventilación deben operar normalmente, debido a que la iluminación de las lámparas de descarga y fluorescentes presentan fluctuaciones por los cambios de temperatura.

##### Cuando se utilice exclusivamente iluminación natural, se debe realizar al menos las mediciones en cada área o puesto de trabajo de acuerdo con lo siguiente:

	Cuando no influye la luz natural en la instalación ni el régimen de trabajo de la instalación,se deberá efectuar una medición en horario indistinto en cada puesto o zona determinada, independientemente de los horarios de trabajo en el sitio.
	Cuando sí influye la luz natural en la instalación, el turno en horario diurno (sin periodo de oscuridad en el turno o turnos) y turnos en horario diurno y nocturnos (con periodo de oscuridad en el turno o turnos), deberán efectuarse 3 mediciones en cada punto o zona 8 determinada distribuidas en un turno de trabajo que pueda presentar las condiciones críticas de iluminación.
	Cuando sí influye la luz natural en la instalación y se presentan condiciones críticas, efectuar una medición en cada punto o zona determinada en el horario que presente tales condiciones críticas de iluminación.

###### 7
------------

#### 1. 7. Ubicación de los puntos de medición

##### Los puntos de medición deben seleccionarse en función de las necesidades y características de cada centro de trabajo, de tal manera que describan el entorno ambiental de la iluminación de una forma confiable, considerando: el proceso de producción, la clasificación de las áreas y puestos de trabajo, el nivel de iluminación requerido en base el Tabla 2.1, la ubicación de las luminarias respecto a los planos de trabajo, el cálculo del índice de áreas correspondiente a cada una de las áreas, la posición de la maquinaria y equipo, así como los riesgos informados a los trabajadores.

##### Las áreas de trabajo se deben dividir en zonas del mismo tamaño, de acuerdo a lo establecido en la columna A (número mínimo de zonas a evaluar) de la Tabla A1, y realizar la medición en el lugar donde haya mayor concentración de trabajadores o en el centro geométrico de cada una de estas zonas; en caso de que los puntos de medición coincidan con los puntos focales de las luminarias, se debe considerar el número de zonas de evaluación de acuerdo a lo establecido en la columna B (número mínimo de zonas a considerar por la limitación) de la Tabla A1. En caso de coincidir nuevamente el centro geométrico de cada zona de evaluación con la ubicación del punto focal de la luminaria, se debe mantener el número de zonas previamente definido.

|Índice de área|A) Número mínimo de zonas a evaluar|B) Número de zonas a considerar por la limitación|
| ------------ | ------------ | ------------ |
|IC < 1 |4|6|
|1 ≤ IC < 2|9|12|
|2 ≤ IC >3|16|20|
|3 ≤ IC|25|30|
|**Tabla 2.2. Tabla A1**|

###### 8
------------

##### El valor del índice de área, para establecer el número de zonas a evaluar, está dado por la ecuación siguiente:

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/EcIC.JPG?raw=true)

##### Donde:
##### IC = índice del área
##### x, y = dimensiones del área (largo y ancho), en metros
##### h = altura de la luminaria respecto al plano de trabajo, en metros
##### En donde x es el valor de índice de área (IA) del lugar, redondeado al entero superior, excepto que para valores iguales o mayores a 3 el valor de x es 4. A partir de la ecuación se obtiene el número mínimo de puntos de medición.

##### En pasillos o escaleras, el plano de trabajo por evaluar debe ser un plano horizontal a 75 cm ± 10 cm, sobre el nivel del piso, realizando mediciones en los puntos medios entre luminarias contiguas.

##### NOTA: En el puesto de trabajo se debe realizar al menos una medición en cada plano de trabajo, colocando el luxómetro tan cerca como sea posible del plano de trabajo y tomando precauciones para no proyectar sombras ni reflejar luz adicional sobre el luxómetro. Se debe verificar el luxómetro antes y después de iniciar una evaluación conforme lo establezca el fabricante y evitar bloquear la iluminación durante la realización de la evaluación.

###### 9
------------

### 2. Descripción general de hardware

##### El dispositivo está conformado por una Raspberry Pi 3 Modelo B+, que coordina la adquisición de datos de los siguientes módulos:

##### 1. Módulo CJMCU-8128 (Temperatura y humedad)
##### 2. Módulo GY-30 (Iluminación)
##### 3. Microphone Sound Input Module (Nivel de Presión Sonora)
##### 4. Cámara Pi V2

##### Además, se utiliza un convertidor analógico - digital ADS1115 para tomar las lecturas del micrófono, debido a que la señal de salida del micrófono es analógica.

#### 2. 1. Propósito general del dispositivo

##### El dispositivo THIS permitirá medir las condiciones de confort térmico, acústico y lumínico dentro de edificaciones, ya que cuenta con sensores que miden la temperatura, humedad relativa, iluminación y presión sonora, estos datos servirán para evaluar el uso eficiente de la energía y en un futuro, poder implementar estrategias para mejorarlo.

#### 2. 2. Esquema general del dispositivo y principio de funcionamiento

##### El dispositivo THIS está diseñado para monitorear las condiciones de confort térmico, lumínico y acústico en interiores, su componente principal es una Raspberry Pi 3 modelo B+, es una computadora del tamaño de una tarjeta de crédito, muy útil porque cuenta con conectividad inalámbrica a internet, ideal para transmitir datos. Además, cuenta con un módulo CJMCU-8128 encargado de medir temperatura y humedad relativa, un módulo GY-30 utilizado para medir la iluminancia, un módulo de micrófono para medir el nivel de presión sonora y para este último es necesario contar con un conversor analógico-digital ADS1115. Todos los componentes deben

###### 10
------------
##### conectarse a la Raspberry mediante el bus I2C y los datos recopilados son enviados a Thingsboard.

##### En la siguiente figura se observa la representación pictórica del dispositivo.

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/figurarepresentativaTHIS.JPG?raw=true)

##### Además, el dispositivo cuenta con la cámara Pi para medir la iluminación en diferentes puntos de la habitación o aula en la cual se encuentre instalado. La cámara se conecta directamente al puerto de cámara en la Raspberry Pi 3.

##### El principio de operación consiste en tomar lecturas de los sensores cada 5 minutos, además de tomar una fotografía y procesarla, los datos son enviados a Thingsboard y también se imprime en consola.

##### Antes de que el dispositivo sea armado, se debe instalar el Raspberry Pi OS y configurar la Raspberry, de preferencia establecer una conexión remota por SSH, en la que se debe trabajar mediante la consola, para mayor facilidad en el manejo se puede establecer una conexión por VNC, de esta forma se puede manejar el dispositivo desde el escritorio de la Raspberry, remotamente.

###### 11
------------

##### El dispositivo debe ser montado, existe un espacio para cada componente en la carcasa, posteriormente debe ser conectado, en los anexos se presenta el diagrama esquemático. Posteriormente, se debe ejecutar el programa principal del dispositivo THIS, manteniendo siempre los programas librerías en la misma carpeta que el programa principal. El programa principal no podrá ser ejecutado si no se instalan las librerías correspondientes.

#### 2. 3. Descripción a detalle de cada sección que conforma al dispositivo THIS

##### 2. 3. 1. Raspberry Pi 3 modelo B+

##### La Raspberry Pi 3 Modelo B+ es la tercera generación de Raspberry Pi. Esta computadora del tamaño de una tarjeta de crédito se puede usar para muchas aplicaciones, posee un procesador 10 veces más rápido que la primera generación de Raspberry Pi. Además, agrega conectividad LAN inalámbrica y Bluetooth por lo que es la solución ideal para diseños en donde se requiera transferencia de datos inalámbricos.

##### Especificaciones:

● CPU Quadcom 1.2MHz Broadcom BCM2837 64bit
● 1GB de RAM
● BCM43438 LAN inalámbrica y Bluetooth de baja energía (BLE) a bordo
● 100 Base Ethernet
● GPIO extendido de 40 pines
● 4 puertos USB 2.0
● Salida estéreo de 4 polos y puerto de video compuesto
● HDMI de tamaño completo
● Puerto de cámara CSI para conectar una cámara Raspberry Pi

###### 12
------------

● Puerto de pantalla DSI para conectar una pantalla táctil Raspberry Pi 25
● Puerto Micro SD para cargar su sistema operativo y almacenar datos
● Entrada de alimentación Micro USB 5V/2.5A DC

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/Raspberry%20Pi%20Model%203.JPG?raw=true)

##### 2. 3. 2. Módulo CJMCU-8128

##### El CJMCU-8128 es una pequeña placa de conexión disponible en Banggood.com o Aliexpress. Viene con 3 sensores principales a bordo que incluyen:

● BMP280 - Presión y temperatura
● HDC10XX - Humedad y temperatura
● CCS811 - Indice de C02 y Compuestos Orgánicos Volátiles (VOC)todos los sensores a través de ese protocolo simplemente conectando los pines SDA, SCL, VCC y GND en el sensor.
● La placa de conexión se comunica mediante I2C

###### 13
------------

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/CJMCU.JPG?raw=true)

##### 2. 3. 3. Módulo GY-30

##### Contiene el sensor BH1750FVI, un sensor digital de iluminación ambiente con interfaz I2C. Es posible la detección en alta resolución de 1 a 65535 lx. Gracias a su construcción el sensor no es afectado por radiación infrarroja, temperatura o los diversos colores de iluminación y funciona tanto para luz natural como artificial. Es posible seleccionar 2 tipos de comunicación por I2C esclavo. Este tipo de sensor es usado para aplicaciones con teléfonos celulares, pantallas LCD, computadoras portátiles, cámaras digitales, cámaras de video digital, PDA, entre otros.

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/GY30.JPG?raw=true)

###### 14
------------

##### 2. 3. 4. Micrófono (Microphone Audio & Sound Pressure)

##### Un amplificador de señal dual integrado, convierte el sonido en canales separados para la medición de pulso / frecuencia y el nivel de volumen (presión) del sonido. Diseñado para conectarse directamente a un microcontrolador compatible con Arduino, convertidor analógico a digital o muchos otros circuitos. Las dos salidas proporcionan acceso independiente a la forma de onda de la señal sin procesar (la salida MIC) o al nivel de presión de sonido (la salida SPL) para proporcionar la máxima flexibilidad en sus proyectos. Si desea procesar la forma de onda de audio directamente, puede usar la salida MIC, o si solo desea detectar el nivel de sonido (por ejemplo, para detectar ruido por encima de cierto umbral) puede usar la salida SPL. (Freetronics, 2020).

● Micrófono omnidireccional
● Respuesta de frecuencia de 60 Hz a 15 kHz
● Sensibilidad -40dB típica
● Dimensiones: 23 (W) x 16 (H) x 8 (D) mm

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/Microphone.JPG?raw=true)

###### 15
------------

##### 2. 3. 5. Conversor analógico - digital ADS1115

##### El ADS1115 cuenta con 4 canales y es perfecta para agregar conversion analógica a digital de alta resolución a cualquier proyecto basado en microcontrolador. Puede funcionar con señales entre 2 y 5 v. Puede ser controlada mediante I2C haciendo muy fácil su conexión ya que solo se utilizan 2 cables. Se incluye un amplificador programable que proporciona una ganancia de hasta x16 para señales pequeñas.

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/ADS.JPG?raw=true)

##### 2. 3. 6. Módulo Raspberry Pi camera V2

##### El módulo de cámara V2 tiene un sensor Sony IMX219 de 8 megapíxeles. Se puede utilizar para tomar videos de alta definición, así como fotografías fijas. Es fácil de usar para principiantes, pero tiene mucho que ofrecer a usuarios avanzados. Funciona con los modelos de Raspberry Pi 1, 2, 3 y 4. Se puede acceder a ella a través de las API MMAL y V4L, existen numerosas librerías de terceros creadas para ella, incluida la librería Picamera Python.

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/camera.JPG?raw=true)

###### 16
------------

##### 2. 4. Requerimientos necesarios para utilizar el dispositivo

###### 1. El dispositivo debe tener una fuente de alimentación no menor a 5V/2.5A

###### 2. Antes de ser programado debe de verificar que estén instaladas todas las librerías

###### 3. Siempre verificar que la comunicación I2C esté activa en la raspberry 4. No encender la raspberry si no se encuentra en su carcasa para evitar fallos

###### 5. Nunca apagar la Raspberry Pi 3 desconectando la alimentación.

###### 17
------------



### 3. Descripción general del software

##### El software programado funciona por medio de la creación de funciones, cada una contiene la programación para adquirir valores de su respectivo sensor y otras acciones necesarias, estas se mandan a llamar una a una para la extracción de datos.

#### 3. 1. Diagrama de flujo del software en general 

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/DiagramaDeFlujo.JPG?raw=true)

###### 18
------------

#### 3. 2. Instalación de librerías

##### Antes de iniciar con la instalación de las librerías, es necesario asegurar que todos los paquetes de la Raspberry Pi 3 están actualizados, para ello se usan los comandos sudo apt-get update y  sudo apt-get upgrade en la terminal. Una vez actualizados los paquetes, se puede proceder con la instalación de las librerías.

#### 3. 2. 1. Protocolo I2C

##### El primer paso será activar la conexión por I2C en la Raspberry Pi 3. Se deben seguir los siguientes pasos:

##### 1. Acceder a la herramienta de configuración, ejecutar el comando *sudo raspi-config*

##### 2. Seleccionar *Interfacing Options*

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/config1.JPG?raw=true)

##### 3. Seleccionar la opción *P5*


![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/config2.JPG?raw=true)

##### 4. Confirmar la habilitación de la interfaz

##### 5. Reiniciar el sistema de la Raspberry Pi

###### 19
------------

#### 3. 2. 2. Remote GPIO

##### Para activar el acceso remoto a los pines GPIO de la Raspberry es necesario seguir los pasos mencionados para el protocolo I2C, con la diferencia de que en el paso 3 se debe seleccionar la opción P8.

#### 3. 2. 3. Librerías CircuitPython (board y busio)

##### Para instalar las librerías de CircuitPython es necesario ejecutar las siguientes líneas en la terminal.

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/config3.JPG?raw=true)

##### Una vez realizado lo anterior se podrá hacer uso de las librerías board y busio.

#### 3. 2. 4. Librería Numpy

##### Para la instalación de la librería numpy en la Raspberry solo será necesario ejecutar el comando *sudo pip3 install numpy* en la terminal.

##### 3. 2. 5. Librería adafruit_ads1x15

##### Esta librería es necesaria para el uso del ADS1115 y para instalarla basta con ejecutar el comando sudo pip3 install adafruit-circuitpython-ads1x15 en la terminal.

###### 20
------------

#### 3. 2. 6. Librería Paho-mqtt 

##### Esta librería es necesaria para el envío de datos a Thingsboard mediante Wi-Fi. Se instala únicamente usando el comando *sudo pip3 install paho-mqtt* en la terminal.

#### 3. 2. 7. Librería opencv-python 4.5.1.48

##### Esta librería se utiliza para realizar las funciones de la cámara Pi, su instalación también es muy sencilla, basta con ejecutar el comando *sudo pip3 install opencv-python* en la terminal.

#### 3. 3. Requerimientos necesarios para ejecutar la programación del dispositivo

##### 1. Verificar instalación correcta de librerías a utilizar
##### 2. Comprender la lógica de programación en python
##### 3. Tener en cuenta que un indentado correcto inuye en la programación
##### 4. Ante algún error, probar programación por separado
##### 5. Colocar nombres fáciles de recordar en las funciones

###### 21
------------

### REFERENCIAS

- Montoro, A. F. (2012). Python 3 al descubierto. México: Alfaohmega Grupo Editor.
- Corona, L. (2014). Sensores y actuadores. México: Grupo Editorial Patria S.A. de C.V.
- Aranda, D. (2014). Electrónica: plataformas Arduino y Raspberry. Buenos Aires: DÁLAGA
- Bentley, R. E. (1998). Temperature and Humidity Measurment. Australia: Springer
- Fernández, J. R. (2012). Instalaciones Domóticas. Madrid: Paraninfo
- Ortega, J. E. (2002). Predicción y evaluación de impactos ambientales sobre la atmosfera. Cordoba: Encuentro.

###### 22
------------

### ANEXOS
#### ANEXO A. PROGRAMACIÓN DEL DISPOSITIVO THIS

**######################### Importar librerías
import time import busio import board import
numpy as np import SDL_Pi_HDC1000 import
adafruit_ads1x15.ads1115 as ADS from
adafruit_ads1x15.analog_in import AnalogIn
import gy30_bh1750 import
paho.mqtt.client as mqtt import
json from datetime import datetime
import cv2 import camarapi_THIS
as camera**
**######################### Fin
######################### Configuración sensor temperatura y humedad
hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000()
######################### Fin**
**######################### Configuracíon para sensor de sonido i2c
= busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c) ads.gain
= 1
chan = AnalogIn(ads, ADS.P0)
def readSPL():
value = ((chan.value * 32768) / 1023) *
0.000001250039 spl_dB = (np.log10(value/0.000020)) *
20 return spl_dB
######################### Fin**
**######################### Thingsboard
THINGSBOARD_HOST = 'iot.ier.unam.mx'
UNIQUE_ID = 'a5194240-081a-11eb-9c3f-d1ead9980bc3'
ACCESS_TOKEN = 'JpaErOQ6qDid8JXZW1Lu'
sensor_data = {'Humedad Relativa': 0, 'Temperatura': 0, 'Iluminacion': 0, 'Promedio Pixeles': 0,
'Nivel Sonoro': 0} #Debe poseer el mismo texto que "sensor_data" para poderse sobre escribir
el valor
client = mqtt.Client(UNIQUE_ID, False)
client.username_pw_set(ACCESS_TOKEN, password=None)**
**######################### Tiempo entre mediciones
INTERVAL = 300 #Intervalo entre mediciones en segundos
next_reading = time.time() #Tiempo al iniciar
client.connect(THINGSBOARD_HOST, 1883, 60, "")
client.loop_start() try: while True: **

###### 23
------------

**TL = hdc1000.readTemperature() # Lectura temperatura HL =
hdc1000.readHumidity() # Lectura humedad
lightLevel = gy30_bh1750.readLight() # Lectura iluminación
dB = readSPL() # Lectura sonido**

**######################### Camara Pi
nombre_foto = 'foto.png'**

**camera.captura_foto(nombre_foto) # Captura foto
imagen = cv2.imread(nombre_foto) gris =
cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imwrite('foto_grises.png',gris) alto =
gris.shape[0]
ancho = gris.shape[1]**

**avg1 = camera.prom_pixeles(gris,alto,ancho) # Promedio de pixeles único**

**cuadrantes = 16
avg_cuadrantes = camera.cuadrantes_pix(gris,cuadrantes,alto,ancho) #Promedio
por cuadrantes**
**######################### Fin**

**######################### Escribir la fecha
fecha = datetime.now()
formato = fecha.strftime('Hora: %H:%M:%S Fecha: %d/%m/%Y, ')
print(formato)**
**######################### Fin**

**######################### Escribir lecturas
print()
print("Temperatura : " + format(TL, '.4f') + " C") print("Humedad
Relativa : " + format(HL, '.4f') + " %") print("Nivel de Luz : " +
format(lightLevel,'.4f') + " lx")
print("Nivel sonoro : " + format(dB, '.4f') + ' dB')
print()
print("Promedio de pixeles único: " + format(avg1,'.4f'))
print("Por cuadrantes: ")
camera.escribe_matriz(cuadrantes,avg_cuadrantes)
print() print()**
**######################### Fin**

**######################### Publicar en Thingsboard
sensor_data['Temperatura'] = TL sensor_data['Humedad Relativa'] =
HL sensor_data['Iluminacion'] = lightLevel
sensor_data['Promedio Pixeles'] = avg1**

###### 24
------------

**sensor_data['Nivel Sonoro'] = dB time.sleep(1)
client.publish('v1/devices/me/telemetry', json.dumps(sensor_data))
time.sleep(1)**
**######################### Fin**

**next_reading += INTERVAL # Siguiente medición
sleep_time = next_reading - time.time() # Tiempo restante para la siguiente
medición if sleep_time > 0:
time.sleep(sleep_time) # Tiempo de espera para la siguiente medición except KeyboardInterrupt:
pass
client.loop_stop()
client.disconnect()**

###### 25
------------

### ANEXO B. DIAGRAMA ESQUEMÁTICO DEL DISPOSITIVO THIS

[**Diagrama en KiCAD**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Diagramas/ESQUEM%C3%81TICO-THIS.pdf)

###### 26
------------

### ANEXO C. DISEÑO DE LA CARCASA DEL DISPOSITIVO THIS

[**Plano 1**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/CAD/base_carcasa_THIS.pdf)

[**Plano 2**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/CAD/tapa_carcasa_THIS.pdf)

[**Plano 3**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/CAD/base_carcasa_Raspberry.pdf)

[**Plano 4**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/CAD/tapa_carcasa_Raspberry.pdf)
