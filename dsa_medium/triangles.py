import math

"""
   2
  3 4
 6 5 7
4 1 8 3
"""

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

def is_valid(new_id, prev_id):
    if prev_id + 1 == new_id or prev_id == new_id:
        return True
    return False

sum = math.inf
def triangle_solve(cand_sum, r, c, triangle): # main recursing function
    # base case
    if r == len(triangle):
        return cand_sum

    else:
        # recursion phase
        summy = math.inf
        for idx in range(len(triangle[r])):
            if is_valid(idx, c):
                summy_cand = triangle_solve(cand_sum + triangle[r][idx], r + 1, idx, triangle)

        # comparison phase
                if summy_cand < summy:
                    summy = summy_cand

        return summy

print(triangle_solve(0, 0, -1, [[-10]]))
print(triangle_solve(0, 0, -1, triangle))
