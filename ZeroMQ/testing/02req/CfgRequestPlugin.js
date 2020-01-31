var zmq = require('zeromq')

var socket = zmq.socket('req')
socket.connect('tcp://localhost:19412')
socket.on('message', function(msg) {
  console.log(JSON.stringify(JSON.parse(msg.toString()), null, 2));
})
var dic = {'function':'CfgRequestPlugin'}
socket.send(JSON.stringify(dic));
