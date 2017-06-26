def yieldfun():
    print ('get in yield')
    yield
    print ('get out yield')

def w(gen):
    gen.__next__()
    while True:
        if gen:
            print(gen)

def w2():
    while True:
        print ('get in yield')
        yield
        print ('get out yield')

import time
import pdb

import threading

gen = w2()

# threading.Thread(target=w, args=(gen)).start()
next(gen)
time.sleep(1)
gen.send(1)
time.sleep(1)
gen.send(2)
