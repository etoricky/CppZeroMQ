var zmq = require('zeromq')

var socket = zmq.socket('req')
socket.connect('tcp://localhost:19412')
socket.on('message', function(msg) {
  console.log(msg.toString())
})
var dic = {'function':'SetDealerDelay', 'arguments':{'id':'50004','delay':'4'}};
socket.send(JSON.stringify(dic));
