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

def solve():
    n, m = a_map()
    graph = [[] for i in range(1,n+1)]
    incoming = [0] * (n+1)
    undirected = []

    for i in range(m):
        s, parent, child = a_map()
        if not s: 
            undirected.append([parent, child])
            continue
        graph[parent].append(child)
        incoming[child] += 1

    if is_cycle():
        return 'NO'
    
    

    

    
    def is_cycle():
        dq = deque([ i for i in range(1,n+1) if not incoming[i]])
        ans = 0
        while dq:
            parent = dq.popleft()
            ans.append(parent)
            for child in graph[parent]:
                incoming[child] -= 1

                if not incoming[child]:
                    dq.append(child)
        
        return n != ans


for _ in range(a_n()):
    print(solve())