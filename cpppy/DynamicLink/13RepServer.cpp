#include "zmq.h"
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
    //  Socket to talk to clients
    void *context = zmq_ctx_new ();
    void *responder = zmq_socket (context, ZMQ_REP);
    int rc = zmq_bind (responder, "tcp://*:5555");
    assert (rc == 0);

    while (1) {
        char buffer [10];
        zmq_recv (responder, buffer, 10, 0);
        printf ("Received %s\n", buffer);
        fflush(stdout);
        std::this_thread::sleep_for(std::chrono::seconds(1));          //  Do some 'work'
        zmq_send (responder, "World", 5, 0);
    }
    return 0;
}