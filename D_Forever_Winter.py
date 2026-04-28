from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def a_n():
    return int(input())

def a_s():
    return input().strip()

def a_map():
    return map(int, input().split())

def a_nums():
    return list(map(int, input().split()))

for _ in range(int(input())):
    v,e = map(int, input().split())
    graph = defaultdict(list)
    c_to_p = defaultdict(list)
    for P in range(e):
        child, parent = map(int, input().split())
        graph[parent].append(child)
        c_to_p[child].append(parent)

    for i in range(1, v+1):
        if not graph[i]:
            p = c_to_p[i]
            len(graph)



    
