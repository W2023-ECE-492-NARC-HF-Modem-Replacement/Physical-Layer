#!/usr/bin/python3
# -*- coding: utf-8 -*-

# sub_file.py
# Author: Jenish patel

import zmq
import numpy as np
import time
import pmt

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:55555") # connect, not bind, the PUB will bind, only 1 can bind
socket.setsockopt(zmq.SUBSCRIBE, b'') # subscribe to topic of all (needed or else it won't work)

with open("small_rx_file.txt",'w') as file:
    pass

while True:
    if socket.poll(10) != 0: # check if there is a message on the socket
        recv_pmt_msg_len = socket.recv() # grab the message
        print(recv_pmt_msg_len) 
        print("length: ", list(recv_pmt_msg_len)[4])

        arr = []
        for _ in range(list(recv_pmt_msg_len)[4]):
            recv_pmt_msg = socket.recv() # grab the message
            arr.append(chr(list(recv_pmt_msg)[4]))

        new_arr = arr[2:-1]
        msg = ''.join(new_arr)
        
        # Write message to file
        f = open("small_rx_file.txt", "a")
        f.write(msg)
        f.close()
    else:
        time.sleep(0.1) # wait 100ms and try again
