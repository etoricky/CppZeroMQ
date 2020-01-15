var zmq = require('zeromq')

var socket = zmq.socket('req')
socket.connect('tcp://localhost:19412')
socket.on('message', function(msg) {
  console.log(msg.toString())
})
var dic = {'function':'Ping'}
socket.send(JSON.stringify(dic));
