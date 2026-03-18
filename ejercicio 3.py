import threading
import time

lock = threading.Lock()

def imprimir(letra):
    with lock:
        print(f"inicio {letra}")
        for _ in range(5):
            print(letra)
            time.sleep(0.2)
        print(f"finalizo {letra}")

letras = ['a', 'b', 'c', 'd', 'e']

hilos = []

for letra in letras:
    hilo = threading.Thread(target=imprimir, args=(letra,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()