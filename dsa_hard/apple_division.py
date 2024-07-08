import math
import sys
import pdb

def apple_division(n, array):
    array = sorted(array)
    if n == 1:
        return array[0]
    
    elif n == 2:
        return array[1] - array[0]

    else:
        return main(array[n - 2], array[n - 1], array[: n - 2])

def main(l_sum, r_sum, rem):
    if len(rem) == 0:
        return abs(l_sum - r_sum)

    else:
        min_pro_return = math.inf
        # choice making
        for idx in range(len(rem)):
            if l_sum < r_sum:
                rem_holder = rem
                val = rem_holder.pop(idx)
                return main(l_sum + val, r_sum, rem_holder)

            else:
                rem_holder = rem
                val = rem_holder.pop(idx)
                return main(l_sum, r_sum + val, rem_holder)

            if return_value < min_pro_return:
                min_pro_return = return_value
        
        return min_pro_return

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().rstrip().split()))
    print(apple_division(n, p))

