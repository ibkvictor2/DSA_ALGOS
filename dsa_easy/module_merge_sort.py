import math
from collections import defaultdict

"""
merge sort

spit array into two and continue splitting
operation
----------
if len(left_part) > 2:
    choose what comes left and right
    return sorted_array

else:
    use mid to get parts
    operation(left_part)
    operation(right_part)
    merge(left_part, right_part)
    return sorted_array
"""
12
1357 2468

def merge(left, right):
    result = list()
    left_pointer = 0
    right_pointer = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left_pointer > right_pointer:
            result.append(left[left_pointer])
            left += 1

        else:
            result.append(right[right_pointer])
            right += 1

    if left_pointer >= len(left):
        result.append(right[right_pointer:])

    if right_pointer >= len(right):
        result.append(left[left_pointer:])

    return result

def sort(array):
    if len(array) <= 1:
        return array

    else:
        mid = array // 2
        left = sort(array[:mid])
        right = sort(array[mid:])
        sorted_array = merge(left, right)

    return sorted_array
