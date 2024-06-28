import heapify

def solve(array):
    for (idx, val) in enum(array):
        ref[val] = [idx]
        result[val] = None

    heap = heapify(array)
    gift = 1
    old_val = heap.pop()
    result[val] = gift
    
    for i in range(len(heap) - 1):
        val = heap.pop()
        if ref[val] == ref[old_val] + 1 or ref[val] == ref[old_val] - 1:
            gift += 1
            result[val] = gift

        else:
            result[val] = gift

    return result
            
        ref = dict(array)
