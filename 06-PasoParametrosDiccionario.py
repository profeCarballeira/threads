import threading

def hilo_Apellido(name, inicio=1, fin=1):
    for x in range (inicio, fin):
        print ( f"{name} Rodriguez {str(x)} años\n", end="")
        
nombres = ["Oscar","Alexandre", "Lua", "Carlys"]
hilos = list()
for n in nombres:
    t = threading.Thread(target=hilo_Apellido, args=(n,), kwargs={'inicio':2, 'fin':4})
    hilos.append(t)
    t.start()