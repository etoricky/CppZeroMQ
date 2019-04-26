#include "zhelpers.h"
#include "zmq.h"
#include <iostream>
#include <assert.h>
#include <thread>
#include <chrono>
#include <random>

#ifdef _DEBUG
#pragma comment(lib,"libzmq-mt-gd-4_3_2.lib")
#else
#pragma comment(lib,"libzmq-mt-4_3_2.lib")
#endif
#pragma comment(lib,"Ws2_32.lib")
#pragma comment(lib,"Iphlpapi.lib")

int main (void)
{
    void *context = zmq_ctx_new ();

    //  First, connect our subscriber socket
    void *subscriber = zmq_socket (context, ZMQ_SUB);
    zmq_connect (subscriber, "tcp://localhost:5561");
    zmq_setsockopt (subscriber, ZMQ_SUBSCRIBE, "", 0);

    //  0MQ is so fast, we need to wait a while
    std::this_thread::sleep_for(std::chrono::milliseconds(10));

    //  Second, synchronize with publisher
    void *syncclient = zmq_socket (context, ZMQ_REQ);
    zmq_connect (syncclient, "tcp://localhost:5562");

    //  - send a synchronization request
    s_send (syncclient, "");

    //  - wait for synchronization reply
    char *string = s_recv (syncclient);
    free (string);

    //  Third, get our updates and report how many we got
    int update_nbr = 0;
    while (1) {
        char *string = s_recv (subscriber);
        if (strcmp (string, "END") == 0) {
            free (string);
            break;
        }
        free (string);
        update_nbr++;
    }
    printf ("Received %d updates\n", update_nbr);

    zmq_close (subscriber);
    zmq_close (syncclient);
    zmq_ctx_destroy (context);
    return 0;
}