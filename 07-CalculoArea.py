import threading

# Bloqueo para sincronizar el acceso a la variable global areaTotal
lock = threading.Lock()

# Función que calcula el área según la figura y la suma a la variable global
def Area(base, altura, figura):
    global areaTotal
    if figura == "triangulo":
        area = (base * altura) / 2  # Fórmula para el área de un triángulo
    elif figura == "cuadrilatero":
        area = base * altura  # Fórmula para el área de un cuadrilátero
    else:
        area = 0  # Si la figura no es válida, se asigna 0 de área
    
    # Bloqueamos el acceso a areaTotal mientras lo actualizamos
    with lock:
        areaTotal += area
        print(f"{figura} con base {base} y altura {altura} tiene un área de {area}. Área total: {areaTotal}")

# Lista de figuras y sus dimensiones
figuras = [["triangulo", 10, 12], ["cuadrilatero", 12, 8], ["cuadrilatero", 6, 4], ["triangulo", 2, 5]]

areaTotal = 0
hilos = list()

# Crear y arrancar los hilos para calcular el área de cada figura
for f in figuras:
    t = threading.Thread(target=Area, args=(f[1], f[2], f[0]))  # Pasar los argumentos
    hilos.append(t)
    t.start()

# Esperar a que todos los hilos terminen
for t in hilos:
    t.join()

# Imprimir el área total después de que todos los hilos hayan terminado
print(f"El área total es: {areaTotal}")
