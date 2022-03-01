# abb_energia
Repositorio para el proyecto de medición de energía eléctrica usando el sistema ABB
# SISTEMA ABB  PARA MEDICION ELECTRICA CMS 700
## 1.0 INTRODUCCIÓN.

Diferentes tecnologías de la actualidad ofrecen la medición de circuitos energéticos, con la finalidad de mejorar el consumo de energía y lograr una eficiencia energética óptima. Para ello se realizan mediciones de diferentes parámetros que son clave para identificar los consumos excesivos, generar estadísticas de los consumos, identificar áreas de oportunidad para lograr la eficiencia energética y de esta forma reducir el impacto ambiental que tiene al generar energía. Dentro de todas las tecnologías que brindan apoyo en la medición de circuitos y dispositivos eléctricos y electrónicos, se encuentran los dispositivos que se les hace llamar como Unidades de control ABB, los cuales ofrecen extensos beneficios que facilitan la medición de distintos parámetros dentro del circuito eléctrico, entre ellos, factor de potencia, potencia activa, voltaje, corriente, potencia aparente y potencia reactiva, todos ellos en tiempo real mediante transformadores de corriente de la misma gama. Los transformadores de corriente “CT PRO XT ABB” mediante un principio de operación “inductivo” miden los parámetros mencionados para ofrecer en tiempo real los datos de cada línea del circuito eléctrico trifásico. Es por lo anterior que el siguiente trabajo describe los diferentes pasos que se llevaron a cabo para la medición de los parámetros eléctricos ya mencionados utilizando tecnología ABB específicamente la unidad central de control CMS-700 ABB y los transformadores de corriente “CT PRO XT ABB” ; mismos que son de gran importancia conocer para identificar el estado y la operación física de la instalación eléctrica, así también, para incorporarlo al proyecto “Edificios demostrativos de diseño bioclimático en clima cálido subhúmedo”. En el “Instituto de Energías Renovables UNAM (universidad Autónoma de México.”, proyecto No. 291600 del Fondo de Sustentabilidad Energética.

## 1.1 Sobre los autores 
![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/tablaAutores..PNG?raw=true)
## 2 Alcance.
El sistema ABB CMS-700  tiene como alcance, en esta etapa, contar con toda la documentación necesaria para ser replicado de manera eficaz y eficientemente, después de ser trabajado por un grupo de personas se espera que el proyecto tenga todo lo que se necesita para que otras personas puedan entender el funcionamiento y requisitos de operación.

La audiencia a la que está destinada es:

- Por el momento a personal del IER-UNAM que se encuentra trabajando en el proyecto "Edificios demostrativos de diseño bioclimático en clima cálido subhúmedo en el Instituto de Energías Renovables UNAM". Proyecto número 291600 del Fondo de Sustentabilidad Energética.

- Compañeros que se interesen en aportar al proyecto para mejorar o para replicarlo directamente.

## Conceptos y definiciones.
### 3.1  Saber como
Es necesario conocer algunas cosas antes de intentar entender muchos puntos del proyecto, como por ejemplo: lectura de planos electrónicos, diseño CAD, conocimiento medio de electrónica, programación, entre otras.

### 3.2 Diseño.
Deberá manejar algún software de diseño por computadora, para modificar, replicar el diseño existente e incluso conocer la sección de ensamble de piezas en el software de su preferencia.

### 3.3 Hacer
Fabricar, construir, ensamblar, imprimir, configurar, programar y compilar códigos.

### 3.4  Open source
Por su traducción al español, "fuente abierta" durante el desarrollo del proyecto se busca que todos los programas a usar, sean de fuente abierta para evitar pagos costosos de Licencia, para cada necesidad existe un software de fuente abierta.

### 3.5 Github
Plataforma web, que sirve como "bodega" para almacenar un proyecto con sus respectivas versiones o modificaciones que pueda sufirir durante el desarrollo, al mismo tiempo ayuda a documentar y a entender la estructura de su funcionamiento.

# 4.0 Especificaciones de la estructura
### 4.1 Introducción.
En esta sección se encuentra la estructura general del proyecto, de forma que sea entendible y que se le pueda dar seguimiento para la lectura del mismo y entender que lleva un orden. Esta forma de estructurar el proyecto es un formato estándar de Open Know-How, cabe mencionar que no es el ideal pero para entender de forma general un proyecto de electrónica es aceptable. El almacenamiento en Github nos ayuda en todo momento a realizar modificaciones que creemos necesarias y sobre todo a tener control total de los cambios que va sufriendo el proyecto durante el desarrollo, si alguna no nos agrada o no es la correcta, podemos regresar sin ningún problema y dejarlo como antes.

### 4.2 Estructura.
### 4.2.1 Formato.
El formato de archivo para la documentación del dispositivo H2O es Markdown por su facilidad de uso. Algunos archivos están en formato PDF pero es necesario para una mejor visualización de los esquemas que se muestran en ese formato.

### 4.2.2 Nombre del archivo.
Para los nombres de los archivos, es necesario que no se usen comas, virgulilla o tilde de la ñ, las separaciones de las palabras pueden ser usadas con guiones o sin espacios, pero con una letra mayúscula para saber donde termina e inicia otra palabra, por ejemplo: ArchivoEstructura". Las extensiones de los archivos pueden ser:

- .json | Para los archivos que se realizaron con EasyEDA.
- .md | Para los archivos que son creados en formato de texto Markdown, M Editor, DILLINGER e incluso el archivo README de Github.
- .fzz | Para los archivos que fueron creados en el software de Fritzing, pictogramas de conexiones.
- .ESTEP | Para los archivos de diseño CAD, que pueden ser visualizados en cualquier software de diseño, es formato general.
- .STL | Para los archivos de impresión, para que el diseño de la carcasa del dispositivo pueda ser visualizado al momento de imprimirlo en 3D.
- .zip | Para los archivos de impresión de la placa o PCB, están comprimidos porque son varios archivos.
- .PDF | Para los archivos que si se guardan en otro formato, posiblemente se moverían mucho las líneas, formas, tablas, imágenes, etc. Los archivos que se encontrarán en el repositorio en este formato serán los planos para el diseño de la carcasa.

### 4.2.3 Vínculos.
En algunas secciones de la documentación es necesario nombrar o hacer referencias a rutas externas, pueden ser a imágenes, páginas web entre otras, simplemente se hace uso de los links originales de la web en cuestión, copiando y posteriormente pegando en la sección correspondiente para no tener que buscar de manera externa, deberán dejar espacios entre título o texto para que no existan errores de posición en el archivo de texto final.

### 4.2.4 Ubicación del repositorio.
El repositorio de todo el proyecto se encuentra en Github, las diferentes carpetas y archivos están alojadas en un un solo repositorio, no existe una carpeta raíz, pero sí existe una dirección raíz y es la siguiente:

![](https://github.com/AltamarMx/SensorH2O/raw/master/Imagenes/LogoGithubB.jpg?raw=true)

[abb_energia](https://github.com/AltamarMx/abb_energia "abb_energia")

### 4.3 Información de la web.
La página de presentación del proyecto, está en la sección de Github.

El sitio web del formato estándar para documentar es el siguiente:

[README](https://github.com/AltamarMx/abb_energia/blob/main/README.md "README")

### 4.4 Propiedades descriptivas.
### 4.4.1 Título.
SISTEMA ABB
Medidor de parametros eléctricos en una instalación eléctrica.

### 4.4.2 Descripción
Energías Renovables.
Dispositivo pensado para el uso de medición de parametros eléctricos  y preservar el cuidado del recurso en edificaciones, donde existe gran demanda del mismo.

### 4.4.3 Uso previsto.
Informa al usuario sobre el consumo de energía de una o varias lineas de la instalación eléctrica trifásica,puede ser cuantificado para conocer exactamente en que momento se ha consumido mas y con base a esa información pueden aplicarse estrategias para mantener un consumo menor o aplicar ciertas medidas que ayuden a disminuirlo.

### 4.4.4 Palabras clave

Dispositivo
ABB CMS-700
ABB CT XT PRO

### 4.4.5 Precauciones y recomendaciones
S on recomendaciones para operar el dispositivo ABB, pueden existir más, esto dependiendo del usuario, ya que pueden surgir nuevas dudas, en el siguiente link se ofece información para aclarar dudas.
[manual de operación](https://github.com/AltamarMx/abb_energia/tree/main/Manuales "manual de operación")

### 4.5.6 Contacto primario.
Inv. A tiempo completo: Dr. Guillermo Barrios del Valle

Email: gbv@ier.unam.mx

Posdoc.: Dr. Guillermo Ramírez Zúñiga

Email: guraz@ier.unam.mx

### 4.5.7 Colaboradores
Nombre: Leana Cobos Emmanuel 

Instituto: Instituto Tecnologico de Zacatepec.

Email: cobosbatero@gmail.com

### 4.5.7 Imagen
![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/ABB%20CMS-700.PNG?raw=true)
![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/Arquitectura%20ABB%20CMS-700.PNG?raw=true)
![](https://github.com/LEANA14/SISTEMA-ABB/blob/main/Imagenes/mains%20online%20values.PNG?raw=true)

### 4.5.8 Etapa de desarrollo.
La etapa en la que se encuentra el desarrollo del dispositivo ABB CMS-700, es la de documentación, se espera que sea la penúltima etapa, para poder ser replicado de forma eficiente y eficaz.

### 4.5.9 Fue hecho físicamente
El dispositivo fue llevado a la prueba fisica donde se colocaron los sensores o de otra forma llamados transformadores de corriente, se habilitó la interfaz de usuario, se intentó vincular mediante microcontroladores, sin embargo no fue exitoso por su incopatibilidad. Por otro lado se llevo a pruebas durante un periodo largo de tiempo.

### 4.5.10 Se ha comprobado la documentación.

La réplica del dispositivo usando la estructura aquí mostrada y siguiendo la documentación no se ha realizado, aún está en revisión de estructura de documentación y de archivos factibles para el desarrollo eficiente.

### 4.5.11 Estándares usados
El estándar de documentación completo, no se ha seguido, pero si se ha usado el estándar para esta documentación de Open Know-How, algunos puntos se han omitido porque al no ser la estructura para documentar proyectos electrónicos, existen puntos que salen sobrando o que definitivamente no aplican para este tipo de proyectos. El link del estándar usado es el siguiente:

[EstandarOpenKnowHow](https://app.standardsrepo.com/MakerNetAlliance/OpenKnowHow/src/branch/master/1#a40dfa47-8bff-4e28-9338-3f808ddfe6ae "EstandarOpenKnowHow")

### 4.6 Documentación
### 4.6.1 Punto de entrada de la documentación:

#### Carpeta [Diagramas](https://github.com/LEANA14/SISTEMA-ABB/tree/main/Diagramas "Diagramas")
En la carpeta diagramas  se encuentrael diagrama esquematico de conexión del sistema ABB, la unidad de control cms-700 .jpg en la cual se detalla la conexión de los sensores y/o transformadores de corriente .
Así también se añade una ilustración alusiva a la conexión de los transformadores de corriente.

#### Carpeta [Imagenes ](https://github.com/AltamarMx/abb_energia/tree/main/Imagenes "Imagenes ")
En esta carpeta están todas las imagenes que se usaron en los archivos de los manuales y otras imagenes necesarias para el complemento del dispositivo ABB CMS-700, que en todas se mencionan en algún archivo existente en el repositorio.

Carpeta [Manuales](https://github.com/AltamarMx/abb_energia/tree/main/Manuales "Manuales")
En esta carpeta se encuentran dos archivos, los cuales corresponden  tanto a la configuración y operación de la unidad de control CMS-700 ABB. 
Así también como de la operación y de la manera correcta de instalar los transformadores de corriente CT XT PRO.

Carpeta [SRC](https://github.com/AltamarMx/abb_energia/tree/main/SRC "SRC")
En esta carpeta se encuentra detallado el codigo que servirá para la visualización de datos correspondientes al periodo que se requiere. Esto haciendo uso de la plataforma "jupyter notebook" .


### 5.0 Bibliografía
[1] Open Know-How https://app.standardsrepo.com/MakerNetAlliance/OpenKnowHow/src/branch/master/1#a40dfa47-8bff-4e28-9338-3f808ddfe6ae

[1] Github https://github.com/

[2] DILLINGER https://dillinger.io/

[3] M Editor.md https://pandao.github.io/editor.md/en.html
