import threading

def hilo_Apellido(name):
    print (name + " Rodriguez")

nombres = ["Oscar","Alexandre", "Lua", "Carlys"]
hilos = list()
for n in nombres:
    t = threading.Thread(target=hilo_Apellido, args=(n,))
    hilos.append(t)
    t.start()