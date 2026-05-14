import sys
import math
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
    n, m, k = a_map()
    if n - math.ceil(n/m) > k:
        print("YES")
    else:
        print('NO')