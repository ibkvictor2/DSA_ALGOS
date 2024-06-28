"""
    time : O(n)
    space: O(n)
"""

class NumArray: -> None
    def __init__(array: List) -> None:
        self.array : List = array

    def SumRange(left: int, right: int) -> int:
        return sum(self.array(left, right + 1))

def parser(operations: List, values: List):
    recentArray: NumArray = None
    result: List = []
    for idx in range(len(operations)):
        if operations[idx] == "SumRange":
            if recentArray:
                left = values[idx][0]
                right = values[idx][1]
                sum_value = recentArray.SumRange(left : right + 1)
                result.append(sum_value)

        elif operations[idx] == "NumArray":
            recentArray = NumArray(values[idx])
            result.append(None)

        else:
            return NotImplementedError

        return result
