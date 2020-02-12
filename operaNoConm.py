import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

cant = 1
# Con el lock hago que los threads se esperen entre sí: sincronicen. 
# y me aseguro que cant siempre termina en 4.
lock = threading.Lock()

def sumarUno():
    global cant
    global lock
    # time.sleep(1) #simula un proceso

    try:
        cant += 1
    finally:
       lock.release() #¿qué pasa si comento este release y descomento el pass?
    #    pass

def multPorDos():
    global cant
    global lock
    lock.acquire()
    try:
        cant *= 2
    finally:
        lock.release()
    
lock.acquire()

t1 = threading.Thread(target=sumarUno)
t2 = threading.Thread(target=multPorDos)

# ya no importa el orden en que lance los threads.
# con el lock() me aseguro el orden: primero +1 y luego por 2.
t2.start()
# t1.join() # ya no necesito los joins porque lo manejo por el lock.
# antes, sin el lock, la sincronización para que cant siempre termine en 4 
# la manejaba el main thread mendiante joins.
t1.start()
# t2.join()


# y acá sigue haciendo cosas el main thread
time.sleep(0.5)

logging.info(f'Cantidad vale {cant}')