t = int(input())
for _ in range(t):
    n =  int(input())
    l = list(map(int, input().split()))
    non_zero = 0
    summ = 0
    for a in l:
        summ+=a
        if a!=0:
            non_zero+=1

    if summ == n:
        print(1)
    else:
        print(non_zero)
        
    # presum, greedy 