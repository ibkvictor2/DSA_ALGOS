import math
import sys
import pdb

"""
Digit Query Algorithm (index)
----------------------
storage : cache : dictionary : 
a format 1, 10, 100, 10000
idx format 9, 189, 2889, 38889, 488889, ect. per digit

what digit type is it?
    greater than or  less than
    obtain the l and r throught a loop through idx format

What number is it?
    left last idx digit number
    subtract 
    divide by number of digits
    add to
    left last idx digit number
    
what digit of that number is it?
    subract
    digit = mod by number of digits
    return str(number)[digit]
"""

def digit_query(q: int) -> int:
    pdb.set_trace()
    pattern = [9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889, 98888888889]
    cache = {pat: {"a" : float(f"1e{pat_idx}"), "l" : (float(f"1e{pat_idx}")) - 1, "d" : (pat + 1)} for (pat_idx, pat) in enumerate(pattern)}

    def binary_search(q, pattern):
        if len(pattern) == 1:
            return cache[pattern[0]]

        else:
            mid_floor = len(pattern) // 2
            if q > pattern[mid_floor]:
                return binary_search(q, pattern[mid_floor :])
            else:
                return binary_search(q, pattern[: mid_floor])
    
    l, r, d = binary_search(q, pattern)

    num = ((q - l)//d) + l
    digit = (q - l) % d

    return int(str(num)[digit])

if __name__ == "__main__":
    k = int(sys.stdin.readline())
    for idx in range(k):
        print(digit_query(int(sys.stdin.readline())))
