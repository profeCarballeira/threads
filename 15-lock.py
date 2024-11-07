from threading import Lock, Thread
import time

def suma_uno():
    global g
    lock.acquire()
    a = g
    time.sleep (0.001)
    g = a+1
    lock.release()
    
def suma_tres():
    global g
    with lock:
        a = g
        time.sleep (0.001)
        g = a+3 
        
g = 0
lock = Lock()
listaHilos = []
for func in [suma_uno,suma_tres]:
    listaHilos.append(Thread(target=func))
    listaHilos[-1].start()

for h in listaHilos:
    h.join()
    
print (g)
