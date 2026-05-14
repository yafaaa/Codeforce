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

for _ in range(a_n()):
    n = a_n()
    nums = a_nums()
    d = dict()
    for i, num in enumerate(nums):
        if nums[nums[i]-1]-1 == i:
            print(2)
            break
    else:
        print(3)
        

    
