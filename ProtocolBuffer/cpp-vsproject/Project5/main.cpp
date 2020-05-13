#include "addressbook.pb.h"
#include <iostream>
#include <sstream>

#ifdef _DEBUG
	#pragma comment(lib, "libprotobufd.lib")
#else
	#pragma comment(lib, "libprotobuf.lib")
#endif

int main() {
	using namespace tutorial;
	Person person;
	person.set_id(12345);
	person.set_name("peter");
	std::string serialized = person.SerializeAsString();
	Person deserialized;
	deserialized.ParseFromString(serialized);
	std::cout << person.name();
	return 0;
}