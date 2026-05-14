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



class DSU:
    
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
    
    def find(self, u):
        while self.parent[u] != u:
            u = self.parent[u]
        return u
    
    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)

        if u_parent != v_parent:

            if self.rank[u_parent] > self.rank[v_parent]:
                self.parent[v_parent] = u_parent
            
            elif self.rank[u_parent] < self.rank[v_parent]:
                self.parent[u_parent] = v_parent
            
            else:
                self.parent[v_parent] = u_parent
                self.rank[u_parent] += 1
n, m = a_map()
        
dsu = DSU(n)

for _ in range(m):
    typ, u, v = input().split()
    u = int(u)
    v = int(v)

    if typ == "union":
        dsu.union(u, v)
    else:
        if dsu.find(u) == dsu.find(v):
            print('YES')
        else:
            print('NO')
