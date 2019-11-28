import sys
import zmq
context = zmq.Context()

socket1 = context.socket(zmq.SUB)
socket1.connect("tcp://172.16.36.110:19403")
socket1.setsockopt_string(zmq.SUBSCRIBE, "")

socket2 = context.socket(zmq.SUB)
socket2.connect("tcp://172.16.36.110:19603")
socket2.setsockopt_string(zmq.SUBSCRIBE, "")

poller = zmq.Poller()
poller.register(socket1, zmq.POLLIN)
poller.register(socket2, zmq.POLLIN)

while True:
    try:
        socks = dict(poller.poll())
    except KeyboardInterrupt:
        break
        
    if socket1 in socks:
        message = socket1.recv_string()
        print('socket1', message)
        
    if socket2 in socks:
        message = socket2.recv_string()
        if 'OnTick' not in message:
            print('socket2', message)
    