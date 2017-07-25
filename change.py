import pdb
# from simulator import client
from simulator.client import Client
from tornado.ioloop import IOLoop
from functools import partial
import sys


if __name__ == "__main__":

    if sys.argv[1].find('h'):
        print 'import port method and dir as argv'
        print 'exp: 9801 randomImg IMG\\emptytuple\\eptlight1\\'
    else:
        port = int(sys.argv[1])
        para = (sys.argv[2], sys.argv[3])
    # IOLoop.current().run_sync(partial(Client(port=port).get_change, para))