## Errores, soluciones y recomendaciones para operar el dispositivo H2O

![](https://github.com/jwilliamsee/H2O-PRUEBA-JW/blob/main/Imagenes/ErroresSoluciones1.png?raw=true)

1.	Del repositorio del dispositivo de agua para evitar que el ESP no cargue el boot.py por defecto y evitar confusión al momento de cargar los archivos, se recomienda cambiar el nombre de ese mismo documento boot.py a uno que se nos haga cómodo identificar, así evitamos confusión de cargar el boot.py que no es.

2.	El sensor de flujo deberá trabajarse de forma horizontal y no vertical, lo anterior es porque de manera vertical el líquido del fluido puede aumentar la presión y la velocidad por la gravedad, por lo que puede existir variaciones al leer datos.

![](https://github.com/jwilliamsee/H2O-PRUEBA-JW/blob/main/Imagenes/ErroresSolucion.PNG?raw=true)


3.	Considerar que no es un sensor de precisión por lo que la orientación, presión del agua y otras condiciones pueden afectar la medición.

4.	Se recomienda calibrar el sensor realizando mediciones con volúmenes conocidos. Calibrado puede llegar a tener una precisión de hasta 10%.

	El repositorio que está en la plataforma de GitHub, aunque cuenta con lo necesario para que el prototipo de medición de flujo de agua funcione, puede someterse a algunas mejoras.

5.	Almacenar dentro de carpetas los archivos necesarios para 1,2,3….8 sensores disponibles por dispositivo al momento de descargarlos para trabajar mejor. 