import math


"""
sorting
-------
space O(1)
time O(n + nlogn)

using in-place sorting

array = sorted(array) # use langauge provided sorting algorithm

while 1 < count < n:
    if array[i] != count:
        return count
    count += 1
return False


dictionary
----------
space O(n)
time O(3n)

create a new dictionary name cache
cache = defaultdict(array)

while 1 < count < n:
    cache[array[count]] += 1
    
while 1 < count < n:
    if cache[count] != 0:
        return count
"""


def missing_number(array) -> int:
    """
    simple loop approach
    """
    array = sorted(array)

    for i in range(1, len(array) + 2):
        if i != array[i - 1]:
            return i

    return 0

"""
def missing_number(array) -> int:
    "
    dictionary approach
    "
    cache = defaultdict(array)

    for i in range(1, len(array) + 1):
        cache[array[i - 1]] = 1

    for i in range(1, len(array) + 2): # or n
        if not cache[i]:
            return i
    
    return False
"""
