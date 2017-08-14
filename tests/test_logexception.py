import logging
import threading
import traceback
from time import sleep

import sys

logger = logging.getLogger(__name__)



def raise_error():
    raise ValueError()

def get_raise_error():
    try:
        raise_error()
    except Exception as e:
        print e

def main():
    logging.basicConfig(filename="tests\\data\\testlog.log",
                        filemode="w", format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
                        level=logging.ERROR)
    # sleep(0.5)
    logger.error(traceback.format_exception(*sys.exc_info()))


if __name__ == '__main__':

    logging.basicConfig(filename="tests\\data\\testlog.log",
                        format="%(asctime)s-%(levelname)s-%(name)s-%(message)s",
                        level=logging.ERROR)
    logger.error("start logging")
    threading.Thread(target=get_raise_error).start()
    logger.error(traceback.format_exception(*sys.exc_info()))

