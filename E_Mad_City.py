
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
    n, mar, var = a_map()
    graph = [[] for _ in range(n+1)]
    bound = [0] * (n+1)
    incoming  = [0] * (n+1)

    for _ in range(n):
        u, v = a_map()
        graph[u].append(v)
        graph[v].append(u)
        incoming[v] += 1
        incoming[u] += 1
        
    
    dq = deque([mar])
    visited = set([mar])
    t = 0
    while dq:
        lght = len(dq)
        t += 1
        for _ in range(lght):
            parent = dq.popleft()

            for child in graph[parent]:
                if child in visited: continue
                bound[child] = t
                dq.append(child)
                visited.add(child)
        
    dq = deque([i for i in range(1,n+1) if len(graph[i]) == 1])
    
    while dq:
        parent = dq.popleft()
        

        for child in graph[parent]:
            incoming[child] -= 1
            if incoming[child] == 1:
                dq.append(child)

    cycle_element = set([i for i in range(1, n+1) if incoming[i] > 1])

    
    dq = deque([var])
    visited = set([var])
    t = 0
    while dq:
        lgth = len(dq)

        for _ in range(lgth):
            parent = dq.popleft()
            if parent in cycle_element and  bound[parent] > t:
                return 'YES'
            for child in graph[parent]:
                if child not in visited:
                    dq.append(child)
                    visited.add(child)
        t += 1
    return 'NO'



    
    
    

for _ in range(a_n()):
    print(solve())



    