#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    result = 0
    for i in range(31,-1,-1):
        if n//(2**i) == 1:
            n = n - 2**i
            x = 0
        else:
            x = 1
        result += 2**i * x

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    for q_itr in xrange(q):
        n = int(raw_input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
