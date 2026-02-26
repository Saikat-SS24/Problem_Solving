## Cats and a Mouse

```bash
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_a = abs(z - x)
    cat_b = abs(z - y)
    
    if cat_a > cat_b:
        return "Cat B"
    elif cat_a == cat_b:
        return "Mouse C"
    else:
        return "Cat A"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
```