var zmq = require('zeromq')

var socket1 = zmq.socket('sub')
socket1.subscribe('10001')
socket1.on('message', function(msg) {
  console.log(msg.toString())
})

var socket2 = zmq.socket('sub')
socket2.subscribe('')
socket2.on('message', function(msg) {
  console.log(msg.toString())
})

socket1.connect('tcp://172.16.36.110:19403')
socket2.connect('tcp://172.16.36.110:19603')