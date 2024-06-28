import math

"""
[3, 3, 5, 0, 0, 3, 1, 4]
"""

def generate_choice(array):
    results = []
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] - array[i] >= 0:
                results.append([i, j])
    return results

def strategy(tran_sum, portion, depth, full_array):
    if not portion or depth == 2:
        return tran_sum

    else:
        max_tran_sum = -math.inf
        choices = generate_choice(portion)
        for ch in choices:
            cand_tran_sum = strategy(((portion[ch[1]] - portion[ch[0]]) + tran_sum), full_array[(ch[1] + 1) :], depth + 1, full_array)
            
            if cand_tran_sum > max_tran_sum:
                max_tran_sum = cand_tran_sum

        return max_tran_sum

array = [3, 3, 5, 0, 0, 3, 1, 4]
print(strategy(0, array, 0, array))
