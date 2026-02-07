
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    dge = dict()
    dl = dict()
    
    for i, a in enumerate(l):
        if a>=i:
            k = a-i
            dge[k] = dge.get(k, 0)+1
        
        else:
            k = i-a
            dl[k] = dl.get(k, 0)+1
        
    sge = sum(((c-1)*c)//2 for c in dge.values() if c!=1)
    sl = sum(((c-1)*c)//2 for c in dl.values() if c!=1)

    print(f"{sl+sge}")