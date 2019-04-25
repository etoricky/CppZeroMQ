#include "zmq.h"
#include <iostream>

#ifdef _DEBUG
#pragma comment(lib,"libzmq-mt-sgd-4_3_2.lib")
#else
#pragma comment(lib,"libzmq-mt-s-4_3_2.lib")
#endif
#pragma comment(lib,"Ws2_32.lib")
#pragma comment(lib,"Iphlpapi.lib")

int main()
{
	int major = 0;
	int minor = 0;
	int patch = 0;
	zmq_version(&major, &minor, &patch);
	std::wcout << "Current 0MQ version is " << major << '.' << minor << '.' << patch << '\n';
}