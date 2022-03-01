# Dispositivo Factor de potencia
Repositorio para el proyecto de medición del factor de potencia eléctrica para el nuevo edificio del IER-UNAM.

Esta versión del proyecto se conforma de un código modular para facilitar la manipulación de ciertos parámetros que nos ayuden a monitorear el consumo de energía eléctrica en los diferentes circuitos eléctricos del edificio nuevo del IER-UNAM.


A continuación se explican cada una de las funciones definidas en el archivo "funciones.py"

**Clase conteo**

Esta clase crea un objeto, este objeto será el sensor que se utilizará para la medición del flujo de agua.

La clase se compone de seis métodos. 

**Método init**

El método **init** no es más que para definir la varibale contador y la variable de entrada pin.

**Método callback**

El método **callback** es el que sirve para aumentar en 1 la variable contador cada señal recibida.

**Método irq**

El método **irq** es el que detecta cada pulso digital y envía la señal al metodo callback.

**Método ecuaciones**

Este método es el que aplica las constantes de conversión al conteo de pulsos digitales para así obtener una variable en Litros.

**Método datos**

Este método tan solo sirve para empaquetar los datos junto con una etiqueta para que estén listos.
para ser publicados en Thingsboard.	

**Método publica**

Este metodo se encarga de verificar si hay algún consumo de agua, de serlo así almacena los datos, en cuanto detecta que ya no lo hay, comineza un conteo, el conteo se interrumpe si vuelve a haber consumo, si el conteo concluye, publica los datos en Thingsboard.

**Última actualización de códigos por Miguel Ángel**

A continuación se explica de forma breve como se compone el código.

El código se modificó para hacer lecturas de ocho sensores. Cuenta con ocho secciones, una para cada número de sensores que se ocuparán. Todas las secciones se encuentran bloqueadas (comentadas). Esto con el fin de que se descomente la sección que se requiera, la primera sección es para un sensor, la segunda es para dos sensores y así sucesivamente hasta llegar a los ocho sensores.

