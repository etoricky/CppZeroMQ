const zmq = require("zeromq/v5-compat")
const sock = zmq.socket("pull")
sock.on("message", msg => {
    console.log(msg);
  })
sock.connect("tcp://127.0.0.1:3000")
console.log("Worker connected to port 3000")