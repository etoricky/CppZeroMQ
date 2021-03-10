const zmq = require("zeromq/v5-compat")
const sock = zmq.socket("req")
sock.connect("tcp://127.0.0.1:3000")
sock.send("4");
sock.on('message', msg => {
	console.log(msg.toString());
})

setInterval(()=>{
	sock.send("client " + new Date())
}, 500);