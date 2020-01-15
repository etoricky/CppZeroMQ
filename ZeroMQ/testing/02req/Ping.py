import zmq, json
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:19412")
dic = {'function':'Ping'}
print(dic)
socket.send_string(json.dumps(dic))
respond = socket.recv()
try:
    result = json.loads(respond.decode())
    if result:
        print(result.keys())
        res = result.get('res', 2)
        print(res)
except Exception as e:
    logging.error(e, exc_info=True)
    logging.error("respond " + respond)
