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

#define SUBSCRIBERS_EXPECTED  1
int main (void)
{
    void *context = zmq_ctx_new ();

    //  Socket to talk to clients
    void *publisher = zmq_socket (context, ZMQ_PUB);

    int sndhwm = 1100000;
    zmq_setsockopt (publisher, ZMQ_SNDHWM, &sndhwm, sizeof (int));

    zmq_bind (publisher, "tcp://*:5561");

    //  Socket to receive signals
    void *syncservice = zmq_socket (context, ZMQ_REP);
    zmq_bind (syncservice, "tcp://*:5562");

    while (true) {
        //  Get synchronization from subscribers
        printf ("Waiting for subscribers\n");
        int subscribers = 0;
        while (subscribers < SUBSCRIBERS_EXPECTED) {
            //  - wait for synchronization request
            char *string = s_recv (syncservice);
            free (string);
            //  - send synchronization reply
            s_send (syncservice, "");
            subscribers++;
        }
        //  Now broadcast exactly 1M updates followed by END
        printf ("Broadcasting messages\n");
        int update_nbr;
        for (update_nbr = 0; update_nbr < 1000000; update_nbr++)
            s_send (publisher, "Rhubarb");

        s_send (publisher, "END");
    }
    

    zmq_close (publisher);
    zmq_close (syncservice);
    zmq_ctx_destroy (context);
    return 0;
}