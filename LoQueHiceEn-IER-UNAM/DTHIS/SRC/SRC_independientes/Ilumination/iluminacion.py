import gy30_bh1750
import time

while True:
    lightLevel = gy30_bh1750.readLight()
    print("Nivel de Luz     : " + format(lightLevel,'.4f')       + " lx")
    time.sleep(10)








