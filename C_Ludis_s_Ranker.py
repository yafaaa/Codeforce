n = int(input())
string = list(map(int,input().split()))
sort_ed = sorted(string, reverse=True)
rank = dict()
res = []
for i, a in enumerate(sort_ed):
    if a not in rank:
        rank[a]=str(i+1)    
for i in range(len(string)):
    a = string[i]
    res.append(rank[a])
print(" ".join(res))

    