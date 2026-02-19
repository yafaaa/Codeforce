n = int(input())
l = list(map(int, input().split()))
day = 1
for a in sorted(l):
    if a >= day:
        day += 1
print(day-1)