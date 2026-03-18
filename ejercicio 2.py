import threading
import time

def programar():
    print("inicio 1")
    time.sleep(4)
    print("finalizo 1")

def beber_agua():
    print("inicio 2")
    time.sleep(6)
    print("finalizo 2")

def estudiar():
    print("inicio 3")
    time.sleep(4)
    print("finalizo 3")

inicio = time.perf_counter()

# Crear hilos
hilo1 = threading.Thread(target=programar)
hilo2 = threading.Thread(target=beber_agua)
hilo3 = threading.Thread(target=estudiar)

# Iniciar hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Esperar a que terminen
hilo1.join()
hilo2.join()
hilo3.join()

fin = time.perf_counter()

print(f"Tiempo total: {fin - inicio:.2f} segundos")