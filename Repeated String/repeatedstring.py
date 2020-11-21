#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    a = 0
    for c in s:
        if c == 'a':
            a += 1
    
    sub = n/len(s)
    if sub - int(sub) == 0:
        return int(sub * a)
    else:
        mod = n % len(s)
        more = 0
        for i in range(mod):
            if s[i] == 'a':
                more += 1
        
        return int(sub)*a + more
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
