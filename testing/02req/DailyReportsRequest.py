import zmq, json
context = zmq.Context()
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:19404")
dic = {'function':'DailyReportsRequest','arguments':{'from':1575158400,'to':1576108800,'limit':1}}
print(dic)
socket.send_string(json.dumps(dic))
respond = socket.recv()
try:
    result = json.loads(respond.decode())
    print(result.keys())
    if result.get('res', 2)==0:
        data = result.get('data', [])
        for datum in data:
            print(data)
except Exception as e:
    logging.error(e, exc_info=True)
    logging.error("respond " + respond)
