import math
import sys
import pdb

def weird_algo(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
            result.append(n)

        else:
            n = int((n * 3) + 1)
            result.append(n)
    return result

if __name__ == "__main__":
    str_n = sys.stdin.readline().rstrip()
    n = int(str_n)
    result = weird_algo(n)
    for re_idx in range(len(result)):
        if re_idx  == len(result) - 1:
            sys.stdout.write(f"{result[re_idx]}")
        
        else:
            sys.stdout.write(f"{result[re_idx]} ")
