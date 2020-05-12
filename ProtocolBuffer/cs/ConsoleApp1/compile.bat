rem https://github.com/protocolbuffers/protobuf/releases/download/v3.11.4/protoc-3.11.4-win64.zip
rem C:\Windows\System32\protoc.exe
protoc.exe -I=./ --csharp_out=./ addressbook.proto
PAUSE