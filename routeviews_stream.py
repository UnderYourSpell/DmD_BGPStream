import pybgpstream
import sys
import time

'''
This document outputs routing information from a live server called routeviews
I am still trying to understand the information it pulls
'''

runtime = 6

stream = pybgpstream.BGPStream(
    # accessing routeview-stream
    project="routeviews-stream",
    # filter to show only stream from amsix bmp stream
    filter="router amsix",
)


with open('routeviws_stream.txt','w') as r_stream:
    sys.stdout = r_stream
    
    start_time = time.time()

    for elem in stream:
        if time.time() - start_time >= runtime:
            break
        print(elem)
    
    r_stream.close()