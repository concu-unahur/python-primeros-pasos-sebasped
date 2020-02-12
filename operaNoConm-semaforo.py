import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

cant = 1
sem = threading.Semaphore(0)

def sumarUno():
    global cant
    global sem

    try:
        cant += 1
    finally:
       sem.release() 

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

t2.start()
time.sleep(1)
t1.start()


# y acá sigue haciendo cosas el main thread
time.sleep(1)

logging.info(f'Cantidad vale {cant}')