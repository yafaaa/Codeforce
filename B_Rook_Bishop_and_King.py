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
    r1, c1, r2, c2 = a_map()
    if r1 == r2 and c1 == c2:
        return "0 0 0"
    a = 1 if (r1 == r2 or c1 == c2) else 2
    if (r1-c1 == r2-c2 or r1+c1 == r2+c2):
        b = 1
    elif abs((r1-c1)%2) == abs((r2-c2)%2):
        b = 2
    else:
        b = 0
    
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def isbound(nw_r, nw_c):
        return 1<= nw_r < 9 and 1<= nw_c < 9

    def bfs(): 
        dq = deque([(r1,c1)])
        visited = set((r1,c1))
        level = 0
        while dq:
            level += 1
            lgth = len(dq)
            for _ in range(lgth):
                r, c = dq.popleft()
                if r == r2 and c == c2:
                    return level-1
                for dr, dc in direction:
                    nw_r = dr + r
                    nw_c = dc + c

                    if isbound(nw_r, nw_c) and (nw_r, nw_c) not in visited:
                        dq.append((nw_r, nw_c))
                        visited.add((nw_r, nw_c))
    c = bfs()
    return f"{a} {b} {c}"
print(solve())
