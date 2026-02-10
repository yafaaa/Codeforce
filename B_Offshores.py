
for _ in range(int(input())):
    n, cut, credit = list(map(int, input().split()))
    l = list(map(int, input().split()))
    m = 0
    idx = 0
    for i, a in enumerate(l):
        if m<(a%cut):
            idx = i
            m = a%cut
            if m == cut-1:
                break
    summ = l[idx]
    for i, a in enumerate(l):
        if i == idx:
            continue
        summ+=(a//cut)*credit
    print(summ)
        
        