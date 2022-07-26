#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    t = s[-2:] # am||pm
    h = s[:2]   # 
    m = s[2:-2]
    res =''
    if(t=='PM'):
        if(int(h)>=1 and int(h)!=12):
            res = str(12+int(h))+m
        else:
            res = (h+m)
    else:
        if(int(h)==12):
            res = '00'+m
        else:
            res =h+m;
    return (res)
            
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
