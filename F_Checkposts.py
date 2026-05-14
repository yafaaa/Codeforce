import sys
sys.setrecursionlimit(10**7)
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
cost = [0] + a_nums()
graph = [[] for _ in range(n+1)]

for _ in range(a_n()):
    u, v = a_map()
    graph[u].append(v)

time = 1

visited_time = [0]*(n+1)
shortest_time = [0]*(n+1)
visited = [False] * (n+1)
instack = [False] * (n+1)

stack = []

def dfs(node):
    global time
    visited_time[node] = time
    shortest_time[node] = time
    time += 1

    visited[node] = True

    stack.append(node)
    instack[node] = True

    for child in graph[node]:
        if not visited[child]:
            dfs(child)
        if instack[child]:
            shortest_time[node] = min(shortest_time[node], shortest_time[child])
    
    if visited_time[node] == shortest_time[node]:
        while stack[-1] != node:
            cur = stack.pop()
            instack[cur] = False
            shortest_time[cur] = shortest_time[node]
        instack[stack.pop()] = False
        
        

for i in range(1, n+1):
    if not visited[i] :
        dfs(i)
groups = defaultdict(list)
for node in range(1, n + 1):
    groups[shortest_time[node]].append(cost[node])
ans = 0
ways = 1
mod = 10**9 + 7
for key in groups:
    mn = min(groups[key])
    cnt = groups[key].count(mn)
    ans += mn
    ways = (ways * cnt) % mod
print(ans, ways)

