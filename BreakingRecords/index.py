
import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    cmin =0
    cmax =0
    minimum = scores[0]
    maximum = scores[0]
    for i in scores:
        if(i<minimum):
            minimum = i;
            cmin +=1;
        elif(i>maximum):
            maximum =i;
            cmax +=1
    return cmax,cmin

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
