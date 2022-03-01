![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/logoIER.png?raw=true)

## Universidad Nacional Autónoma de México
### Instituto de Energías Renovables
### Manual de operación
## Dispositivo medidor de caudal (H2O)

------------

#### Tabla de contenido

1. Resumen ................................................................................................................................................. 3
2. Sensor de caudal ................................................................................................................................. 3
3. Descripción general del Hardware ............................................................................................... 4
4. Objetivo general del dispositivo ................................................................................................... 4
5. Esquema general del dispositivo de prueba y principio de funcionamiento............... 5
6. Descripción a detalle de cada parte y componente del dispositivo ............................... 6

	6.1 NodeMCU Lolin V3 ESP8266-12E ......................................................................................... 6
	
	6.2 Características de la placa NodeMCU V3 Lolin ................................................................ 7
	
	6.3 Los terminales del NodeMCU V3 Lolin ................................................................................ 7
	
	6.4 ¿Qué quiere decir esto? ¿Cómo lo puedo interpretar? ................................................. 8
	
	6.5 Detalles del NodeMCU ............................................................................................................... 9
7. Identificación de Pines ..................................................................................................................... 10

	7.1 Patillaje de la tarjeta NodeMCU V3 Lolin ........................................................................... 10
	
	7.2 Patillaje del ESP8266-12E ......................................................................................................... 10
	
	7.3 Los LED´s azules ........................................................................................................................... 11
8. Instalación de Python en Linux ..................................................................................................... 12
9. Configuración del ESP8266-12E ................................................................................................... 12
10. Cargar los códigos del dispositivo H2O .................................................................................... 17
11. Agregar un dispositivo en Thingsboard .................................................................................... 18
12. Calibrar el sensor ................................................................................................................................ 20

------------

**1. Resumen**

En el Instituto de Energías Renovables de la UNAM en Temixco Morelos, se tiene planeado construir un edificio sustentable, por lo que hay variables que tendrán que ser medidas y ser compatibles con el medio ambiente, para esto se tiene contemplado la construcción de dispositivos electrónicos que ayuden a medir dichas variables como: agua, consumo eléctrico, temperatura, luminosidad de espacios, nivel sonoro entre otras, con la intención de poder manipular los datos para posteriormente tener control sobre ellas y lograr el confort de los usuarios.
Cabe mencionar que un edificio sustentable debe cumplir con ciertas normas para que pueda ser considerado como sustentable, es por eso la necesidad de controlar dichas variables.

**2. Sensor de caudal**

Los sensores de caudal recogen las velocidades del flujo de aire o líquidos. Los sensores de caudal usan diferentes principios de medición. Este sensor se acopla muy bien a la tubería de agua de cualquier edificio o casa y contiene un sensor de molino para medir la cantidad de líquido que ha pasado a través de él. También tiene un sensor magnético de efecto Hall que emite un impulso eléctrico con cada revolución. El sensor de efecto Hall está sellado para permanecer seguro y seco.
El sensor viene con tres cables:
Rojo (energía 5-24 VDC)
Negro (tierra)
Amarillo (salida de pulsos de efecto Hall)
Al contar los pulsos de la salida del sensor, se puede calcular fácilmente el flujo de agua. Cada pulso es de aproximadamente 2.25 mililitros. Cabe mencionar que el sensor YF-S201, no es un sensor de precisión, y la frecuencia del pulso varía un poco dependiendo de la velocidad de flujo, presión del flujo y la orientación del sensor. Si se necesita más del 10% de precisión se tendrá que hacer la calibración adecuada.
La señal de pulso es una simple onda cuadrada así que es bastante fácil de registrar y convertir en litros por minuto utilizando la siguiente ecuación.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/EcuacionB.PNG?raw=true)

*Pág. 3*

------------

**3. Descripción general del hardware**

El dispositivo está conformado por un módulo NodeMCU que se encarga de adquirir datos que envía el sensor de caudal y posteriormente envía información a Thingsboard para visualizar los datos de manera gráfica en tiempo real, para posteriormente poder decidir si es necesario reducir el consumo y controlarlo como sea conveniente.

**4. Objetivo general del dispositivo**

Este dispositivo se elaboró con la intención de medir la cantidad de agua que se consume en un edificio y poder implementar medidas para evitar consumos excesivos de este valioso recurso.

*Pág. 4*

------------

**5. Esquema general del dispositivo de prueba y principio de funcionamiento**

El dispositivo funciona con un módulo NodeMCU Lolin V3→ESP8266-12E, permitiendo interpretar los datos que recolecta el sensor YF-S201, el módulo tiene un microcontrolador que permite interpretar datos y después enviarlos a través de Wifi. La ventaja más significativa es precisamente esa, que el módulo tiene wifi, permitiendo que pueda enviar datos en tiempo real a diferentes plataformas de visualización, otra ventaja es su tamaño.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/MontajeParaPruebaB.PNG?raw=true)

**Representación del esquema armado para prueba**

El esquema presentado arriba, se realizó con la intención, de poder visualizar de manera muy general una forma de hacer pruebas para calibrar el sensor antes de ser implementado en alguna de las instalaciones eléctricas, si se desea una vez cargado el código al ESP alimentar al mismo con una fuente externa o con la misma entrada del USB, será necesario hacer el arreglo de resistencias (divisor de voltaje).

*Pág. 5*

------------

**6. Descripción a detalle de cada parte y componente del dispositivo**

**6.1 NodeMCU Lolin V3 ESP8266-12E**

El NodeMCU es un módulo que tiene el ESP8266, además ya tiene conexión directa mediante el chip CH340 a USB, tiene wifi y muchas terminales.
El NodeMCU es en realidad un ESP8266-12 con conector a USB (CH340 driver), es mejor que el ESP8266 porque éste tiene más complicación al conectar y configurar ya que no tiene conector USB. Además, el pequeño ESP8266-1 solo tiene dos puertos de conexión y el NodeMCU al contener al ESP8266 tiene 16 puertos de conexión.
Existen 3 versiones:
El ESP8266-1, tiene un precio aproximado de $25.00 pesos mexicanos en el mercado chino. Solo tiene 2 puertos de entrada/salida. Es complicado de conectar al ordenador, hace falta un FTDI o un Arduino para conectarlo al ordenador, sus pines de conexión no entran bien en la placa de pruebas.
El ESP8266-12E, es una versión del anterior, pero con 16 puertos de entrada/salida. También tiene el mismo problema de conexión al ordenador para programarlo, ya que no tiene conector USB. Su precio aproximado es de $25.00 pesos mexicanos en el mercado chino. Los pines machos para el conector suelen venir con el pedido, pero hay que soldarlo.
El NodeMCU V3 Lolin, tiene un precio de unos $75.00 pesos mexicanos en el mercado chino. Es una tarjeta (3x6 cm) que, tiene integrado el ESP8266, con lo cual tiene 16 puertos de entrada/salida. Además, la gran ventaja es que tiene el chip CH340 que sirve para conectarlo al ordenador por USB. Tiene conectores machos que se pueden insertar en la placa de pruebas, pero es un poco ancho y no deja espacio en los pines laterales de la placa de pruebas. Velocidad de 80 MHz.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/VersionesESPB.PNG?raw=true)

*Pág. 6*

------------

**6.2 Características de la placa NodeMCU V3 Lolin**

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/CarateristicasNodeMCUB.PNG?raw=true)

**6.3 Los terminales del NodeMCU V3 Lolin**

Esto es muy importante poder identificar los terminales y puede resultar hasta confuso y tedioso de lograr cuando aún se está empezando con la placa.
La nomenclatura de terminales del NodeMCU son diferentes de los GPIO´s y hasta en el código al momento de declararlos.
Los terminales de la tarjeta NodeMCU se denominan: D0, D1, D2, D3, D4, D5, D6, D7, D8(RX), D9(TX), D10, SD2 y SD3.
Los terminales del integrado ESP8266-12E, que está soldado a la tarjeta se denominan: GPIO0, GPIO1, GPIO2, GPIO3, GPIO,4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10, GPIO11, GPIO12 y GPIO13.
Esto es confuso, porque resulta que no coinciden, es decir el D7 no es el GPIO7, esta es la confusión principal de casi todas las fuentes de información, dando por hecho que todos saben que no se identifica con los mismos números.
A continuación, se presenta una tabla donde se relacionan las terminales de la tarjeta con los del ESP8266, para poder identificar de manera fácil cada uno.

*Pág. 7*

------------

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/RelacionDeTerminalesB.PNG?raw=true)

**6.4 ¿Qué quiere decir esto? ¿Cómo lo puedo interpretar?**

Supongamos que conectamos un LED al terminal D1 de la tarjeta NodeMCU, como en la imagen.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/LedESPB.PNG?raw=true)

El terminal D1 de la tarjeta corresponde con el GPIO5, según la tabla presentada anteriormente.
En el código se debe poner el número 5, es decir el GPIO5. No debe confundirse con el número de terminal de la tarjeta.
Esto es demasiado confuso cuando realmente no se conoce nada de la tarjeta y seguirá causando confusión hasta que se tenga claro cómo se identifica.

*Pág. 8*

------------

**6.5 Detalles del NodeMCU**

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/DetallesNodeMCUB.PNG?raw=true)

Se puede observar el LED azul integrado en la placa del ESP8266-12E.
La frecuencia del Wifi es de 2,4 GHz, es decir, longitud de onda→ λ= velocidad de la luz/frecuencia= 300,000,000/2,400,000,000=12,5cm
Las ondas emitidas tienen una longitud de 12,5 cm, por eso se llama microondas.
Potencia de 25 dBm, son decibelios referenciados a miliwatios, para convertirlos en watios, 10^2(25/10) * 10^ (-3) = 0,32 W es la potencia de emisión.
El CHIP 340, el conector micro USB, un cristal de 12 MHz.
Un regulador de tensión que cambia los 5V del USB a los 3,3 V que necesita el ESP8266.
También se observa dos pulsadores, uno FLASH y otro RST.
Algunas resistencias de superficie SMD, por ejemplo, la de 103 sería de 10,000 Ohmios, la 471, sería de 470 Ohmios.

*Pág. 9*

------------

**7. Identificación de pines**

**7.1 Patillaje de la tarjeta NodeMCU V3 Lolin**

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/IdentificacionDePatillaje.PNG?raw=true)

**7.2 Patillaje del ESP8266-12E**

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/PatillajeESPB.PNG?raw=true)

**7.3 Los LED´s azules**

Se debe considerar que se dispone de dos LED azules.
Uno en el ESP8266-12E, correspondiente a su GPIO2 (que debe ir al terminal D4 del NodeMCU).
Otro en la misma tarjeta del NodeMCU, correspondiente al GPIO16 (que irá al terminal D0 del NodeMCU).

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/LedsAzulesB.PNG?raw=true)

*Pág. 11*

------------

**8. Instalación de Python en Linux**

1. Se debe actualizar los paquetes con el comando “sudo apt update” abriendo la terminal en Linux.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/SudoAptUpdateB.PNG?raw=true)

Posteriormente se debe instalar Python, de igual forma usando la terminal, es preferible instalar Python de versiones mayores que la de 3.0 porque con versiones inferiores es probable que algunas librerías presenten problemas al momento de usarlas.

2. El comando para instalar Python es “sudo apt install python3".

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/InstallPython3B.PNG?raw=true)

Después se debe instalar el administrador de paquetes para Python (Pip3), que nos ayuda a agregar librerías o paquetes de Python.

3. El comando a utilizar es “sudo apt install Python3-pip”.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/InstallPython3PipB.PNG?raw=true)

Los pasos que deben hacerse previamente a todo el proceso mostrado a continuación se encuentran en la pág.

[http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware](http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware)

De igual forma ahí se encuentran los firmwares que pueden ser usados según el ESP con el que se vaya a trabajar.

**9. Configuración del ESP8266-12E**

Como primer paso a seguir antes de meterse a lo que es el sensor de caudal

1. Descargar de la página siguiente:

[https://micropython.org/download/esp8266/](https://micropython.org/download/esp8266/)

el firmware a utilizar, según la capacidad del ESP8266-12E, para este caso en particular, el que se usará es:

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/FirmwareB.PNG?raw=true)

ese firmware descargado se guardará en una carpeta previamente creada por nosotros en alguna parte de nuestro equipo con algún nombre en específico.

*Pág. 12*

------------

Asumiendo que ya se ha guardado el firmware descargado en una carpeta en el equipo.

2. Del mismo link anteriormente mencionado, entrar a la parte de la página en donde se muestran las letras rojas “in the tutorial”.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/InTheTutorialB.PNG?raw=true)

Una vez dentro del link, están los pasos para poder “limpiar” o “formatear” el ESP, para posteriormente cargar el firmware y se logre un buen funcionamiento.

3. Se deberá conectar el ESP8266-12E a nuestro equipo para realizar los siguientes pasos.

4. Como cuarto paso para llevar a cabo lo anterior es abrir la terminal del sistema operativo Linux, una vez abierto, se deberá copiar lo siguiente:

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/InstallSptollB.PNG?raw=true)

En caso de no poder usar ese comando, se puede sustituir con: "sudo apt install esptool"

El comando anterior permite cargar herramientas que proporcionan acceso a muchas de las funciones de señal.

5. Para conocer en qué puerto está conectado nuestro ESP debemos escribir el siguiente comando en la terminal.

**ls /dev/tty***

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/ListarEnLinux.PNG?raw=true)

Lo anterior es para conocer exactamente en qué puerto está conectado nuestro ESP, dependiendo del puerto nos aparecerá USB0 o USB1.

A continuación, se debe formatear (borrar flash) de la tarjeta que se está usando, en este caso el ESP8266, si sucede cualquier detalle cuando ya se está operando con la tarjeta ESP es necesario empezar nuevamente desde este paso para garantizar que la tarjeta se está “limpiando” de todos los programas que tiene cargado.

*Pág. 13*

------------

Para formatear la tarjeta completamente es necesario tener conectado el ESP y se utiliza el comando “esptool.py -port /dev/ttyUSB0 erase_flash".

6. El siguiente paso, es copiar en la terminal el comando:

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/erase_flashB.PNG?raw=true)

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/erase_flash_portB.PNG?raw=true)

**NOTA:** En ocasiones se presenta un detalle de error despuès de ejecutar el comando el comando anterior, esto sucede porque en algunas placas genèricas es
          necesario entrar al modo "FLASH", lo anterior se logra de la siguiente manera:
	  
	Paso 1: Escribir en la terminal el comando para flashear la tarjeta, el comando mostrado arriba pero sin ejecutarlo.
	
	Paso 2: Sin ejecutar el comando, se debe desconectar el cable de datos del ESP.
	
	Paso 3: Presionar el botòn del ESP llamado "FLASH", mantener presionado.
	
	Paso 4: Sin dejar de presionar, se deberà conectar el cable de datos al ESP, presionando en todo momento.
	
	Paso 5: Aùn presionando el botòn y el cable conectado, debera`ejecutar la lìnea de comando previamente preparada en la terminal, en cuanto ejecute el 
		comando debe dejar de presionar el botòn y si realizò bien el procedimiento no habrà error y se llevarà a cabo el proceso satisfactoriamente.
	
Lo anterior es para “limpiar” el esp8266, posterior a eso, se procede a abrir la terminal de nuestro equipo y se deberá tener conectado el ESP8266 al equipo.

7. Se deberá escribir en la terminal lo siguiente:

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/cd_lsB.PNG?raw=true)

**cd** es para meternos al disco de nuestro equipo
**ls** es para poner en forma de lista lo que tenemos en nuestro equipo
En este caso en particular, en la carpeta “firmwares” que se creó previamente se descargó y se guardó el firmware a utilizar.

8. Debemos acceder a ella de la siguiente manera:

**cd firmwares/**
Una vez dentro, escribimos nuevamente
**ls** para enlistar lo que hay dentro de la carpeta
Lo único que tenemos dentro de esa carpeta es el firmware a utilizar que previamente se ha descargado.
Conectado el ESP, se procede con la instalación del firmware a utilizar de la siguiente forma:
“esptool.py –port/dev/ttyUSB0 --baud 46080 write_flash_size=detect 0 (aquí va el firmware)”.

9. Para este caso en particular todo el comando con el firmware descargado previamente quedaría así:

“esptool.py –port/dev/ttyUSB0 --baud 46080 write_flash_size=detect 0 esp8266-20200911-v1.13.bin

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/FirmwareEnTerminalB.PNG?raw=true)

*Pág. 14*

------------

Puede suceder que el comando no funcione correctamente a la primera, si es así, se tendrá que implementar el siguiente comando:
“esptool.py --port dev/ttyUSB0 –baud 46080 write_flash –flash_size=detect -fm dio 0 esp8266-20200911-v1.13.bin”
Hasta este punto si los comandos se ejecutaron sin presentar ningún error, Micropython debería estar instalado en el ESP.

10. Ahora es necesario instalar el intérprete mpfshell con el comando “sudo pip install mpfshell” o con el comando “sudo pip3 install mpfshell”.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/InstallMpfshellB.PNG?raw=true)

11. Escribir el comando “mpfshell”.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/RunMpfshellB.PNG?raw=true)

12. Con el comando “open ttyUSB0” u “open ttyUSB1” se conecta el ESP para cargar códigos.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/openttyusbB.PNG?raw=true)

13. Después listamos con (ls) y obtenemos el archivo que el ESP carga por defecto cada vez que abrimos la tarjeta (boot.py).

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/RemotefilesB.PNG?raw=true)

El otro archivo que el ESP ejecutará por defecto es el “main.py”, para eso se deberá crear antes.
Se deberá guardar de preferencia en el mismo lugar (directorio), en el que se obtuvo el “boot.py” con la intención de que al momento de ejecutar nuevamente el comando “open ttyUSB0”, se encuentre en el mismo directorio y no se tenga que abrir de manera individual.

14. Abrir un lector de texto y crear el archivo “main.py”, para obtener finalmente los dos ejecutables.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/BootAndMain.PNG?raw=true)

*Pág. 15*

------------

Como demostración, los dos archivos se guardaron en el directorio “Desktop”, internamente en el directorio “Prueba” y se ha creado unas líneas de código en el archivo main.py para una prueba.
El ESP debe estar conectado al equipo en todo momento para después solo cargar los archivos.

15. Abrimos la terminal y nos vamos directamente a donde se guardaron los 2 archivos, los abrimos con el comando “gedit main.py” y “gedit boot.py”, no es necesario abrir el segundo archivo.

16. Escribimos las líneas de código en el archivo main.py (print “Hola mundo”), guardamos y cargamos al ESP, nos conectamos ejecutando mpfshell y cargamos una vez que se ha conectado con el comando “put boot.py” y “put main.py”.

17. Ejecutamos el comando “repl” y después “ctrl D” para correr el programa y visualizamos la línea de código que hemos escrito.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/PruebaMpfshellB.PNG?raw=true)

En este caso, el programa se detiene sólo porque es una línea de código sin una condición cíclica, pero en caso de que el programa cargado al ESP sea cíclico, deberá detenerse presionando “ctrl C” y para cerrar el entorno se presiona “ctrl +”.

*Pág. 16*

------------

**10. Cargar los códigos del dispositivo H2O**

Para el siguiente proceso, es necesario ir a la plataforma donde se encuentran los códigos para el funcionamiento del dispositivo H2O.
Se deberá descargar todos los archivos en el equipo y guardar en un directorio, con ayuda del pictograma del dispositivo H2O, se realizan las conexiones necesarias, identificando los GPIO adecuados para el sensor y modificando en el código, en caso de tener dudas con la identificación de pines, en la Tabla 2 se encuentra la descripción de pines del módulo con el ESP8266.
Cuando ya se ha identificado el Pin a utilizar con la entrada del sensor, se procede a cargar los programas.
En el archivo main.py se deberá cambiar el Pin de entrada, en el que el sensor será conectado.
En el archivo funciones.py se deberá introducir el nombre de la red local de wifi y la clave o contraseña de la red. En este paso, por lo pronto será todo lo que se tiene que modificar de los códigos.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/VisualizacionCodigosB.PNG?raw=true)

*Pág. 17*

------------

**11. Agregar un dispositivo en Thingsboard**

Ir a la página oficial de Thingsboard, se puede usar los datos de versión demo o registrarse con datos personales y entrar para crear un nuevo espacio para publicar.

1. Dirigirse dentro de la página a la sección de dispositivos.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/Thingsboard1B.PNG?raw=true)

2. Buscar en alguna parte de la pantalla el signo +, para agregar un nuevo dispositivo, ya que la página cambia en ocasiones debido a actualizaciones se encuentra en el mismo lugar.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/Thingsboard2B.PNG?raw=true)

3. Introducimos el nombre deseado y agregamos.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/Thingsboard3B.PNG?raw=true)

*Pág. 18*

------------

4. Ya que se ha creado el espacio, podemos seleccionar nuestro nuevo dispositivo para ver los detalles y copiamos el ID y el token para después pegarlo en nuestro código.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/Thingsboard4B.PNG?raw=true)

5. En el archivo funciones.py se deberá pegar el ID y token que hemos copiado anteriormente.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/Codigo5B.PNG?raw=true)

6. Posterior a eso, en la parte de “última telemetría” se podrá visualizar los datos que se ha estado enviando.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/Thingsboard6B.PNG?raw=true)

*Pág. 19*

------------

**12. Calibrar el sensor**

Cuando ya se ha realizado todo lo anterior sin ningún problema, se procede a cargar los códigos modificados al ESP y se ejecuta en la terminal para visualizar que en realidad está midiendo y enviando datos el sensor. Para poder calibrar el sensor, es necesario tener 1 recipiente con agua de una medida establecida, puede ser de 1L,2L,3L, según con lo que se disponga.
En el archivo main.py se encuentra el valor de K, es la constante que se tiene que ir modificando, hasta que el código completo, funcionando, mida 1L cuando se le desocupe 1L y después corroborar con otras cantidades.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/DeclararElSensorB.PNG?raw=true)

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/CalibrarSensor.PNG?raw=true)

*Pág. 20*

------------


![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/CalibrarSensor1.PNG?raw=true)

Para el ciclo de prueba 4, se podía ver que en comparación al 3, ya se estaba pasando con los valores de prueba, es decir, del ciclo 3 medir 1.0078L al ciclo 4 medir 1.0073L, en los valores promedio estaba disminuyendo y acercándose a 1L en ambos casos, pero si nos guiamos en los valores individuales de los ciclos de prueba, se puede ver que hay más valores en el ciclo 4, por debajo de 1L, por eso se determinó que el valor de K debería estar más cercano al del ciclo 3.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/UltimaPruebaSensor.PNG?raw=true)

Finalmente, en el archivo main.py se dejó con el valor de K a 0.0017380.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/UltimaDeclaracionSensor.PNG?raw=true)

*Pág. 21*

------------
