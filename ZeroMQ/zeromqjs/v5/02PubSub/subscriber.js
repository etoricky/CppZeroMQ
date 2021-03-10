const zmq = require("zeromq/v5-compat")
const sub = zmq.socket("sub")

sub.on("message", msg => {
    console.log(msg);
  })
sub.subscribe(''); // subscribe to all events
sub.connect("tcp://127.0.0.1:3000")