import random
import threading
from multiprocessing import Lock
import queue

lock = queue
class A:
    setA = set()
    setB = set()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    threads = []

    def fun(self, lock):
        lock.acquire()
        for i in self.arr:
            if (not i in self.setA):
                self.setA.add(i)
            else:
                self.setB.add(i)
        lock.release()


    def tFun(self):
        for i in range(10):
            lock = Lock()
            t = threading.Thread(target=self.fun, args=(lock,))
            self.threads.append(t)
            t.start()
        for t in self.threads:
            t.join()
        print(self.setA)
        print(self.setB)


a = A()
a.tFun()


import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
    t.join()





















