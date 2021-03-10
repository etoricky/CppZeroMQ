const zmq = require("zeromq/v5-compat")
 
const pub = zmq.socket("pub")

pub.bind("tcp://127.0.0.1:3000", err => {
  if (err) {
  	console.log(err);
  	throw err;
  }
})

setInterval(()=>{
	pub.send(+new Date())
}, 500);

