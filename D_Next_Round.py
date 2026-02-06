import sys
n, i = map(int, input().split())
l = list(map(int, input().split()))
if i>n:
    print("NO")
    sys.exit()
cut_point = l[i-1]
s = 0
for a in l:
    if a>= cut_point and a!=0:
        s+=1
print(s)