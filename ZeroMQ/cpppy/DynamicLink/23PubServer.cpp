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
    //  Prepare our context and publisher
    void *context = zmq_ctx_new ();
    void *publisher = zmq_socket (context, ZMQ_PUB);
    int rc = zmq_bind (publisher, "tcp://*:5556");
    assert (rc == 0);

    //  Initialize random number generator
    std::default_random_engine generator;
    std::uniform_int_distribution<int> distribution1(1,100000);
    std::uniform_int_distribution<int> distribution2(1,215);
    std::uniform_int_distribution<int> distribution3(1,50);
    while (1) {
        //  Get values that will fool the boss
        int zipcode, temperature, relhumidity;
        zipcode     = distribution1(generator);
        temperature = distribution2(generator) - 80;
        relhumidity = distribution3(generator) + 10;

        //  Send message to all subscribers
        char update [20];
        sprintf (update, "%05d %d %d", zipcode, temperature, relhumidity);
        s_send (publisher, update);
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    zmq_close (publisher);
    zmq_ctx_destroy (context);
    return 0;
}