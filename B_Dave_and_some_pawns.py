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
    n = int(input())
    nums = []

    for _ in range(2):
        nums.append(list(map(int,input())))
        
    direction = [(-1,0), (-1,-1), (-1,1)]
    i = 1

    def inbound(nw_c):
        return 0 <= nw_c < n

    cnt = 0
    for j in range(n):
        r, c = i, j
        if nums[r][j] == 0:
            continue
        for dr, dc in direction:
            nw_r = dr + r
            nw_c = dc + c
        
            if inbound(nw_c):
                if dr == -1 and dc == 0:
                    if nums[nw_r][nw_c] == 0:
                        cnt += 1
                        nums[nw_r][nw_c] = 2
                        break
                else:
                    if nums[nw_r][nw_c] == 1:
                        cnt += 1
                        nums[nw_r][nw_c] = 2
                        break
                        

                
    print(cnt)
                    
