# PROGRAMA PSOC 5LP
Este programa se encarga de realizar las lecturas de flujo de calor y de temeratura de dos sensores tipo PHFS-01e, después de obtener las lecturas, manda a impriumir los caracteres en una pantala LCD de 16x2 y al mismo tiempo manda los datos por via serial al ESP8266, este ciclo se repite cada 0.5 segundos.

# PROGRAMA ESP8266
Este programa tiene la función de conectarse por vía wifi a la plataforma Thingsboar,para que después pueda recibir los datos que envía el PSoC por el puerto serial, obteniedo los datos realiza una separación de los mismos, para que finalmente puedan ser enviados a  Thingsboard.
