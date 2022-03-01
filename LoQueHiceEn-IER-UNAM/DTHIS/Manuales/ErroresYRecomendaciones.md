### Errores, soluciones y recomendaciones para operar el dispositivo THIS

##### 1. Primero debemos instalar raspbian en la raspberry pi, siguiendo el video del Dr. Barrios en el siguiente vínculo:

[**Instalar raspbian**](https://www.youtube.com/watch?v=JOzr38A48q8)

##### En el video se encuentra lo necesario para poder operar la raspberry pi de manera remota, para la conexión ssh es necesario entrar con las credenciales que por default se muestran en el video, si se hizo el proceso desde cero con la instalación de raspbian, deberá seguir el proceso del video, en caso contario si se está usando una raspberry que ya se trabajó, entonces la credenciales para acceder serán diferentes y están en el README del repositorio.

##### 2. Si aún no se ha familiarizado con el uso de la raspberry y conexión ssh, lo ideal es conectarse con un monitor, ahí no le pedirá contraseña para acceder y la parte gráfica ayuda a entender lo que se está haciendo, necesitará además del monitor, conexión a internet de preferencia cableado, un teclado y un mouse, todo cableado, se pueden usar por bluetooth pero hay que configurar otras cosas en la raspberry y si se usa internet inalámbrico resulta que se pierde un poco la señal entre bluetooth y wifi, aunque sean independientes.

##### 3. Deberá seguir el manual de operación para poder operar el THIS, asegurarse que cuenta con todos los materiales y con los componentes necesarios para lograr la ejecución de manera adecuada.

##### 4. Se recomienda usar el intérprete de código Thonny, para entender lo que sucede con el código al momento de ejecutarlo y poder ver si en los códigos hay errores.

##### 5. Deberá asegurarse que los módulos se encuentren en los lugares que deben ir y en posición correcta, en la imagen se muestra como deberían ir:

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/THIS-SENTIDO.jpg?raw=true)

##### 6. En cuanto al módulo CJMCU, en muchas ocasiones hay errores de operación o que no mide correctamente, para eso se recomienda conectar el pin WAK a GND, con la intención de que no genere "ruido", otro detalle es que en algunas páginas mencionan que se energiza con 3.3v y otras dicen que con 5v, no ha habido error al energizarlo con 3 y 5 pero, puede generar mayor "ruido" si se alimenta con 5v, por eso se recomienda que sea con 3.3 y el pin WAK a GND.

##### 7. Antes de ponerlo en la carcasa y en posición correcta, se recomienda probarlo antes con los módulos en un protoboard para poder manipular fácilmente en caso de fallas:

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DTHIS/blob/master/Imagenes/THIS-EN-PROTO.jpg?raw=true)

##### 8. El ADS no es neceario que se ponga en una posición específica pero para poder manipularlo se sugiere que sea con los pineas hacia arriba.

##### 9. Se sugiere energizar la raspberry con el cargador o eliminador original para que suministre el voltaje, la corriente y los watts adecuados, porque si se energiza vía usb de la computadora u otro, puede llegar a presentar fallos de conexión.

##### 10. Se recomienda revisar la continuidad en los jumpers cuando se realicen pruebas, aunque sean nuevos.
##### Elegir colores para identificar las conexiones puede ser de gran ayuda para no equivocarse con las conexiones.

##### 11. Una forma de asegurarse que la conexión I2C de los módulos es la correcta y se estan reconociendo los mismos, es ejecutar en la terminal la siguiente línea:
   i2cdetect -y 1
##### Con la línea naterior nos deberá aparecer en la terminal que cada conexión I2C está en una columna y fila diferente a las demás, ésto nos indica que está bien y además que sí están conectados los cuatro módulos.
