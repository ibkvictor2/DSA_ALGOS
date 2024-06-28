import math
import sys
import pdb

handler_sum = 0
def dice_mem(n):
    cache = {str(k): None for k in range(1, n)}

    def dice(sum_val):
        remainder = n - sum_val
        if cache[str(remainder)]:
            return cache[str(remainder)]

        elif sum_val == n:
            return 1

        else:
            pro_sum = 0
            for face in range(1, 7): # available dice options
                if sum_val + face < n:
                    val = dice((sum_val + face))
                    pro_sum += val

            cache[str(n - sum_val)] = pro_sum
            return pro_sum

    dice(n)
    return cache[str(n - 1)] + 1

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    p_sum = dice_mem(n)
    print(int(p_sum % (1E9 + 7)))
