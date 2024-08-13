memo = {}

# Memoization example
def factorial_memo(n):
    if not isinstance(n, int):  
        raise TypeError("Input must be an integer")
    
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = n * factorial_memo(n - 1)
    return memo[n]

# Tail recursion optimization
def factorial_tail(n, acc=1):
    if not isinstance(n, int):  
        raise TypeError("Input must be an integer")
    
    if n == 0:
        return acc
    return factorial_tail(n - 1, n * acc)

# Loop unrolling example
def bubble_sort_unrolled(arr):
    n = len(arr)
    for i in range(0, n-1, 2):
        for j in range(n-1, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            if arr[j-2] > arr[j-1]:
                arr[j-2], arr[j-1] = arr[j-1], arr[j-2]
    return arr

# Binary search optimization
def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Element not found

# Parallelism example
import concurrent.futures

def parallel_factorials(nums):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(factorial_memo, nums))
    return results

# Lazy evaluation
def lazy_factorial(n):
    if not isinstance(n, int):  
        raise TypeError("Input must be an integer")
    
    def compute():
        if n == 0:
            return 1
        return n * factorial_memo(n - 1)
    
    return compute

# Heuristic optimization (Greedy Knapsack)
def greedy_knapsack(weights, values, capacity):
    n = len(weights)
    ratio = [(values[i] / weights[i], i) for i in range(n)]
    ratio.sort(reverse=True)

    max_value = 0
    for r, i in ratio:
        if capacity >= weights[i]:
            capacity -= weights[i]
            max_value += values[i]
        else:
            max_value += r * capacity
            break
    return max_value

# Dynamic Programming (Fibonacci)
def fibonacci_dp(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    return fib[n]


# memo = {}

# def factorial_memo(n):
#     if not isinstance(n, int):  
#         raise TypeError("Input must be an integer")
    
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         return 1
#     memo[n] = n * factorial_memo(n - 1)
#     return memo[n]

# def bubble_sort_unrolled(arr):
#     n = len(arr)
#     for i in range(0, n-1, 2):
#         for j in range(n-1, 0, -1):
#             if arr[j-1] > arr[j]:
#                 arr[j-1], arr[j] = arr[j], arr[j-1]
#             if arr[j-2] > arr[j-1]:
#                 arr[j-2], arr[j-1] = arr[j-1], arr[j-2]
#     return arr



