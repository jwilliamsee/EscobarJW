# Dispositivo THIS
## 1. Introducción
Uno de los pilares más importantes de la arquitectura sustentable es la disminución del consumo energético y el fomento al uso de energías renovables. El aumento de la calidad de vida de los ocupantes de los edificios es otro pilar importante en la arquitectura sustentable, esto se logra manteniendo el interior del edificio confortable, es decir, manteniendo el interior del edificio dentro de los rangos de confort térmico, lumínico y acústico.

Una opción para lograr una reducción en el consumo energético y un aumento de la calidad de vida de los ocupantes es crear dispositivos inteligentes que ayuden a monitorear ciertas variables en el interior de las edificaciones, de esta forma se obtendrán datos que pueden ser utilizados con el fin de crear sistemas o estrategias que permitan la reducción del gasto energético y el mantenimiento de las condiciones de confort en interiores, por ejemplo, la reducción del uso excesivo de sistemas de acondicionamiento de aire, reducción del uso excesivo de luminarias, implementación de estrategias para el aprovechamiento de la luz y ventilación natural, etc.

El dispositivo THIS está diseñado para monitorear las condiciones de confort térmico, lumínico y acústico en interiores, su componente principal es una Raspberry Pi 3 modelo B+, es una computadora del tamaño de una tarjeta de crédito, muy útil porque cuenta con conectividad inalámbrica a internet, ideal para transmitir datos. Además, cuenta con un módulo CJMCU-8128 encargado de medir temperatura y humedad relativa, un módulo GY-30 utilizado para medir la iluminancia, un módulo de micrófono para medir el nivel de presión sonora y para éste último es necesario contar con un conversor analogico-digital ADS1115. Todos los componentes deben conectarse a la Raspberry mediante el bus I2C y los datos recopilados son enviados a Thingsboard.

### 1.1 Sobre los autores
| Nombre | Instituto/Organización | Email |
| :------------: | :------------: | :------------: |
| Oliver Stif Galvez Oliveros | ITZ | oliverstif95@gmail.com |
| Abraham González Castro | UTEZ |   |
| José Manuel Rodríguez Labra | UTEZ |  |
| Victor Zamora Martínez | UTEZ |  |
| Guillermo Barrios del Valle | IER-UNAM | gbv@ier.unam.mx |
| Guillermo Ramírez Zúñiga | IER-UNAM | guraz@ier.unam.mx |

## 2. Alcance
Se necesita realizar la referenciación de los sensores con los que cuenta el dispositivo, una vez realizado, se debe contar con toda la documentación necesaria para ser replicado de manera eficaz.

La audiencia a la que está destinada es:

-  Personal del IER-UNAM que se encuentra trabajando en el proyecto "Edificios demostrativos de diseño bioclimático en clima cálido subhúmedo en el Instituto de Energías Renovables UNAM". Proyecto número 291600 del Fondo de Sustentabilidad Energética.
- Compañeros y personas interesadas en aportar al proyecto para mejorarlo o replicarlo directamente.

## 3. Conceptos y definiciones
### 3.1 Saber como
Es necesario conocer algunas cosas antes de intentar entender muchos puntos del proyecto, como por ejemplo: lectura de planos electrónicos, diseño CAD, conocimiento medio de electrónica, programación, entre otras.

### 3.2 Diseño
Deberá manejar algún software de diseño por computadora, para modificar, replicar el diseño existente e incluso conocer la sección de ensamble de piezas en el software de su preferencia.

### 3.3 Hacer
Fabricar, construir, ensamblar, imprimir, configurar, programar y compilar códigos.

### 3.4 Open source
Por su traducción al español, "fuente abierta" durante el desarrollo del proyecto se busca que todos los programas a usar, sean de fuente abierta para evitar pagos costosos de Licencia, para cada necesidad existe un software de fuente abierta.

### 3.5 Thingsboard
Es una plataforma web que nos ayuda a visualizar gráficamente las variables que estamos midiendo para tener referencias de lo que se está haciendo.

### 3.6 Github
Plataforma web, que sirve como "bodega" para almacenar un proyecto con sus respectivas versiones o modificaciones que pueda sufirir durante el desarrollo, al mismo tiempo ayuda a documentar y a entender la estructura de su funcionamiento.

## 4. Especificaciones de la estructura
### 4.1 Introducción
En esta sección se encuentra la estructura general del proyecto, de forma que sea entendible y que se le pueda dar seguimiento para la lectura del mismo y entender que lleva un orden. Esta forma de estructurar el proyecto es un formato estándar de Open Know-How, cabe mencionar que no es el ideal pero para entender de forma general un proyecto de electrónica es aceptable. El almacenamiento en Github nos ayuda en todo momento a realizar modificaciones que creemos necesarias y sobre todo a tener control total de los cambios que va sufriendo el proyecto durante el desarrollo, si alguna no nos agrada o no es la correcta, podemos regresar sin ningún problema y dejarlo como antes.

### 4.2 Estructura
#### 4.2.1 Formato
El formato de archivo para la documentación del dispositivo H2O es Markdown por su facilidad de uso. Algunos archivos están en formato PDF pero es necesario para una mejor visualización de los esquemas que se muestran en ese formato.

#### 4.2.2 Nombre del archivo
Para los nombres de los archivos, es necesario que no se usen comas, virgulilla o tilde de la ñ, las separaciones de las palabras pueden ser usadas con guiones o sin espacios, pero con una letra mayúscula para saber donde termina e inicia otra palabra, por ejemplo: ArchivoEstructura". Las extensiones de los archivos pueden ser:

- .json | Para los archivos que se realizaron con EasyEDA.
- .md | Para los archivos que son creados en formato de texto Markdown, M Editor, DILLINGER e incluso el archivo README de Github.
- .fzz | Para los archivos que fueron creados en el software de Fritzing, pictogramas de conexiones.
- .ESTEP | Para los archivos de diseño CAD, que pueden ser visualizados en cualquier software de diseño, es formato general.
- .STL | Para los archivos de impresión, para que el diseño de la carcasa del dispositivo pueda ser visualizado al momento de imprimirlo en 3D.
- .zip | Para los archivos de impresión de la placa o PCB, están comprimidos porque son varios archivos.
- .PDF | Para los archivos que si se guardan en otro formato, posiblemente se moverían mucho las líneas, formas, tablas, imágenes, etc. Los archivos que se encontrarán en el repositorio en este formato serán los planos para el diseño de la carcasa.

#### 4.2.3 Vínculos
En algunas secciones de la documentación es necesario nombrar o hacer referencias a rutas externas, pueden ser a imágenes, páginas web, entre otras, simplemente se hace uso de los links originales de la web en cuestión, copiando y posteriormente pegando en la sección correspondiente para no tener que buscar de manera externa, deberán dejar espacios entre título o texto para que no existan errores de posición en el archivo de texto final.

#### 4.2.4 Ubicación del repositorio
El repositorio de todo el proyecto se encuentra en Github, las diferentes carpetas y archivos están alojadas en un solo repositorio, no existe una carpeta raíz, pero sí existe una dirección raíz y es la siguiente:

[**Dispositivo THIS**](https://github.com/AltamarMx/DTHIS)

### 4.3 Información de la web
La página de presentación del proyecto, está en la sección de Github.

El sitio web del formato estándar para documentar es el siguiente:

[**README**](https://github.com/AltamarMx/DTHIS/blob/master/README.md)

### 4.4 Propiedades descriptivas
#### 4.4.1 Título
Dispositivo THIS

Monitor de temperatura, humedad relativa, iluminación y sonido en interiores

#### 4.4.2 Descripción
Energías renovables

Dispositivo diseñado para monitorear variables de confort térmico, lumínico y acústico en edificaciones.

#### 4.4.3 Uso previsto
Control de variable

Envía el valor de la temperatura, humedad relativa, iluminación y presión sonora a Thingsboard cada 5 minutos.

#### 4.4.4 Palabras clave
THIS

Dispositivo

Temperatura

Humedad

Presión sonora

Iluminación

#### 4.4.5 Precauciones y recomendaciones

#### 4.4.6 Contacto primario
 **Inv. A tiempo completo:** Dr. Guillermo Barrios del Valle
 
 **Email:** gbv@ier.unam.mx
 
 **Posdoc.:** Dr. Guillermo Ramírez Zúñiga
 
 **Email:** guraz@ier.unam.mx
 
 #### 4.4.7 Colaboradores
 **Nombre:** Oliver Stif Galvez Oliveros

**Instituto:** Instituto Tecnológico de Zacatepec (ITZ)

**Email:** oliverstif95@gmail.com

 **Nombre:** Abraham Gonzalez Castro

**Instituto:** Universidad Tecnológica Emiliano Zapata (UTEZ)

**Email:** 

 **Nombre:** José Manuel Rodríguez Labra
 
**Instituto:** Universidad Tecnológica Emiliano Zapata (UTEZ)

**Email:** 

 **Nombre:** Victor Zamora Martínez
 
**Instituto:** Universidad Tecnológica Emiliano Zapata (UTEZ)

**Email:** 

#### 4.4.8 Imagen
Representación gráfica del dispositivo THIS
![Imagen](https://github.com/AltamarMx/DTHIS/blob/master/Imagenes/dispositivo_THIS.png)

#### 4.4.9 Etapa de desarrollo
La etapa en la que se encuentra el desarrollo del dispositivo THIS es la de documentación final, realmente el THIS ya funciona bien, según lo establecido pero, falta complementar la información para cuando se tenga todo hecho.

**El porcentaje de avance en las actividades corresponde a un valor máximo de 10% para cada una, para hacer un total de 100%.**

#### Actividades y tiempos para construir el THIS

##### Sugerencias : Dejar actividades, tiempo estimado, notas con referencia a la documentaci'on y cambiar tiempo a horas
|**Actividad**|**Tiempo estimado de ejecución**|**% de avance**|**Pendientes**|**Notas**   |
| :------------: | :------------: | :------------: | :------------: | :------------: |
|**1. Revisión de documentos existentes necesarios para operarlo de acuerdo a la CHECK-LIST**|1-2 horas|10%|   |   |
|   |   |   |   |   |
|**2. Verificar si cuenta con los materiales requeridos**|30 minutos|5%|   |Falta maquinar una placa y serán 30 minutos si ya se tiene todo listo, si no, puede llavarse hasta 1 día|
|componentes electrónicos|carcasa del THIS|Monitor, Raspberry y Sistema Raspbian instalado|Jumper's y cables para conexión|   |
|   |   |   |   |   |
|**3. Leer el manual de operación para entender lo que se hará**|30 minutos|10%|   |   |
|   |   |   |   |   |
|**4. Ver los diagramas de conexión**|30 minutos|10%|   |   |
|   |   |   |   |   |
|**5. Conectar la Raspberry al monitor con los módulos y configurar de acuerdo al manual de operación**|30 minutos|10%|   |   |
|   |   |   |   |   |
|**6. Descargar los códigos e instalarlos en la Raspberry**|30 minutos|10%|   |   |
|   |   |   |   |   |
|**7. Ejecutar los códigos como primeras pruebas**|30 minutos|10%|   |   |
|   |   |   |   |   |
|**8. Verificar si envía datos de telemetría correctamente a Thingsboard**|30 minutos|10%|   |Si no se está enviando datos puede llavar hasta 1 hora para corregir|
|   |   |   |   |   |
|**9. Montar el dispositivo en el lugar requerido**|1 hora|10%|   |   |
|   |   |   |   |   |
|**10. Dejarlo operando durante 48 horas como prueba "Burn it"**|2 días|10%|   |   |
|----------|----------|----------|----------|----------|
|**Resumen**|**%**|**Nota-1**|**Nota-2**|**Nota-3**|
|**Porcentaje de avance total**|95%|Cuestiones estéticas pendientes(cableado, placa PCB de complemento)|Complemento Luminance maps pendiente|   |
|**Pruebas prácticas**|100%|Prueba de funcionamiento en 2 Raspberry|Conexión remota ssh y cableada|   |
|**Por probar**|   |   |   |   |
|1. Luminance maps|2. Manual de montaje||   |   |

------------

#### CHECK-LIST de lo que debe tener el dispositivo
- [x] Lista de costos
- [x] SRC completos
- [x] Pictograma de conexión
- [x] Esquemático de conexión
- [x] Archivos de diseño PCB
- [x] Archivos gerber para el maquinado del PCB
- [x] Lista de materiales
- [x] Planos CAD
- [x] Archivos de diseño CAD
- [x] Archivos STL para impresión 3D
- [x] Manual de operación
- [ ] Manual de ensamble
- [x] Fichas técnicas o datasheet de los módulos, sensores y componentes usados
- [x] Documento de errores, soluciones y recomendaciones

#### 4.4.10 Fue hecho físicamente
El dispositivo sí se ha hecho de forma práctica, es decir, se ha llevado a la práctica para comprobar el funcionamiento del mismo, solo como pruebas de funcionamiento, hace falta la referenciación de sus sensores.

#### 4.4.11 Se ha comprobado la documentación
La réplica del dispositivo usando la estructura aquí mostrada y siguiendo la documentación no se ha realizado, aún está en revisión de estructura de documentación y de archivos factibles para el desarrollo eficiente.

#### 4.4.12 Estándares usados
El estándar de documentación completo, no se ha seguido, pero si se ha usado el estándar para esta documentación de Open Know-How, algunos puntos se han omitido porque al no ser la estructura para documentar proyectos electrónicos, existen puntos que salen sobrando o que definitivamente no aplican para este tipo de proyectos. El link del estándar usado es el siguiente:

[**EstandarOpenKnowHow**](https://app.standardsrepo.com/MakerNetAlliance/OpenKnowHow/src/branch/master/1#a40dfa47-8bff-4e28-9338-3f808ddfe6ae)

### 4.5 Documentación
#### 4.6.1 Punto de entrada de la documentación:

[**Carpeta CAD**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/tree/master/CAD)

En la carpeta CAD se encuentran los archivos del diseño de la carcasa realizado, hasta el momento en FreeCAD.

En la misma carpeta se encuentran planos de la carcasa en formato PDF y los archivos .STL para visualización.

[**Carpeta Diagramas**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/tree/master/Diagramas)

Se encuentra el diagrama de conexiones en PDF. El dispositivo THIS no utiliza una placa PCB.

Tambien se encuentra el archivo con extensión .fzz,  contiene el diagrama de conexión realizado en el software Open source Fritzing.

[**Carpeta Imágenes**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/tree/master/Imagenes)

En esta carpeta están todas las imagenes que se usaron en los archivos del dispositivo.

[**Carpeta Manuales**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/tree/master/Manuales)

En esta carpeta se encuentra un manual de operación del dispositivo.

[**Carpeta Materiales**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/tree/master/Materiales)

En esta carpeta se encuentran, la lista de materiales y de costos, están en una misma.

[**Carpeta SRC**](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/tree/master/SRC)

En esta carpeta está el código principal del dispositivo THIS, que usa los módulos CJMCU-8128, GY-30, el módulo de micrófono y presión sonora y el convertidor analógico-digital ADS1115, así como el módulo de cámara Pi.

### Credenciales para acceder a las raspberry vía ssh

#### THIS principal (THIS OLIVER)
###### Hostname: LATA
###### Username: pi
###### Password: lata123

#### THIS replicado (THIS EEJW)
###### Hostname: LATA2
###### Username: pi
###### Password: lata1234

#### THIS nueva o con nueva SD
###### Usuario: pi
###### Password: raspberrypi

**En caso de que en alguna raspberry para la conexión ssh no se pueda entrar con las credenciales, deberá sustituir el Hostname por la ip de cada raspberry, según en la que no se pueda entrar con las credenciales arriba mencionadas, para saber la ip de la raspberry puede usar métodos en la terminal o de manera gráfica con programas, en Windows hay uno que se llama "Advanced IP Scanner", es muy útil. Para una nueva raspberry o nueva SD, como se quiera ver, las credenciales serán las que vienen por default.**

### Thingsboard

Dashboard del dispositivo THIS en la plataforma de Thingsboard:

Las credenciales para tener acceso se deberán solicitar con alguno de los doctores.

La web (Dashboard) se encuantra aquí:

[**DTHIS**](http://iot.ier.unam.mx:8080/dashboard/347b6380-c9c6-11e9-b63c-1566f7f95663?publicId=0e7066c0-6e70-11e8-b1f3-991d62d050bd)

## 5.0 Bibliografía
[1] Open Know-How https://app.standardsrepo.com/MakerNetAlliance/OpenKnowHow/src/branch/master/1#a40dfa47-8bff-4e28-9338-3f808ddfe6ae

[2] Github https://github.com/

[3] EasyEDA https://easyeda.com/editor

[4] Fritzing https://fritzing.org/

[5] DILLINGER https://dillinger.io/

[6] M Editor.md https://pandao.github.io/editor.md/en.html
