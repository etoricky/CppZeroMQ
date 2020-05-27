protoc.exe -I=./ --js_out=import_style=commonjs,binary:./ addressbook.proto
.\node_modules\.bin\browserify addressbook_pb.js -o bundle.js
PAUSE