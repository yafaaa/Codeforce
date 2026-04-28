
def solve():
    n = int(input())
    if n <=3:
        return n
    elif not n%2:
        return 0
    return 1
for _ in range(int(input())):
    print(solve())