#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    for i in range(97, 123):
        if(chr(i) in s.lower()):
            continue
        else:
            return 'not pangram'
    return 'pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
