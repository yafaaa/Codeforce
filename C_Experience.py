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

parent = [i for i in range(n + 1)]
size = [1] * (n + 1)
ans = [0] * (n + 1)

def find(node):
    while node != parent[node]:
        node = parent[node]
    return node

def union(u, v):
    pu, pv = find(u), find(v)
    if pu == pv: return

    if size[pu] < size[pv]:
        pu, pv = pv, pu
    
    ans[pv] -= ans[pu]
    parent[pv] = pu
    size[pu] += size[pv]

def res(node):
    cur = ans[node]
    while node != parent[node]:
        node = parent[node]
        cur += ans[node]
    return cur


for _ in range(m):
    inpt = list(input().split())
    if inpt[0] == "add":
        node, val = int(inpt[1]), int(inpt[2])
        ans[find(node)] += val

    elif inpt[0] == "join":
        u, v = int(inpt[1]), int(inpt[2])
        union(u, v)
    else:
        node = int(inpt[1])
        print(res(node))
        
