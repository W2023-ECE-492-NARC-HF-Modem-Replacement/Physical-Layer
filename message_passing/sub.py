#!/usr/bin/python3
# -*- coding: utf-8 -*-

# zmq_SUB_proc.py
# Author: Marc Lichtman

import zmq
import numpy as np
import time
import pmt

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:55555") # connect, not bind, the PUB will bind, only 1 can bind
socket.setsockopt(zmq.SUBSCRIBE, b'') # subscribe to topic of all (needed or else it won't work)

while True:
    if socket.poll(10) != 0: # check if there is a message on the socket
        recv_pmt_msg_len = socket.recv() # grab the message
        print(recv_pmt_msg_len) 
        print("length: ", list(recv_pmt_msg_len)[4])

        arr = []
        for _ in range(list(recv_pmt_msg_len)[4]):
            recv_pmt_msg = socket.recv() # grab the message
            arr.append(chr(list(recv_pmt_msg)[4]))

        msg = ''.join(arr)
        print(msg)
    else:
        time.sleep(0.1) # wait 100ms and try again
