import time
import zmq
import random

def consumer():
    id = random.randrange(1,10005)
    print("I am consumer #%s" % (id))
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://127.0.0.1:5557")
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://127.0.0.1:5558")
    while True:
        work = receiver.recv_json()
        num = work['num']
        result = { 'id' : id, 'num' : num}
        if num%2 == 0: 
            sender.send_json(result)

consumer()