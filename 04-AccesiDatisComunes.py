import threading
import time
import random

def tareaUno():
    global Realizado #permiso escritura variabel externa
    time.sleep(random.random())
    if not Realizado:
        print ("Tarea realizada")
        Realizado= True
    return

Realizado = False
t = threading.Thread(target=tareaUno)
t.start()
tareaUno()
#tareaUno()
time.sleep(1)