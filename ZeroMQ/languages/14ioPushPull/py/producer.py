import time
import zmq

def producer():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://127.0.0.1:5557")
    # start collector and consumers before producer
    for num in range(20000):
        work = { 'num' : num }
        socket.send_json(work)

producer()
