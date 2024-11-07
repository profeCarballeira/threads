# Crear una clase que maneje un hilo (herencia Thread)
# Se la pasan dos valores al constructor (min y max)
# Al invocar a run (start) un bucle hara un print de todosl los valoreos comprendidos entre min y max
# Crear 10 hilos con valores de minimo y máximo aleatorios min < max
# Lanzar los 10 hilos en ejecución

import threading
import random
import time

# Definimos la clase que hereda de Thread
class RangoThread(threading.Thread):
    def __init__(self, min_val, max_val):
        super().__init__()
        self.min_val = min_val
        self.max_val = max_val

    def run(self):
        for i in range(self.min_val, self.max_val + 1):
            print(f"Hilo {self.name} - Valor: {i}")
            time.sleep(0.1)  # Agregamos una pequeña pausa para observar la salida

# Creamos 10 hilos con valores aleatorios
threads = []
for _ in range(10):
    min_val = random.randint(1, 50)
    max_val = random.randint(min_val + 1, 100)  # Aseguramos que max > min
    hilo = RangoThread(min_val, max_val)
    threads.append(hilo)

# Iniciamos todos los hilos
for hilo in threads:
    hilo.start()

# Esperamos a que todos los hilos terminen
# for hilo in threads:
#     hilo.join()

print("Todos los hilos han terminado.")
