# hacer un programa con una variable global contador
# Diez hilos van a hacer 100 iteraciones en las que incrementan el valor de esa variable en uno y se duermen sleep 0.0001 segundo
# lanzarlos todos y observar el valor final que toma el contador
# Usar join para esperar por todos los hilos
# Si el valor no es el esperado usar lock

import threading
import time

# Variable global contador
contador = 0

# Función que incrementa el contador 100 veces con un pequeño delay
def incrementar_contador():
    global contador
    for _ in range(10000):
        time.sleep(0.0001)
        contador += 1
        

# Lista para guardar los hilos
hilos = []

# Crear y lanzar 10 hilos
for _ in range(10):
    hilo = threading.Thread(target=incrementar_contador)
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# Mostrar el valor final del contador
print("Valor final del contador sin Lock:", contador)
