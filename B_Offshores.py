
for _ in range(int(input())):
    n, cut, credit = list(map(int, input().split()))
    l = list(map(int, input().split()))
    maxx = 0
    max_save_idx = 0
    for i, a in enumerate(l):
        trans_cut = (a//cut)*(cut-credit)
        left_cut = a%cut
        total = trans_cut+left_cut
        if total > maxx:
            maxx = total
            max_save_idx = i
    summ = l[max_save_idx]
    for i, a in enumerate(l):
        if i == max_save_idx:
            continue
        summ += (a//cut)*(credit)
    print(summ)
    
        