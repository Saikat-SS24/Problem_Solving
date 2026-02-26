## Breaking the Records

```bash
#!/bin/python3

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
    max_score = scores[0]
    min_score = scores[0]
    max_count = 0
    min_count = 0
    
    for i in range(len(scores)):
        if scores[i] > max_score:
            max_count += 1
            max_score = scores[i]
            
        elif scores[i] < min_score:
            min_count += 1
            min_score = scores[i]
            
    return max_count, min_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
```