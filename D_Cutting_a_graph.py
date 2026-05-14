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

n, m, k = a_map()
query = []
for _ in range(m):
    input()
for _ in range(k):
    t, u, v = input().split()
    query.append((t, int(u), int(v)))
query.reverse()

size = [1] * (n+1)
parent = [i for i in range(n+1)]

def find(node):
    while node != parent[node]:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node

def union(u, v):
    u_parent = find(u)
    v_parent = find(v)

    if u_parent != v_parent:
        if size[u_parent] < size[v_parent]:
            u_parent, v_parent = v_parent, u_parent
        
        parent[v_parent] = u_parent
        size[u_parent] += size[v_parent]
ans = []   
for t, u, v in query:
    
    if t == "ask":
        ans.append("YES" if find(v) == find(u) else "NO")

    else:
        union(u,v)

for a in reversed(ans):
    print(a)