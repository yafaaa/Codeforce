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
        self.det = [[i, i, 1] for i in range(n+1)]
    
    def find(self, u):
        t = u
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
    
    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)

        if u_parent != v_parent:
            if self.det[u_parent][2] < self.det[v_parent][2]:
                u_parent, v_parent = v_parent, u_parent
                
            self.doer(u_parent, v_parent)
            self.parent[v_parent] = u_parent
    
    def doer(self, parent, child):
            a, b, c = self.det[child]
            d, e, f = self.det[parent]
            self.det[parent][0], self.det[parent][1], self.det[parent][2] = min(a,d), max(b,e), c+f

n, m = a_map()
        
dsu = DSU(n)

for _ in range(m):
    inpt = list(input().split())

    if len(inpt) == 3:
        u = int(inpt[1])
        v = int(inpt[2])
        dsu.union(u, v)

    else:
        u = int(inpt[1])
        print (*dsu.det[dsu.find(u)] )




