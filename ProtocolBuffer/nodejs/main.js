const protobuf = require("protobufjs");

const main = async function() {
    const root = await protobuf.load("addressbook.proto");
    var Person = root.lookupType("tutorial.Person");
    const message = Person.create({name:'Peters', id:12345});
    console.log(message);
    const encoded = Person.encode(message).finish();
    console.log(encoded);
    const decoded = Person.decode(encoded);
    console.log(decoded);
}

if (require.main===module) {
    try {
        main();
    } catch (err) {
        console.log(err);
    }
    console.log('bye');
}