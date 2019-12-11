import zmq, json
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:19412")
dic = {'function':'DailyReportsRequest','arguments':{'from':1575158400,'to':1576108800,'limit':1,'logins':[145313793]}}
print(dic)
socket.send_string(json.dumps(dic))
respond = socket.recv()
try:
    result = json.loads(respond.decode())
    print(result.keys())
    if result.get('res', 2)==0:
        data = result.get('data', [])
        with open('DailyReportsRequest.json', 'w') as outfile:
            json.dump(data, outfile, indent=2)
        for datum in data:
            print(data)
except Exception as e:
    logging.error(e, exc_info=True)
    logging.error("respond " + respond)
