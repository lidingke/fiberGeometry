import socket
import json
import sys
import os

para = ('randomImg', 'IMG/midoctagon/img/')


if __name__ == "__main__":
    print sys.argv
    assert len(sys.argv) == 3
    # assert sys.argv[-1][-1] == '/'
    para = sys.argv[1:]
    sock = socket.socket()
    sock.connect(("127.0.0.1", 9880))
    cmd = 'change:' + json.dumps(para) + '\n\r'
    sock.sendall(cmd)