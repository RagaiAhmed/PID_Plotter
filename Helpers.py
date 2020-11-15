from random import random
from random import seed

sum = 0
seed(0)

def perfect_response(x):
    """
        Acts as a feedback sensor
    :return: "hypothetical" reading after applying x
    """
    global sum
    if (x == -1): return 0

    sum += x
    return sum  # Example of accumulating system


def perfect_w_offset(x,offset):
    """
        Acts as a feedback sensor
    :return: "hypothetical" reading after applying x
    """
    global sum
    if (x == -1): return 0

    sum += x-offset
    return sum  # Example of a accumulating system with offset


def perfect_w_noise(x,offset,range):
    """
        Acts as a feedback sensor
    :return: "hypothetical" reading after applying x
    """
    global sum
    if (x == -1): return 0

    sum += x-offset+random()*range
    return sum  # Example of a accumulating system with offset and constant noise

time =0

def perfect_w_noise_at_t(x,offset,range,t):
    """
        Acts as a feedback sensor
    :return: "hypothetical" reading after applying x
    """
    global sum,time
    if (x == -1): return 0
    time+=1
    if time==t: sum+=random()*range
    sum += x-offset
    return sum  # Example of a accumulating system with offset and noise at specific time


def sensor_read(x):
    return perfect_w_noise_at_t(x,5,10,50)  # Maps to the underlying system
