var zmq = require('zeromq')

var socket = zmq.socket('req')
socket.connect('tcp://localhost:19412')
socket.on('message', function(msg) {
  console.log(msg.toString());
  socket.close();
})
var dic = {'function':'SetDealerDelay', 'arguments':{'50006':{'delay':'16'},'50005':{'delay':'15'}}};
socket.send(JSON.stringify(dic));
