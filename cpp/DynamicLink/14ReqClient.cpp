#include "zmq.h"
#include <iostream>

#ifdef _DEBUG
#pragma comment(lib,"libzmq-mt-gd-4_3_2.lib")
#else
#pragma comment(lib,"libzmq-mt-4_3_2.lib")
#endif
#pragma comment(lib,"Ws2_32.lib")
#pragma comment(lib,"Iphlpapi.lib")

int main (void)
{
    printf ("Connecting to hello world server\n");
    void *context = zmq_ctx_new ();
    void *requester = zmq_socket (context, ZMQ_REQ);
    zmq_connect (requester, "tcp://localhost:5555");

    int request_nbr;
    for (request_nbr = 0; request_nbr != 10*1000*1000; request_nbr++) {
        char buffer [10];
        printf ("Sending Hello %d\n", request_nbr);
        fflush(stdout);
        zmq_send (requester, "Hello", 5, 0);
        zmq_recv (requester, buffer, 10, 0);
        printf ("Received World %d\n", request_nbr);
        fflush(stdout);
    }
    zmq_close (requester);
    zmq_ctx_destroy (context);
    return 0;
}