
test = int(input())
l = []
for i in range(test):
    ll = list(map(int, input().split()))
    ll.append(i)
    l.append(ll)
    
    
l.sort(key=lambda x: (x[0], -x[1]))
for i in range(1,len(l)):
    if l[i][1]<=l[i-1][1]:
        print(f"{l[i][2]+1} {l[i-1][2]+1}")
        break
else:
    print(f" {-1} {-1}")