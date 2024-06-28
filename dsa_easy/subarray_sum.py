"""
    recursive approach
"""

def subarray_sum(array, k):
    result = 0

    def recursive(sum_val, sub_array):
        if not sub_array:
            if sum_val == k:
                result += 1
            return

        else:
            for i in range(len(sub_array)):
                return recursive(sum_val + sub_array[i], sub_array.remove(i))

        return result

"""
    iterative approach
"""

def sub_array_sum(array, k):
    result = 0
    for idx_i in range(len(array)):
        for idx_j in range(idx_i + 1, len(array)):
            sum_val = sum(array[idx_i, idx_j + 1])
            if sum_val == k:
                result += 1
    return result
