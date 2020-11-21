#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    if n == 1:
        return 0
    color_nmbs = defaultdict(lambda: 0)

    for color in ar:
        color_nmbs[color] += 1

    result = 0
    for value in color_nmbs.values():
        if value % 2 == 0:
            result += value/2
        else:
            result += (value - 1) / 2
    return int(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
