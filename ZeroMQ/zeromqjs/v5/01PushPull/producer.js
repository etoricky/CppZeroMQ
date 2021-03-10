const zmq = require("zeromq/v5-compat")

function run() {
  const sock = zmq.socket("push")

  sock.bind("tcp://127.0.0.1:3000", err => {
      if (err) {
        console.log(err);
        throw err;
      }
    })
  console.log("Producer bound to port 3000")

  setInterval(()=>{
	sock.send("kitty cats" + new Date())
}, 500);
}

run()