import SDL_Pi_HDC1000
import time

hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000()

while True:
    TL = hdc1000.readTemperature()
    HL = hdc1000.readHumidity()
    print("Temperatura      : " + format(TL, '.4f') + " C")
    print("Humedad Relativa : " + format(HL, '.4f') + " %")
    time.sleep(10)