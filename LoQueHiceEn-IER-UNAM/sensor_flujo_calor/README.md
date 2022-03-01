# Dispositivo “Flujo de calor”.

# 1.0 Introducción.
En este repositorio se encuentran los archivos necesarios para dar seguimiento al proyecto “Sensores de flujo de calor” el cual tiene como objetivo medir el flujo de calor en muros. Este proyecto se realizó de dos maneras.
 La primera es utilizando un ESP32 para leer el voltaje y convertirlo a unidades de flujo de calor ( 𝑊 / 𝑚2 ), para lo cual, es necesario realizar un sistema de acondicionamiento de señal que permita interpretar la señal eléctrica proveniente del sensor de calor y amplificarla.
 La segunda manera es la utilización de un PSoC 5, el cual cuenta con la resolución necesaria para conectar el sensor directamente, es decir, sin tener que amplificar la señal del voltaje; adicionalmente, se utiliza el ESP32 para poder publicar los datos, ya que el PSoC no cuenta con un módulo wifi como lo tiene el ESP32.

### 1.1 Sobre los autores.

|Nombre|Instituto/Organización|Email|
| ------------ | ------------ | ------------ |
|Gonzalo Octavio Gaona Terrones|ITZ|gonzalogaona96@gmail.com|
|Guillermo Barrios del Valle|IER-UNAM|gbv@ier.unam.mx|
|Guillermo Ramírez Zúñiga|IER-UNAM|guraz@ier.unam.mx|
------------

# 2 Alcance.

------------

El dispositivo tiene como alcance, en esta etapa, contar con toda la documentación necesaria para ser replicado de manera eficaz y eficientemente, después de ser trabajado por un grupo de personas se espera que el proyecto tenga todo lo que se necesita para que otras personas puedan entender el funcionamiento y requisitos de operación.

La audiencia a la que está destinada es:

- Por el momento a personal del IER-UNAM que se encuentra trabajando en el proyecto "Edificios demostrativos de diseño bioclimático en clima cálido subhúmedo en el Instituto de Energías Renovables UNAM".
Proyecto número 291600 del Fondo de Sustentabilidad Energética.
- Compañeros que se interesen en aportar al proyecto para mejorar o para replicarlo directamente.

------------

# 3. Conceptos y definiciones.

### 3.1 Saber cómo.

Es necesario conocer algunas cosas antes de intentar entender muchos puntos del proyecto, como, por ejemplo: lectura de planos electrónicos, conocimiento medio de electrónica, programación, entre otras.

### 3.2 Diseño

Deberá manejar algún software de diseño por computadora, para modificar, replicar el diseño existente. 

### 3.3 Hacer

Conectar, programar y compilar códigos.

### 3.4 Open source.

Por su traducción al español, "fuente abierta" durante el desarrollo del proyecto se busca que todos los programas a usar, sean de fuente abierta para evitar pagos costosos de Licencia, para cada necesidad existe un software de fuente abierta.

### 3.5 Thingsboard.

Es una plataforma web que nos ayuda a visualizar en tiempo real las variables que estamos midiendo.

### 3.6 Github.

Plataforma web, que sirve como para almacenar un proyecto con sus respectivas versiones o modificaciones que pueda sufrir durante el desarrollo, al mismo tiempo ayuda a documentar y a entender la estructura de su funcionamiento.

------------

# 4.0 Especificaciones de la estructura.

### 4.1 Introducción.

En esta sección se encuentra la estructura general del proyecto, de forma que sea entendible y que se le pueda dar seguimiento para la lectura del mismo y entender que lleva un orden.
Esta forma de estructurar el proyecto es un formato estándar de Open Know-How, cabe mencionar que no es el ideal, pero para entender de forma general un proyecto de electrónica es aceptable.
El almacenamiento en Github nos ayuda en todo momento a realizar modificaciones que creemos necesarias y sobre todo a tener control total de los cambios que va sufriendo el proyecto durante el desarrollo, si alguna no nos agrada o no es la correcta, podemos regresar sin ningún problema y dejarlo como antes.

### 4.2 Estructura.

### 4.2.1 Formato.

El formato de archivo para la documentación del dispositivo sensor_flujo_calor es Markdown por su facilidad de uso.

### 4.2.2 Nombre del archivo.

Para los nombres de los archivos, es necesario que no se usen comas, virgulilla o tilde de la ñ, las separaciones de las palabras pueden ser usadas con guiones o sin espacios, pero con una letra mayúscula para saber dónde termina e inicia otra palabra, por ejemplo: ArchivoEstructura".
Las extensiones de los archivos pueden ser:

- .md | Para los archivos que son creados en formato de texto Markdown, M Editor, DILLINGER e incluso el archivo README de Github.

### 4.2.3 Vínculos.

En algunas secciones de la documentación es necesario nombrar o hacer referencias a rutas externas, pueden ser a imágenes, páginas web entre otras, simplemente se hace uso de los links originales de la web en cuestión, copiando y posteriormente pegando en la sección correspondiente para no tener que buscar de manera externa, deberán dejar espacios entre título o texto para que no existan errores de posición en el archivo de texto final.

#### 4.2.4 Ubicación del repositorio.

El repositorio de todo el proyecto se encuentra en Github, las diferentes carpetas y archivos están alojadas en un un solo repositorio, no existe una carpeta raíz, pero sí existe una dirección raíz y es la siguiente:

[Sensor_calor]( https://github.com/AltamarMx/sensor_flujo_calor)

### 4.3 Información de la web.

La página de presentación del proyecto, está en la sección de Github.

El sitio web del formato estándar para documentar es el siguiente:

[README]( https://github.com/AltamarMx/sensor_flujo_calor/blob/main/README.md)

### 4.4 Propiedades descriptivas.

### 4.4.1 Título.

##### Dispositivo sensor_flujo_calor.
##### Medidor del flujo de calor.

### 4.4.2 Descripción.

##### Energías renovables
##### Dispositivo pensado para el uso de medición del flujo de calor y preservar el cuidado del recurso en edificaciones, donde existe gran demanda del mismo

### 4.4.3 Uso previsto

##### Control de variable
###### Informa al usuario el consumo de agua de un lugar donde existe gran consumo del recurso, puede ser cuantificado para conocer exactamente en que momento se ha consumido más y con base a esa información pueden aplicarse estrategias para mantener un consumo menor o aplicar ciertas medidas que ayuden a disminuirlo.

### 4.4.4 Palabras clave

##### sensor_flujo_calor
##### Electrónica
##### Dispositivo
##### Medidor del flujo de calor.

### 4.5.5 Contacto primario

**Inv. A tiempo completo:** Dr. Guillermo Barrios del Valle

**Email:** gbv@ier.unam.mx



**Posdoc.:** Dr. Guillermo Ramírez Zúñiga

**Email:** guraz@ier.unam.mx

### 4.5.7 Colaboradores


**Nombre:** Gonzalo Octavio Gaona Terrones.

**Instituto:** Instituto Tecnológico de Zacatepec (ITZ).

**Email:** gonzalogaona96@gmail.com


### 4.5.6 Imagen.

Representación gráfica del dispositivo sensor_flujo_calor

![]( https://github.com/AltamarMx/sensor_flujo_calor/blob/main/Imagenes/149339853_865312114030147_6079459958832472293_n.png)
Y
![]( https://github.com/AltamarMx/sensor_flujo_calor/blob/main/Imagenes/150366421_449064419566301_5391584911727403617_n.png)


### 4.5.7 Etapa de desarrollo.

La etapa en la que se encuentra el desarrollo del dispositivo sensor_flujo_calor, es la de documentación, se espera que sea la penúltima etapa, para poder ser replicado de forma eficiente y eficaz.

### 4.5.8 Fue hecho físicamente.

El dispositivo sí se ha hecho de forma práctica, es decir, se ha llevado a la práctica para comprobar el funcionamiento del mismo, solo como pruebas de funcionamiento, el dispositivo completo. 

### 4.5.9 Se ha comprobado la documentación.

La réplica del dispositivo usando la estructura aquí mostrada y siguiendo la documentación no se ha realizado, aún está en revisión de estructura de documentación y de archivos factibles para el desarrollo eficiente.

### 4.6 Documentación.

### 4.6.1 Punto de entrada de la documentación:


### Carpeta [Diagramas]( https://github.com/AltamarMx/sensor_flujo_calor/tree/main/Diagramas)

En la carpeta de Diagramas se encuentra el diagrama utilizado para el ESP32.

### Carpeta [Imagenes]( https://github.com/AltamarMx/sensor_flujo_calor/tree/main/Imagenes)

En esta carpeta están todas las imagenes que se usaron en los archivos de los manuales y otras imagenes necesarias para el complemento del dispositivo sensor_flujo_calor, que en todas se mencionan en algún archivo existente en el repositorio.

### Carpeta [Materiales]( https://github.com/AltamarMx/sensor_flujo_calor/tree/main/Materiales)

En la carpeta "Materiales" se encuentran un archivo con extensión md.
1. En el archivo Lista_material se encuentran los materiales que se necesitan para el circuito de ganacia.

### Carpeta [SRC]( https://github.com/AltamarMx/sensor_flujo_calor/tree/main/SCR)

En esta carpeta está los códigos para el sensor de flujo de calor, para los dos microcontroladores, ESP32 Y PSoC 5.

### Thingsboard

Dashboard del dispositivo de Flujo de calor en la plataforma de Thingsboard:

Flujo_calor_Gonzalo

Las credenciales para tener acceso se deberán solicitar con alguno de los doctores.

La web (Dashboard) se encuantra aquí:

[**Flujo_calor_Gonzalo**](http://iot.ier.unam.mx:8080/dashboard/5edaef40-5df1-11eb-9c3f-d1ead9980bc3?publicId=0e7066c0-6e70-11e8-b1f3-991d62d050bd)

------------

# 5.0 Bibliografía

[1] Github
https://github.com/

[2] DILLINGER
https://dillinger.io/

[3] M Editor.md
https://pandao.github.io/editor.md/en.html


