memo = {}

def factorial_memo(n):
    if not isinstance(n, int):  
        raise TypeError("Input must be an integer")
    
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = n * factorial_memo(n - 1)
    return memo[n]

def bubble_sort_unrolled(arr):
    n = len(arr)
    for i in range(0, n-1, 2):
        for j in range(n-1, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            if arr[j-2] > arr[j-1]:
                arr[j-2], arr[j-1] = arr[j-1], arr[j-2]
    return arr



