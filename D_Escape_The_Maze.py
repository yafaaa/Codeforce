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

for _ in range(int(input())):
    input()
    n, friend = a_map()
    nums = a_nums()
    graph = [[] for _ in range(n+1)]    
    bound = [0] * (n+1)

    for _ in range(n-1):
        u, v = a_map()
        graph[u].append(v)
        graph[v].append(u)
    
    dq = deque(nums)
    t = 1
    visited = set()
    while dq:
        lgth = len(dq)
        
        for _ in range(lgth):
            parent = dq.popleft()
            visited.add(parent)
            for child in graph[parent]:
                if not bound[child] and child not in visited:
                    bound[child] = t
                    dq.append(child)
        t += 1
    
    dq = deque([1])
    t = 1
    # print(bound)
    f = False
    visited = set()
    while dq:
        # print(dq, "dq")
        lgth = len(dq)
        for _ in range(lgth):
            parent = dq.popleft()
            visited.add(parent)
            if not set(graph[parent])-visited:
                print("YES")
                f = True
                break
            for child in graph[parent]:
                if child in visited: continue
                if bound[child] <= t: continue

                dq.append(child)
                
        t += 1
        if f:
            break
    if not f:
        print('NO')

                
            
            


