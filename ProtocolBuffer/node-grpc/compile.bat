.\node_modules\grpc-tools\bin\protoc --js_out=import_style=commonjs,binary:./ --plugin=protoc-gen-grpc=.\node_modules\grpc-tools\bin\grpc_node_plugin.exe --grpc_out=./ helloworld.proto
PAUSE