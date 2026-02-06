from collections import Counter
for _ in range(int(input())):
    n = int(input())
    string = input()
    maxx = 0
    set1 = set()
    d = Counter(string)
    a, b= 0, len(set(string))
    for i,s in enumerate(string):
        if s not in set1:
            a+=1
            set1.add(s)
        d[s]-=1
        if d[s]==0:
            del d[s]
        if s not in d:
            b-=1
        maxx = max(maxx,a+b)
        if maxx == n*(n-1):
            break
    print(maxx)
