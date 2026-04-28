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
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input())))
    ans = [1]
    for i in range(2, n+1):
        
        for j, num in enumerate(ans):
            if not matrix[i-1][num-1]:
                ans = ans[:j] + [i] +ans[j:]
                break
        else:
            ans.append(i)
    
    print(*ans)



        



