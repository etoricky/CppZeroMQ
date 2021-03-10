const zmq = require("zeromq/v5-compat")

const sock = zmq.socket("rep")
sock.bind("tcp://127.0.0.1:3000", err => {
  if (err) {
  	console.log(err);
  	throw err;
  }
})
sock.on('message', msg => {
	const answer = msg.toString() + ' ' + new Date();
	console.log(answer);
	sock.send(answer);
})