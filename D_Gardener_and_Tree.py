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
    input()
    n, k = a_map()
    graph = [set() for _ in range(n+1)]
    incoming = [0] * (n+1)
    for _ in range(n-1):
        u, v = a_map()
        if v not in graph[u]:
            graph[u].add(v)
            incoming[v] += 1

        if u not in graph[v]:
            graph[v].add(u)
            incoming[u] += 1
    
    
    
    
    dq = deque([node for node in range(1, n+1) if incoming[node] < 2])
    leaves = 0
    i = 0
    while dq and i < k:    
        
        lgth = len(dq)
        
        for _ in range(lgth):
            parent = dq.popleft()
            leaves += 1
            incoming[parent] = 0
            for child in graph[parent]:
                graph[child].remove(parent)
                incoming[child] -= 1
                if incoming[child] == 1:
                    dq.append(child)
        i += 1
        
    print(n-leaves)