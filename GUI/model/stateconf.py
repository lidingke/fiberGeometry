CONTEXT = [{}, {}, {}, {}, {}]
CONTEXT[1] = {"_platform_state": "PLAT1"}
CONTEXT[3] = {"_platform_state": "PLAT2"}


def state_number():
    while True:
        for i in xrange(6):
            yield i


if __name__ == '__main__':
    s = state_number()
    for i in range(10):
        print(next(s))
