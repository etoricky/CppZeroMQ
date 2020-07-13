#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5555")
pid = os.getpid()
print('pid', pid)

while True:
    #  Wait for next request from client
    line = socket.recv_string()
    print(pid, 'received', line)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string(str(sum(map(int, line.split()))))
