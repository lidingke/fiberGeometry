# python3.5
def consumer():
    while True:
        n = yield
        if not n:
            break
        print('[CONSUMER]Consuming %s...' % n)


def produce(c):
    next(c)
    for n in range(1, 5):
        print('[PRODUCER]Producing %s...' % n)
        c.send(n)
    c.close()


c = consumer()
produce(c)
