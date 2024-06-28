"""
    time : O(n^2)
    space: O(c)
"""

def find_pivot(array: List):
    left_cum_sum = [0]
    right_cum_sum = []
    for i in range(len(array)):
        left_cum_sum.append(array[i] + left_cum_sum[-1])
        if right_cum_sum:
            right_cum_sum.append(array[-(i + 1)] + right_sum_sum[-1])
        else:
            right_cum_sum.append(0 + array[-(i + 1)])

    for idx_i in range(left_cum_sum):
        for idx_j in range(right_cum_sum):
            if (left_cum_sum[idx_i] == right_cum_sum[idx_j]) and (idx_i + idx_j + 1 == len(array) - 1):
                return idx_i
    return -1
