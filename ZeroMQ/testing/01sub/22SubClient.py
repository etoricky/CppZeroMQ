import sys
import zmq
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://172.16.36.110:19603")
socket.setsockopt_string(zmq.SUBSCRIBE, "")
while True:
    string = socket.recv_string()
    print(string)