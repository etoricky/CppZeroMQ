import time
import zmq
import pprint

def collector():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://127.0.0.1:5558")
    counter = {}
    for x in range(1000):
        result = socket.recv_json()
        id = result['id']
        counter[id] = counter.get(id, 0) + 1
    pprint.pprint(counter)

collector()