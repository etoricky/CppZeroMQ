var zmq = require('zeromq')

var socket = zmq.socket('req')
socket.connect('tcp://172.16.36.110:19412')
socket.on('message', function(msg) {
  console.log(msg.toString())
})
var dic = {'function':'DailyReportsRequest','arguments':{'from':1575158400,'to':1576108800,'limit':1,'logins':[145313793]}}
socket.send(JSON.stringify(dic));
