import sys
import pdb

def distinct(integers: list):
    hashmap = set()
    return len(set(integers))

if __name__ == "__main__":
    size = int(sys.stdin.readline())
    in_list = list(map(int, sys.stdin.readline().rstrip().split()))
    assert(len(in_list) == size)
    print(distinct(in_list))
