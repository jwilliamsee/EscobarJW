# SISTEMA DE MONITOREO DE CIRCUITOS.
## CMS-700 Manual de usuario.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/ABB%20CMS-700.PNG?raw=true)

------------

# Uso y almacenamiento del manual.
Este manual contiene toda la información de seguridad, la información técnica aspectos y el funcionamiento necesarios para asegurar el correcto uso de el dispositivo y manténgalo en condiciones seguras.
## Almacenamiento.
El manual debe guardarse cerca del dispositivo; a salvo de líquidos y cualquier otra cosa que pueda comprometer su legibilidad. El manual y la declaración de conformidad son parte integrante del dispositivo hasta que sea desmontado. Si el manual se pierde o es ilegible, solicite una copia al fabricante.
## Derechos de autor.
Los derechos de autor de este manual son propiedad de ABB Ltd. Este manual contiene textos, diseños e ilustraciones de carácter técnico que no deben ser divulgadas ni transmitidas a terceros, incluso parcialmente, sin la autorización por escrito de ABB Ltd.
## Descargo de responsabilidad.
La información contenida en este documento está sujeta a cambios sin previo aviso y no puede ser considerado como una obligación por ABB Ltd. ABB Ltd. no es responsable de los errores que puedan aparecer en este documento. ABB Ltd.no es responsable bajo ninguna circunstancia por ningún incidente directo, indirecto, especial o incidental. o daños consecuentes de cualquier tipo que puedan surgir del uso de este documento. ABB Ltd. tampoco es responsable de los daños incidentales o consecuentes que puedan surgir del uso del software o hardware mencionado en este documento.
## Marca.
ABB Ltd. es una marca registrada de ABB Group. Todas las demás marcas o nombres de productos mencionados en este documento son marcas comerciales o marcas comerciales registradas de sus respectivos propietarios.

------------

# INFORMACIÓN GENERAL.
## Limpieza.
Utilice un paño seco.
## Instalación a la red.
La instalación de CMS-700 a la red debe incluir un interruptor o disyuntor para la conexión a la red. El interruptor o disyuntor debe estar convenientemente ubicado y ser fácilmente accesible y debe estar marcado como el dispositivo de desconexión para el CMS-700.
## Desconexión de la red o conexión a la red.
Apague el disyuntor o el interruptor antes de desconectar de la red eléctrica o conectar a la red eléctrica. Lo mismo se aplica a todas las demás conexiones (L1, L2, L3, N).
##Advertencias de seguridad.
##Atención: Incumplimiento de la los siguientes puntos pueden provocar lesiones graves o la muerte.
Utilice los dispositivos de protección personal adecuados y cumpla con las normas regulaciones que rigen la seguridad eléctrica.
##Este dispositivo debe ser instalado exclusivamente por personal calificado que tenga leer toda la información relativa a la instalación.
- Compruebe que la tensión en el lado principal sea compatible con el rango permitido por el dispositivo.
- Asegúrese de que todos los suministros de corriente y voltaje estén desconectados antes de transportar todos los controles, inspecciones visuales y pruebas del dispositivo.
- Asuma siempre que todos los circuitos están bajo voltaje hasta que estén completamente desconectado, sometido a pruebas y etiquetado.
- Desconecte toda la fuente de alimentación antes de trabajar en el dispositivo.
- Utilice siempre un dispositivo de detección de voltaje adecuado para verificar que el suministro esté interrumpido.
- Preste atención a cualquier peligro y controle cuidadosamente el área de trabajo asegurándose de que no haya instrumentos o extraños se han dejado objetos dentro del compartimento en el que está alojado el dispositivo.
- El uso correcto de este dispositivo depende de una correcta manipulación, instalación y uso.
- El incumplimiento de la información básica de instalación también puede provocar lesiones. Como daños a los instrumentos eléctricos oa cualquier otro producto.
- Las pruebas realizadas a alto voltaje pueden dañar los componentes electrónicos del dispositivo.
##Disposición.
Los dispositivos defectuosos deben eliminarse como residuos especiales en la recolección adecuada puntos establecidos a tal efecto. Regulaciones nacionales o regionales sobre la eliminación de deben seguirse los residuos.
##Servicio y mantenimiento.
El dispositivo se somete a varias evaluaciones de seguridad antes del envío y se sellará. Si se abre un dispositivo, las evaluaciones de seguridad deben repetirse. Se proporcionará una garantía solo para dispositivos sin abrir.

------------

# Contenido del empaque.
- Unidad de control (CMS-700)
- Manual de instalación.
## Atención: los siguientes elementos no son incluido en la entrega del producto.
- Sensores CMS
- Transformador de corriente (CT).
- CMS-Bus.
- Conjunto de conectores.

------------

#Descripción del producto.
Uso previsto
La unidad de control CMS-700 es un instrumento de medida para registrar el rendimiento y la energía de la red y de hasta 96 sensores de derivación.
El sistema consta de una unidad de control y sensores con diferentes rangos de medición.
Los sensores miden corrientes alternas, directas y mixtas (TRMS) y se conectan al control unidad mediante un cable plano, el CMS-Bus. Los datos de medición se pueden mostrar o analizar a través de la interfaz LAN con el servidor web integrado o los protocolos Modbus TCP o SNMP o mediante la interfaz RS485, como Modbus RTU.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/Arquitectura%20ABB%20CMS-700.PNG?raw=true)

## Descargo de responsabilidad de seguridad cibernética.
El CMS-700 está diseñado para conectarse y comunicar información y datos a través de una red. interfaz, que debe estar conectada a una red segura. Es su exclusiva responsabilidad proporcionar y garantizar continuamente una conexión segura entre el producto y su red o cualquier otra red (según sea el caso) y para establecer y mantener medidas apropiadas (tales como, entre otras, la instalación de cortafuegos, aplicación de medidas de autenticación, cifrado de datos, instalación de programas antivirus, etc.) para proteger el producto CMS-700, la red, su sistema e interfaces contra cualquier tipo de brechas de seguridad, acceso no autorizado, interferencia, intrusión, fuga y / o robo de datos o información. ABB Ltd y sus filiales no son responsables de los daños y / o pérdidas relacionados a tales violaciones de seguridad, acceso no autorizado, interferencia, intrusión, fuga y / o robo de datos o información. Aunque ABB Ltd proporciona pruebas de funcionalidad en los productos y actualizaciones que publicamos, usted debe instituir su propio programa de prueba para cualquier actualización de producto u otras actualizaciones importantes del sistema (para incluir, entre otros, cambios de código, cambios de archivos de configuración, actualizaciones de software de terceros o parches, cambio de hardware, etc.) para garantizar que las medidas de seguridad que ha implementado no se han visto comprometidas y la funcionalidad del sistema en su entorno es la esperada.

------------

# Descripción del producto.
## Botón de reinicio.
Hay un botón empotrado para reiniciar el dispositivo o para restablecerlo a una condición definida como entregado.
- Al presionar el botón durante 3 a menos de 6 segundos se reinicia el dispositivo con la configuración actual.
- Al presionar el botón durante más de 10 segundos se restablece el dispositivo a la configuración de fábrica.
## LEDs.
Dos LED indican respectivamente el estado del dispositivo y el de la red.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/Captura.PNG?raw=true)

------------


# Especificaciones técnicas.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/TABLAS%20CMS-700.PNG?raw=true)


------------

# Dimensiones totales.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/DIMENSIONES.PNG?raw=true)


------------

# Definición de Medidas y Eventos.
## Principio de medida.
El principio de medición para CA de la unidad de control CMS-700 incluye la medición en el principales y sucursales. En el lado de la red, todos los valores se miden directamente. En las ramas, la corriente es medido mientras que el voltaje, el factor de potencia, así como la potencia activa y la energía se calculan utilizando valores de red medidos.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/TABLA%20PRINCIPIO%20FUNCIONAMIENTO.PNG?raw=true)



------------

# Definición de Medidas y Eventos.
## Eventos.
Si un objeto de medición (por ejemplo, corriente TRMS de una rama) cruza las condiciones de umbral predefinidas (valor, dirección y tiempo de retardo) entonces se registra un evento.
Están disponibles las siguientes opciones vinculadas al registro de eventos:
- Visualización de todos los eventos detectados en WebUi.
- Lectura del estado de eventos / alarmas a través del registro Modbus o trampas SNMP.
- Exportar a través de FTP y correo electrónico.
Para configurar un evento, se requieren las siguientes especificaciones:
- El valor umbral
- Indicación de dirección transversal (cruz arriba, cruz abajo).
- indicación de tiempo de retraso.
Los eventos se pueden vincular tanto a valores de objetos de red como de ramales.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/TABLA%20DE%20RAMAS%20CMS-700.PNG?raw=true)


------------

# Arquitectura de memoria.
Los valores medidos de la red eléctrica principal y los de las 96 salidas se almacenan en las siguientes áreas de memoria:

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUG_6dAO_VzSbebC3u-cH9TmtWCNdBe-w-hA&usqp=CAU)

### Valores almacenados.
- Voltaje [V]: L1, L2, L3
- Corriente [A]: L1, L2, L3, N.
- Factor de potencia [-]: L1, L2, L3.
- THD U [%]: L1, L2, L3.
- THD I [%]: L1, L2, L3, N.
- Potencia activa [W]: L1, L2, L3
- Potencia aparente [VA]: L1, L2, L3.
- Potencia reactiva [VAR]: L1, L2, L3.
- Suma de potencia activa [W].
- Suma de potencia aparente [VA]
- Suma de potencia reactiva [VAR].
- Energía activa [Wh]: L1, L2, L3.
- Energía aparente [VAh]: L1, L2, L3.
### Ramas.
- Corriente (TRMS, CA, CC) [A].
- Potencia activa [W].
- Energía activa [Wh].
> Estos valores de las respectivas pilas se pueden exportar como un archivo .CSV y se coloca en un FTP o se envía por correo electrónico.
> Referencia de tiempo
> Los valores medidos se proporcionan con una marca de tiempo UTC. UTC (hora universal coordinada)
 representa la hora mundial independiente de la ubicación en segundos.

------------

# Componentes del sistema.
## Unidad de control.

![](https://s1.bukalapak.com/img/66030319061/s-330-330/150582461_76129609_6bd7_46ec_bf51_9a13c5cd6be6_1180_1180_abb.png.webp)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/CMS-Sensor.PNG?raw=true)


> Estado del LED del sensor:
>-  ON.
> El sensor está en línea y en modo de medición. Hay una característica en la configuración para apagar el LED después de un tiempo especificado.
> - OFF
> El sensor no está conectado a CMS-Bus o el LED está apagado en la configuración.

> - Parpadeando lentamente: El sensor no está asignado.

> Parpadeando rápido: Sensor en proceso de asignación o en modo "configuración / ramas". Este sensor es el sensor correspondiente a la fila marcada en amarillo en la pantalla para la configuración del servidor web.


------------

# Componentes del sistema CMS.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/ESPECIFICACIONES%20SENSORES%201.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/ESPECIFICACIONES%20SENSORES%202.PNG?raw=true)



------------

# Componentes del sistema CMS.

##Transfomadores de corriente.

![](https://www.solarshoponline.com.au/wp-content/uploads/2020/03/ABB-CT-PRO-XT-400.jpg)

### Cable plano CMS.
El cable plano CMS es un cable de 4 pines para conectar varios sensores a una unidad de control. El cable está disponible en las siguientes cuatro longitudes: 2 m (CMS-800), 5 m (CMS-802), 10 m (CMS-803), y 30 m (CMS-805).
Tenga en cuenta la siguiente información sobre la posible longitud de cable del cable plano CMS dependiendo del número y forma de los sensores:

![](https://cdn.manomano.com/cable-plano-5-m-cms-805-abb-2cca880331r0001-P-6054354-18483586_1.jpg)
![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/MEDIDAS%20PARA%20CABLE%20PLANO.PNG?raw=true)

### Conjunto de conectores.
El juego de conectores CMS-820 contiene carcasas de conectores y conectores para conectar el cable plano a los sensores.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQc65GA9ZW3qX-pWnCawk3eFXa6MODZqi3vYg&usqp=CAU)


------------

# Guía de instalación.
- Garantía
Se garantiza un funcionamiento seguro si los trabajos de montaje se han realizado de acuerdo con estas instrucciones de uso. Además, se deben respetar las instrucciones del manual.
- Personal autorizado.
Los trabajos de montaje, conexión y desmontaje solo deben ser realizados por personal autorizado.
- Montaje en carril DIN de 35 mm.
Para montar la unidad de control, realice los pasos 1 y 2. El dispositivo se puede montar horizontal o verticalmente. Para desconectar, realice los pasos 3 y 4.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxKOKR_MjAYAE47DGHLvdsAuZ9DBxjmumeoQ&usqp=CAU)

> El CMS-700 se puede montar en todos los rieles DIN de 35 mm (DIN50022).
> El dispositivo se puede instalar para uso monofásico o trifásico.
> Cuando esté disponible, conecte el cable LAN de la red local.

### Cable plano - Montaje de conectores.

> Utilice los conectores solo una vez.
> Conectar máx. 96 sensores a cada interfaz CMS-Bus de la unidad de control.
> Considere la longitud máxima del cable plano.
> El cable plano no debe ejercer fuerza sobre el sensor, de lo contrario pueden ocurrir errores de medición.
>  Mantenga una distancia mínima de 5,5 mm entre el cable plano y las partes activas no aisladas.

Marque la ubicación deseada del conector con un bolígrafo:

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR87fdAs1HXIhjqrfnNo5yJDw6xwGUc2_1-ig&usqp=CAU)

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoJcb5ontDDjsjHy1hSdRhtNNRgmcRRGrcCQ&usqp=CAU)

1. Presione el cable plano en el conducto de cables del carcasa del conector.

2. Inserte el conector en el conector  de alojamiento en la posición marcada.

3. Presione juntos usando alicates paralelos. Repita el proceso en todas las demás marcas.

### Posición del cable.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0Dx2TMkeKgEtEoBxZmgLceu9k6BNRwM6ZIw&usqp=CAU)

> El cable no debe doblarse directamente sobre el sensor. Si usa sensores de núcleo abierto, asegúreseel cable está en la posición correcta, de lo contrario Pueden ocurrir errores de medición.

------------


### Montaje de los sensores System pro M compact y SMISSLINE.

• Los sensores se adaptan a todos los dispositivos de instalación de ABB con terminales dobles.
• El cable plano no debe ejercer fuerza sobre el sensor, de lo contrario pueden ocurrir errores de medición.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRE4g3g5PiP_trnzBbC6gD0IaSPDNOQCwm6sg&usqp=CAU)

> 1. Desatornille el terminal de la instalación dispositivo. Enchufe la clavija de metal del sensor en la conexión del terminal trasero.

> 2. Pase el cable por la abertura del sensor en el dispositivo instalado. El cable debe estar aislado dentro del sensor.

> 3. Luego apriete el tornillo.

### Montaje de sensores en rieles DIN.

> Los sensores se pueden montar en todos los rieles DIN de 35 mm (DIN50022).
> El cable no debe ejercer fuerza sobre el sensor, de lo contrario pueden ocurrir errores de medición.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5_OjD9HDvk0Bl2oJELfFY4qgHcrUkuqTIUQ&usqp=CAU)

1. Encaje el soporte en el riel DIN.
2. Inserte el cable en el dispositivo instalado a través de la abertura del sensor. El cable debe estar aislado dentro del sensor.
3. Fije el cable con una brida.
4. Encaje el sensor en el soporte.

------------

### Montaje de sensores CMS-101
 El cable no debe ejercer fuerza sobre el sensor, de lo contrario pueden ocurrir errores de medición.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRc7Yvv6EwbOFM-p3rsk0l93B7Zs8Eo-Jte9g&usqp=CAU)

1. Inserte el cable en el dispositivo instalado a través de la abertura del sensor.
2. Fije el cable con una brida.

### Conexión.
Finalmente, conecte los sensores CMS a la unidad de control.
Enchufe el cable, compruebe la dirección de conexión correcta. 

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS63vfckU_1RRnsTQ5J-RuHMhztnnmztzNTlQ&usqp=CAU)

> Atención: al conectar el cable plano CMS en los sensores, compruebe la dirección de conexión correcta.

------------

# Diagramas de cableado.
Las operaciones a realizar para la correcta conexión del dispositivo, en función del tipo de línea disponible, se describen en esta sección
El CMS-700 incluye una fuente de alimentación propia en L1-N. No se requiere fuente de alimentación externa. Los contactos l1, l2, l3, l4 / N están previstos para conectar el transformador de corriente externo.

## Instalación a la red.
La instalación de CMS-700 a la red debe incluir un interruptor o un disyuntor para la conexión a ellos.

El interruptor o disyuntor debe estar convenientemente ubicado y ser fácilmente accesible y debe estar marcado como el dispositivo de desconexión del CMS-700.

## Desconexión de la red o conexión a la red.

Apague el disyuntor o el interruptor antes de desconectarlo de la red eléctrica o conectarlo al suministro de red. Lo mismo se aplica a todas las demás conexiones (L1, L2, L3, N).

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQGbXwzeNMvWMyAm2FC47QBiUY5U2iIfXXEA&usqp=CAU)

> Atención: La instalación y el cableado del dispositivo debe ser realizado por personal calificado. Peligro de electrocución, quemaduras y arco eléctrico. Utilice los dispositivos de protección personal adecuados para cumplir con la normativa vigente que rige la seguridad eléctrica. Antes de realizar cualquier conexión comprobar el seccionamiento de la alimentación eléctrica con el dispositivo de detección de tensión.

## Trifásico más neutro.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-_IG-JDRVkmCFJ_MBTFHALRD_TA6yPsP8EQ&usqp=CAU)

> Atención: Por favor, refiriéndose al diagrama de la figura aparte, observe que N en el suministro tiene que estar conectado para evitar daños en el dispositivo.

> Atención: asegúrese de que N no se mezcla con el fases L1, L2, L3.

> Atención: la salida de CT debe no estar conectado al tierra. No es posible conectar más de uno CMS-700 en serie con el mismo CT.

## Linea más Neutro.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/CMS%201%20LINEA%20Y%20NEUTRO.PNG?raw=true)
> Atención: Por favor, refiriéndose al diagrama de la figura aparte, observe que N en el el suministro tiene que estar conectado para evitar daños en el dispositivo
> Atención: asegúrese de que N no se confunde con el fases L1, L2, L3.
> Atención: la salida de CT debe no estar conectado al tierra. No es posible conectar más de uno CMS-700 en serie con el mismo CT.

------------

# Puesta en servicio inicial.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/PUESTA%20EN%20SERVICIO%20INICIAL..PNG?raw=true)

> Para la primera configuración, debe utilizar la conexión LAN directa. Siga las instrucciones del punto b. Conexión LAN directa.

> Verifique la hora interna del dispositivo.
> Si no es correcto, debe configurarse manualmente.

> Para obtener más información sobre la configuración manual de la hora, menú de configuración - Otro / Hora.

## Conexión de red.

Las siguientes secciones muestran los pasos necesarios para configurar la unidad de control CMS-700.
La unidad de control se puede utilizar en diferentes modos de funcionamiento:
• Conexión LAN mediante enrutador.
• Conexión LAN directa.
• Además, todos los datos están disponibles a través del puerto serie: Modbus RTU (RS485).


------------

## Conexión LAN mediante enrutador.
La unidad de control CMS-700 se conecta al enrutador mediante un cable RJ45 (RED).

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/LAN%20conexi%C3%B3n..PNG?raw=true)

## Acceso a la interfaz de usuario web a través del nombre de host.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/acceso%20a%20la%20web%20UI.PNG?raw=true)

Nombre de host: CMS-700, Puerto: 8000
Se agregará a la dirección IP para definir el número de puerto (por ejemplo, 192.168.1.200:8000) para acceder su navegador web. Definir el número de puerto es importante porque sin un número de puerto el acceso no es posible.

> En el caso de DHCP, el administrador del sistema puede leer la dirección IP asignada al Dispositivo CMS-700 por DHCP en el enrutador.

## Conexión LAN directa.

Para la conexión de red, puede ser necesario un acceso con dirección estática en el primer paso.
Dirección IP: 192.168.1.200:8000 / Máscara de subred: 255.255.255.0

------------

La unidad de control se configura mediante una interfaz web. Para conectar una PC o computadora portátil al CMS-700 sin DHCP, debe configurar la interfaz LAN con una dirección IP estática. Usando el ejemplo de Windows, a continuación se muestran los pasos de configuracin.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/LAN%201.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/LAN%202.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/LAN%203.PNG?raw=true)

Ingrese la dirección IP: 192.168.1.200:1.5 y la máscara de subred: 255.255.255.0 y confirme con OK

Asegúrese de que la dirección IP en la LAN no esté ya tomada. En caso de que se tome, los ajustes son necesario. (192.168.1.x; x = 2… 199, 201… 255)

Ahora conecte su dispositivo a la unidad de control CMS-700.

------------

> La interfaz de usuario web está diseñada para su uso en dispositivos basados en navegador. El navegador web recomendado es Google Chrome, otro compatible
Los navegadores web son Safari, Firefox, Opera, Internet Explorer.

## Pantalla de inicio (inicio de sesión).
Inserte la dirección IP del dispositivo en la barra de direcciones del navegador.
Para acceder al navegador web, también es importante definir el número de puerto 8000.
Ajustes de fábrica con:
IP alternativa: 192.168.1.200:8000
Inicio de sesión alternativo - nombre de usuario: admin, contraseña: admin.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/cms-700%20web%20UI.PNG?raw=true)

>Tenga en cuenta que la unidad de control utiliza una conexión https: // segura y el puerto 7999. Primero, es necesario confirmar la conexión segura.

> Más adelante no se te pedirá que lo confirmes siempre que cargue el Certificado SSL como se describe en la sección dedicada.

> Después de iniciar sesión, se le pedirá que cambie los datos de inicio de sesión. Se recomienda encarecidamente cambiar el inicio de sesión datos lo antes posible por motivos de seguridad.

> La nueva contraseña debe contener un mínimo de 8 caracteres, al menos una letra mayúscula y un número.

------------

## Descripción general del servidor web.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/ABB-MAINS.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/CMS-700%20WEB-UI%20STRUCTURE.PNG?raw=true)


------------

# Interfaz de usuario WEB - Configuración.

Apagado seguro: para asegurarse de que se guarden todas las configuraciones, se recomienda realizar un apagado seguro después de cambiar cualquier configuración y luego reiniciar el sistema (Configuración - Otro / Reinicio del sistema).

### Configuración -(  De RED)
Es posible configurar la frecuencia, la relación del TC externo para las fases y el neutro y la tensión de CC de referencia, si es necesario.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-MAINS.PNG?raw=true)

La relación CT para L1, L2, L3 tiene que ser la misma, mientras que puede ser diferente para N.
La relación de TC se calcula dividiendo la corriente nominal primaria por la corriente secundaria estándar (5A).
> La corriente de la red se mide mediante TC. Se necesita una referencia de voltaje de CC para calcular la potencia de CC a nivel de sucursales.


------------

### Configuración - Ramas.
El menú permite tener acceso a la información que se enumera brevemente a continuación junto con los botones que puedo usar.

Es posible utilizar el filtro de selección y la función de clasificación en las etiquetas de fase y grupo para encontrar valores deseados. También es posible agregar nuevos sensores por su propio número de identificación definido y cambiar el Número de identificación.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-BRANCHES.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/TABLA%20BUTTONS.PNG?raw=true)

> Asegúrese de seleccionar la fase correcta en la que está instalado el sensor CMS en la columna de fase

Si es necesario, cambie el factor de potencia (PF) de Automático a un valor manual correspondiente al PF del carga medida.

### Configuración - Grupos.

Esta página permite crear o eliminar grupos de sensores.

Al hacer clic en "Agregar nuevo", es posible crear un nuevo grupo. 

 Una vez que se ha creado un grupo, es posible asociar un sensor a un grupo en la sección "Configuración - Ramas".
 
Es posible cambiar el nombre de un grupo y visualizar el número de sensores asociados a la grupo.

Al hacer clic en "Eliminar seleccionados", se eliminará el ID del grupo seleccionado.

Tenga en cuenta que es posible asociar un sensor a un solo grupo solamente.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-GROUPS.PNG?raw=true)


------------

### Configuración - Eventos.
Esta página permite configurar eventos. Si ocurre un evento, se muestra en el menú de eventos históricos. Un evento puede ocurren después de exceder los valores de umbral seleccionados (cross-up) o después de medir valores inferiores al valores de umbral seleccionados (cross-down) para un período determinado (retardo de tiempo). Se envía el informe por correo electrónico después de 1 minuto desde que ocurrió el primer evento y consta de todos los eventos que ocurrieron en este período. El próximo informe solo se puede enviar después de al menos 30 minutos desde la ocurrencia del primer evento y solo en caso las condiciones del evento aún están en curso.

El estado del evento se puede solicitar a través de Modbus (para obtener más información, consulte "Medidas y Definición de Eventos ”).

Si se configura una trampa SNMP, se enviará una notificación del evento.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/TABLA%20CONFIGURACI%C3%93N%20EVENTOS.PNG?raw=true)

------------

### Configuración: exportación de datos.
Para realizar la exportación de datos por correo electrónico y / o FTP, datos de contacto para correo electrónico y servidor FTP debe configurarse (consulte Configuración - Correo electrónico, FTP). Se debe proporcionar la siguiente información para la exportación automática de datos a través de correo electrónico o conexión a un servidor FTP:

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-%20DATA%20EXPORT.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/TABLA%20SETTINGS%20DATA%20EXPORT.PNG?raw=true)


------------

### Configuración: correo electrónico / FTP.
Configuración de los datos de contacto. Se necesitan configuraciones de correo electrónico y FTP para llevar correo electrónico y exportación de datos FTP. Asegúrese de que ningún firewall bloqueará la exportación.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-EMAIL.PNG?raw=true)

> Asegúrese de que la comunicación en el puerto SMTP 587 o 465 (SSL) esté permitida en su red. Ingrese los detalles de su servidor FTP (dirección y credenciales de inicio de sesión) para permitir la exportación automática de datos (medida y / o eventos).

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-FTP.PNG?raw=true)


------------

### Configuración - Comunicación / IP.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-IP.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/TABLA%20CONFIGURACI%C3%93N%20IP.PNG?raw=true)

> Los ajustes inapropiados pueden hacer que la interfaz de usuario se vuelva inaccesible. Para poder restaurar el acceso del dispositivo a la IP alternativa, utilice el botón de reinicio. (El dispositivo es visible cuando DHCP está activo).


------------

### Configuración: comunicación / SNMP.
El servicio SNMP está desactivado en el dispositivo de forma predeterminada. Para activarlo, utilice este sección:

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-SNMP.PNG?raw=true)

Versión 1 / 2c: para habilitar las versiones 1 y 2c, marque la casilla de verificación v.1 / 2c, ingrese el número de puerto y la contraseña para el protocolo. El número de puerto debe ser 161 o superior a 1024. El servicio SNMP está funcionando Puerto UDP para que no haya colisión de puertos con el Modbus o el servicio web que están funcionando en los puertos TCP.

La contraseña debe tener al menos 5 signos. En las versiones 1 y 2c la autenticación es solo por contraseña que no está encriptado.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-SNMP%202.PNG?raw=true)


------------

### Configuración: comunicación / SNMP.
Versión 3: para habilitar la versión 3, marque la casilla de verificación v.3, ingrese el número de puerto, contraseña, nombre de usuario y ID del motor. Igual que para las versiones v.1 / 2c, el número de puerto debe ser 161 o superior a 1024. La contraseña para la versión 3 debe tener al menos 8 signos, mientras que la identificación del motor debe tener al menos 12 caracteres en formato hexadecimal. Para acceder a los datos mediante SNMPv3, la solicitud autenticada y cifrada debe enviado. La autenticación se realiza mediante nombre de usuario y contraseña. Para la autentificación del MD5 se utiliza el protocolo. Los mensajes se cifran además con el algoritmo DES.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-SNMP%203.PNG?raw=true)

Descargar archivo MIB: haga clic en el botón para descargar el archivo MIB CMS-700 a su PC.
> Tenga en cuenta que las versiones 1 / 2c y 3 pueden funcionar simultáneamente.

------------

### Configuración: comunicación / captura SNMP.
Esta página permite habilitar / deshabilitar el sistema de captura SNMP. La trampa SNMP es un protocolo que permite mensajes (trampas) que se enviarán desde el dispositivo al servidor de supervisión.

SNMP está diseñado para informar eventos.
Es posible habilitar la trampa para cada evento individual en la página "Configuración de eventos".

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS%20SNMP%20TRAP.PNG?raw=true)

Hay dos versiones diferentes del protocolo de captura SNMP disponibles en el dispositivo: versión 2c (v.2c) y versión 3 (v.3). La versión 2c es más fácil de usar y más rápida. La versión 3 proporciona una mayor seguridad

Versión 2c: para habilitar la versión 2c, marque la casilla de verificación v.2c. Para todos los ajustes relacionados, consulte la siguiente tabla:

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-SNMP-TRAP%202.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/V.2.C.PROTOCOL%20CONFIGURATION.PNG?raw=true)


------------

### Configuración: comunicación / captura SNMP.
Versión 3: para habilitar la versión 3, marque la casilla de verificación v.3. Para todos los ajustes relacionados, consulte la siguiente tabla:

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-SNMP-TRAP%203.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/V.3%20PROTOCOL%20CONFIGURATION.PNG?raw=true)

------------

### Configuración: comunicación / Modbus.
Esta sección permite tener acceso a la configuración de Modbus TCP y RTU.

## Modbus TCP.
Es posible habilitar o deshabilitar el protocolo de comunicación correspondiente y cambie el puerto TCP.

### Modbus RTU.
Aquí se pueden configurar los campos ID de Modbus, velocidad en baudios y paridad.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/MODBUS%20TCP%20SETINGS.PNG?raw=true)

> Debido a la seguridad cibernética, los números de puerto mayores a 1025 no están permitidos, excepto el puerto Modbus estándar, que es el puerto 502. Los puertos 8000 y 7999 están reservados para el servicio web.

------------

### Configuración: certificado SSL.
En esta sección es posible cargar o generar un archivo .pem que contiene una clave privada y una pública. 

Certificado para proporcionar una conexión segura a través del navegador web.

### Subir.
Es posible buscar, cargar o descargar el certificado actualmente en vigor.
Para este propósito, arrastre y suelte el archivo .pem en el navegador o haga clic para navegar, luego presione el botón de carga y espere a que finalice la carga. Después de un proceso de carga exitoso, la web el servidor se reinicia.

También es posible descargar un certificado utilizado actualmente haciendo clic en descargar certificado.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SETTINGS-UPLOAD%20SSL%20CERTIFICATE.PNG?raw=true)


------------

### Configuración: certificado SSL.
### Generar.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/settings%20generate%20ssl%20certificate.PNG?raw=true)

Después de la configuración de la tabla de dominios / direcciones IP, haga clic en el botón Generar. Cuando finaliza el proceso de generación, el servidor web se reinicia y debido a un cambio de certificado la página ha para ser recargado manualmente.

Siga los pasajes que se informan a continuación para importar el certificado descargado a su navegador web.

### Certificate Import Wizard.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/certificate%20import%20wizzart.PNG?raw=true)

Primero es necesario abrir el Asistente de importación de certificados de acuerdo con el navegador que están usando y luego instalar el certificado.

------------

### Configuración - Exportar / Importar.
## Exportar
Esta página permite la exportación de configuraciones de sensores / grupos y de valores históricos marcando el casillas correspondientes y luego haciendo clic en "Generar".

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/settings%20export.PNG?raw=true)

### Importar.
Esta página permite la importación de configuraciones y / o valores históricos. Es posible elegir incluir o excluir sensores / grupos en la importación. Antes de iniciar la importación, haga clic en "Importar", asegúrese de que el archivo de configuración que desea importar se ha arrastrado y soltado en el correspondiente "Arrastrar y soltar" ventana.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/settings%20import.PNG?raw=true)


------------

### Configuración - Otro / Hora.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/time%20settings.PNG?raw=true)

## Ajustes de hora.
Es posible sincronizar la hora para comparar la hora del dispositivo y la de la web navegador. La sincronización es obligatoria para poder visualizar y almacenar correctamente los datos.

Al hacer clic en el botón "Sincronizar", el CMS se sincronizará con la hora del navegador web.

Tenga en cuenta: si la hora del dispositivo difiere en más de 10 minutos de la hora del navegador web, aparecerá un mensaje de advertencia se mostrará.

### Establecer la hora manualmente.
También es posible configurar la hora manualmente. Seleccione la fecha y la hora utilizando los iconos de calendario y reloj.

### NTP.
Si hay un servidor NTP disponible, puede configurar la dirección IP (servidor de hora 1, servidor de hora 2) para la hora automática. sincronización.

En este caso, el procedimiento de sincronización puede tardar hasta 10 minutos.

Asegúrese de que ningún firewall bloquee el servidor NTP.

> Verifique la hora interna del dispositivo para garantizar el correcto funcionamiento del CMS-700. Si no es correcto, debe configurarse manualmente.

> Una vez que se configuran la fecha y la hora, no es posible cambiarlas sin dañar la base de datos.


------------

### Configuración - Otro / Sesión.
Esta página permite cambiar el tiempo de espera de la sesión del usuario registrado.

Seleccione el tiempo de espera de la sesión deseada de la lista desplegable y luego haga clic en "Aplicar" para guardar los cambios.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/settings%20session.PNG?raw=true)

### Configuración - Otra / Actualización FW.
Con este menú puede actualizar el firmware de la unidad de control.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/settings%20firmware%20update.PNG?raw=true)

Se recomienda encarecidamente actualizar el firmware a la última versión por seguridad y funcionalidad.

Consulte el sitio web de ABB para conocer la revisión de SW actual y descargar la última versión de el firmware.

Después de examinar el archivo descargado, utilice el botón "Actualizar archivo" para enviar el nuevo firmware a el dispositivo.

Además, puede encontrar la versión de firmware instalada y el número de serie del dispositivo en la parte inferior de la página web.

------------

### Configuración - Otro / Sistema.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/system%20reset.PNG?raw=true)

En esta sección es posible realizar un reinicio del sistema (para reiniciar el dispositivo con la configuración actual), para restaurar la configuración predeterminada y realizar un apagado seguro.

Después de cualquier cambio en la configuración, le recomiendo que haga un apagado seguro. Para hacerlo, presione el botón "Apagar".

 Si el LED de estado está brilla en verde sin parpadear, y si el LED de red está apagado, puede apagar la fuente de alimentación.

Para iniciar el dispositivo, encienda la fuente de alimentación. El CMS-700 se iniciará automáticamente.

------------

### RED: valores en línea, valores históricos.
La sección "Valores en línea" muestra todos los valores medidos en el lado de la red informando la tendencia del último 10 s.

La sección "Valores históricos" le permite cambiar, acercar o alejar el marco de tiempo en el que se muestran los valores medidos.

Después de seleccionar el parámetro, la resolución y el tiempo de referencia marco, el botón "Exportar" permite al usuario realizar la exportación directa de datos como archivo .CSV.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/mains%20online%20values.PNG?raw=true)

Nota: Si no hay un gráfico visible, es necesario sincronizar la hora del dispositivo con la opción "Establecer la hora manualmente". en el menú Configuración - Otro / Hora.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/MAINS%20HISTORICAL%20VALUES.PNG?raw=true)

------------

### Sucursales: valores en línea, valores históricos.
Aquí es posible visualizar tanto los "Valores en línea" como los "Valores históricos" para las Ramas.

> Primero deben asignarse y configurarse sensores para la medición de ramales (consulte Configuración - Ramas).

> En caso de medición de rama de CC, consulte "Configuración-Ramas" y configure "Fase" como CC. En consecuencia, cuando se muestra "CC" en "Fase", los valores de corriente CC y potencia activa se muestran en esta página.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/BRANCHES%20ONLINE%20VALUES.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/BRANCHES%20HISTORICAL%20VALUES.PNG?raw=true)

------------

### Energía - Red, Grupos, Sucursales.
Aquí es posible visualizar consumos de energía de Red, Grupos y Ramas.

Para Red, los consumos se visualizan por fases (L1, L2 y L3), mientras que para Grupos se visualizan dividido por grupos definidos por el usuario.

Para las ramas, la visualización de energía se divide por sensor; es posible filtrar por fases y / o grupos. Para todos los consumos de energía se tiene un tiempo de inicio, finalización y resolución por definir.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/ENERGY%20MAINS.PNG?raw=true)

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/ENERGY%20GROUPS.PNG?raw=true)

------------

### Energía - Red, Grupos, Sucursales.
El menú Energy - Branches muestra los valores de energía activa para cada sensor individual.

Puedes elegir más sensores para comparar el consumo de energía dentro de un período de tiempo definido.

Puede configurar la pantalla seleccionando un intervalo de fechas y una resolución.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/ENERGY%20BRANCHES.PNG?raw=true)

### Eventos: eventos en línea, eventos históricos.
Las últimas ocurrencias que se establecieron en el menú de configuración de eventos se muestran en "Eventos en línea" página.

Aquí, la tabla se actualiza automáticamente cada segundo y muestra los 18 eventos más recientes.

Filas se pueden ordenar y / o filtrar haciendo clic en los encabezados y seleccionando el valor deseado de las listas desplegables.

El estado del evento se actualiza automáticamente cada segundo para obtener nuevos eventos.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/events-online%20events.PNG?raw=true)

En la página "Eventos históricos" es posible visualizar y exportar ocurrencias según fecha / hora de inicio y finalización definidas por el usuario.

------------

# Modbus.
### Protocolo de comunicación.

### Presentación del protocolo MODBUS.
El protocolo de línea serie Modbus es un protocolo maestro-esclavo. Esto significa que solo un maestro y uno o se pueden conectar más nodos esclavos (máx. 247) al mismo bus serie. Una comunicación Modbus es  siempre iniciada por el maestro y solo hay una transacción al mismo tiempo.

Para más información: www.modbus.org.

Si tiene la intención de utilizar Modbus, solo debe utilizar caracteres ASCII en la interfaz de usuario web. Los caracteres Unicode no aparecer en Modbus.

Descripción de la trama Modbus (modo RTU).

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/ADU%20FRAME.PNG?raw=true)

El tamaño máximo de una trama Modbus RTU es de 256 bytes.
> NOTA: En el modo RTU, los telegramas están separados por un intervalo de silencio de al menos 3,5 veces el carácter. Todo el marco del mensaje debe transmitirse como una cadena continua de caracteres. Si se produce un intervalo de silencio de más de 1,5 caracteres entre dos caracteres, el marco de mensaje se declara incompleto y el receptor debe descartarlo.

### Codificación de datos Modbus.
Modbus utiliza una asignación big-endian para direcciones y elementos de datos. Esto significa que, cuando un número se transmite una cantidad mayor que un solo byte, primero se envía el byte más significativo. Ejemplo: 1234h → primeras 12h luego 34h

------------

### Comunicación a CMS.
### Interfaz física RS-485.
Para comunicarse con el CMS desde un sistema superior, todos los dispositivos (maestros y esclavos) deben tener el mismo velocidad de datos y formato de datos. Estas configuraciones se definen en la interfaz de usuario web, como se describe en el capítulo.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/PARAMETROS%20RS485.PNG?raw=true)

Se debe agregar una resistencia de terminación de línea (120Ω), si es necesario, para CMS-700 con número de serie después de 700K1820000.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/MOSBUS%20RTU%20GRAFICO.PNG?raw=true)

Puede conectar hasta 247 unidades de control a una línea Modbus RTU. Cada unidad de control debe tener un único ID de Modbus (dirección).

### Código de función.
- La operación de lectura en registros con código de acceso "R" o "RW" se define mediante la función 03h "Leer retención Registros "

- La operación de escritura en registros con código de acceso "W" o "RW" se define mediante la función 06h "Write Single Registrarse"

No aplique funciones distintas a las especificadas.

------------

### Códigos de error.
El protocolo Modbus define una forma común de informar errores. Cada solicitud (lectura o escritura) enviada en unidifusión se espera que el modo devuelva un valor en el paquete de la misma estructura. En caso de error en la entrega del mensaje (no es un problema de CRC sino un problema de ejecución de mensajes), la respuesta generada contiene una función código con MSB (80h) configurado y un solo byte que representa el código de error, llamado "código de excepción"

Están disponibles los siguientes códigos de excepción predeterminados:

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/ERRORES%20MODBUS.PNG?raw=true)

### Registros de datos y control.
Un registro es siempre un valor de dos bytes (16 bits), que se puede interpretar como con signo o sin signo valores o que tenga un formato especial.

En caso de datos representados en más de un registro, los registros concatenados contendrán información con MSB en la dirección más baja y LSB en la dirección más alta dentro de concatenados direcciones.

No utilice registros distintos a los especificados.
Nota 1: formato de registro de una palabra para valores actuales.

unsigned = notación de entero sin signo de 16 bits, resolución 0.01 A
firmado = notación de entero con signo de 6 bits, resolución 0.01 A
0000h…7FEFh = 0.00 … 327.51 A
8000h…FFFFh = -327.66 … -0.01 A

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/VALORES%20ESPECIALES%20TABLA.PNG?raw=true)

Nota 2: Formato de registro de palabra doble para valores de potencia y energía de rama.
unsigned = notación de entero sin signo de 32 bits,
signed = 32-bit signed integer notation.

------------

### Valores con significados especiales: potencia de rama calculada y valores de energía.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/VALORES%20ESPECIALES%20TABLA%202.PNG?raw=true)

máscara de bits = operación bit a bit
especial = como se especifica en la descripción del registro.

### Disparador de retención, restablecimiento de valores mínimos y máximos.
La operación de escritura en este registro activa la medición de retención de todos los sensores y / o restablece los valores mínimo y máximo de todos los sensores.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/adress.PNG?raw=true)

Los comandos tienen el siguiente formato de bits: 0000 0000 000T 000R.

• T 1 = medición de retención del gatillo.
• R 1 = Restablecer valores mínimos y máximos.


El comando será reconocido por el mensaje de respuesta en Modbus y por un mensaje corto.

------------

### Mostrar sensor.
"La operación de escritura en este registro inicia o detiene el parpadeo rápido del LED de un sensor para fines de diagnóstico ".

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/shnow%20sensor.PNG?raw=true)

El comando de inicio / parada está en la siguiente posición de formato de bit: 000S 0000 0CCC CCCC.
• C Sensor ID
• S 1 = Inicia el parpadeo rápido del LED
•0 = detiene el parpadeo rápido del LED

Los datos escritos deben especificar un ID de sensor conocido.
Ejemplo: 0x1017 significa "Iniciar parpadeo rápido del LED del sensor con ID 23".

• When sensor is addressed correctly, common response will follow.
• When the sensor ID is not used in the system, and exception response with Modbus exception code 03h “Illegal data value” will follow. (If fast LED blinking was already active, it will be stopped) 

Es posible volver al contenido de la pantalla normal enviando el comando de parada.

------------

### Polaridad de los sensores (para corrientes CC).
Estos registros contienen el valor de corriente nominal configurado y la información de polaridad CC de cada sensor con el siguiente formato de bits:  

000P RRRR RRRR RRRR

• R Reserved for future use
• P DC polarity information
0 = direct, DC current coming out of the cone is displayed positive.
1 = reverse, DC current coming out of the cone is displayed negative.

This setting has influence on all DC values of the specified sensor. 

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/polaridad%20de%20sensores..PNG?raw=true)

This data has to be set user while system configuration. Factory default value is 0000h.

### Serial number (SID), version and bus line of sensors.
These registers contain system information about each sensor.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/tabla%20serial.PNG?raw=true)

• Each sensor has a unique serial number needed for setup procedure on internal CMS bus. 
• HW and SW version of sensor are readable for diagnosis purpose.
• “ID of internal bus line” identifies the Control Unit’s internal bus line the sensor is connected to.

This data is not hold always in registers but will be prepared on read request.

------------

# Simple Network Management Protocol – SNMP.
### Reading of values

The protocol is applicable for the following items:
• Mains parameters
• Calculated values
• Measured branch current values

If you need to record the values of a subsequent measurement, you have to use the SNMP protocol and the external storage system. Historical data in the device is stored with aresolution of 10s.

### Special values for error codes.
In a fail situation you get error codes. Values with special meanings for branch current values (one word, 16bit) are summarized below.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/special%20values%20for%20error%20codes.PNG?raw=true)

------------

Values with special meanings for calculated branch power and energy values (double word, 32bit) are reported below:

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/simple%20network%20tabla%202.PNG?raw=true)

### MIB.
To retrieve data from the device using the SNMP object identifier (OID), the MIB files from the NET-SNMP package should be copied to the correct location on the client station. 

The NET-SNMP package can be downloaded from the link:
https://sourceforge.net/projects/net-snmp/files/net-snmp/5.7.3/

In the downloaded zip package, MIB files are available in directory: net-snmp-5.7.3.zip\ net-snmp-5.7.3\mibs\

The objects used in CMS-700 are defined in SNMPv2-MIB.txt and NET-SNMP-EXTEND- MIB.txt.

![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/SNMP%20objects.PNG?raw=true)

All objects are read-only. In case of a NET-SNMP-EXTEND::nsExtendOutputFull object, the var field is one of variables defined in table Modbus and SNMP Mapping, for example: NET-SNMP-EXTEND::nsExtendOutputFull."TRMSsens1"

To return all TRMSsens values in a single snmpget request, please use the “TRMSsensAll” variable name.

------------





