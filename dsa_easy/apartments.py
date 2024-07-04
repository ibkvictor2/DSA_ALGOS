import math
import sys

"""
apartments
----------
combinations of all possible solution with best solution with no trimming
iterative and recursive



using any other method would require a specific set of priority definition which would not work in all applications.
"""

def apartments(alloc, aparts, sizes):
    if not len(aparts) or not len(size):
        return alloc

    else:
        invalid = set()
        # solution space
        for si in range sizes:
            for ap in aparts:
                if ap >= (si - k) and ap <= (si + k): # if apartment is greater than upper bound of choice and apparment is less than lower bound of choice.
                    apartments(alloc, )
            
        apartments(alloc, 

def apartments(aparts, sizes, k):
    alloc_ind = set()
    for ap_idx in range(len(aparts)): # ap_idx : aparment index
        for si in sizes:
            if ((aparts[ap_idx] >= si - k) and (aparts[ap_idx] <= si + k)) and ap_idx not in alloc_ind:
                alloc_ind.append(ap_ind)

    return len(alloc_ind)

if __name__ == "__main__":
    m, n, k = sys.stdin.readline().rstrip().split()
    aparts = sys.stdin.readline().rstrip().split()
    sizes = sys.stdin.readline().rstrip().split()
    print(apartmentss(aparts, sizes))
