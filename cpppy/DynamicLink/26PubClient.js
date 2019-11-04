// weather update client in node.js
// connects SUB socket to tcp://localhost:5556
// collects weather updates and finds avg temp in zipcode

var zmq = require('zeromq');

console.log("Collecting updates from weather server...");

// Socket to talk to server
var subscriber = zmq.socket('sub');

// Subscribe to zipcode, default is NYC, 10001
var filter = null;
if (process.argv.length > 2) {
  filter = process.argv[2];
} else {
  filter = "10001";
}
console.log(filter);
subscriber.subscribe('');

// process 100 updates
var total_temp = 0
  , temps      = 0;
subscriber.on('message', function(data) {
  console.log(data.toString());
});

subscriber.connect("tcp://localhost:5556");