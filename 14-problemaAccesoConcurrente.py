from threading import Lock, Thread
import time

def suma_uno():
    global g
    a = g
    time.sleep (0.001)
    g = a+1
    
def suma_tres():
    global g
    a = g
    time.sleep (0.001)
    g = a+3 
    
g = 0
listaHilos = []
for func in [suma_uno,suma_tres]:
    listaHilos.append(Thread(target=func))
    listaHilos[-1].start()

for h in listaHilos:
    h.join()
    
print (g)
