#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import random
import time

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.bind("tcp://*:5555")

# wait all worker connected
time.sleep(1)

#  Do 10 requests, waiting each time for a response
for i in range(9):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    line = str(a) + ' ' + str(b)
    print('sending', line)
    socket.send_string(line)

    #  Get the reply.
    message = socket.recv_string()
    print("received", message)
