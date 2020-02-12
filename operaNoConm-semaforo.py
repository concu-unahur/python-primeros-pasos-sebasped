import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

cant = 1
sem = threading.Semaphore(0)

def sumarUno():
    global cant
    global sem
    
    # time.sleep(1) #simula un proceso
    
    try:
        cant += 1
    finally:
       sem.release() #¿qué pasa si comento este release y descomento el pass?
    #    pass

def multPorDos():
    global cant
    global sem

    sem.acquire()
    
    try:
        cant *= 2
    finally:
        sem.release()
    

t1 = threading.Thread(target=sumarUno)
t2 = threading.Thread(target=multPorDos)

# a pesar de que lanzo primero mult por dos, se ejecuta primero
# sumar uno, pues el semáforo lo impide.
t2.start()
t1.start()


# y acá sigue haciendo cosas el main thread
time.sleep(0.5)

logging.info(f'Cantidad vale {cant}')