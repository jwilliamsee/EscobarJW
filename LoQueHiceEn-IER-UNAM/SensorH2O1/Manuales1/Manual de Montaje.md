![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/logoIER.png?raw=true)


### Universidad Nacional Autónoma de México
#### Instituto de Energías Renovables
**Manual de ensamble**


## Dispositivo medidor de caudal (H20)
------------
### Tabla de contenido

1. Introducción ...................................................................3
2. Precauciones ..................................................................3
3. Herramientas necesarias ........................................... 3
4. Comprobar piezas ........................................................ 3
5. Materiales del dispositivo ......................................... 4
6. Placa principal ............................................................... 5
7. Identificación de componentes en la placa ....... 6
8. Tabla de componentes ............................................... 7
9. Montaje de componentes ........................................ 7
	
	9.1 Resistencias ............................................................ 8
	
	9.2 Circuito integrado LM324 ................................. 9
	
	9.3 TBLOCK-M3........................................................... 10
	
	9.4 NodeMCU (ESP8266) ....................................... 10
	
	9.5 USBCONN ............................................................. 11
10. Corte de pines ............................................................ 11
11. Conexión de los sensores ...................................... 12
12. Prueba de encendido .............................................. 13

	13.1 Nota importante .............................................. 14
14. Base de la carcasa ..................................................... 15
15. Partes del ensamble completo ............................ 16
16. Vista del ensamble completo .............................. 16
17. Consideraciones .........................................................17

------------
**1. Introducción**

Este manual contiene instrucciones para ensamblar el dispositivo H2O, que ha sido desarrollado por el Grupo de energía en edificaciones del Instituto de Energías Renovables de la UNAM, como parte del proyecto “Edificios demostrativos de diseño bioclimático en clima cálido subhúmedo en el Instituto de Energías Renovables UNAM”.
Proyecto número 291600 del Fondo de Sustentabilidad Energética.
El dispositivo H2O mide la cantidad de agua consumida por periodos de tiempo, con la intención de llevar un control del consumo de agua en el edificio, para posteriormente tomar medidas para disminuir dicho consumo en caso de tener exceso por fugas o descuidos de los usuarios, garantizando así, el control en todo momento.

**2. Precauciones**
- Es necesario tomar ciertas medidas para realizar el proceso sin complicaciones.
- Para soldar, la temperatura del cautín debe estar entre 200 y 350 °C.
- Usar protección en manos y ojos para evitar daños por quemaduras o cortes causados por quitarle la insulación a los cables o por cortarlos.
- Manejar con cuidado los cables y componentes del dispositivo para evitar reemplazo por manipulación inadecuada de los mismos.

**3. Herramientas necesarias**
1. Pinzas de corte
2. Alicates para manipular pines metálicos o cualquier componente
3. Cautín
4. Kit de destornilladores para electrónica

**4. Comprobar piezas**

Verificar que se tienen todos los componentes para realizar el ensamble e identificar la parte del dispositivo a donde pertenecen con la ayuda de los pictogramas, imágenes y lista de materiales. En caso de faltar algún componente, es recomendable que se consiga antes de empezar.

*pág. 3*

------------
**5. Materiales del dispositivo**

[Ver lista de materiales del dispositivo](https://github.com/AltamarMx/SensorH2O/blob/master/Materiales/Lista_de_materiales_H2O.md)

*Pág. 4*

------------
**6. Placa principal**

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/PCB3DEASYH2O1FRONTAL.PNG?raw=true)

**PCB Vista superior**

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/PCBEASYH2O13DABAJO.PNG?raw=true)

**PCB Vista inferior**

Se recomienda poner un componente a la vez en la placa para poder soldarlo cómodamente y poder manipularlo sin problemas. Aunque cada persona tiene su método y cuenta con diferentes herramientas que harán mas fácil el proceso de soldar los componentes.

*Pág. 5*

------------
**7. Identificación de componentes en la placa**

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/globoscomponentes.PNG?raw=true)

**Componentes**

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/IDENTIFICACIONCOMPH2O1.PNG?raw=true)

**Componentes en PCB**

*Pág. 6*

------------
**8. Tabla de componentes**

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/TABLACOMPONENTES.PNG?raw=true)

**9. Montaje de componentes**

Los componentes van en la parte superior de la placa, con la intención de que queden fijos al momento de soldarlos, se recomienda que se aplique soldadura de manera individual, para poder manipular la placa cómodamente.
En caso de requerir orientación del dispositivo para colocarlo en la placa o tener dudas sobre características de operación de algún componente, se puede dirigir a la carpeta donde se encuentran las hojas de datos de algunos componentes complejos.

*Pág. 7*

------------
![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/ImagenCorteDePinesB.PNG?raw=true)

**Soldar las piezas de manera individual**

**9.1 Resistencias**

Son un total de 14 resistencias de 3 valores diferentes, 220Ω, 1k y 2k. Las resistencias no tienen polaridad, por lo que la orientación en la placa realmente no influye en el buen funcionamiento. Si se desconoce los valores de las resistencias representadas en la placa al momento de querer interpretar con los colores, es necesario que consulte el código de colores para asegurarse de que se está usando la resistencia adecuada en el lugar correspondiente.
Los primeros componentes a soldar, se recomienda que sean las resistencias porque son componentes pequeños y si se empieza por los mas grandes es seguro que sea difícil soldar las resistencias por los espacios.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/ResistenciasDeParteSuperiorB.PNG?raw=true)

**Resistencias de la parte superior**

*Pág. 8*

------------

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/RPARTECENTRAL.PNG?raw=true)

**Resistencia parte central**

**9.2 Circuito integrado LM324**

El integrado LM324, tiene una orientación, se puede ver la hoja de datos en caso de ser necesario, pero para el caso en particular de los LM324 se recomienda primero soldar una patilla o pin para darle seguridad y manipular cómodamente para soldar los pines restantes.

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/LM324ENPLACA.PNG?raw=true)

**Orientación del LM324**

*Pág. 9*

------------
**9.3 TBLOCK-M3**

Los conectores TBLOCK-M3 se deben conectar con las terminales de frente, la parte metálica hacía nosotros o hacía los límites de la placa, con los orificios de conexión libres para realizar el aseguramiento de los cables de los sensores.
Los conectores TBLOCK-M3 no tienen polaridad, por lo que no es necesario ver diagramas o cualquier otra información, pero es importante que los terminales de conexión vayan de frente.

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/TBLOCKENPLACA.PNG?raw=true)

**Orientación de los TBLOCK-M3 en la placa**

**9.4 NodeMCU (ESP8266)**

Para posicionar el ESP en la placa, se recomienda soldar de inicio solo un pin y después los demás, con la intención de manipular la placa cómodamente, para hacer el proceso de soldado de este componente en particular es necesario contar con una base para el ESP y no tener que soldar los pines directamente de la placa, en caso de tener dudas sobre su operación o alguna característica en particular deberá usar la hoja de datos, almacenada en la carpeta.

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/ESPENPLACA.PNG?raw=true)

*Pág. 10*

------------
**9.5 USBCONN**

El conector hembra USB es para alimentar con una fuente externa a la placa en general, será por ese conector donde entre la energía eléctrica para alimentar a todos los componentes, la alimentación será con un cable USB tipo A-A.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/USBCONN.PNG?raw=true)

**10. Corte de pines**

Cuando se ha realizado el proceso de soldar todas las piezas, por el otro lado de la placa tendrá los pines muy largos y si se deja así, causaría muchos problemas, se cortará el excedente cuidando que la soldadura aplicada no se dañe, de preferencia se debe dejar el pin de 1 o 2 mm después de la soldadura aplicada.

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/PINESCUTPLACA.PNG?raw=true)

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/PINESCUTPLACA1.PNG?raw=true)

**Pines cortados**

*pág. 11*

------------
**11. Conexión del sensor**

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/SENSORENPLACA.PNG?raw=true)

**Conexión de sensor**

*Pág. 12*

------------
![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/COMPONENTESENPLACACOMPLETA.PNG?raw=true)

**Placa con componentes montados**

**12. Prueba de encendido**

Hasta este punto ya se tienen montados los componentes en la placa, lo que sigue a continuación es hacer una prueba de encendido, con la intención de verificar que las conexiones de los componentes se encuentren correctas, en caso de no ser así, será fácil modificarlo porque aún no está montado en la carcasa.
Debe asegurarse, de usar los cables adecuados, que no se encuentren en mal estado para evitar confusiones de fallas, comprobar que al momento de conectar el

*Pág. 13*

------------
led azul debe parpadear, sólo una vez, eso indica que se ha conectado bien y que nuestro cable está en buenas condiciones.

![](https://github.com/AltamarMx/SensorH2O/blob/master/Imagenes/PruebaDeEncendidoB.PNG?raw=true)

**Prueba de encendido**

En este punto se deberá consultar el manual de operación para cargar el firmware y los códigos a usar.
Aquí va el link de MO

**12.1 Nota importante:**

al energizar del ESP debe realizarse por separado, es decir, independiente de la energización de la placa, primero se debe conectar el ESP y cargar los códigos, cuando se han cargado los códigos completos, se puede montar el ESP a la base, pero no debe montar el ESP, energizarlo y al mismo tiempo energizar la placa en general, podría causar daño a los componentes o a la placa.
En caso de hacer prueba completa con todos los componentes montados y los sensores conectados, será conveniente que se conecte por jumper a la base, pero sin energizar el ESP, debido a que está conectado a la computadora.
Para prueba completa sin montar el ESP con conexión por jumper y al mismo tiempo energizar la placa y conectar los sensores se puede guiar de la figura.

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/CORRECTOINCORRECTO.PNG?raw=true)

**Forma incorrecta...........................................Forma correcta**

*Pág 14*

------------
**13. Base de la carcasa**

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/BASEYPLACA1.PNG?raw=true)

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/BASEYPLACA.PNG?raw=true)

*Pág. 15*

------------
**14. Partes ensamble completo**

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/ENSAMBLEFINAL.PNG?raw=true)

**15. Vista del ensamble completo**

![](https://github.com/jwilliamsee/SensorH2O1/blob/main/Imagenes/SENSORCONECTADO.PNG?raw=true)

*Pág. 16*

------------
**16. Consideraciones**

- La tarjeta NodeMCU debe manejarse con cuidado, cuidando de no dañar los componentes, debido a que son componentes electrónicos que sufren daños con la presencia de campo magnético.
- Deberá manipularse en lugar seco, libre de cualquier recipiente con líquido, cuando se realicen pruebas deberá manejarse con mucho cuidado.
- La carcasa tiene orificios para la circulación de aire al interior evitando que la placa se caliente, aunque es difícil que llegue a calentarse.
- Deberá ponerse en un lugar protegido de la lluvia y el sol para evitar cualquier daño causado por el ambiente.
- La conexión del sensor con el conector TBLOCK-M3 deberá realizarse con cable resistente y de buen grosor para evitar cambiarlos repetidamente y pueda manipularlos cómodamente.

*Pág. 17*

------------
