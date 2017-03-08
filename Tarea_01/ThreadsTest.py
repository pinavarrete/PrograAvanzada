import threading
import random
import time

class Mult(threading.Thread):
    lock = threading.Lock()
    def __init__(self, ident, numero, start):
        super().__init__()
        self._id = ident
        self.num = numero
        self.resultado = 1
        self.timex = start

    def run(self):
        with Mult.lock:
            print("ahora")
            while self.num > 0:
                self.resultado = self.resultado*self.num
                self.num -= 1
            print('El Thread {} finalizo, resultado {}'.format(self._id, self.resultado%2))
            print("tiempo = {}".format(time.time() - self.timex))

time_start = time.time()
th = Mult(0, 3, time_start)
th.start()
for i in range(1, 10):
    th_time = time.time()
    num = random.randint(10000, 100000)
    th = Mult(i, num, time_start)
    th.start()

print("*** Termino programa principal ***")
print("*** Tiempo programa principal = {} ***".format(time.time() - time_start))