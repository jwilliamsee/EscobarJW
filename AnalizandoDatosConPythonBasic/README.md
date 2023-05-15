<center><img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/mylogo.png?raw=true" title="JW" alt="mylogo" height="80" width="80"></center>

## Cabe mencionar que este mini-curso es un resumen del curso original de Ansys enfocado al procesamiento de datos, la intención es mostrar el procedimiento de forma más sencilla y en español, para que las personas que quieren empezar y no tienen nada de conocimientos con Python también se animen como yo, a conocer este lenguaje de programación y hacerlo parte de su día a día, mi propósito es aprender con la práctica y al mismo tiempo documentar como estoy avanzando para compartir el conocimiento.

## Recuerden que las herramientas están en la web al alcance de todos, pocos se atreven a procesar todo el trabajo de aprendizaje de nuevas herramientas, así que depende de ustedes hasta donde quieren llegar.

# El link del curso original lo encuentras dando click aquí: [**Curso original**](https://courses.ansys.com/index.php/courses/intro-to-python/lessons/prerequisites-installation-of-python/)

<img src="https://cdn3.emoji.gg/emojis/1850-python-logo.png" title="Python" alt="HTML" width="50" height="50"/>
<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/sunglasses.png?raw=true" title="sunglasses" alt="HTML" width="50" height="50"/>
<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/exel.png?raw=true" title="Exel" alt="HTML" width="50" height="50"/>
<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/snake.png?raw=true" title="snake" alt="HTML" width="50" height="50"/>

### El propósito de este mini-curso es para el procesamiento de gran cantidad de datos que son adquiridos por ejemplo, en la obtención de medidas con algún sensor en la indutria, alguna prueba que realicemos físicamente pero simplemente nos quedamos con esos datos de medición y no sabemos como interpretarlos, que significado darle o que conclusiones obtener con esos datos almacenados, la intención es poder darle una intrepretación gráfica a todos esos datos.
# Cómo se hará?
### Después de obtener archivos de texto con las medidas o con información valiosa para nosotros, se procesará con líneas de código en Python, esos datos serán mostrados finalmente en gráficas para darle la interpretación que a nosotros más nos convenga, se mostrará el procedimiento con un paso a paso, archivos muestras como ejemplos y videos del procedimiento.
### En la carpeta "filedata" se encontrarán archivos con extensión .csv para usarlos como ejemplo, se irán agregando datos de sensores simulados o físicos en forma de archivos de textos.

# *Indicaciones:*
#### Para poder escribir textos de procesos o avances de tus códigos debes tener alguno de los editores que a continuación se muestran, puede ser "vs code", "notepad++" o "vim", eso dependerá de tus gustos o de tu familiaridad con alguno, yo te recomiendo que instales *vs code*, con VS Code podrás trabajar prácticamente todo lo relacionado a este mini-curso, desde leer o abrir los textos del curso, abrir y visualizar los archivos de datos con extensión .csv sin abrir Excel, apertura de Jupyter notebook para escribir código de python o bien si lo que prefieres es trabajar directamente con líneas de código y estar en contacto con el entorno de programación de "raíz", también funciona como un IDE (Integrated Development Environment) y lo mejor es que desde ahí puedes usar la terminal para instalar librerías de python que usaremos durante el mini-curso, instalar otros IDEs y podrás probar ahí mismo el código que vas escribiendo.

**Visual Studio Code** <img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/vscode.png?raw=true" title="vscode" alt="HTML" width="40" height="40"/>
**Notepad++** <img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/notepad.png?raw=true" title="notepad" alt="HTML" width="40" height="40"/>
**Vim** <img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/vim.png?raw=true" title="vim" alt="HTML" width="40" height="40"/>

#### En este link puedes descargar [**Visual Studio Code**](https://code.visualstudio.com/download)<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/vscode.png?raw=true" title="vscode" alt="HTML" width="40" height="40"/>

#### Aquí tienes el link para descargar [**Python**](https://www.python.org/)<img src="https://cdn3.emoji.gg/emojis/1850-python-logo.png" title="Python" alt="HTML" width="40" height="40"/>

### Como sugerencia si nunca has instalado Python, ver los pasos para que todo lo que hagas con Python en cuanto a código y almacenamiento se guarde en "Path", es la mejor opción, si realizas las configuraciones mencionadas antes de instalar Python, te ahorrarás mucho trabajo, pero si ya tienes instalado Python, tendrás que hacer algunas configuraciones importantes, en este tutorial omitiré ese paso porque el objetivo es la visualización gráfica de datos. En el link del curso original que he compartido arriba, podrás ver todo al respecto.

### Como aclaración, los créditos totales del curso es para el autor en Ansys, no me adjudico nada del curso, mi intención es digerir un poco la información para las personas no tan experimentadas con Python y al mismo tiempo, sigo aprendiendo con la práctica.

#### En la terminal de VS Code puedes comprobar si realmente has instalado Python y ver la versión que tienes instalado, simplemente con escribir la palabra Python en tu terminal:
```python
Python
```

<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/VersionPython.PNG?raw=true" title="VersionPython" alt="HTML" width="800" height="150"/>

#### Deberás ver una versión igual a 3.8 o mayor, porque más adelante se usará  ipython y Jupyther, ambos están disponibles en la versión de Python mayor a 3.8.

# Ahora instalaremos las librerías necesarias para el tratamiento de datos

### De forma muy general, así como nosotros vamos a leer líneas de código, existen códigos o programación que ya existen y fueron hechos por otras personas, a esos programas o códigos en Python se les conoce como "librerías" o "paquetes", nos facilitan mucho la vida para realizar otros códigos, de lo contrario, tendríamos que hacer todo el código desde cero y sería más difícil.
Las siguientes indicaciones nos ayudan a instalar 3 librerías que usaremos constantemente:

```
pip install jupyter
```
### Debes copiar la línea de código escrita arriba y pegar en una terminal, como había mencionado antes, les sugiero que sea en VS Code, se verá algo similar a lo que se muestra en la imagen.

<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/pipjupyter.png?raw=true" title="pipjupyter" alt="HTML" width="800" height="600"/>

### La siguiente línea de código es:

```
pip install numpy 
```
<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/pipnumpy.png?raw=true" title="pipnumpy" alt="HTML" width="800" height="130"/>

### La siguiente línea de código es:

```
pip install matplotlib 
```
<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/pipmatplotlib.png?raw=true" title="pipmatplotlib" alt="HTML" width="800" height="300"/>

### Si en alguno de esos intentos de instalación se presenta algún problema, en su mayoría es por la versión de Python que se está usando, en teoría si se está siguiendo estas indicaciones no debería existir detalles de instalación, pero seguramente algunos de ustedes están usando una versión diferente o una más actualizada, suelen solucionarse con: python -m pip install, la palabra "python" se debe sustituir de acuerdo a la versión que se tenga instalado, por ejemplo para algunas versiones es: "py3", "python3", entre otros, una de esas líneas de código es:

```
py3 -m pip install 
```

### Si aún sustituyendo esas líneas iniciales no se encontró solución, de acuerdo a la versión de Python instalado, se puede enconstrar la solución [**aquí**](https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages).

### A continuación vamos a instalar "Ipython", Ipython es una herramienta de Python que nos sirve para escribir código y desde ahí podemos ejecutar el mismo código, en pocas palabras, Ipython es un intérprete de código escrito en python, en inglés literalemente significa "Interactive python", a diferencia de otros intérpretes, en Ipython puedes ir probando tus líneas de código casi al instante, mientras que con otros, necesitarías el editor de texto  para escribir código y aparte una terminal para ejecutar tu código y probar si funciona, para empezar está muy bien, la intención de darte a conocer Ipython es que vayas probando líneas de código básico, se verá algo similar a ésto:

<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/InstallIpython.PNG?raw=true" title="InstallIpython" alt="HTML" width="800" height="300"/>

### La línea de código para instalar Ipython es:

```
pip install ipython 
```


### En mi caso al realizar la instalación me indicó al final que había una nueva versión de "pip", pip es un gestor de instalación o administrador de instalación que por default usa Python, por eso me indicó que había una nueva versión, lo que hice fué hacer caso a la indicación y lo actualicé:

<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/pipversionnew.PNG?raw=true" title="NewVersionPip" alt="HTML" width="800" height="300"/>

### En mi caso, por alguna extraña razón (actualizaré cuando conozca las razones), cuando requiero ejecutar ipython en una terminal cmd de Windows no me deja interactuar con ipython, investigué otra opción y es la siguiente:

### Realmente no es otra opción, se realiza como a continuación les muestro, seguramente hay otras formas y se puede llegar al mismo punto, recordemos que el objetivo de esta instrucción es para instalar el intérprete interactivo de Python: **"Ipython"**.

#### Nos dirigimos al buscador de Windows y buscamos "PowerShell", el nombre completo es "Windows PowerShell", le damos click al que tiene el logo o símbolo de sistema y nos abre una especie de cmd, en pocas palabras es un administrador de sistema en la que se ejecuta líneas de código para gestionar gran cantidad de información y es usado por DevOps o desarrolladores, no es común que una persona use estas herramientas pero considero que aprender un lenguaje de programación debería ser obligatorio en las escuelas, sin importar que carrera universitaria o técnica se estudia. A continuación se muestra una imagen como la que ustedes deberán ver:

![](https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/Powershell.PNG?raw=true)

#### Después de haber instalado "ipython", podemos escribir la línea de código con el nombre y nos abrirá lo que queremos ver, el intérprete estará funcionando y listo para probar nuestras líneas de código para pruebas rápidas.

![](https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/Powershell1.PNG?raw=true)

### Ahora como ya tenemos instalado ipython podemos ejecutarlo en una terminal cmd como la que todos conocemos y hemos usado en algún momento.

#### Después de haber instalado ipython y saber que ya tenemos nuestras bibliotecas listas para ser usadas, podemos empezar con revisiones rápidas, nos dirigimos a una terminal, puede ser cmd, Windows PowerShell o desde una terminal en Visual Studio Code, en nuestro caso usaremos nuestras primeras pruebas con el PowerShell de Windows.
#### Cuando entramos a la terminal tenemos que buscar la carpeta donde estan nuestros datos a analizar, el archivo con el que trabajaremos, sí o sí tenemos que trabajar dentro de la carpeta que contiene el archivo, de lo contrario nunca podremos manipular el archivo. Usamos cd seguido del nombre de nuestra carpeta, por ejemplo cuando abrimos nuestra terminal nos dirige al espacio con el nombre de usuario, en mi caso es JWilliams_E_E, desde ahí tengo que buscar mi carpeta donde contiene mi archivo con el que trabajaré y avanzamos con cd, cd Desktop, cd nombre-de-mi-carpeta, cd hasta-ubicarlo y en cuando llegamos a la ubicación del archivo ejecutamos ipython.
#### Después de entrar a ipython, importamos numpy para hacer matrices y funciones matemáticas, sin numpy no podríamos hacerlo.
<img src="https://github.com/jwilliamsee/BancoDeImagenes/blob/main/IMAGENES/Ipython123.PNG?raw=true" title="NewVersionPip" alt="HTML" width="800" height="300"/>

#### Lo que comentaba anteriormente lo pueden ver en la imagen, se usa el cd para ir nuestras carpetas y cuando llegamos a la carpeta que contiene el archivo, ejecutamos ipython, ahora explicaré los números 1, 2 y 3 que aparecen en la imagen de color rojo, el núm. 1 "numpy.loadtxt()", eso significa que estamos llamando un archivo de texto, el núm. 2 se refiere al nombre del archivo que debe ir dentro de los paréntesis y con comilla simple " ' ", la coma la usamos para separar una instrucción de otra, en este caso como estamos haciendo uso del numpy.loadtxt le indicamos que los datos que se nos presentan en el archivo llamado 'experiment01.csv' se delimiten con una coma " , " (núm. 3), dicho de otra forma es algo como: numpy.loadtxt por favor abre el archivo de texto que se llama experiment01.csv y los datos que están ahí separalo con una coma.

### Este curso lo trabajo en mis tiempos libres, hay avances constantes.
#This page is updating constantly 

