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
    a, b = a_map()
    mn = float('inf')
    def fun(a, b, c):
        global mn
        if a == 0 or b > a or c > mn: 
            mn = min(mn, c)
            return
        c += 1
        
        if b != 1:
            fun(a//b, b, c)
                
        
        fun(a, b+1, c)
            
        
    fun(a,b,0)
    print(mn+1)