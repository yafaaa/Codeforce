t = int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    alfa = [0]*26
    res = []
    s =0
    for a in ls:
        if a == 0:
            res.append(chr(ord('a')+ s))
            alfa[s]+=1
            s+=1
            
        else:
            for i in range(26):
                if alfa[i]==a:
                    res.append(chr(ord('a')+i))
                    alfa[i]+=1
                    break
    print("".join(res))

        



    
