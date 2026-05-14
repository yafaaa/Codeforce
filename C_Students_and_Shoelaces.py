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

n, m = a_map()
graph = [[] for _ in range(n+1)]
incoming = [0] * (n+1)

for _ in range(m):
    u, v = a_map()
    graph[u].append(v)
    graph[v].append(u)
    incoming[u] += 1
    incoming[v] += 1

level = 0
while True:
    
    dq = [i for i in range(1, n + 1) if incoming[i] == 1]

    if not dq:
        break
    
    level += 1
    
    for student in dq:
        incoming[student] -= 1
        for neighbor in graph[student]:
                incoming[neighbor] -= 1

print(level)