
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    res = []
    
    for val in range(1, n+1):
        if val in l1:
            idx = l1.index(val)
            for i in range(idx-1, val-2, -1): #val-1 is index
                l1[i], l1[i+1] = l1[i+1], l1[i]
                res.append([1, i+1])
        else:
            idx = l2.index(val)
            if val-1 <= idx:
                for i in range(idx-1, val-2, -1): #val-1 is index
                    l2[i], l2[i+1] = l2[i+1], l2[i]
                    res.append([2, i+1])
        
            else:
                for i in range(idx, val-1):
                    l2[i], l2[i+1] = l2[i+1], l2[i]
                    res.append([2, i+1])
            
            l1[val-1], l2[val-1] = l2[val-1], l1[val-1]
            res.append([3, val-1+1])
       

    
    for val in range(n+1, 2*n+1): # val-(n+1) is val-1 here
        idx = l2.index(val)
        if val-(n+1) <= idx:
            for i in range(idx-1, val-(n+1)-1, -1): 
                l2[i], l2[i+1] = l2[i+1], l2[i]
                res.append([2, i+1])        
            
        else:
            for i in range(idx, val-(n+1)):
                l2[i], l2[i+1] = l2[i+1], l2[i]
                res.append([2, i+1])

    print(l1)
    print(l2)
    print(len(res))
    for l in res:
        print(" ".join(map(str,l)))




