import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here

    arr = sorted(arr)
    print sum(arr[:-1]),sum(arr[1:])
        
        

if __name__ == '__main__':

    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
