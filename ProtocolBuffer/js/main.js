const addressbook_pb = require("./addressbook_pb");
const opn = require('opn');
const express = require('express');

function startExpress() {
    const host = '127.0.0.1';
    const port = 65432;
    opn('http://' + host + ':' + port);
    const app = express();
    app.use(express.static('templates'));
    app.use(express.urlencoded({extended: true})); // Parse URL-encoded bodies (as sent by HTML forms)
    app.use(express.json()); // Parse JSON bodies (as sent by API clients)
    app.set('json spaces', 2);
    const server = app.listen(port, host, ()=>{
        const address = server.address();
        console.log("listen http://%s:%s", address.address, address.port);
    });
}

const main = async function() {
    const message = new addressbook_pb.Person();
    message.setId(12345);
    message.setName('Peter');
    console.log(message);
    const encoded = message.serializeBinary();
    console.log(encoded);
    const decoded = proto.tutorial.Person.deserializeBinary(encoded);
    console.log(decoded);
    
    startExpress();
}

if (require.main===module) {
    try {
        main();
    } catch (err) {
        console.log(err);
    }
    console.log('bye');
}