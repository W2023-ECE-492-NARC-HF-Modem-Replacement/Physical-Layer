#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pub.py
# Author: Jenish patel

import zmq
import time
import signal
import pmt

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:55557")

while True:
    try:
        outMsg = input(">")
        # socket.send(pmt.serialize_str(pmt.cons(pmt.PMT_NIL,pmt.init_u8vector(1, ord(outMsg)))))
        outMsg_stream = list(outMsg)

        #while(True):

        socket.send(pmt.serialize_str(pmt.to_pmt(len(outMsg_stream))))
        for byte in outMsg_stream:
            socket.send(pmt.serialize_str(pmt.to_pmt(ord(byte))))
            # time.sleep(0.10)
        # send a dummy byte for delimiting purposes
        dummy_byte = 0xFF
        socket.send(pmt.serialize_str(pmt.to_pmt(dummy_byte)))

        #time.sleep(0.10)
    except KeyboardInterrupt:
        print ("interrupt received. shutting down.")
        # clean up
        socket.close()
        context.term()
        exit()