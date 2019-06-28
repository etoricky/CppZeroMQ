#include "zmq.hpp"
#include <string>
#include <iostream>
#include <assert.h>
#include <thread>
#include <chrono>

#ifdef _DEBUG
#pragma comment(lib,"libzmq-mt-gd-4_3_2.lib")
#else
#pragma comment(lib,"libzmq-mt-4_3_2.lib")
#endif
#pragma comment(lib,"Ws2_32.lib")
#pragma comment(lib,"Iphlpapi.lib")

int main (void)
{
    //  Prepare our context and socket
    zmq::context_t context (1);
    zmq::socket_t socket (context, ZMQ_REP);
    socket.bind ("tcp://*:5555");

    while (true) {
        zmq::message_t request;
        
        //  Wait for next request from client
        socket.recv (request);
        std::string rpl = std::string(static_cast<char*>(request.data()), request.size());
        std::cout << "Received " << rpl.size() << " bytes, " << rpl << std::endl;
        
        std::this_thread::sleep_for(std::chrono::seconds(1));          //  Do some 'work'
        
        //  Send reply back to client
        zmq::message_t reply (5);
        memcpy (reply.data (), "World", 5);
        socket.send (reply);
    }
    return 0;
}