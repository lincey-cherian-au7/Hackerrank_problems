#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    XOR = 0
    a = sorted(a);
    for i in range(len(a)) :
        XOR = XOR ^ a[i]
    return XOR
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    a = map(int, raw_input().rstrip().split())

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
