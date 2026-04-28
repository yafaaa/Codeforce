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
    val = "314159265358979323846264338327"
    string = input()
    a = 0
    cnt = 0
    for ch in string:
        if ch == val[a]:
            cnt += 1
            a += 1
        else:
            break
    print(cnt)

    