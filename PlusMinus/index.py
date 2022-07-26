#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr);
    p=0.0;
    m=0.0;
    z=0.0;
    
    for x in arr:
        if(x==0):
            z+=1
        elif(x<0):
            m+=1;
        else:
            p+=1;
    print("{:.6f}".format(p/n))
    print("{:.6f}".format(m/n))
    print("{:.6f}".format(z/n))

if __name__ == '__main__':
    n = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
