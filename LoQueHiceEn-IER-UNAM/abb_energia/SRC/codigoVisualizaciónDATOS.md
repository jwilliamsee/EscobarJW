# Codigo para visualización de datos del sistema ABB CMS-700

En el siguiente código describe la visualización de un archivo descargado directamente de la plataforma de usuario del sistema ABB CMS-700, el cual tiene como finalidad, reordenar el formato del archivo descargado, debido a que el formato del archivo se tiene por formato predeterminado  la extensión .CSV.

Por lo tanto al importar el archivo al block de programación "jupyter notebook" e importar la libreria "pandas", la cual ayudará a la visualización de los datos requeridos con base al periodo solicitado..

Es decir, que si se solicitamos la descarga de datos correspondientes al día. El código de programación ordenará el archivo .CSV de manera que entregue los datos de consumo correspondientes de la L1, L2 y L3  en unidades de (Wh).

A  continuación se muestra el código correspondiente.


> importamos la libreria "pandas" misma que ayudará a la visualización de datos

import pandas as pd 
> posteriormente se define el nombre del archivo correspondiente a la descarga de datos y de la misma forma se define que tipo de separaciones contiene el archivo descargado desde la plataforma de usurio ABB CMS-700

df = pd.read_csv('example.csv', sep=";", index_col=0)

> Con lo aterior se logra la visualización de los consumos correspondientes a las 3 lineas del sistema. A continuación se muestran lo pasos para lograr la visualización gráfica de los consumos de dichas líneas de alimentación.

import matplotlib.pyplot as plt

> importa la libreria "matplotib" la cual ofrece diferentes beneficios, entre las diferentes herraminetas que contiene u ofrece, está la de graficar, que en este caso graficará los consumos mencionados anteriormente.

surveys = pd.read_csv("data/surveys.csv")

my_plot = surveys.plot("hindfoot_length", "weight", kind="scatter")

> leemos los datos del archivo correspondiente y damos la indicación de graficar.

plt.show() # graficamos los datos
