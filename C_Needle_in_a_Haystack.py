from collections import Counter
import sys 
test = int(input())
for i in range(test):
    needle = input()
    haystack = input()
    if len(needle)>len(haystack):
        print("Impossible")
        continue
    d_hay = Counter(haystack)
    f = False
    l = []
    res = []
    s=" "
    for i in range(len(needle)):
        a = needle[i]
        if a not in d_hay:
            print("Impossible")
            f = True
            break
        d_hay[a]-=1
        if d_hay[a]==0:
            del d_hay[a]

    if f:
        continue
    for k, v in d_hay.items():
        l.append(k*v)
    l = sorted(l)
    a,b = 0, 0
    while a<len(needle) and b<len(l):
        if needle[a]>l[b]:
            res.append(l[b])
            b+=1
        else:
            res.append(needle[a])
            a+=1
    if a<len(needle):
        res.extend(needle[a:])
    if b<len(l):
        res.extend(l[b:])
    r = "".join(res)
    print(r)



    
    


        
    
        
    

        
    
    

