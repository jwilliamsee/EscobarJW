def do_connect(red,clave):
    import network
    import time
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
	sta_if.connect(red,clave)
        #sta_if.connect('IER', 'acadier2014')
        while not sta_if.isconnected():
            pass
    else:
      print("Already connected")
    print('network config:', sta_if.ifconfig())
    time.sleep(5)

