from typing import List

def mergeSort(arr: List[int]) -> List[int]:
    # Your code here
    pass

# Read input
arr = list(map(int, input().split()))
result = mergeSort(arr)
print(' '.join(map(str, result)))