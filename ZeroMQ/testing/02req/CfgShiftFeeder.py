import zmq, json
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:19412")
dic = {'function':'CfgShiftFeeder', 'arguments':{'pos':1,'shift':1}}
print(dic)
socket.send_string(json.dumps(dic))
respond = socket.recv()
try:
    result = json.loads(respond.decode())
    if result:
        res = result.get('res', 2)
        print('res', res)
        print(result.keys())
        if res==0:
            data = result.get('data', [])
            with open('CfgShiftFeeder.json', 'w') as outfile:
                json.dump(data, outfile, indent=2)
            for datum in data:
                print(data)
except Exception as e:
    logging.error(e, exc_info=True)
    logging.error("respond " + respond)
