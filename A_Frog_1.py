import sys
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def a_n():
    return int(input())

def a_s():
    return input().strip()

def a_map():
    return map(int, input().split())

def a_nums():
    return list(map(int, input().split()))

n = a_n()
nums = a_nums()

memo = {}
def fun(i):
    if i == n-1:
        return 0
    
    if i in memo:
        return memo[i]
    
    #if i+1 < n:
    memo[i] = abs(nums[i] - nums[i+1]) + fun(i + 1) # , memo[i])
        
        
    if i+2 < n:
        memo[i] = min(abs(nums[i] - nums[i+2]) + fun(i + 2), memo[i])
    return memo[i]
print(fun(0))

    


