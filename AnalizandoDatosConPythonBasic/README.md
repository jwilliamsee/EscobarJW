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
### En la carpeta "filedata" se encontrarán archivos de excel para usarlos como ejemplo, se irán agregando datos de sensores simulados o físicos en forma de archivos de textos.

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

### Si en alguno de esos intentos de instalación se presenta algún problema, en su mayoría es por la versión de Python que se está usando, en teoría si se está siguiendo estas indicaciones no debería existir detalles de instalación, pero seguramente algunos de ustedes están usando una versión diferente (anteriores), suelen solucionarse con: python -m pip install, la palabra "python" se debe sustituir de acuerdo a la versión que se tenga instalado, por ejemplo para algunas versiones es: "py3", "python3", entre otros, una de esas líneas de código es:

```
py3 -m pip install 
```

### Si aún sustituyendo esas líneas iniciales no se encontró solución, de acuerdo a la versión de Python instalado, se puede encontrar la solución [**aquí**](https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages).
