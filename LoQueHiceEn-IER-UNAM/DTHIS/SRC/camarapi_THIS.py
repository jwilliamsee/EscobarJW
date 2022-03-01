######################### Dispositivo THIS
######################### Librería para la camara Pi
import picamera
import time
import math
import decimal

def captura_foto(NOMBRE_FOTO):
    with picamera.PiCamera() as camera:
        camera.iso = 640
        camera.start_preview()
        camera.capture(NOMBRE_FOTO, bayer=True)
        camera.stop_preview()
        time.sleep(0.5)
        
def prom_pixeles(FOTO,ALTURA,ANCHO):
    total = 0
    for j in range(0,ALTURA):
        for i in range(0,ANCHO):
            k = FOTO[j,i]
            total += k
    promedio = total / (ALTURA * ANCHO)
    return promedio

def cuadrantes_pix(FOTO,NO_CUADRANTES,HEIGHT,WIDTH):
    cuad = round(math.sqrt(NO_CUADRANTES))
    alto_cuadrante = HEIGHT // cuad
    ancho_cuadrante = WIDTH // cuad
    alto1 = 0
    ancho1 = 0
    alto2 = alto_cuadrante
    ancho2 = ancho_cuadrante
    promedios = []
    for y in range(0,cuad):
        for x in range(0,cuad):
            total = 0
            for j in range(alto1,alto2):
                for i in range(ancho1,ancho2):
                    k = FOTO[j,i]
                    total += k
            prom = total / ((alto2-alto1)*(ancho2-ancho1))
            avg = decimal.Decimal(prom)
            promedios.append('{:.10}'.format(avg))
            
            ancho1 += ancho_cuadrante
            ancho2 += ancho_cuadrante
        alto1 += alto_cuadrante
        alto2 += alto_cuadrante
        ancho1 = 0
        ancho2 = ancho_cuadrante
    return promedios

def escribe_matriz(NO_CUADRANTES,MATRIZ):
    fila = round(math.sqrt(NO_CUADRANTES))
    for i in range(NO_CUADRANTES):
        if (i%fila) == 0:
            print()
        print("\t", MATRIZ[i], end=' ')
########################################### Fin