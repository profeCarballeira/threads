import threading
#método de asición de hilo
def Saludo():
    print ("HOLA")
    
t = threading.Thread(target=Saludo)
t.start()

print ("hola") #impresión en el hilo principal

