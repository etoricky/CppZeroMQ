import addressbook_pb2 as addressbook
source = addressbook.Person()
source.name = 'Alice'
source.id = 123456
serialized = source.SerializeToString()
print(len(serialized), serialized)
parsed = addressbook.Person()
parsed.ParseFromString(serialized)
print(parsed.name)
print(parsed.id)